import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
from dfs_bfs_iterative import bfs_iterative, dfs_iterative, dijkstra_iterative

library_malvina_coords = (46.8483985,35.3752914)

nodes = {
    "FIZ_FAQ_TDATU": 1374602845,
    "CENTRAL_MARKET": 463015689
}


G_Melitopol_Maliatko_District = ox.graph_from_point(
    library_malvina_coords,
    dist=500,
    network_type="drive"
)

adj_list_G_Melitopol_Maliatko_District = {node: list(G_Melitopol_Maliatko_District.adj[node]) for node in G_Melitopol_Maliatko_District.nodes}

melitopol_maliatko_nodes = G_Melitopol_Maliatko_District.nodes()
melitopol_maliatko_edges = G_Melitopol_Maliatko_District.edges()
print ("""
This Graph represents the schema of drive ways of one of the central districts of Melitopol, Ukraine.
It is oriented graph, so the edges are directed.
Each edge has a length attribute, which represents the distance between the two nodes, so it can be used as a weight in shortest path algorithms.
The alhorythm tries to find the shortest root from the Kafedra Fizvykhovannya ta Sportu TDATU to the Rynok Zrazkovyy.
You can use following link to the Google Maps for your reference:
https://www.google.com/maps/dir/46.85004,35.377096/Kafedra+Fizvykhovannya+I+Sportu+Tdatu,+Bohdana+Khmelnytskoho+Ave,+Melitopol%27,+Zaporizhia+Oblast,+Ukraine,+72300/Chernyshevs%27koho+St,+33,+Melitopol%27,+Zaporiz%27ka+oblast,+Ukraine,+72300/46.844243,35.381728/@46.8467847,35.3780345,17z/data=!4m16!4m15!1m0!1m5!1m1!1s0x40c2ae033b947f61:0xa8992e906def74ff!2m2!1d35.3770781!2d46.8494847!1m5!1m1!1s0x40c2ae1b6da682bf:0xd43527a0df040455!2m2!1d35.3779805!2d46.8462294!1m0!3e0?entry=ttu&g_ep=EgoyMDI1MTIwOS4wIKXMDSoKLDEwMDc5MjA2OUgBUAM%3D
""")

print("********************************************************")
print(f" Nodes quantity: {len(melitopol_maliatko_nodes)}, Edges quantity: {len(melitopol_maliatko_edges)}")
# Nodes quantity: 19, Edges quantity: 45
print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print("Nodes:")
print(melitopol_maliatko_nodes)
print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print("Edges:")
print(melitopol_maliatko_edges)
print("********************************************************")

# Dijkstra
dijkstra = nx.single_source_dijkstra_path(G_Melitopol_Maliatko_District, source=nodes['FIZ_FAQ_TDATU'])
print("********************************************************")
print("Dijkstra nx (Shortest path node list):")
print(dijkstra)
print("Dijkstra custom (Distance in meters):")
print(dijkstra_iterative(G_Melitopol_Maliatko_District, nodes['FIZ_FAQ_TDATU']))
print("********************************************************")

# Shortest path
path = nx.shortest_path(G_Melitopol_Maliatko_District, source=nodes['FIZ_FAQ_TDATU'], target=nodes['CENTRAL_MARKET'], weight='length')
path_length = nx.shortest_path_length(G_Melitopol_Maliatko_District, source=nodes['FIZ_FAQ_TDATU'], target=nodes['CENTRAL_MARKET'], weight='length')
print("********************************************************")
print("Shortest path:")
print(path)
print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print("Shortest path length:")
print(path_length)
print("********************************************************")

# DFS
dfs_tree = nx.dfs_tree(G_Melitopol_Maliatko_District, source=nodes['FIZ_FAQ_TDATU'])
print("********************************************************")
print("DFS nx:")
print(list(dfs_tree.nodes()))  # виведе ребра DFS-дерева з коренем у вузлі FIZ_FAQ_TDATU
print("DFS custom:")
print(dfs_iterative(adj_list_G_Melitopol_Maliatko_District, nodes['FIZ_FAQ_TDATU']))
print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''")

# BFS
bfs_tree = nx.bfs_tree(G_Melitopol_Maliatko_District, source=nodes['FIZ_FAQ_TDATU'])
print("BFS nx:")
print(list(bfs_tree.nodes()))  # виведе ребра BFS-дерева з коренем у вузлі FIZ_FAQ_TDATU
print("BFS custom:")
print(bfs_iterative(adj_list_G_Melitopol_Maliatko_District, nodes['FIZ_FAQ_TDATU']))
print("********************************************************")


# Visualize the graph and the shortest path
fig, ax = ox.plot_graph_route(G_Melitopol_Maliatko_District, path, route_linewidth=6, node_size=2, bgcolor="white", show=False, close=False)
for u, v in zip(path[:-1], path[1:]):
    edge_data = G_Melitopol_Maliatko_District.get_edge_data(u, v)

    name = edge_data[0]["name"]

    x = (G_Melitopol_Maliatko_District.nodes[u]["x"] + G_Melitopol_Maliatko_District.nodes[v]["x"]) / 2
    y = (G_Melitopol_Maliatko_District.nodes[u]["y"] + G_Melitopol_Maliatko_District.nodes[v]["y"]) / 2

    ax.text(
        x, y, name,
        fontsize=6,
        color="blue"
    )

plt.show()
