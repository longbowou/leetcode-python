# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/description/
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# 
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
# 
#  
# 
# Example 1:
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:
# 
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
#  
# 
# Constraints:
# 
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
# O( N + P) N: node P: Prerequisites
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        crs_visited = set()

        def dfs(crs):
            if pre_map[crs] == []:
                return True

            if crs in crs_visited:
                return False

            crs_visited.add(crs)
            for pre_crs in pre_map[crs]:
                if not dfs(pre_crs):
                    return False
            crs_visited.remove(crs)

            pre_map[crs] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
