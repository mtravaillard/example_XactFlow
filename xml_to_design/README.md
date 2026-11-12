# xml_to_design

Creates an .xml IP-XACT design file from .xml IP-XACT component files. A Python script lists the IPs and
how they are connected.

The `.xml` files are AI-generated and reviewed by me to match the `.sv` files in `sv_to_design/`.
They are not made with XactFlow-sv.

## Run

From this folder:

```bash
xactflow archidesc design.py --then design --output out/
xactflow archidesc design.py --then component --output out/
```

`Design("example.org:design:soc_a:1.0", ...)` names the SoC: the first command writes the design,
`out/example.org_design_soc_a.design_1.0.xml`, the second the component that contains it (the SoC
seen as one IP), `out/example.org_design_soc_a.component_1.0.xml`. `--then` takes one exporter, so
it is two commands.

Or, to also check the design by linking it to the library, and write both files if there is no
error:

```bash
python build_and_check.py
```
