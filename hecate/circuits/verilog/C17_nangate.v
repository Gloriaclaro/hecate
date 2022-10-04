// Verilog
// c17
// Ninputs 5
// Noutputs 2
// NtotalGates 6
// NAND2 6

module c17 (N1,N2,N3,N6,N7,N22,N23);

input N1,N2,N3,N6,N7;

output N22,N23;

wire N10,N11,N16,N19;

NAND2_X1 NAND2_1 (N10, N1, N3);
NAND2_X1 NAND2_2 (N11, N3, N6);
NAND2_X1 NAND2_3 (N16, N2, N11);
NAND2_X1 NAND2_4 (N19, N11, N7);
NAND2_X1 NAND2_5 (N22, N10, N16);
NAND2_X1 NAND2_6 (N23, N16, N19);

endmodule