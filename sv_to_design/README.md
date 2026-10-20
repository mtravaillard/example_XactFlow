# sv_to_design

Creates an .xml IP-XACT design file from SystemVerilog files. Each `.sv` file comes with a JSON file
that gives what the SystemVerilog code does not say (VLNV, bus interfaces).

## Run

From this folder, first create one .xml IP-XACT component file for each `.sv` file:

```bash
xactflow sv <ip>.sv --option metadata=<ip>_ipxact.json --then component --output out/
```

Then create the design file:

```bash
xactflow archidesc design.py --then design --output out/
```

Or do everything in one command, it also checks the design with an elaboration, and writes
`out/soc_b.xml` only if there is no error:

```bash
python build_and_check.py
```

## Bypassing .xml component files

`design.py` reads the .xml component files written in `out/`. So each `.sv` file is first read into
a Python component object, then written as an .xml IP-XACT component file, then read again to get
the same Python object back.
`design_from_sv.py` describes the same design, but reads the `.sv` and `.json` files directly:
the components stay in memory and no component file is written. It gives the same `out/soc_b.xml`.

From this folder:

```bash
xactflow archidesc design_from_sv.py --then design --output out/
```
