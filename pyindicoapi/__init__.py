import requests
import pandas as pd

from .category import IndicoCategory


class IndicoAPI:
    """
    Simple wrapper for the Indico HTTP API.
    See: https://indico-pedro.readthedocs.io/en/latest/http_api/index.html
    """

    def __init__(self, base_url, api_key=None, verify_ssl=True):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.verify_ssl = verify_ssl

    def _request(self, method, endpoint, params={}, data=None, files=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        headers = {}
        if self.api_key:
            headers['Authorization'] = f"Bearer {self.api_key}"
        response = requests.request(
            method,
            url,
            params=params,
            data=data,
            files=files,
            headers=headers,
            verify=self.verify_ssl
        )
        response.raise_for_status()
        return response.json()

    def get_custom_resource(self, resource_name, resource_id, location=None, output_type='json', params={}):
        """
        Get details of a specific custom resource.
        """
        if location:
            endpoint = f'export/{resource_name}/{location}/{resource_id}.{output_type}'
        else:
            endpoint = f'export/{resource_name}/{resource_id}.{output_type}'
        return self._request('GET', endpoint, params=params)

    def get_event(self, event_id, params={}):
        """
        Get details of a specific event.
        """
        return self._request('GET', f'export/event/{event_id}.json', params=params)

    def list_events(self, category_id=0, **params):
        """
        List events with optional filters.
        """

        category = self.get_category(category_id, params={})
        if isinstance(category, dict):
            events = category.get('results')

        return events

    def get_category(self, category_id, params={}):
        """
        Get details of a specific category.
        """
        return self._request('GET', f'export/categ/{category_id}.json', params=params)

    def list_categories(self, root_category_id=0, **params):
        """
        List categories with optional filters.

        If root_category_id is 0, it will list all categories.
        If a specific root_category_id is provided, it will list categories under that root.
        """
        list_of_categories = list()
        root_category = self.get_category(root_category_id, params={})

        if isinstance(root_category, dict):
            categories = root_category.get(
                'additionalInfo').get('eventCategories')

        for category in categories:
            list_of_categories.append(IndicoCategory(category))

        return list_of_categories

    def get_user(self, user_id, params={}):
        """
        Get details of a specific user.
        """
        return self._request('GET', f'export/user/{user_id}.json', params=params)

    def get_contribution(self, event_id, contribution_id, params={}, output_type='dict'):
        """
        Get details of a specific contribution.
        """
        params['detail'] = 'contributions'
        event = self.get_event(event_id, params=params)
        if not isinstance(event, dict):
            raise ValueError(
                f"Event with ID {event_id} not found or invalid response.")
        if 'results' not in event or not event['results']:
            raise ValueError(
                f"No contributions found for event with ID {event_id}.")

        df = pd.DataFrame(event['results'][0]['contributions'])
        query_result = df.query(f"db_id=={contribution_id}")

        if output_type == 'dict':
            return query_result.to_dict()
        elif output_type == 'dataframe':
            return query_result
        else:
            raise ValueError(f"Unknown output type: {output_type}")

    # Add more methods as needed, following the API reference.
