from ceres.objects import Spacecraft

def test_spacecraft():
    sc = Spacecraft()
    assert sc.test() == 'test'

test_spacecraft()