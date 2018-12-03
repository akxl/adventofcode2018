from collections import defaultdict
from itertools import accumulate

# O(n log n)
# assume that some external code has passed in the string lines of the input puzzle.
def solve(lines):
    data = [int(line) for line in lines]

    # calculate the cumulative sums
    sums = [0] + list(accumulate(data))

    # check if the repetition occurs in the first iteration
    sum_set = set()
    for s in sums:
        if s in sum_set:
            return s
        sum_set.add(s)

    # find the final sum after performing one iteration
    final_sum = sums[-1]
    if final_sum == 0:
        return 0  # if the shift is 0, then the first repetition is 0

    sums = sums[:-1]  # Remove the last element as it belongs to iteration 2, not iteration 1.

    # populate a dictionary of all the groups where the value is the list of frequencies in the group
    groups = defaultdict(list)
    for i, s in enumerate(sums):
        groups[s % final_sum].append((i, s))  # each value will be a tuple of the index and the frequency

    # find the minimum difference frequencies
    min_index, min_diff, min_freq = None, None, None
    for group in groups.values():
        # sort by frequency
        sorted_vals = list(sorted(group, key=lambda t: t[1]))
        for i in range(1, len(sorted_vals)):
            # calculate the difference and the index of the repetition inside the list of frequencies
            diff = sorted_vals[i][1] - sorted_vals[i - 1][1]
            index = sorted_vals[i-1][0] if final_sum > 0 else sorted_vals[i][0]
            freq = sorted_vals[i][1] if final_sum > 0 else sorted_vals[i-1][1]
            if min_diff is None or diff < min_diff or (diff == min_diff and index < min_index):
                min_index = index
                min_diff = diff
                min_freq = freq

    return min_freq


if __name__ == "__main__":
	
	f = open("input.txt", "r")
	numbers = list(map(int, f.read().split()))
	
	print(solve(numbers))