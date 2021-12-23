def targetIndices(arr, target):
    indexes = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    for k in range(len(arr)):
        if arr[k] == target:
            indexes.append(k)

    return indexes
