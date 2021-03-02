def partition(l):
    def run(left, right, current_level, aux):
        if current_level >= len(l):
            aux.append((left, right))
            return
        first = l[current_level]
        run(left + [first], right, current_level + 1, aux)
        run(left, right + [first], current_level + 1, aux)
    aux = []
    run([], [], 0, aux)
    # print(aux)
    # def minimal_differecne(aux):
    first = aux[0]
    l_perfect = aux[0]
    min = sum(first[0]) - sum(first[1])
    for i in range(1, len(aux)):
        total1 = sum(aux[i][0])
        total2 = sum(aux[i][1])
        if total2 == total1:
            return aux[i]
        minimal = abs(total1 - total2)
        if min > minimal:
            l_perfect = aux[i]
            min = minimal
    return l_perfect
    # minimal_differecne(aux)
    # print(minimal_differecne(aux))
l = [1, 3, 7, 11]
l2= [([1, 3, 7], []), ([1, 3], [7])]
# print(l2[0][0])
print(partition(l))