#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0 and high % 2 ==0:
            result = (high + 1) - low
            return result // 2
        else:
            result = (high + 1) - (low - 1)
            return result // 2

