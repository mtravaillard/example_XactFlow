import sys
from pathlib import Path
from xactflow import Library, Severity, link
from xactflow_archidesc import ArchiDescImporter
from xactflow_design import DesignExporter

here = Path(__file__).resolve().parent
library = Library.scan(here.parent / "bus_definitions", here)

# Building the design from design.py
design = ArchiDescImporter().import_(here / "design.py")

# Linking the design against the library
linked = link(design, library)
diagnostics = library.diagnostics + linked.diagnostics
for diagnostic in diagnostics:
    print(diagnostic)

if any(d.severity == Severity.ERROR for d in diagnostics):
    print("linking failed, design not exported")
    sys.exit(1)

print(f"linked with no errors ({len(linked.instances)} instances, "
      f"{len(linked.interconnections)} interconnections)")

# Writing the design file
DesignExporter().export(design, here / "out")
print(f"design written to {here / 'out'}")
