import networkx as nx

class KDMGraphBuilder:

    def build(self, model, variables=None):

        graph = nx.DiGraph()

        graph.add_node(
            model["program"],
            type="Program"
        )

        for paragraph in model["paragraphs"]:

            graph.add_node(
                paragraph,
                type="Paragraph"
            )

            graph.add_edge(
                model["program"],
                paragraph,
                relation="contains"
            )

        for call in model["calls"]:

            graph.add_edge(
                "MAIN",
                call,
                relation="calls"
            )

        if variables is None:
            variables = []

        for variable in variables:

            graph.add_node(
                variable["name"],
                type="Variable"
            )

            graph.add_edge(
                model["program"],
                variable["name"],
                relation="contains"
            )

        return graph