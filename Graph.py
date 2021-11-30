from networkx.generators.classic import null_graph
import pandas as pd
import folium

from noeud import Noeud

class Graph:

    def __init__(self) -> None:
        self.noeuds =[]
        self.arcs = {}

    def creerNoeuds(self,fichierNoeuds):

        for i, nlrow in fichierNoeuds.iterrows():
            self.noeuds.append(nlrow[0])
        print(self.noeuds)
        
    def creerArc(self,fichierNoeuds):
        for i, elrow in fichierNoeuds.iterrows():
            self.arcs.update({'src':elrow,'dst':elrow,'relationship':elrow,'cost':elrow[3]}),
        print(self.arcs)

    def getNoeud(self,name):
        if name in self.noeuds:
            print(self.noeuds)


#function to create and display the base map
def visualiserFolium(dessiner, points, locationpardefaut = [52.3791890, 4.899431], tiles='Stamen Toner', explored = None ):
    basemapp = folium.vector_layers.PolyLine(points, color='yellow', weight=3).add_to(basemap)
    return basemapp
    

nodeList = pd.read_csv("transport-nodes(1).csv")
edgelist =pd.read_csv("transport-relationships.csv")

G = Graph()
G.creerNoeuds(nodeList)
G.creerArc(edgelist)
G.getNoeud('Amsterdam')

# print(G.getNoeud('id'))
# G.visualiserFolium()

