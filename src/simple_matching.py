from coefficient import coefficient
from dstar import dstar_node

class simple_matching(coefficient):
    def __init__(self) -> None:
        pass

    def calculate(self, node:dstar_node) -> float:
        return ((node.ncf + node.nus)) / (node.ncf + node.ncs + node.nus + node.nuf)
