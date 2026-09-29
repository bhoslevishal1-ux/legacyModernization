import re

class BusinessRuleExtractor:

    def extract(self, source):

        rules = []

        patterns = [

            (
                r'IF\s+.*AGE.*<\s*18',
                'Customer must be at least 18 years old'
            ),

            (
                r'IF\s+.*BALANCE.*<\s*0',
                'Account cannot have negative balance'
            ),

            (
                r'IF\s+.*CREDIT.*LIMIT',
                'Credit limit validation exists'
            )
        ]

        for regex, description in patterns:

            if re.search(
                regex,
                source,
                re.IGNORECASE
            ):
                rules.append(description)

        return rules
