from coe_number.alternating import alternatingCharacters

def test_basic_cases():
    assert alternatingCharacters("AAAA") == 3
    assert alternatingCharacters("BBBBB") == 4
    assert alternatingCharacters("ABABABAB") == 0
    assert alternatingCharacters("BABABA") == 0
    assert alternatingCharacters("AAABBB") == 4
def test_alternating_single_char():
    assert alternatingCharacters("A") == 0

def test_alternating_all_same():
    assert alternatingCharacters("AAAA") == 3

def test_alternating_valid():
    assert alternatingCharacters("ABABAB") == 0