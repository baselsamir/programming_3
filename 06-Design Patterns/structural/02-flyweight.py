class Tree:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def display(self, x, y):
        print(f"Tree: {self.name}, Color: {self.color}, Position: ({x}, {y})")


class TreeFactory:
    tree_types = {}

    @staticmethod
    def get_tree_type(name, color):
        if (name, color) not in TreeFactory.tree_types:
            TreeFactory.tree_types[(name, color)] = Tree(name, color)
        return TreeFactory.tree_types[(name, color)]


class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, name, color, x, y):
        tree_type = TreeFactory.get_tree_type(name, color)
        tree_type.display(x, y)
        self.trees.append(tree_type)

    def display_forest(self):
        for tree in self.trees:
            tree.display(0, 0)


# Client code
forest = Forest()
forest.plant_tree("Oak", "Green", 10, 20)
forest.plant_tree("Oak", "Green", 30, 40)
forest.plant_tree("Pine", "Green", 50, 60)

forest.display_forest()