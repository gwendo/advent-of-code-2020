from functools import lru_cache


def find_diff(input_data):
    sorted_ = sorted(input_data)
    diffs_ = [1]
    for i in range(1, len(input_data)):
        diffs_.append(sorted_[i] - sorted_[i-1])
    return (diffs_.count(1)) * (diffs_.count(3)+1)


def find_all_combos(input_data):
    global sorted_
    sorted_ = sorted(input_data)
    sorted_.insert(0, 0)
    sorted_.append(max(sorted_)+3)
    return dp(0)


@lru_cache(maxsize=None)
def dp(i):
    if i == len(sorted_)-1:
        return 1
    ans = 0
    for j in range(i+1, min(i+4, len(sorted_))):
        if sorted_[j]-sorted_[i] <= 3:
            ans += dp(j)
    return ans

