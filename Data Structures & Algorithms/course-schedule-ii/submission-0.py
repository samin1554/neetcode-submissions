class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prereq = {c: [] for c in range(numCourses)}

        for course, req in prerequisites:
            prereq[course].append(req)

        output = []
        visited = set()
        cycle = set()

        def dfs(course):
            if course in visited:
                return True

            if course in cycle:
                return False

            cycle.add(course)

            for pre in prereq[course]:
                if dfs(pre) == False:
                    return False

            cycle.remove(course)
            visited.add(course)
            output.append(course)

            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return output