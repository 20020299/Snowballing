class Interval:
    def __init__(self, s=0, e=0):
        self.s = s
        self.e = e


def mycomp(interval):
    return interval.s


def insertNewInterval(Intervals, newInterval):
    ans = []
    n = len(Intervals)
    Intervals.append(newInterval)
    Intervals.sort(key=mycomp)

    index = 0
    for i in range(1, n + 1):
        if Intervals[index].e >= Intervals[i].s:
            Intervals[index].e = max(Intervals[index].e, Intervals[i].e)
        else:
            index += 1
            Intervals[index] = Intervals[i]

    for i in range(index + 1):
        print(Intervals[i].s, Intervals[i].e)
