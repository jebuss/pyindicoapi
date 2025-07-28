import requests


class IndicoCategory:
    """
    Represents a response from the Indico API for categories.
    """

    def __init__(self, result_json):
        self.response = result_json
        self.set_attributes()

    def set_attributes(self):
        """
        Set attributes from the response JSON.
        """
        self.category_id = self.response.get('categoryId')
        self._path = self.response.get('path')
        self.name = self._path[-2].get('name')
        self.type = self._path[-2].get('type')
        self.id = self._path[-2].get('id')
        self.url = self._path[-2].get('url')
        self.parent_id = self._path[-3].get(
            'id') if len(self._path) > 2 else None

    def get_attributes(self):
        """
        Get attributes from the response JSON.
        """
        return {
            "id": self.id,
            "category_id": self.category_id,
            "name": self.name,
            "type": self.type,
            "url": self.url,
            "parent_id": self.parent_id
        }

    def __repr__(self):
        return f"IndicoCategoryResponse(data={self.get_attributes()})"
    
    def as_dict(self):
        """
        Return the category attributes as a dictionary.
        """
        return self.get_attributes()


class IndicoAPI:
    """
    Simple wrapper for the Indico HTTP API.
    See: https://indico-pedro.readthedocs.io/en/latest/http_api/index.html
    """

    def __init__(self, base_url, api_key=None, verify_ssl=True):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.verify_ssl = verify_ssl

    def _request(self, method, endpoint, params=None, data=None, files=None):
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

    def get_custom_resource(self, resource_name, resource_id, location=None, output_type='json', params=None):
        """
        Get details of a specific custom resource.
        """
        if location:
            endpoint = f'export/{resource_name}/{location}/{resource_id}.{output_type}'
        else:
            endpoint = f'export/{resource_name}/{resource_id}.{output_type}'
        return self._request('GET', endpoint, params=params)

    def get_event(self, event_id, params=None):
        """
        Get details of a specific event.
        """
        return self._request('GET', f'export/event/{event_id}.json', params=params)

    def list_events(self, category_id=0, **params):
        """
        List events with optional filters.
        """

        category = self.get_category(category_id, params=None)
        if isinstance(category, dict):
            events = category.get('results')

        return events

    def get_category(self, category_id, params=None):
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
        root_category = self.get_category(root_category_id, params=None)

        if isinstance(root_category, dict):
            categories = root_category.get(
                'additionalInfo').get('eventCategories')

        for category in categories:
            list_of_categories.append(IndicoCategory(category))

        return list_of_categories

    def get_user(self, user_id, params=None):
        """
        Get details of a specific user.
        """
        return self._request('GET', f'export/user/{user_id}.json', params=params)

    # Add more methods as needed, following the API reference.
