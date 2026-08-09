# used help

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # build adjacency list
        adj = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre)
        
        # courses along current dfs path
        visiting = set()

        def dfs(course: int) -> bool:
            # is it possible to take this particular course?
            if adj[course] == []:
                return True
            if course in visiting:
                return False
            
            visiting.add(course)
            for pre in adj[course]:
                if not dfs(pre): return False
            visiting.remove(course)
            adj[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

