from typing import List, Tuple, Optional
from itertools import groupby


def friends_and_Jan_on_track(number_of_tracks: int, number_of_friends: int) -> Tuple[List[Optional[int]], int]:
    index = 0
    tracks = list(range(number_of_tracks))

    for _ in range(number_of_friends + 1):
        if tracks[0] or tracks[0] == 0:
            tracks[0] = None
            continue
        elif tracks[-1]:
            tracks[-1] = None
            continue

        slice_tracks = groupby(tracks, key=lambda x: isinstance(x, int))
        slice_tracks = [list(v) for k, v in slice_tracks if k == True]

        slice_tracks = max(slice_tracks, key=len)
        index = slice_tracks[len(slice_tracks) // 2]
        tracks[index] = None

    return tracks, index


def output_left_and_right_borders(tracks: List[Optional[int]], index: int) -> Tuple[int]:
    left = 0
    right = 0

    for i in range(index - 1, -1, -1):
        if tracks[i] is None:
            break
        left += 1

    for i in range(index + 1, len(tracks)):
        if tracks[i] is None:
            break
        right += 1

    return left, right


if __name__ == '__main__':
    tracks, index = friends_and_Jan_on_track(*map(int, input().split()))
    result = output_left_and_right_borders(tracks, index)
    print(*sorted(result))
