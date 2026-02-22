from coe_number.grid_challenge import gridChallenge

def test_grid_yes():
    assert gridChallenge(["abc", "ade", "efg"]) == "YES"

def test_grid_no_case1():
    assert gridChallenge(["cba", "daf", "ghi"]) == "YES"

def test_grid_no_case2():
    assert gridChallenge(["xy", "yx"]) == "YES"

def test_grid_more():
    assert gridChallenge(["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]) == "YES"
def test_grid_real_no_case():
    assert gridChallenge(["mpxz", "abcd", "wlmf"]) == "NO"