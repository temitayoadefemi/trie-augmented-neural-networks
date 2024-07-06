

class Trie():
    def __init__(self, depth=1, node = None):
        # Initialize the Trie with a neural network and a specified depth.
        self.depth = depth
        self.node = node
        self.root = None
        

    def build_trie(self, current_depth=None):
        # Recursively build the Trie structure up to the specified depth.
        if current_depth is None:
            current_depth = self.depth  # Start with the max depth if not specified.

        if current_depth == 0:
            return None  # Base case: no more depth to build, return None.

        self.root = self.node # Create a new Trie node with the default network.
        self.root.left_child = self.build_trie(current_depth - 1)  # Recursively build the left child.
        self.root.right_child = self.build_trie(current_depth - 1)  # Recursively build the right child.
        return self.root  # Return the root of this sub-trie.
    
    def traverse_nodes(self, node):
        # Traverse the Trie and collect all neural networks from the nodes.
        nodes = []  # List to store neural networks.
        if node is None:
            return nodes  # If the node is None, return the empty list.

        nodes.append(node.neural_network)  # Add the current node's network to the list.
        nodes.extend(self.traverse_nodes(node.left_child))  # Recursively traverse the left child.
        nodes.extend(self.traverse_nodes(node.right_child))  # Recursively traverse the right child.
        return nodes  # Return the list of all networks.
