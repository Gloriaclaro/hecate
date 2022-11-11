// Verilog
// schvittz
// Ninputs 2
// Noutputs 1
// NtotalGates 3
// INV 2
// NAND2 1

module schvittz (N1,N2,N3,N22);

input N1,N2,N3;

output N7;

wire N3,N4;

INV_X1 INV_1 (N4, N1);
INV_X1 INV_2 (N5, N2);
INV_X1 INV_3 (N6, N3);
AOI21_X1 AOI21_1 (N7, N6, N5, N4);

endmodule