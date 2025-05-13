from dataclasses import dataclass

from model.nation import Nation


@dataclass

class Edge:
    o1: Nation
    o2: Nation
