from coe_number.two_characters import alternate

def test_case1():
    assert alternate("beabeefeab") == 5

def test_case2():
    assert alternate("aaaa") == 0

def test_case3():
    assert alternate("abababab") == 8

def test_case4():
    assert alternate("abcabcabc") == 6