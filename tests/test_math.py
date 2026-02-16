def test_math():
    values = [1, 2, 3]
    double = [n * 2 for n in values]

    assert double == [2, 4, 6]