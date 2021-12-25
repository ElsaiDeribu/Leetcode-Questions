def kClosest(arr, k):
    for i in range(len(arr)):
        distance = ((arr[i][0])**2 + (arr[i][1])**2)**0.5
        arr[i].append(distance)
        arr[i] = arr[i][::-1]
    arr.sort()
    for j in range(len(arr)):
        arr[j] = arr[j][1:]
        arr[j] = arr[j][::-1]
    arr = arr[0:k]
    return arr
