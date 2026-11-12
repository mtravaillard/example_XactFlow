# sv_to_design

Creates an .xml IP-XACT design file from SystemVerilog files. Each `.sv` file comes with a JSON file
that gives what the SystemVerilog code does not say (VLNV, bus interfaces).

## Run

From this folder, first create one .xml IP-XACT component file for each `.sv` file:

```bash
xactflow sv <ip>.sv --option metadata=<ip>_ipxact.json --then component --output out/
```

Then create the design file, and the component file that contains it (the SoC seen as one IP).
`--then` takes one exporter, so it is two commands:

```bash
xactflow archidesc design.py --then design --output out/
xactflow archidesc design.py --then component --output out/
```

`Design("example.org:design:soc_b:1.0", ...)` names the SoC: the design is written to
`out/example.org_design_soc_b.design_1.0.xml` and its component to
`out/example.org_design_soc_b.component_1.0.xml`.

Or do everything in one command, it also checks the design by linking it to the library, and writes
the design and component files only if there is no error:

```bash
python build_and_check.py
```

## Bypassing .xml component files

`design.py` reads the .xml component files written in `out/`. So each `.sv` file is first read into
a Python component object, then written as an .xml IP-XACT component file, then read again to get
the same Python object back.
`design_from_sv.py` describes the same design, but reads the `.sv` and `.json` files directly:
the IP components stay in memory and no IP component file is written. It gives the same
design and SoC component files.

From this folder:

```bash
xactflow archidesc design_from_sv.py --then design --output out_in_memory/
xactflow archidesc design_from_sv.py --then component --output out_in_memory/
```

The files are written in `out_in_memory/`, not in `out/`: both runs give files with the same names, so
the second one would replace the first.
