class ModernizationPlanner:

    def generate_plan(
        self,
        architecture,
        business_rules
    ):

        plan = []

        plan.append(
            "Convert COBOL paragraphs to Java service methods"
        )

        plan.append(
            "Convert WORKING-STORAGE SECTION to Java POJOs"
        )

        plan.append(
            "Convert file access to repository layer"
        )

        plan.append(
            "Preserve extracted business rules"
        )

        for rule in business_rules:

            plan.append(
                f"Validate rule during migration: {rule}"
            )

        return plan