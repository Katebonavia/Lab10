import networkx as nx

from database.DAO import DAO
from model.model import Model

myModel = Model()
nations = DAO.getAllNations()

nodes = DAO.getAllNodes(2000, myModel.getIdMap())
edges = DAO.getAllEdges(2000,myModel.getIdMap())

myModel.buildGraph(2000)
#print(nations)

#print(nodes)

#print(edges)

#print(myModel.getGraph())

#print(nx.number_connected_components(myModel.getGraph()))

#print(myModel.getDegreeNodes())

print(myModel.getConnections(2))