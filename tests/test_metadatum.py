import cto
import pytest


def test_metadatum_attributes_exist():
    m = cto.Metadatum("")

    assert isinstance(m, cto.Metadatum)
    assert "tags" in dir(m)
    assert "description" in dir(m)
    assert "meta" in dir(m)


def test_metadatum_from_object():
    c = "The type of cake @pii"
    m = cto.Metadatum(c)

    assert isinstance(m.tags, list)
    assert "pii" in m.tags
    assert m.description == "The type of cake"


def test_regex_detectors():

    tags = ["@pii", "@w3c::bunny"]
    attributes = ["@state=ohio"]
    json = ['@meta({"google":"bug"})']

