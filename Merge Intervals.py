class Solution:
    def merge(self, intervals):
        res = sorted(intervals, key=lambda x: x[0])
        temp = []
        for i in range(len(res)-1):
            if res[i][-1] >= res[i+1][0]:
                last = max(res[i][-1], res[i+1][-1])
                res[i+1] = [res[i][0], last]
                temp.append(res[i])
        for v in temp:
            res.remove(v)
        return res
