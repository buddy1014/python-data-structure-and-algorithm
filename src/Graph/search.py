from collections import deque

graph = dict()
graph['A'] = ['B', 'G', 'D']
graph['B'] = ['A', 'F', 'E']
graph['C'] = ['F', 'H']
graph['D'] = ['F', 'A']
graph['E'] = ['B', 'G']
graph['F'] = ['B', 'D', 'C']
graph['G'] = ['A', 'E']
graph['H'] = ['C']


def breadth_first_search(graph_arg, root):
    visited_vertices = list()
    graph_queue = deque([root])
    visited_vertices.append(root)

    while len(graph_queue) > 0:
        node = graph_queue.popleft()
        adj_nodes = graph_arg[node]
        remaining_vertices = set(adj_nodes).difference(set(visited_vertices))
        if len(remaining_vertices) > 0:
            for adj_node in remaining_vertices:
                visited_vertices.append(adj_node)
                graph_queue.append(adj_node)

    return visited_vertices


# TODO: fix this function
# def depth_first_search(graph_arg, root):
#     visited_vertices = list()
#     graph_stack = list()
#
#     graph_stack.append(root)
#     node = root
#
#     while len(graph_stack) > 0:
#         if node not in visited_vertices:
#             visited_vertices.append(node)
#
#         adj_nodes = graph_arg[node]
#
#         # if set(adj_nodes).issubset(set(visited_vertices)):
#         graph_stack.pop()
#
#         if len(graph_stack) > 0:
#             node = graph_stack[-1]
#             continue
#         else:
#             remaining_vertices = set(adj_nodes).difference(set(visited_vertices))
#             first_adj_node = sorted(remaining_vertices)[0]
#             graph_stack.append(first_adj_node)
#             node = first_adj_node
#
#     return visited_vertices


# print(breadth_first_search(graph, 'A'))

