from typing import List


def count_how_many_pairs_give_sum_eq_target(arr: List[int],
                                            target: int) -> int:
    result: int = 0
    for i in range(len(arr)):
        val_to_find = target - arr[i]
        result += arr[i:].count(val_to_find)
    return result

print(count_how_many_pairs_give_sum_eq_target([1, 3, 6, 2, 2, 0, 4, 5], 5))