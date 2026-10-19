// Debug module: one APB target for its registers (regs), one APB initiator for
// system bus access (sba). Header only, no logic.
module debug (
    input  logic        clk_i,
    input  logic        rst_ni,

    // APB target regs
    input  logic [31:0] regs_paddr_i,
    input  logic [2:0]  regs_pprot_i,
    input  logic        regs_psel_i,
    input  logic        regs_penable_i,
    input  logic        regs_pwrite_i,
    input  logic [31:0] regs_pwdata_i,
    input  logic [3:0]  regs_pstrb_i,
    output logic        regs_pready_o,
    output logic [31:0] regs_prdata_o,
    output logic        regs_pslverr_o,

    // APB initiator sba
    output logic [31:0] sba_paddr_o,
    output logic [2:0]  sba_pprot_o,
    output logic        sba_psel_o,
    output logic        sba_penable_o,
    output logic        sba_pwrite_o,
    output logic [31:0] sba_pwdata_o,
    output logic [3:0]  sba_pstrb_o,
    input  logic        sba_pready_i,
    input  logic [31:0] sba_prdata_i,
    input  logic        sba_pslverr_i,

    output logic        debug_req_o
);
endmodule
