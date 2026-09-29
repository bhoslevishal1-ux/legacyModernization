from pathlib import Path

from parser.cobol_parser import CobolParser
from kdm.graph_builder import KDMGraphBuilder
from analysis.business_rules import BusinessRuleExtractor
from analysis.architecture import ArchitectureAnalyzer
from modernization.planner import ModernizationPlanner


source = Path(
    "sample/CUSTOMER.cbl"
).read_text()

parser = CobolParser(source)

model = parser.parse()

from analysis.data_division import DataDivisionExtractor

variables = DataDivisionExtractor().extract(
    source
)

graph = KDMGraphBuilder().build(
    model,
    variables
)

rules = BusinessRuleExtractor().extract(source)

architecture = ArchitectureAnalyzer().analyze(graph)

plan = ModernizationPlanner().generate_plan(
    architecture,
    rules
)

print("\nPROGRAM")
print(model["program"])

print("\nPARAGRAPHS")
for p in model["paragraphs"]:
    print("-", p)

print("\nBUSINESS RULES")
for rule in rules:
    print("-", rule)

print("\nMODERNIZATION PLAN")
for step in plan:
    print("-", step)


print("\nVARIABLES")

for v in variables:

    print(
        v["name"],
        v["picture"]
    )




from analysis.report_generator import ReportGenerator

report = ReportGenerator().generate(
    architecture,
    rules,
    variables
)

with open(
    "analysis_report.md",
    "w"
) as file:

    file.write(report)

print(
    "\nReport saved."
)


from analysis.graph_visualizer import GraphVisualizer

GraphVisualizer().draw(graph)