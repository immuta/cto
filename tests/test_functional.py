import cto
import pytest


def test_comment_can_be_converted_to_dict():
    c = "Example description. @funny_guy @pii"
    o = {"description": "Example description.", "tags": ["funny_guy", "pii"]}

    mc = cto.Metadatum(c)

    assert mc.to_object() == o
    assert mc.to_comment() == c

    mo = cto.Metadatum(o)

    assert mo.to_object() == o
    assert mo.to_comment() == c
    
    for a in ["description", "tags", "attributes", "meta"]:
        assert getattr(mc, a) == getattr(mo, a)

