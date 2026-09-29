class ArchitectureAnalyzer:

    def analyze(self, graph):

        result = {
            "programs": [],
            "paragraphs": []
        }

        for node, attrs in graph.nodes(data=True):

            node_type = attrs.get("type")

            if node_type == "Program":
                result["programs"].append(node)

            if node_type == "Paragraph":
                result["paragraphs"].append(node)

        return result