from solve import box_range, exrange


def test_exrange():
    assert list(exrange(0, 1)) == [1]
    assert list(exrange(0, 2)) == [1, 2]

    assert list(exrange(0, -1)) == [-1]
    assert list(exrange(0, -2)) == [-1, -2]


def test_box_points_simple():
    assert box_range((0, 0, 0), axis=0, delta=1) == [(1, 0, 0)]
    assert box_range((0, 0, 0), axis=1, delta=1) == [(0, 1, 0)]
    assert box_range((0, 0, 0), axis=2, delta=1) == [(0, 0, 1)]

    assert box_range((0, 0, 0), axis=0, delta=-1) == [(-1, 0, 0)]
    assert box_range((0, 0, 0), axis=1, delta=-1) == [(0, -1, 0)]
    assert box_range((0, 0, 0), axis=2, delta=-1) == [(0, 0, -1)]


def test_box_points_complex():
    assert box_range((3, 1, 2), axis=1, delta=1) == [(3, 2, 2)]
    assert box_range((3, 1, 2), axis=1, delta=2) == [(3, 2, 2), (3, 3, 2)]
