import csv
from os import get_terminal_size
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import folium
 
#Utilisez la bibliothéque pandas pour lire le fichier transport-nodes.csv

edgelist =pd.read_csv("transport-relationships.csv")

# Utilisez la bibliothéque pandas pour lire le fichier transport-relationships.csv

nodeList = pd.read_csv("transport-nodes(1).csv")

# Construisez le graphe et le visualiser avec la fonction from_pandas_dataframe de networkx
df= edgelist[['src','dst']]
g = nx.Graph()
g = nx.from_pandas_edgelist(df,'src','dst')

node_tail = []

for i in g.nodes:
    t = 0
        # while j < len(nodeList.id):
    for j in nodeList.id:
        
        if i == j:
            node_tail.append(nodeList.population[t]/1000)
        t = t+1



plt.figure(figsize=(4, 3))
nx.draw(g,with_labels=True,node_size=node_tail,node_color='yellow')
plt.show()


#Ajouter des attributs longitude et latitude aux noeuds avec Networkx en utilisant:
# - le dictionnaire "node" de networkx qui contient les noeuds
# - le dataframe transportnode defini plus haut

def ajouterAttribut(myGraphe, dfnode, nameAttr, Index):
    for node in myGraphe.nodes:
        myGraphe.add_nodes_from([
            (node, {
                nameAttr:
                dfnode[(dfnode[Index] == node)][nameAttr].values[0],
            }),
        ])

ajouterAttribut(g,nodeList,'latitude','id')
ajouterAttribut(g,nodeList,'longitude','id')
ajouterAttribut(g,nodeList,'population','id')
print(dict(g.nodes.data()))



def construirePointsImage(myGraphe):
    points = []
    for i in myGraphe.nodes:
        for neighbor in myGraphe.neighbors(i):
            points.append()
        return points

coordonneesvoisins = construirePointsImage(g)
print(coordonneesvoisins)
           