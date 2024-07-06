// Benchmark "top" written by ABC on Sun Jun 16 00:03:18 2024

module top ( 
    \opcode[0] , \opcode[1] , \opcode[2] , \opcode[3] , \opcode[4] ,
    \op_ext[0] , \op_ext[1] ,
    \sel_reg_dst[0] , \sel_reg_dst[1] , \sel_alu_opB[0] , \sel_alu_opB[1] ,
    \alu_op[0] , \alu_op[1] , \alu_op[2] , \alu_op_ext[0] ,
    \alu_op_ext[1] , \alu_op_ext[2] , \alu_op_ext[3] , halt, reg_write,
    sel_pc_opA, sel_pc_opB, beqz, bnez, bgez, bltz, jump, Cin, invA, invB,
    mem_write, sel_wb  );
  input  \opcode[0] , \opcode[1] , \opcode[2] , \opcode[3] , \opcode[4] ,
    \op_ext[0] , \op_ext[1] ;
  output \sel_reg_dst[0] , \sel_reg_dst[1] , \sel_alu_opB[0] ,
    \sel_alu_opB[1] , \alu_op[0] , \alu_op[1] , \alu_op[2] ,
    \alu_op_ext[0] , \alu_op_ext[1] , \alu_op_ext[2] , \alu_op_ext[3] ,
    halt, reg_write, sel_pc_opA, sel_pc_opB, beqz, bnez, bgez, bltz, jump,
    Cin, invA, invB, mem_write, sel_wb;
  wire n33, n34, n35, n36, n37, n38, n40, n41, n42, n43, n44, n45, n46, n48,
    n49, n50, n51, n52, n54, n55, n56, n57, n58, n60, n61, n62, n63, n64,
    n65, n66, n67, n69, n70, n72, n73, n74, n75, n77, n78, n80, n81, n82,
    n84, n85, n86, n88, n90, n91, n92, n95, n96, n101, n106, n107, n108,
    n109, n110, n112, n113, n115, n118;
  wire n33, n34, n35, n36, n37, n38, n40, n41, n42, n43, n44, n45, n46, n48,
    n49, n50, n51, n52, n54, n55, n56, n57, n58, n60, n61, n62, n63, n64,
    n65, n66, n67, n69, n70, n72, n73, n74, n75, n77, n78, n80, n81, n82,
    n84, n85, n86, n88, n90, n91, n92, n95, n96, n101, n106, n107, n108,
    n109, n110, n112, n113, n115, n118;
  INV_X1    g00(.A(\opcode[0] ), .ZN(n33));
  INV_X1    g01(.A(\opcode[1] ), .ZN(n34));
  NAND2_X1  g02(.A1(\opcode[4] ), .A2(\opcode[3] ), .ZN(n35));
  AOI21_X1  g03(.A(n35), .B1(n34), .B2(n33), .ZN(n36));
  OR2_X1    g04(.A1(\opcode[4] ), .A2(\opcode[3] ), .ZN(n37));
  OAI21_X1  g05(.A(n35), .B1(n37), .B2(n34), .ZN(n38));
  MUX2_X1   g06(.S(\opcode[2] ), .B(n38), .A(n36), .Z(\sel_reg_dst[0] ));
  INV_X1    g07(.A(\opcode[2] ), .ZN(n40));
  OAI21_X1  g08(.A(n34), .B1(n35), .B2(\opcode[0] ), .ZN(n41));
  INV_X1    g09(.A(\opcode[4] ), .ZN(n42));
  NOR2_X1   g10(.A1(n42), .A2(\opcode[3] ), .ZN(n43));
  OAI21_X1  g11(.A(n41), .B1(n43), .B2(n34), .ZN(n44));
  OAI21_X1  g12(.A(\opcode[1] ), .B1(\opcode[4] ), .B2(\opcode[3] ), .ZN(n45));
  AOI21_X1  g13(.A(n40), .B1(n45), .B2(\opcode[1] ), .ZN(n46));
  AOI21_X1  g14(.A(n46), .B1(n44), .B2(n40), .ZN(\sel_reg_dst[1] ));
  INV_X1    g15(.A(n41), .ZN(n48));
  XOR2_X1   g16(.A(\opcode[4] ), .B(\opcode[3] ), .Z(n49));
  INV_X1    g17(.A(n49), .ZN(n50));
  NAND2_X1  g18(.A1(n42), .A2(\opcode[3] ), .ZN(n51));
  MUX2_X1   g19(.S(\opcode[0] ), .B(n51), .A(n50), .Z(n52));
  AOI211_X1 g20(.A(n48), .B(\opcode[2] ), .C1(\opcode[1] ), .C2(n52), .ZN(\sel_alu_opB[0] ));
  INV_X1    g21(.A(\opcode[3] ), .ZN(n54));
  AOI21_X1  g22(.A(n34), .B1(\opcode[4] ), .B2(n54), .ZN(n55));
  OR3_X1    g23(.A1(\opcode[4] ), .A2(\opcode[3] ), .A3(\opcode[0] ), .ZN(n56));
  OAI21_X1  g24(.A(n56), .B1(n49), .B2(n33), .ZN(n57));
  AOI21_X1  g25(.A(n55), .B1(n57), .B2(n34), .ZN(n58));
  MUX2_X1   g26(.S(n40), .B(n58), .A(n43), .Z(\sel_alu_opB[1] ));
  NAND4_X1  g27(.A1(\opcode[4] ), .A2(\opcode[3] ), .A3(n33), .A4(\op_ext[0] ), .ZN(n60));
  NOR3_X1   g28(.A1(\op_ext[1] ), .A2(\opcode[4] ), .A3(n54), .ZN(n61));
  INV_X1    g29(.A(\op_ext[0] ), .ZN(n62));
  INV_X1    g30(.A(\op_ext[1] ), .ZN(n63));
  AOI211_X1 g31(.A(n54), .B(n63), .C1(n62), .C2(\opcode[4] ), .ZN(n64));
  OAI21_X1  g32(.A(\opcode[0] ), .B1(n64), .B2(n61), .ZN(n65));
  AOI21_X1  g33(.A(n34), .B1(n65), .B2(n60), .ZN(n66));
  NOR3_X1   g34(.A1(n42), .A2(\opcode[3] ), .A3(n33), .ZN(n67));
  MUX2_X1   g35(.S(\opcode[2] ), .B(n67), .A(n66), .Z(\alu_op[0] ));
  AOI211_X1 g36(.A(n54), .B(n34), .C1(\opcode[4] ), .C2(n63), .ZN(n69));
  NOR3_X1   g37(.A1(n42), .A2(\opcode[3] ), .A3(n34), .ZN(n70));
  MUX2_X1   g38(.S(\opcode[2] ), .B(n70), .A(n69), .Z(\alu_op[1] ));
  INV_X1    g39(.A(n35), .ZN(n72));
  AOI21_X1  g40(.A(\opcode[1] ), .B1(\opcode[4] ), .B2(\opcode[3] ), .ZN(n73));
  NAND2_X1  g41(.A1(n73), .A2(n37), .ZN(n74));
  AOI21_X1  g42(.A(\opcode[0] ), .B1(\opcode[4] ), .B2(\opcode[3] ), .ZN(n75));
  AOI22_X1  g43(.A1(n75), .A2(n37), .B1(\opcode[0] ), .B2(n37), .ZN(n77));
  OAI21_X1  g44(.A(n74), .B1(n77), .B2(n34), .ZN(n78));
  MUX2_X1   g45(.S(n40), .B(n78), .A(n72), .Z(\alu_op[2] ));
  OR4_X1    g46(.A1(\opcode[2] ), .A2(\opcode[1] ), .A3(\opcode[0] ), .A4(n35), .ZN(n80));
  NOR2_X1   g47(.A1(\opcode[1] ), .A2(n33), .ZN(n81));
  AOI22_X1  g48(.A1(n72), .A2(n81), .B1(\opcode[1] ), .B2(n57), .ZN(n82));
  OAI21_X1  g49(.A(n80), .B1(n82), .B2(n40), .ZN(\alu_op_ext[0] ));
  NAND3_X1  g50(.A1(\opcode[4] ), .A2(n54), .A3(n33), .ZN(n84));
  OR3_X1    g51(.A1(n84), .A2(\opcode[2] ), .A3(n34), .ZN(n85));
  OR3_X1    g52(.A1(n49), .A2(n40), .A3(n34), .ZN(n86));
  NAND2_X1  g53(.A1(n86), .A2(n85), .ZN(\alu_op_ext[1] ));
  MUX2_X1   g54(.S(\opcode[1] ), .B(n84), .A(n35), .Z(n88));
  AOI21_X1  g55(.A(n46), .B1(n88), .B2(n40), .ZN(\alu_op_ext[2] ));
  AOI21_X1  g56(.A(n40), .B1(\opcode[4] ), .B2(n54), .ZN(n90));
  OAI21_X1  g57(.A(n54), .B1(n42), .B2(n33), .ZN(n91));
  AOI221_X1 g58(.A(\opcode[2] ), .B1(n37), .B2(n73), .C1(\opcode[1] ), .C2(n91), .ZN(n92));
  NOR2_X1   g59(.A1(n92), .A2(n90), .ZN(\alu_op_ext[3] ));
  NOR4_X1   g60(.A1(\opcode[2] ), .A2(\opcode[1] ), .A3(\opcode[0] ), .A4(n37), .ZN(halt));
  MUX2_X1   g61(.S(n34), .B(n91), .A(n37), .Z(n95));
  OAI21_X1  g62(.A(n42), .B1(\opcode[3] ), .B2(n34), .ZN(n96));
  MUX2_X1   g63(.S(\opcode[2] ), .B(n96), .A(n95), .Z(reg_write));
  NOR3_X1   g64(.A1(n37), .A2(n40), .A3(n33), .ZN(sel_pc_opA));
  NOR3_X1   g65(.A1(n37), .A2(n40), .A3(\opcode[0] ), .ZN(sel_pc_opB));
  NOR4_X1   g66(.A1(n40), .A2(\opcode[1] ), .A3(\opcode[0] ), .A4(n51), .ZN(beqz));
  OAI21_X1  g67(.A(\opcode[0] ), .B1(\opcode[4] ), .B2(n54), .ZN(n101));
  AND4_X1   g68(.A1(\opcode[2] ), .A2(n34), .A3(\opcode[0] ), .A4(n101), .ZN(bnez));
  AND4_X1   g69(.A1(\opcode[2] ), .A2(\opcode[1] ), .A3(\opcode[0] ), .A4(n101), .ZN(bgez));
  NOR4_X1   g70(.A1(n40), .A2(n34), .A3(\opcode[0] ), .A4(n51), .ZN(bltz));
  NOR2_X1   g71(.A1(n37), .A2(n40), .ZN(jump));
  AOI21_X1  g72(.A(n54), .B1(n62), .B2(\opcode[4] ), .ZN(n106));
  AND2_X1   g73(.A1(\opcode[1] ), .A2(\opcode[0] ), .ZN(n107));
  AOI221_X1 g74(.A(\opcode[2] ), .B1(n101), .B2(n81), .C1(n107), .C2(n106), .ZN(n108));
  AOI21_X1  g75(.A(n35), .B1(\opcode[1] ), .B2(\opcode[0] ), .ZN(n109));
  NOR2_X1   g76(.A1(n109), .A2(n40), .ZN(n110));
  NOR2_X1   g77(.A1(n110), .A2(n108), .ZN(Cin));
  AOI21_X1  g78(.A(\opcode[1] ), .B1(n101), .B2(\opcode[0] ), .ZN(n112));
  OR4_X1    g79(.A1(\op_ext[1] ), .A2(n62), .A3(n33), .A4(n35), .ZN(n113));
  AOI211_X1 g80(.A(n112), .B(\opcode[2] ), .C1(\opcode[1] ), .C2(n113), .ZN(invA));
  OAI21_X1  g81(.A(n107), .B1(n64), .B2(n61), .ZN(n115));
  AOI21_X1  g82(.A(n110), .B1(n115), .B2(n40), .ZN(invB));
  NOR2_X1   g84(.A1(n67), .A2(n34), .ZN(n118));
  AOI211_X1 g85(.A(\opcode[2] ), .B(n118), .C1(n84), .C2(n34), .ZN(mem_write));
  AND3_X1   g86(.A1(n67), .A2(n40), .A3(n34), .ZN(sel_wb));
