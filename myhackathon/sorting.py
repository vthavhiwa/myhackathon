def bubble_sort(items):
    """Return array of items, sorted in ascending order"""
    count = 0
    for item in range(len(items)-1):
        if items[item] > items[item + 1]:
            items[item],items[item + 1] = items[item + 1],items[item]
            count += 1
    if count == 0:
        return items
    else:
        return bubbleSort(items)

def merge_sort(items):
    """Return array of items, sorted in ascending order"""

    if len(items) < 2:
        return items
    result = []          # moved!
    mid = int(len(items) / 2)
    y = merge_sort(items[:mid])
    z = merge_sort(items[mid:])
    while (len(y) > 0) and (len(z) > 0):
        if y[0] > z[0]:
            result.append(z[0])
            z.pop(0)
        else:
            result.append(y[0])
            y.pop(0)
    result += y
    result += z
    return result

def quick_sort(items):
    """Return array of items, sorted in ascending order"""
    if len(items) == 0:
        return items
    p = len(items) // 2
    l = [i for i in items if i < items[p]]
    m = [i for i in items if i == items[p]]
    r = [i for i in items if i > items[p]]
    return quick_sort(l) + m + quick_sort(r)
