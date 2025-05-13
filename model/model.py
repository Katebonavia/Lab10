import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self._nations = DAO.getAllNations()
        self._idMapNationsCode={}
        self._idMapNationsName = {}
        for v in DAO.getAllNations():
            self._idMapNationsCode[v.CCode]=v
            self._idMapNationsName[v.StateNme]=v
    def getIdMap(self):
        return self._idMapNationsCode

    def buildGraph(self,anno):
        nodes = DAO.getAllNodes(anno, self._idMapNationsCode)
        edges = DAO.getAllEdges(anno, self._idMapNationsCode)
        self._graph.add_nodes_from(nodes)
        for e in edges:
            self._graph.add_edge(e.o1,e.o2)

    def getCompConnesse(self):
        return nx.number_connected_components(self.getGraph())

    def getDegreeNodes(self):
        nodesOrdinati = sorted(nx.degree(self._graph), key=lambda x: x[0].StateNme)
        return nodesOrdinati

    def getGraph(self):
        return self._graph

    def getNations(self):
        return  self._nations

    def getConnections(self, idInput):
        source = self._idMapNationsCode[idInput]
        conn = nx.node_connected_component(self._graph, source)
        return conn