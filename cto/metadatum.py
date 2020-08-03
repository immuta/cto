import copy
import json
import logging
import re


class Metadatum:

    description = ""  # Expects string
    tags = []  # Expects list
    meta = {}  # Expects dict

    def __init__(self, raw=None, **kwargs):
        self.raw = raw

        if isinstance(raw, str):
            self.parse_comment(raw)
        elif isinstance(raw, dict):
            self.parse_object(raw)
        else:
            raise TypeError("Input argument must be dict or string.")

    def to_object(self):
        output = dict(
            description=self.description, tags=self.tags, **self.meta
        )
        output = {k: v for k, v in output.items() if v is not None}
        return output

    def to_comment(self):
        "Dumps metadata out to a string."
        compiled = []
        compiled.append(self.description)
        compiled += [f"@{tag}" for tag in self.tags]
        compiled += [f"@{k}({v})" for k, v in self.meta.items() if type(v) == str]
        compiled += [f"@{k}({json.dumps(v, separators=(',', ':'))})" for k, v in self.meta.items() if type(v) in [list, dict]]
        logging.info("Compiled text units: %s", compiled)
        return " ".join([txt for txt in compiled if txt is not None]).strip()

    def parse_comment(self, comment: str):
        desc_result = self._detect_comment_description(comment)
        if desc_result:
            self.description = desc_result

        tag_result = self._detect_comment_tags(comment)
        if tag_result:
            self.tags = tag_result

        meta_result = self._detect_comment_meta(comment)
        if meta_result:
            self.meta = meta_result

    def parse_object(self, obj: dict):
        copied = copy.deepcopy(obj)
        self.description = copied.pop("description", "")
        self.tags = copied.pop("tags", [])
        self.meta = {k: v for k, v in copied.items() if type(v) in [str, list, dict]}

    def _detect_comment_description(self, comment) -> str:
        # match the initial text, up to the first @
        pattern = re.compile(r"^([\w\W]+?)@")
        result = re.findall(pattern, comment)
        if len(result) > 0:
            return result[0].strip()
        return None

    def _detect_comment_tags(self, comment) -> list:
        # neg. lookahead excludes '(' and '='
        pattern = re.compile(r"@([\w:]+)\b(?![(=])")
        result = re.findall(pattern, comment)
        return sorted(result)

    def _detect_comment_meta(self, comment) -> dict:
        # arbitrary json data, e.g. @owner({"name":"fred astaire"})
        pattern = re.compile(r"@([\w:]+)\b\(([\w\W\"]+?)\)")
        result = re.findall(pattern, comment)
        logging.debug("Result for meta regex: %s", result)

        parsed = {}
        for k, v in result:
            try:
                parsed[k] = json.loads(v)
            except json.JSONDecodeError:
                parsed[k] = json.loads('"' + v + '"')
            except json.JSONDecodeError as e:
                raise

        return parsed
