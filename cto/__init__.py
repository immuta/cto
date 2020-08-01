import typing


class Metadatum:
    
    description = ""
    tags = []
    meta = {}

    def __init__(self, raw=None, **kwargs):
        if isinstance(raw, str):
            self.as_comment = raw
            converted = self.parse_comment(raw)
            self.tags = converted.get("tags", [])
            self.description = converted.get("description", "")
            self.meta = converted.get("meta", {})
        elif isinstance(raw, dict):
            self.as_object = raw
            converted = self.parse_object(raw)
            self.tags = converted.get("tags", [])
            self.description = converted.get("description", "")
            self.meta = converted.get("meta", {})

    @staticmethod
    def parse_comment(comment: str) -> dict:
        return {"tags": ["pii"], "description": "The type of cake"}

    @staticmethod
    def parse_object(object: dict) -> str:
        return ""
