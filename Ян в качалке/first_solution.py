from typing import List, Tuple, Optional


def friends_and_Jan_on_track(number_of_tracks: int, number_of_friends: int) -> Tuple[List[Optional[int]], int]:
    ("""Input:\n  number_of_tracks - количество дорожек\n  """
     """number_of_friends - количество друзей\n"""
     """Output:\n  Выводит tuple, где первый эелемт - список состоящий из int и/или """
     """None, где None занятая дорожка, а int индексы свободных дорожек """
     """и второй элемент int - индекс последней занятой дорожки""")

    index = 0
    tracks = list(range(number_of_tracks))

    for _ in range(number_of_friends + 1):
        if tracks[0] or tracks[0] == 0:
            tracks[0] = None
            continue
        elif tracks[-1]:
            tracks[-1] = None
            continue

        slice_tracks = [[]]

        for i in tracks[1:-1]:
            if i is None:
                slice_tracks.append([])
                continue
            slice_tracks[-1].append(i)

        slice_tracks = max(slice_tracks, key=len)
        index = slice_tracks[len(slice_tracks) // 2]
        tracks[index] = None

    return tracks, index


def output_left_and_right_borders(tracks: List[Optional[int]], index: int) -> Tuple[int]:
    ("""Input:\n  tracks - список состоящий из int и/или None, """
     """где None занятая дорожка и int, индексы свободных дорожек\n  """
     """index - индекс последней занятой дорожки\n"""
     """Output:\n  Выводит tuple, где первый эелемт int, количество свободных """
     """дорожек слева и второй элемент int, количество свободных дорожек справа""")

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
