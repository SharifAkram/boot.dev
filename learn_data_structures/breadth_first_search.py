class Graph:
    def breadth_first_search(self, v):
        visited = []
        to_visit = []
        to_visit.append(v)
        while to_visit:
            s = to_visit.pop(0)
            visited.append(s)
            sorted_neighbors = sorted(self.graph[s])
            for neighbor in sorted_neighbors:
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)
        return visited
