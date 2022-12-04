// Benchmark "c17" written by ABC on Thu Dec 01 09:41:44 2022

module c17 ( 
    \1 , 2, 3, 6, 7,
    22, 23  );
  input  \1 , 2, 3, 6, 7;
  output 22, 23;
  wire n7, n8, n9, n10, n11, n12, n13, n14, n16, n17, n18;
  INV_X1    g00(.A(\1 ), .ZN(n7));
  INV_X1    g01(.A(3), .ZN(n8));
  NOR2_X1   g02(.A1(n8), .A2(n7), .ZN(n9));
  INV_X1    g03(.A(2), .ZN(n10));
  INV_X1    g04(.A(6), .ZN(n11));
  NOR2_X1   g05(.A1(n11), .A2(n8), .ZN(n12));
  NOR2_X1   g06(.A1(n12), .A2(n10), .ZN(n13));
  NOR2_X1   g07(.A1(n13), .A2(n9), .ZN(n14));
  INV_X1    g08(.A(n14), .ZN(22));
  INV_X1    g09(.A(7), .ZN(n16));
  NOR2_X1   g10(.A1(n12), .A2(n16), .ZN(n17));
  NOR2_X1   g11(.A1(n17), .A2(n13), .ZN(n18));
  INV_X1    g12(.A(n18), .ZN(23));
endmodule


