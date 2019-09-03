class Solution:
    def findOrder(self, numCourses, prerequisites):
        indegree = [0 for _ in range(numCourses)]
        adj_list = {i: [] for i in range(numCourses)}

        for link in prerequisites:
            adj_list[link[1]].append(link[0])
            indegree[link[0]] += 1

        zero_degree = []
        for i in range(numCourses):
            if indegree[i] == 0:
                zero_degree.append(i)

        i = 0
        while i < len(zero_degree):
            for node in adj_list[zero_degree[i]]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    zero_degree.append(node)
            i += 1
        if len(zero_degree) == numCourses:
            return zero_degree
        else:
            return []


if __name__ == "__main__":
    print(Solution().findOrder(2, [[1, 0]]))
