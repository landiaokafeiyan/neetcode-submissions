class Solution:
    def merge(self, intervals):
        # ============================================================
        # Problem Pattern: INTERVAL MERGING
        #
        # Core idea:
        #   1. Sort intervals by start time.
        #   2. Scan from left to right.
        #   3. Maintain the last merged interval.
        #   4. Compare:
        #
        #          next_start vs. current_end
        #
        #      NOT next_start vs. current_start.
        #
        #      If next_start <= current_end:
        #          intervals overlap -> merge them.
        #
        #      Otherwise:
        #          no overlap -> start a new interval.
        #
        # Key invariant:
        #   result[-1] is always the merged interval covering
        #   the current overlapping group of intervals.
        #
        # Why sorting works:
        #   After sorting:
        #
        #       start_1 <= start_2 <= ... <= start_n
        #
        #   Therefore, when processing interval i, all future
        #   intervals start no earlier than interval i.
        #   We only need to compare the new start with the
        #   right boundary (end) of the current merged interval.
        #
        # Overlap condition:
        #
        #       next_start <= current_end
        #
        # Non-overlap:
        #
        #       next_start > current_end
        #
        # Merge:
        #
        #       new_start = current_start
        #       new_end   = max(current_end, next_end)
        #
        # IMPORTANT:
        #   Do NOT use next_end directly.
        #
        #   Example:
        #       [1,10], [2,5]
        #
        #   Correct result:
        #       [1,10]
        #
        #   Therefore:
        #       new_end = max(10, 5) = 10
        #
        # Complexity:
        #   Sorting: O(n log n)
        #   Scan:    O(n)
        #   Total:   O(n log n)
        #
        #   Space: O(n) for the output.
        #
        # Generalizable pattern:
        #   "Sort by one boundary, then maintain the other boundary."
        #
        # Related problems:
        #   - Meeting Rooms II -> min heap
        #   - Maximum Overlap -> sweep line
        #   - Interval Intersection -> two pointers
        #   - Insert Interval -> sorted scan
        # ============================================================

        # Step 1: Sort by interval START.
        #
        # Example:
        #   [[8,10], [1,3], [2,6]]
        #
        # becomes:
        #   [[1,3], [2,6], [8,10]]
        intervals.sort(key=lambda x: x[0])

        result = []

        # Step 2: Scan from left to right.
        for interval in intervals:

            # If result is empty, this is the first interval.
            #
            # OR:
            #
            # interval[0] > result[-1][1]
            #
            # means:
            #
            #   next_start > current_end
            #
            # Therefore there is NO overlap.
            if not result or interval[0] > result[-1][1]:

                # Start a new independent merged interval.
                result.append(interval)

            else:
                # There IS overlap:
                #
                #   interval[0] <= result[-1][1]
                #
                # Extend the current interval's right boundary.
                #
                # Use MAX because the new interval might be completely
                # contained inside the current interval.
                #
                # Example:
                #   current = [1,10]
                #   next    = [2,5]
                #
                #   max(10,5) = 10
                result[-1][1] = max(result[-1][1], interval[1])

        # result now contains all merged intervals.
        return result
# First, I sort the intervals by their start time. Then I scan them from left to right while maintaining the current merged interval. For each next interval, if its start is less than or equal to the current end, the two intervals overlap, so I extend the current end using the maximum of the two end points. Otherwise, I add the current interval to the result and start a new current interval.
