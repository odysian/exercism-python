"""
"Middle too small? Search right. Middle too big? Search left."

Practice Recall

What are the initial values of left and right?
    left = 0
    right = len(list) - 1
What's the while condition?
    while left <= right
How do you calculate mid?
    left + right // 2
If arr[mid] is LESS than target, which pointer moves?
    left pointer moves to eliminated lesser values
What happens when the loop exits?
    return value if found
    ValueError if not found


"""


def find(search_list, value):

    l = 0
    r = len(search_list) - 1

    while l <= r:
        mid = (l + r) // 2

        if search_list[mid] == value:
            return mid
        elif search_list[mid] < value:
            l = mid + 1
        else:
            r = mid - 1

    raise ValueError("value not in array")
