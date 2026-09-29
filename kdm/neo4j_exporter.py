from neo4j import GraphDatabase

class Neo4jExporter:

    def __init__(
        self,
        uri,
        username,
        password
    ):
        self.driver = GraphDatabase.driver(
            uri,
            auth=(username, password)
        )

    def close(self):
        self.driver.close()

    def create_program(
        self,
        program_name
    ):
        with self.driver.session() as session:

            session.run(
                """
                MERGE (p:Program {name:$name})
                """,
                name=program_name
            )

    def create_paragraph(
        self,
        paragraph_name
    ):
        with self.driver.session() as session:

            session.run(
                """
                MERGE (p:Paragraph {name:$name})
                """,
                name=paragraph_name
            )

    def create_contains(
        self,
        program,
        paragraph
    ):
        with self.driver.session() as session:

            session.run(
                """
                MATCH (a:Program {name:$program})
                MATCH (b:Paragraph {name:$paragraph})

                MERGE (a)-[:CONTAINS]->(b)
                """,
                program=program,
                paragraph=paragraph
            )