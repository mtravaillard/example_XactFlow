# XactFlow examples

Examples that show how to use the XactFlow tools to create IP-XACT files.

- [xml_to_design](xml_to_design/): creates an .xml IP-XACT design file from a library of .xml IP-XACT
  components and a archidesc Python script.
- [sv_to_design](sv_to_design/): creates the .xml IP-XACT components from SystemVerilog files, then
  creates the .xml IP-XACT design file that connects them with an archidesc Python script.

## Setup

Requires Python >= 3.9.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
