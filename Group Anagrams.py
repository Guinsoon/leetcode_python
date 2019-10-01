# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/10/1 下午2:30
@desc: Bigo
"""
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        out = defaultdict(list)
        for item in strs:
            k = "".join(sorted(item))
            out[k].append(item)
        res = []
        for _, values in out.items():
            res.append(values)
        return res


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))

