// APB interconnect: two APB targets (s0, s1), three APB initiators (m0, m1, m2).
// Header only, no logic.
module apb_interconnect (
    input  logic        clk_i,
    input  logic        rst_ni,

    // APB target s0
    input  logic [31:0] s0_paddr_i,
    input  logic [2:0]  s0_pprot_i,
    input  logic        s0_psel_i,
    input  logic        s0_penable_i,
    input  logic        s0_pwrite_i,
    input  logic [31:0] s0_pwdata_i,
    input  logic [3:0]  s0_pstrb_i,
    output logic        s0_pready_o,
    output logic [31:0] s0_prdata_o,
    output logic        s0_pslverr_o,

    // APB target s1
    input  logic [31:0] s1_paddr_i,
    input  logic [2:0]  s1_pprot_i,
    input  logic        s1_psel_i,
    input  logic        s1_penable_i,
    input  logic        s1_pwrite_i,
    input  logic [31:0] s1_pwdata_i,
    input  logic [3:0]  s1_pstrb_i,
    output logic        s1_pready_o,
    output logic [31:0] s1_prdata_o,
    output logic        s1_pslverr_o,

    // APB initiator m0
    output logic [31:0] m0_paddr_o,
    output logic [2:0]  m0_pprot_o,
    output logic        m0_psel_o,
    output logic        m0_penable_o,
    output logic        m0_pwrite_o,
    output logic [31:0] m0_pwdata_o,
    output logic [3:0]  m0_pstrb_o,
    input  logic        m0_pready_i,
    input  logic [31:0] m0_prdata_i,
    input  logic        m0_pslverr_i,

    // APB initiator m1
    output logic [31:0] m1_paddr_o,
    output logic [2:0]  m1_pprot_o,
    output logic        m1_psel_o,
    output logic        m1_penable_o,
    output logic        m1_pwrite_o,
    output logic [31:0] m1_pwdata_o,
    output logic [3:0]  m1_pstrb_o,
    input  logic        m1_pready_i,
    input  logic [31:0] m1_prdata_i,
    input  logic        m1_pslverr_i,

    // APB initiator m2
    output logic [31:0] m2_paddr_o,
    output logic [2:0]  m2_pprot_o,
    output logic        m2_psel_o,
    output logic        m2_penable_o,
    output logic        m2_pwrite_o,
    output logic [31:0] m2_pwdata_o,
    output logic [3:0]  m2_pstrb_o,
    input  logic        m2_pready_i,
    input  logic [31:0] m2_prdata_i,
    input  logic        m2_pslverr_i
);
endmodule
