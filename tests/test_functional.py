import cto
import pytest


def test_comment_can_be_converted_to_dict():
    c = 'Example description. @funny_guy @pii @owner(jerry) @origin({"country":"US"})'
    o = {
        "description": "Example description.",
        "tags": ["funny_guy", "pii"],
        "owner": 'jerry',
        "origin": {"country": "US"}}

    mc = cto.Metadatum(c)
    print(mc.to_object())
    print(mc.to_comment())

    assert mc.to_object() == o
    assert mc.to_comment() == c

    mo = cto.Metadatum(o)

    assert mo.to_object() == o
    assert mo.to_comment() == c
    
    for a in ["description", "tags", "meta"]:
        assert getattr(mc, a) == getattr(mo, a)

