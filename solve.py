from typing import Set, Tuple, Optional, List

# puzzle_orig = [4, 2, 4, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 3, 2, 4, 2, 3, 3, 4, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 4, 2, 4, 4, 4, 3]
puzzle = [3, 1, 3, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 3, 1, 2, 2, 3, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 3, 1, 3, 3, 3, 2]
puzzle1_reversed = [2, 3, 3, 3, 1, 3, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 3, 2, 2, 1, 3, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 3, 1, 3]
puzzle = puzzle1_reversed


def exrange(from_excl, to_incl):
    if from_excl < to_incl:
        return range(from_excl + 1, to_incl + 1)
    else:
        return range(from_excl - 1, to_incl - 1, -1)


def box_range(
        origin: Tuple[int, int, int],
        axis: int,
        delta: int
) -> List[Tuple[int, int, int]]:
    cords = []
    for v in exrange(origin[axis], origin[axis] + delta):
        cords.append(tuple(v if i == axis else origin[i] for i in range(3)))
    return cords


def place(
        piece: int,
        origin: Tuple[int, int, int],
        used_coords: Set[Tuple[int, int, int]],
        prev_axis: Optional[int],
        maxs: Tuple[int, int, int],
        mins: Tuple[int, int, int],
):
    if piece == len(puzzle):
        return []
    boxes_to_place = puzzle[piece]
    for axis, direction in valid_moves(piece, prev_axis):
        axis_end = origin[axis] + (direction * boxes_to_place)
        if max(maxs[axis], axis_end) - min(mins[axis], axis_end) > 3:
            continue
        new_coords = box_range(origin, axis, boxes_to_place * direction)
        if any(c in used_coords for c in new_coords):
            continue
        end = new_coords[-1]
        used_coords.update(new_coords)
        new_maxs = (max(maxs[0], end[0]), max(maxs[1], end[1]), max(maxs[2], end[2]))
        new_mins = (min(mins[0], end[0]), min(mins[1], end[1]), min(mins[2], end[2]))
        steps = place(piece + 1, end, used_coords, axis, new_maxs, new_mins)
        if steps is not None:
            steps.append((axis, direction))
            return steps
        else:
            for c in new_coords:
                used_coords.remove(c)

    return None


def valid_moves(piece, prev_axis):
    if piece == 0:
        yield 0, 1
    elif piece == 1:
        yield 1, 1
    elif piece == 2:
        yield 0, 1
        yield 0, -1
        yield 2, 1
    else:
        for axis in range(3):
            if axis != prev_axis:
                yield axis, 1
                yield axis, -1


def convert_steps_to_coordinates(moves):
    c = (0, 0, 0)
    cords = [c]
    for i, (axis, direction) in enumerate(moves):
        c = box_range(c, axis, puzzle[i] * direction)[-1]
        cords.append(c)
    return cords


def main():
    assert sum(puzzle) + 1 == 64
    steps = place(
        piece=0,
        origin=(0, 0, 0),
        used_coords={(0, 0, 0)},
        prev_axis=None,
        maxs=(0, 0, 0),
        mins=(0, 0, 0),
    )
    print(convert_steps_to_coordinates(reversed(steps)))


if __name__ == '__main__':
    main()
