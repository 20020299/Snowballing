import itertools


def findSubsets(s, n):
    return list(itertools.combinations(s, n))
