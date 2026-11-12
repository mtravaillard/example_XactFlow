from pathlib import Path
from xactflow import Library
from xactflow_archidesc import Design

here = Path(__file__).resolve().parent
library = Library.scan(here.parent / "bus_definitions", here / "out")

# Defining the design
design = Design("example.org:design:soc_b:1.0", library)

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

# Top-level I/Os
clk = design.add_port("in", "clk_i")
rst = design.add_port("in", "rst_ni")
for ip in (cpu, bus, uart, gpio, debug):
    design.connect(clk, ip.clk_i)
    design.connect(rst, ip.rst_ni)

design.add_port("out", "uart_tx_o", connect=uart.tx_o)
design.add_port("in", "uart_rx_i", connect=uart.rx_i)

design.add_port("in", "gpio_i", width=16, connect=gpio.gpio_i)
design.add_port("out", "gpio_o", width=16, connect=gpio.gpio_o)
design.add_port("out", "gpio_oe_o", width=16, connect=gpio.gpio_oe_o)

design.add_port("in", "jtag_tck_i", connect=debug.tck_i)
design.add_port("in", "jtag_tms_i", connect=debug.tms_i)
design.add_port("in", "jtag_trst_ni", connect=debug.trst_ni)
design.add_port("in", "jtag_tdi_i", connect=debug.tdi_i)
design.add_port("out", "jtag_tdo_o", connect=debug.tdo_o)
