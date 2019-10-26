#Author: Nawal Ahmed
import networkx as nx
import pylab # Matplotlib
import matplotlib.pyplot as plt

# This displays a graph and uses Dijkstra's algorithm to determine the shortest path from A to G

G = nx.DiGraph() # Directed Graph

# Add edges and weights to the graph
G.add_edges_from([('A','B')], weight=8) , G.add_edges_from([('A','C')], weight=6)
G.add_edges_from([('B','D')], weight=10) , G.add_edges_from([('C','D')], weight=15)
G.add_edges_from([('C','E')], weight=9) , G.add_edges_from([('D','F')], weight=4)
G.add_edges_from([('D','E')], weight=14) , G.add_edges_from([('E','F')], weight=13)
G.add_edges_from([('E','G')], weight=17) , G.add_edges_from([('F','G')], weight=7)

edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in G.edges(data=True)])

# Place nodes at certain coordinates
node_locations = {'A':(0,2),'B':(0,1),'C':(1,2),'D':(1,1),'E':(2,2),'F':(2,1),'G':(3,1)}
node_placements = node_locations.keys()

fig = plt.figure()
pos = nx.spring_layout(G,pos=node_locations, fixed = node_placements)
nx.draw_networkx_edge_labels(G,pos, edge_labels=edge_labels)
nx.draw(G,pos, node_color = 'yellow', node_size=300 , edge_color='black')
fig.set_facecolor("#FFFFFF")
node_labels = {node:node for node in G.nodes()}; nx.draw_networkx_labels(G, pos, labels=node_labels)

print("The shortest path from A to G is through the nodes:" , nx.dijkstra_path(G, 'A', 'G'))

pylab.show()