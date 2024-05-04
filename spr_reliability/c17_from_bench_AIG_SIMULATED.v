// Benchmark "EXPERIMENTO-C17/c17_from_bench" written by ABC on Wed Jan 31 04:17:56 2024

module \EXPERIMENTO-C17/c17_from_bench  ( 
    pi0, pi1, pi2, pi3, pi4,
    po0, po1  );
  input  pi0, pi1, pi2, pi3, pi4;
  output po0, po1;
  wire new_n8, new_n9, new_n10, new_n11, new_n12, new_n13, new_n14, new_n16,
    new_n17, new_n18;
  AND2x2_ASAP7_75t_R  g00(.A(pi2), .B(pi3), .Y(new_n8));
  INVx1_ASAP7_75t_R   g01(.A(new_n8), .Y(new_n9));
  AND2x2_ASAP7_75t_R  g02(.A(pi1), .B(new_n9), .Y(new_n10));
  INVx1_ASAP7_75t_R   g03(.A(new_n10), .Y(new_n11));
  AND2x2_ASAP7_75t_R  g04(.A(pi0), .B(pi2), .Y(new_n12));
  INVx1_ASAP7_75t_R   g05(.A(new_n12), .Y(new_n13));
  AND2x2_ASAP7_75t_R  g06(.A(new_n13), .B(new_n11), .Y(new_n14));
  INVx1_ASAP7_75t_R   g07(.A(new_n14), .Y(po0));
  AND2x2_ASAP7_75t_R  g08(.A(pi4), .B(new_n9), .Y(new_n16));
  INVx1_ASAP7_75t_R   g09(.A(new_n16), .Y(new_n17));
  AND2x2_ASAP7_75t_R  g10(.A(new_n11), .B(new_n17), .Y(new_n18));
  INVx1_ASAP7_75t_R   g11(.A(new_n18), .Y(po1));
endmodule


