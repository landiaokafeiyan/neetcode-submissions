class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # ============================================================
        # Problem: LeetCode 435 - Non-overlapping Intervals
        #
        # Goal:
        #   Remove the MINIMUM number of intervals so that the
        #   remaining intervals do not overlap.
        #minmum number of remove=n-maximum number of the overleap interval
        # ------------------------------------------------------------
        # Key difference from Merge Intervals:
        #
        #   Merge Intervals:
        #       sort by START
        #       -> find and merge overlapping intervals
        #
        #   Non-overlapping Intervals:
        #       sort by END
        #       -> greedily KEEP intervals that finish earliest
        #
        # Core greedy idea:
        #
        #   If two intervals overlap:
        #
        #       [1,4]
        #       [2,5]
        #
        #   We have to remove one.
        #
        #   Which one should we remove?
        #
        #       Keep [1,4]
        #       Remove [2,5]
        #
        #   Why?
        #
        #       [1,4] finishes earlier, so it leaves more room for
        #       future intervals.
        #
        # Therefore:
        #
        #   Always keep the interval with the EARLIEST END.
        #
        # This is the same greedy principle as:
        #
        #       Activity Selection / Interval Scheduling
        #
        # ------------------------------------------------------------
        # Greedy invariant:
        #
        #   prev_end = the smallest possible end time among the
        #              intervals we have decided to KEEP.
        #
        #   When the next interval starts >= prev_end:
        #
        #       No overlap -> keep it.
        #
        #   When next_start < prev_end:
        #
        #       Overlap -> remove one interval.
        #
        #       Because intervals are sorted by END, the current
        #       interval already has the earlier end.
        #
        #       Therefore, remove the new interval.
        #
        # ------------------------------------------------------------
        # Complexity:
        #
        #   Sorting: O(n log n)
        #   Scan:    O(n)
        #
        #   Total:   O(n log n)
        #
        #   Extra space: O(1) excluding the sorting implementation.
        # ============================================================

        # Step 1:
        # Sort by END time, NOT start time.
        #
        # Example:
        #
        #   [[1,4], [2,3], [3,5]]
        #
        # becomes:
        #
        #   [[2,3], [1,4], [3,5]]
        #
        # because:
        #
        #   end = 3, 4, 5
        #
        intervals.sort(key=lambda x: x[1])

        # The first interval has the earliest end,
        # so we keep it.
        prev_end = intervals[0][1]

        removed = 0

        # Step 2:
        # Scan the remaining intervals.
        for start, end in intervals[1:]:

            # If:
            #
            #       start < prev_end
            #
            # then the new interval overlaps with the interval
            # we decided to keep.
            if start < prev_end:

                # Because we sorted by END, the current interval
                # has an end >= prev_end.
                #
                # Keeping the current interval would leave LESS
                # room for future intervals.
                #
                # Therefore:
                #       remove current interval.
                removed += 1

            else:
                # No overlap.
                #
                # Keep this interval and update the boundary.
                prev_end = end

        return removed