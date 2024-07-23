from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        res = []
        adjList = defaultdict(list)
        visited = set()
        cycle = set()
        
        for course, prereq in prerequisites:
            adjList[prereq].append(course)
        
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            
            for next_course in adjList[course]: 
                if not dfs(next_course):
                    return False
            
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res[::-1]  # Reverse the result to get the correct order


s = Solution()
# Courses must be taken in the order of their dependencies
print(s.findOrder(4, [[1, 0], [2, 1], [3, 2]]))
# Expected output: [3, 2, 1, 0]

