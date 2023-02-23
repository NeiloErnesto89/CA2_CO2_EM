import pytest 

# running pytest in other file to test
# result passing, runnings both files simultaneously 

class TestClass:
    def test_one(self):
        tx = "this"
        assert "h" in tx