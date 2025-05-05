class BullyAlgorithm:
    def __init__(self, node_id, nodes):
        self.id = node_id
        self.nodes = nodes

    def start_election(self):
        higher_nodes = [n for n in self.nodes if n > self.id]
        if higher_nodes:
            for n in higher_nodes:
                print(f"Node {self.id} sends Election to Node {n}")
                print(f"Node {self.id} waits for OK from Node {n}")
                print(f"Node {self.id} receives OK from Node {n}")
            new_coordinator = max(higher_nodes)
            print(f"Node {self.id} sends Coordinator message to Node {new_coordinator}")
        else:
            print(f"Node {self.id} becomes the new Coordinator")

nodes = [1, 2, 3, 4, 5]
BullyAlgorithm(3, nodes).start_election()
