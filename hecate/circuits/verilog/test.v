module test (N1,N2,N3,N6,N7,N22,N23,N24);

input N1,N2,N3,N6,N7;

output N22,N23,N24;

wire N10,N11,N16,N19;

NAND2_X1 test1 (N10, N1, N3);
AND2_X1 test2 (N11, N3, N6);
NOR2_X1 test3 (N16, N2, N11);
OR2_X1 test4 (N19, N11, N7);
XOR2_X1 schvittz (N22, N10, N16);
HA_X1 paulo (N24, N23, N16, N19);

endmodule