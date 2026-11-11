import sys
from pathlib import Path
import ipxact
from xactflow import Library, Severity, link
from xactflow_archidesc import ArchiDescImporter
from xactflow_component import ComponentExporter
from xactflow_design import DesignExporter

here = Path(__file__).resolve().parent
library = Library.scan(here.parent / "bus_definitions", here)

# Building the design, and the component containing it, from design.py
ArchiDescImporter().import_(here / "design.py", library)
[design] = library.targets(ipxact.Design)

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

# Writing the design file and the component file
DesignExporter().export(library, here / "out")
ComponentExporter().export(library, here / "out")
print(f"design and component written to {here / 'out'}")
