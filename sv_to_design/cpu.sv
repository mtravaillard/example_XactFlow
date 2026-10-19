// CPU: one APB initiator. Header only, no logic.
module cpu (
    input  logic        clk_i,
    input  logic        rst_ni,

    // APB initiator
    output logic [31:0] paddr_o,
    output logic [2:0]  pprot_o,
    output logic        psel_o,
    output logic        penable_o,
    output logic        pwrite_o,
    output logic [31:0] pwdata_o,
    output logic [3:0]  pstrb_o,
    input  logic        pready_i,
    input  logic [31:0] prdata_i,
    input  logic        pslverr_i,

    input  logic        irq_i,
    input  logic        debug_req_i
);
endmodule
