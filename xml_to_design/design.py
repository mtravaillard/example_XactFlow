from pathlib import Path
from xactflow import Library
from xactflow_archidesc import Design

here = Path(__file__).resolve().parent
library = Library.scan(here.parent / "bus_definitions", here)

# Defining the design
design = Design("example.org:design:soc_a:1.0", library)

# Adding IPs
cpu = design.add_ip("cpu", "example.org:ip:cpu:1.0")
bus = design.add_ip("bus", "example.org:ip:apb_interconnect:1.0")
uart = design.add_ip("uart", "example.org:ip:uart:1.0", parameters={"BAUDRATE": 9600})
gpio = design.add_ip("gpio", "example.org:ip:gpio:1.0", parameters={"DATA_W": 16})
debug = design.add_ip("debug", "example.org:ip:debug:1.0")

# Initiators to the interconnect
design.connect_bus(cpu, bus.bus("s0"))
design.connect_bus(debug.bus("sba"), bus.bus("s1"))

# Interconnect to the targets
design.connect_bus(bus.bus("m0"), uart, base_addr=0x4000_0000, size=0x1000)
design.connect_bus(bus.bus("m1"), gpio, base_addr=0x4000_1000, size=0x1000)
design.connect_bus(bus.bus("m2"), debug.bus("regs"), base_addr=0x4000_2000, size=0x1000)

# AdHoc Connections
design.connect(uart.irq_o, cpu.irq_i)
design.connect(debug.debug_req_o, cpu.debug_req_i)
