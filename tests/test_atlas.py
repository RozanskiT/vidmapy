from vidmapy.kurucz import atlas

def test_sum():
    assert 5 == atlas.sum(2,3)
    assert 5. == atlas.sum(2.,3.)
    