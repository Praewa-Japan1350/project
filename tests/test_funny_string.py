from coe_number.funny_string import funnyString

def test_funny():
    assert funnyString("acxz") == "Funny"
    assert funnyString("bcxz") == "Not Funny"
    assert funnyString("abba") == "Funny"
 def test_funny_single_char():
    assert funnyString("a") == "Funny"

def test_funny_not_funny():
    assert funnyString("abc") == "Not Funny"
