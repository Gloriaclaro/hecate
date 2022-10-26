// Verilog
// schvittz
// Ninputs 2
// Noutputs 1
// NtotalGates 3
// INV 2
// NAND2 1

module schvittz (N1,N2,N22);

input N1,N2;

output N22;

wire N3,N4;

INV_X1 INV_1 (N3, N1);
INV_X1 INV_2 (N4, N2);
NAND2_X1 NAND2_1 (N22, N3, N4);

endmodule