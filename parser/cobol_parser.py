import re


class CobolParser:

    def __init__(self, source):
        self.source = source

    def extract_program(self):

        match = re.search(
            r'PROGRAM-ID\.\s+([A-Z0-9\-]+)',
            self.source,
            re.IGNORECASE
        )

        return match.group(1) if match else "UNKNOWN"

    def extract_paragraphs(self):

        paragraphs = []

        pattern = re.compile(
            r'^([A-Z0-9\-]+)\.\s*$',
            re.MULTILINE
        )

        for match in pattern.finditer(self.source):
            paragraphs.append(match.group(1))

        return paragraphs

    def extract_calls(self):

        calls = []

        pattern = re.compile(
            r'PERFORM\s+([A-Z0-9\-]+)',
            re.IGNORECASE
        )

        for match in pattern.finditer(self.source):
            calls.append(match.group(1))

        return calls

    def parse(self):

        return {
            "program": self.extract_program(),
            "paragraphs": self.extract_paragraphs(),
            "calls": self.extract_calls()
        }