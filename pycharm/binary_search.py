nums = [2, 4, 6, 7, 9, 10, 11, 12, 13, 14, 22, 28]


# n binary search for finding the first and last element always check with l<= r or lo <= hi.
# If the number does not exists then it would be at final lo or l index

def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = int((lo + hi) / 2)
        mid_ele = arr[mid]
        print(lo, hi, mid)
        if target == mid_ele:
            return mid
        elif target > mid_ele:
            lo = mid + 1
        else:
            hi = mid - 1

    return hi


l = [1, 2, 3, 0, 0, 0]

k = [2, 5, 6]


def generate(numRows):
    res = [[1]]
    for i in range(numRows-1):
        res.append(list(map(lambda x, y: x+y, [0]+res[i], res[i]+[0])))
    return res

print(generate(5))
