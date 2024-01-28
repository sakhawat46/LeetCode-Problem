#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        temp_sum = 0
        divider = 0
        for i in salary:
            if i == salary[0] or i == salary[-1]:
                continue
            else:
                divider = divider + 1
                temp_sum = temp_sum + i
        result = temp_sum / divider
        return result

