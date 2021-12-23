def smallerNumbersThanCurrent(arr):
    num = []
    for k in range(len(arr)):
        num.append(0)
    for i in range(len(arr)):
        counter = 0
        for j in range(len(arr)):
            if arr[j] < arr[i]:
                counter += 1
            num[i] = counter
    return num
