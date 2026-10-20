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
