import os

os.environ["MPLCONFIGDIR"] = "./tmp"

import matplotlib.pyplot as plt
import networkx as nx


class GraphVisualizer:

    def draw(self, graph):

        plt.figure(figsize=(12, 8))

        pos = nx.spring_layout(graph)

        nx.draw(
            graph,
            pos,
            with_labels=True,
            node_color="lightblue",
            node_size=4000,
            font_size=8
        )

        plt.savefig("architecture.png")