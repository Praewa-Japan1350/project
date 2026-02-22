from coe_number.alternating import alternatingCharacters


def test_no_delete():
    assert alternatingCharacters("ABABAB") == 0


def test_one_delete():
    assert alternatingCharacters("AAABBB") == 4


def test_mixed():
    assert alternatingCharacters("AABAAB") == 2


def test_single_char():
    assert alternatingCharacters("A") == 0
