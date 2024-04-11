from coefficient import coefficient
from dstar import dstar_node

class kulczynski(coefficient):
    def __init__(self) -> None:
        pass

    def calculate(self, node:dstar_node) -> float:
        if (node.nuf + node.ncs == 0): 
            return (node.ncf * node.ncf)
        return ((node.ncf * node.ncf) / (node.nuf + node.ncs))
