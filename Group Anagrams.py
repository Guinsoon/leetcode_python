# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/10/1 下午2:30
@desc: Bigo
"""
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)

