"""841. Keys and Rooms

https://leetcode.com/problems/keys-and-rooms/

There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.
"""

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        checked_rooms = set()
        can_access = {0, *rooms[0]}

        while checked_rooms != can_access:
            if len(can_access) == len(rooms):
                return True

            checked_room_num = min(can_access.difference(checked_rooms))
            can_access.update({*rooms[checked_room_num]})
            checked_rooms.add(checked_room_num)

        return False