po u// Benchmark "c17" written by ABC on Wed Oct 05 14:09:13 2022

module c17 ( 
    \1 , 2, 3, 6, 7,
    22, 23  );
  input  \1 , 2, 3, 6, 7;
  output 22, 23;
  wire n7, n8, n9, n11;
  INV_X1    g0(.A(2), .ZN(n7));
  NAND2_X1  g1(.A1(3), .A2(\1 ), .ZN(n8));
  AND2_X1   g2(.A1(6), .A2(3), .ZN(n9));
  OAI21_X1  g3(.A(n8), .B1(n9), .B2(n7), .ZN(22));
  INV_X1    g4(.A(7), .ZN(n11));
  AOI21_X1  g5(.A(n9), .B1(n11), .B2(n7), .ZN(23));
endmodule


