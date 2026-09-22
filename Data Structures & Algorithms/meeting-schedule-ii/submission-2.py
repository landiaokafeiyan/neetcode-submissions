"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq
from typing import List
import heapq
from typing import List

from typing import List
# My approach is to first sort the intervals by start time. Then I maintain a min heap containing the end times of meetings that are currently occupying rooms. The minimum value in the heap tells me which room becomes available earliest. For each new meeting, if its start time is greater than or equal to the minimum end time, I can reuse that room by popping the earliest end time. Otherwise, I need another room. In either case, I push the current meeting's end time into the heap. The size of the heap represents the number of rooms currently occupied, and the maximum size reached is the answer.

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # ============================================================
        # LeetCode 253 - Meeting Rooms II
        #
        # Method 2:
        #   Sort START times
        #   Sort END times
        #   Use TWO POINTERS
        #
        # ------------------------------------------------------------
        # Core idea:
        #
        #   We want to know how many meetings are active at every
        #   point in time.
        #
        #   Whenever a meeting STARTS:
        #
        #       rooms += 1
        #
        #   Whenever a meeting ENDS before/equal to the next start:
        #
        #       rooms -= 1
        #
        #   The answer is the maximum value of rooms.
        #
        # ------------------------------------------------------------
        # Example:
        #
        #   intervals:
        #
        #       [0,30]
        #       [5,10]
        #       [15,20]
        #
        #   starts = [0,5,15]
        #   ends   = [10,20,30]
        #
        #   Process chronologically:
        #
        #       start 0 -> rooms = 1
        #       start 5 -> rooms = 2
        #       end 10  -> one room becomes free
        #       start 15 -> rooms = 2
        #
        #   maximum rooms = 2
        #
        # ------------------------------------------------------------
        # Why two sorted arrays?
        #
        #   We only care about the ordering of:
        #
        #       "a meeting starts"
        #
        #   versus:
        #
        #       "a meeting ends"
        #
        #   We don't need to keep each start paired with its original
        #   end anymore.
        #
        # ------------------------------------------------------------
        # Key invariant:
        #
        #   rooms = number of meetings currently active.
        #
        #   max_rooms = maximum number of simultaneously active
        #               meetings seen so far.
        #
        # ------------------------------------------------------------
        # Complexity:
        #
        #   Sort starts: O(n log n)
        #   Sort ends:   O(n log n)
        #   Two pointers: O(n)
        #
        #   Total:
        #       O(n log n)
        #
        #   Space:
        #       O(n)
        # ============================================================

        # Edge case:
        # No meetings -> no rooms.
        if not intervals:
            return 0

        # Step 1:
        # Extract all START times and END times separately.
        starts = sorted(interval[0] for interval in intervals)
        ends = sorted(interval[1] for interval in intervals)

        # Two pointers:
        #
        # start_ptr -> next meeting that is about to start
        # end_ptr   -> earliest meeting that has not been processed
        start_ptr = 0
        end_ptr = 0

        # Current number of rooms being used.
        rooms = 0

        # Maximum number of rooms used at any point.
        max_rooms = 0

        # We process every start event.
        while start_ptr < len(starts):

            # If the next meeting starts BEFORE the earliest
            # currently unprocessed meeting ends:
            #
            #     starts[start_ptr] < ends[end_ptr]
            #
            # then there is an overlap.
            #
            # We need a NEW room.
            if starts[start_ptr] < ends[end_ptr]:

                rooms += 1

                # Move to the next meeting start.
                start_ptr += 1

                # Record the maximum simultaneous meetings.
                max_rooms = max(max_rooms, rooms)

            else:
                # If:
                #
                #     starts[start_ptr] >= ends[end_ptr]
                #
                # then a meeting has already ended before this new
                # meeting starts.
                #
                # Therefore, one room becomes available.
                rooms -= 1

                # Move to the next ending meeting.
                end_ptr += 1

        return max_rooms
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # ============================================================
        # LeetCode 253 - Meeting Rooms II
        #
        # Goal:
        #   Find the MINIMUM number of meeting rooms required so that
        #   no two overlapping meetings use the same room.
        #
        # ------------------------------------------------------------
        # Key observation:
        #
        #   Minimum number of rooms
        #   =
        #   Maximum number of meetings happening simultaneously.
        #
        # Example:
        #
        #   [0,30]
        #   [5,10]
        #   [15,20]
        #
        # At some point there are 2 meetings happening at the same
        # time, so we need at least 2 rooms.
        #
        # ------------------------------------------------------------
        # Core idea:
        #
        #   1. Sort meetings by START time.
        #   2. Use a min heap to store END times of meetings that
        #      are currently occupying rooms.
        #   3. heap[0] is the meeting that finishes EARLIEST.
        #
        # Why do we care about the earliest ending meeting?
        #
        #   When a new meeting starts, we want to know whether ANY
        #   existing room is available.
        #
        #   The earliest available room is heap[0].
        #
        #   If:
        #
        #       new_start >= earliest_end
        #
        #   then that room can be reused.
        #
        #   Otherwise:
        #
        #       new_start < earliest_end
        #
        #   no room is available, so we need a new room.
        #
        # ------------------------------------------------------------
        # IMPORTANT INVARIANT:
        #
        #   heap contains the END times of meetings currently using
        #   rooms.
        #
        #   Therefore:
        #
        #       len(heap)
        #
        #   = number of rooms currently occupied.
        #
        #   And:
        #
        #       heap[0]
        #
        #   = earliest time when any current room becomes available.
        #
        # ------------------------------------------------------------
        # Complexity:
        #
        #   Sorting:
        #       O(n log n)
        #
        #   For each meeting:
        #       heap push/pop -> O(log n)
        #
        #   Total:
        #       O(n log n)
        #
        #   Space:
        #       O(n)
        # ============================================================

        # Edge case:
        # No meetings -> no rooms required.
        if not intervals:
            return 0

        # Step 1:
        # Sort meetings by START time.
        #
        # Example:
        #
        #   [[5,10], [0,30], [15,20]]
        #
        # becomes:
        #
        #   [[0,30], [5,10], [15,20]]
        #
        # This allows us to process meetings chronologically.
        intervals.sort(key=lambda x: x[0])

        # Step 2:
        # Initialize the heap with the END time of the first meeting.
        #
        # heap = [30]
        #
        # This means:
        #   Room 1 is occupied until time 30.
        heap = [intervals[0][1]]

        # Step 3:
        # Process every remaining meeting.
        for start, end in intervals[1:]:

            # heap[0] is the earliest ending meeting.
            earliest_end = heap[0]

            # If the new meeting starts AFTER or EXACTLY WHEN
            # the earliest meeting ends, we can reuse that room.
            #
            # Example:
            #
            #   existing meeting: [0,10]
            #   new meeting:      [10,20]
            #
            # If intervals are treated as [start, end),
            # these meetings do not overlap.
            if start >= earliest_end:

                # Remove the old meeting because its room
                # is now available.
                heapq.heappop(heap)

            # Add the new meeting's end time.
            #
            # If we reused a room, the heap size stays the same.
            #
            # If we could NOT reuse a room, the heap grows by 1,
            # meaning we need one additional room.
            heapq.heappush(heap, end)

        # At the end:
        #
        #   len(heap)
        #
        # equals the maximum number of simultaneously occupied rooms
        # reached during the scan.
        return len(heap)

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # ============================================================
        # LeetCode 253 - Meeting Rooms II
        #
        # Goal:
        #   Find the MINIMUM number of meeting rooms required so that
        #   no two overlapping meetings use the same room.
        #
        # ------------------------------------------------------------
        # Key observation:
        #
        #   Minimum number of rooms
        #   =
        #   Maximum number of meetings happening simultaneously.
        #
        # Example:
        #
        #   [0,30]
        #   [5,10]
        #   [15,20]
        #
        # At some point there are 2 meetings happening at the same
        # time, so we need at least 2 rooms.
        #
        # ------------------------------------------------------------
        # Core idea:
        #
        #   1. Sort meetings by START time.
        #   2. Use a min heap to store END times of meetings that
        #      are currently occupying rooms.
        #   3. heap[0] is the meeting that finishes EARLIEST.
        #
        # Why do we care about the earliest ending meeting?
        #
        #   When a new meeting starts, we want to know whether ANY
        #   existing room is available.
        #
        #   The earliest available room is heap[0].
        #
        #   If:
        #
        #       new_start >= earliest_end
        #
        #   then that room can be reused.
        #
        #   Otherwise:
        #
        #       new_start < earliest_end
        #
        #   no room is available, so we need a new room.
        #
        # ------------------------------------------------------------
        # IMPORTANT INVARIANT:
        #
        #   heap contains the END times of meetings currently using
        #   rooms.
        #
        #   Therefore:
        #
        #       len(heap)
        #
        #   = number of rooms currently occupied.
        #
        #   And:
        #
        #       heap[0]
        #
        #   = earliest time when any current room becomes available.
        #
        # ------------------------------------------------------------
        # Complexity:
        #
        #   Sorting:
        #       O(n log n)
        #
        #   For each meeting:
        #       heap push/pop -> O(log n)
        #
        #   Total:
        #       O(n log n)
        #
        #   Space:
        #       O(n)
        # ============================================================

        # Edge case:
        # No meetings -> no rooms required.
        if not intervals:
            return 0

        # Step 1:
        # Sort meetings by START time.
        #
        # Example:
        #
        #   [[5,10], [0,30], [15,20]]
        #
        # becomes:
        #
        #   [[0,30], [5,10], [15,20]]
        #
        # This allows us to process meetings chronologically.
        intervals.sort(key=lambda x: x[0])

        # Step 2:
        # Initialize the heap with the END time of the first meeting.
        #
        # heap = [30]
        #
        # This means:
        #   Room 1 is occupied until time 30.
        heap = [intervals[0][1]]

        # Step 3:
        # Process every remaining meeting.
        for start, end in intervals[1:]:

            # heap[0] is the earliest ending meeting.
            earliest_end = heap[0]

            # If the new meeting starts AFTER or EXACTLY WHEN
            # the earliest meeting ends, we can reuse that room.
            #
            # Example:
            #
            #   existing meeting: [0,10]
            #   new meeting:      [10,20]
            #
            # If intervals are treated as [start, end),
            # these meetings do not overlap.
            if start >= earliest_end:

                # Remove the old meeting because its room
                # is now available.
                heapq.heappop(heap)

            # Add the new meeting's end time.
            #
            # If we reused a room, the heap size stays the same.
            #
            # If we could NOT reuse a room, the heap grows by 1,
            # meaning we need one additional room.
            heapq.heappush(heap, end)

        # At the end:
        #
        #   len(heap)
        #
        # equals the maximum number of simultaneously occupied rooms
        # reached during the scan.
        return len(heap)


    """
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)