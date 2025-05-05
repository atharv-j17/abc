class TokenRing:
    def __init__(self, nodes):
        self.nodes = nodes

    def run(self):
        token = self.nodes
        i = 0
        while True:
            if token:
                print(f"Node {i}: Received token with data '{token}'")
                print(f"Node {i}: Processing '{self.nodes[i]}'")
                i = (i + 1) % len(self.nodes)
                token = self.nodes[i]
                self.nodes[i] = None
                if i == 0 and token is None:
                    break

ring = TokenRing(["Data 1", "Data 2", "Data 3", "Data 4"])
ring.run()
