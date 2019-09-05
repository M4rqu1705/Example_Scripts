class Node():
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children

    def __str__(self, level=0) -> str:
        ret = "├" + "───" * level + " " + repr(self.value) + "\n"
        for child in self.children:
            if isinstance(child, Node):
                ret += child.__str__(level+1)
            else:
                ret += "├" + "───" * (level+1) + " " + str(child) + "\n"
        return ret

    def __repr__(self):
        return '<tree node object>'
