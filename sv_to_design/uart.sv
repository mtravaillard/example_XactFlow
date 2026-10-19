// UART: one APB target. Header only, no logic.
module uart #(
    parameter int BAUDRATE = 115200
) (
    input  logic        clk_i,
    input  logic        rst_ni,

    // APB target
    input  logic [31:0] paddr_i,
    input  logic [2:0]  pprot_i,
    input  logic        psel_i,
    input  logic        penable_i,
    input  logic        pwrite_i,
    input  logic [31:0] pwdata_i,
    input  logic [3:0]  pstrb_i,
    output logic        pready_o,
    output logic [31:0] prdata_o,
    output logic        pslverr_o,

    output logic        tx_o,
    input  logic        rx_i,
    output logic        irq_o
);
endmodule
