# xml_to_design

Creates an .xml IP-XACT design file from .xml IP-XACT component files. A Python script lists the IPs and
how they are connected.

The `.xml` files are AI-generated and reviewed by me to match the `.sv` files in `sv_to_design/`.
They are not made with XactFlow-sv.

## Run

From this folder:

```bash
xactflow archidesc design.py --then design --output out/
```

Or, to also check the design with an elaboration, and write `out/soc_a.xml` if there is no error:

```bash
python build_and_check.py
```
