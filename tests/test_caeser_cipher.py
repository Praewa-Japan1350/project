from coe_number.caeser_cipher import caesarCipher

def test_caesar():
    assert caesarCipher("middle-Outz", 2) == "okffng-Qwvb"
    assert caesarCipher("Hello-World", 5) == "Mjqqt-Btwqi"
    assert caesarCipher("abcXYZ-", 3) == "defABC-"