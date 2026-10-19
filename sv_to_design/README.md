# sv_to_design

Creates an .xml IP-XACT design file from SystemVerilog files. Each `.sv` file comes with a JSON file
that gives what the SystemVerilog code does not say (VLNV, bus interfaces, registers).

## Run

First, create one .xml IP-XACT component file for each `.sv` file:

```bash
xactflow sv <ip>.sv --option metadata=<ip>_ipxact.json --then component --output library/
```

Then create the design file:

```bash
xactflow archidesc design.py --then design --output out/
```
