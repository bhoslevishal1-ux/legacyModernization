class ReportGenerator:

    def generate(
        self,
        architecture,
        business_rules,
        variables
    ):

        report = []

        report.append(
            "# COBOL Application Analysis\n"
        )

        report.append(
            "## Architecture\n"
        )

        for p in architecture["paragraphs"]:
            report.append(
                f"- {p}"
            )

        report.append(
            "\n## Variables\n"
        )

        for v in variables:

            report.append(
                f"- {v['name']}"
            )

        report.append(
            "\n## Business Rules\n"
        )

        for rule in business_rules:

            report.append(
                f"- {rule}"
            )

        return "\n".join(report)