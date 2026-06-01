class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses

        for dest, src in prerequisites:
            adj_list[src].append(dest)
            in_degree[dest] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0]) 

        order = []

        while queue:
            curr = queue.popleft()
            order.append(curr)

            for neighbor in adj_list[curr]:

                in_degree[neighbor] -= 1  

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == numCourses else []             
