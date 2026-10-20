import sys
from pathlib import Path
from xactflow import Library, Severity, elaborate
from xactflow_archidesc import ArchiDescImporter
from xactflow_component import ComponentExporter
from xactflow_design import DesignExporter
from xactflow_sv import SVImporter

here = Path(__file__).resolve().parent

# Generating one component file for each .sv file
for sv_file in sorted(here.glob("*.sv")):
    metadata = here / f"{sv_file.stem}_ipxact.json"
    component = SVImporter().import_(sv_file, metadata=metadata)
    ComponentExporter().export(component, here / "out")
    print(f"component written for {sv_file.name}")

library = Library.scan(here.parent / "bus_definitions", here / "out")

# Building the design from design.py
design = ArchiDescImporter().import_(here / "design.py")

# Elaborating the design against the library
elaborated = elaborate(design, library)
diagnostics = library.diagnostics + elaborated.diagnostics
for diagnostic in diagnostics:
    print(diagnostic)

if any(d.severity == Severity.ERROR for d in diagnostics):
    print("elaboration failed, design not exported")
    sys.exit(1)

print(f"elaborated with no errors ({len(elaborated.instances)} instances, "
      f"{len(elaborated.interconnections)} interconnections)")

# Writing the design file
DesignExporter().export(design, here / "out")
print(f"design written to {here / 'out'}")
