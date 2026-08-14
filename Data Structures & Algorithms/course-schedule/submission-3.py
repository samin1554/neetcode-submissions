class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_hashmap = {course: [] for course in range(numCourses)}

        for course, prerequisite in prerequisites:
            prereq_hashmap[course].append(prerequisite)

        visited = set()
        completed = set()

        def dfs(course):
            if course in completed:
                return True 
            
            if course in visited:
                return False 

            if not prereq_hashmap[course]:
                return True

            visited.add(course)

            for prereq in prereq_hashmap[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)
            completed.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


        # Prerequisits = [a, b]
        # if you want to take course b , must take a first 
        # required to take numCourses from 0 to Len(numcourses - 1)
        # True = finish all courses 
        # False = did not finish all courses 

        # [a,b] - > [0,1] -> 1 must be taken before 0 