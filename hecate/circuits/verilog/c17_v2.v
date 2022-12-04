// Benchmark "C17.iscas" written by ABC on Wed Nov 30 09:36:35 2022

module C17.iscas ( 
    \1GAT(0) , \2GAT(1) , \3GAT(2) , \6GAT(3) , \7GAT(4) ,
    \22GAT(10) , \23GAT(9)   );
  input  \1GAT(0) , \2GAT(1) , \3GAT(2) , \6GAT(3) , \7GAT(4) ;
  output \22GAT(10) , \23GAT(9) ;
  wire n7, n8, n9, n11;
  INV_X1    g0(.A(\2GAT(1) ), .ZN(n7));
  NAND2_X1  g1(.A1(\3GAT(2) ), .A2(\1GAT(0) ), .ZN(n8));
  AND2_X1   g2(.A1(\6GAT(3) ), .A2(\3GAT(2) ), .ZN(n9));
  OAI21_X1  g3(.A(n8), .B1(n9), .B2(n7), .ZN(\22GAT(10) ));
  INV_X1    g4(.A(\7GAT(4) ), .ZN(n11));
  AOI21_X1  g5(.A(n9), .B1(n11), .B2(n7), .ZN(\23GAT(9) ));
endmodule


