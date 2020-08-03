# cto
Comment-to-object metadata translator for databases

## Usage

The `Metadatum` object will map a string or dictionary to its object model,
then make the metadata translatable to a comment or object.

```
import cto

comment_text = 'A location column. @pii @location @country(usa) @origin({"provider":"us.gov", "date": "2020-08-20"})'

m = cto.Metadatum(comment_text)

m.description
    "A location column."

m.tags
    ["pii", "location"]

m.meta
    {"country": "usa", "origin": {"provider": "us.gov", "date": "2020-08-20"}}
```

This standardization allows us to rewrite the comment as an object, e.g. in catalogs.

```
m.to_object()
    {
        "description": "A location column.",
        "tags": ["pii", "location"],
        "country": "usa",
        "origin": {"provider": "us.gov", "date": "2020-08-20"}
    }
```

It also allows us to pass in an object and map to a comment.

```
o = {"description": "A person's social security number.", "tags": ["DirectIdentifier"]}
m = cto.Metadatum(o)

m.to_comment()
    "A person's social security number. @DirectIdentifier"
```