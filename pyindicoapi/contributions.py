class IndicoContribution:
    def __init__(self, raw_dict):
        self.raw_dict = raw_dict
        self._set_attributes()

    def _set_attributes(self):
        clutter_key = list(self.raw_dict['type'].keys())[0]

        def from_raw_dict(key):
            s = self.raw_dict.get(key, {})
            return s.get(clutter_key, s) if isinstance(s, dict) else s

        self.id = from_raw_dict("id")
        self.db_id = from_raw_dict("db_id")
        self.title = from_raw_dict("title")
        self.description = from_raw_dict("description")
        self.speakers = from_raw_dict("speakers")
        self.start_time = from_raw_dict("start_time")
        self.end_time = from_raw_dict("end_time")
        self.type = from_raw_dict("type")

    def __repr__(self):
        return (
            f"IndicoContribution(data={self.raw_dict}, "
        )

    def get_attributes(self):
        """
        Get attributes from the response JSON.
        """
        key = list(self.raw_dict['type'].keys())[0]
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "speakers": self.speakers,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "type": self.type
        }

    def as_dict(self):
        """
        Return the contribution attributes as a dictionary.
        """
        return self.get_attributes()
