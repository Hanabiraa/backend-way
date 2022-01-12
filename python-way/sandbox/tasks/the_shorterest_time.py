"""
John is a programmer. He treasures his time very much. He lives on the n floor of a building. Every morning he will go downstairs as quickly as possible to begin his great work today.

There are two ways he goes downstairs: walking or taking the elevator.

When John uses the elevator, he will go through the following steps:

1. Waiting the elevator from m floor to n floor;
1a. Or take the stairs to m floor;
2. Waiting the elevator open the door and go in;
3. Waiting the elevator close the door;
4. Waiting the elevator down to 0 floor;
5. Waiting the elevator open the door and go out;
(the time of go in/go out the elevator will be ignored)
Given the following arguments:

n: An integer. The floor of John(0-based).
m: An integer. The floor of the elevator(0-based).
speeds: An array of integer. It contains four integer [a,b,c,d]
        a: The seconds required when the elevator rises or falls 1 floor
        b: The seconds required when the elevator open the door
        c: The seconds required when the elevator close the door
        d: The seconds required when John walks to n-1 or n+1 floor
Please help John to calculate the shortest time to go downstairs.

Example
For n = 4, m = 5 and speeds = [1,2,3,10], the output should be 12.

John go downstairs by using the elevator:

1 + 2 + 3 + 4 + 2 = 12

For n = 0, m = 5 and speeds = [1,2,3,10], the output should be 0.

John is already at 0 floor, so the output is 0.
"""
from typing import List

def shorterest_time(n:int, m:int, speeds:List[int]):
    # simple algo
    el_spd, d_open_spd, d_close_spd, walk_speed = speeds
    secs = 0
    if n < m:
        go_to_el_time = walk_speed * (m - n) + d_open_spd * 2 + d_close_spd + el_spd * m
        walk_down_time = walk_speed * n
        wait_el_ang_go_time = (m - n) * el_spd + d_open_spd * 2 + d_close_spd + el_spd * n
        secs = min(go_to_el_time, walk_down_time, wait_el_ang_go_time)
    else:
        walk_down_time = walk_speed * n
        walk_to_el_and_go_time = walk_speed * (n - m) + d_open_spd * 2 + d_close_spd + el_spd * m
        wait_el_ang_go_time = (n - m) * el_spd + d_open_spd * 2 + d_close_spd + el_spd * n
        secs = min(walk_down_time, walk_to_el_and_go_time, wait_el_ang_go_time)

    return secs

def shorterest_time1(n:int, m:int, speeds:List[int]):
    # improve algo
    if n == 0:
        return 0

    el_spd, open_spd, close_spd, walk_speed = speeds
    return min(
        abs(m - n) * walk_speed + open_spd * 2 + close_spd + m * el_spd,
        abs(m - n) * el_spd + open_spd * 2 + close_spd + n * el_spd,
        walk_speed * n
    )
    