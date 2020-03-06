import itertools


def permutations(List):
    permutation = list(itertools.permutations(List))
    for combinations in permutation:
        print(combinations)


#x = [1, 2, 3]
#permutations(x)


def manual_permutations(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    combinations = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]
        for p in manual_permutations(remLst):
            combinations.append([m] + p)
    return combinations


data = list('1234')
global i
for i, p in enumerate(manual_permutations(data)):
    print(p)
print(str(i) + ' total combinations')
