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