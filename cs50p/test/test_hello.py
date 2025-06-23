# __init__.py will mark the entire as a package (module(s) in a folder)

from hello import hello

def test_detault():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"