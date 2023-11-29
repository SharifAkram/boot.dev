class Graph:
    def bfs_path(self, start, end):
        visited = []
        to_visit = [start]
        path = {start: None}
        while to_visit:
            current_vertex = to_visit.pop(0)
            visited.append(current_vertex)
            if current_vertex == end:
                path_list = []
                while current_vertex is not None:
                    path_list.append(current_vertex)
                    current_vertex = path[current_vertex]
                path_list.reverse()
                return path_list
            sorted_neighbors = sorted(self.graph[current_vertex])
            for neighbor in sorted_neighbors:
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)
                    path[neighbor] = current_vertex
        return None

        # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result
