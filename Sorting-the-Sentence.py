def sortSentence(str):
    str = str.split()
    sorted = []
    for j in range(len(str)):
        sorted.append(str[j])
    for i in str:
        word = i[:-1]
        order = i[-1]
        sorted[(int(order))-1] = word
    sorted = " ".join(sorted)
    return sorted
