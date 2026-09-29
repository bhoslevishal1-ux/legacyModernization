import re

class DataDivisionExtractor:

    def extract(
        self,
        source
    ):

        variables = []

        pattern = re.compile(
            r'\d+\s+([A-Z0-9\-]+)\s+PIC\s+([A-Z0-9\(\)V]+)',
            re.IGNORECASE
        )

        for match in pattern.finditer(source):

            variables.append(
                {
                    "name": match.group(1),
                    "picture": match.group(2)
                }
            )

        return variables