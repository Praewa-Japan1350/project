from coe_number.caesar_cipher import caesarCipher


def test_lowercase():
    assert caesarCipher("abc", 2) == "cde"


def test_uppercase():
    assert caesarCipher("ABC", 2) == "CDE"


def test_mixed_case():
    assert caesarCipher("Abc", 1) == "Bcd"


def test_non_alpha():
    assert caesarCipher("a-b!", 1) == "b-c!"


def test_large_shift():
    assert caesarCipher("abc", 52) == "abc"
