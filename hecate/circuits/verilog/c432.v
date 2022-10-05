// Benchmark "c432" written by ABC on Wed Oct 05 09:29:34 2022

module c432 ( 
 \1 , 4, 8, 11, 14, 17, 21, 24, 27, 30, 34, 37, 40, 43, 47, 50, 53, 56, 60, 63, 66, 69, 73, 76, 79, 82, 86, 89, 92, 95, 99, 102, 105, 108, 112, 115, 223, 329, 370, 421, 430, 431, 432 );
 input \1,4,8,11,14,17,21,24,27,30,34,37,40,43,47,50,53,56,60,63,66,69,73,76,79,82,86,89,92,95,99,102,105,108,112,115;
 output 223,329,370,421,430,431,432;
 wire n43, n44, n45, n46, n47, n48, n49, n50, n51, n52, n53, n54;
 INV_X1 g000 (108, n43);
 NOR2_X1 g001 (n43, 102, n44);
 INV_X1 g002 (82, n45);
 INV_X1 g003 (95, n46);
 OAI22_X1 g004 (89, n46, n45, 76, n47);
 NOR2_X1 g005 (n47, n44, n48);
 INV_X1 g006 (4, n49);
 INV_X1 g007 (17, n50);
 OAI22_X1 g008 (11, n50, n49, \1 , n51);
 INV_X1 g009 (43, n52);
 NOR2_X1 g010 (n52, 37, n53);
 INV_X1 g011 (30, n54);
 NOR2_X1 g012 (n54, 24, n55);
 INV_X1 g013 (56, n56);
 INV_X1 g014 (69, n57);
 OAI22_X1 g015 (63, n57, n56, 50, n58);
 NOR4_X1 g016 (n55, n53, n51, n58, n59);
 AND2_X1 g017 (n59, n48, n60);
 INV_X1 g018 (n60, 223);
 INV_X1 g019 (112, n62);
 OR4_X1 g020 (n55, n53, n51, n58, n63);
 OAI22_X1 g021 (n47, n63, n43, 102, n64);
 NAND3_X1 g022 (n64, n62, 108, n65);
 NOR2_X1 g023 (n46, 89, n66);
 XNOR2_X1 g024 (n60, n66, n67);
 NOR2_X1 g025 (99, n46, n68);
 INV_X1 g026 (n68, n69);
 NOR2_X1 g027 (n45, 76, n70);
 XNOR2_X1 g028 (n60, n70, n71);
 NOR2_X1 g029 (86, n45, n72);
 INV_X1 g030 (n72, n73);
 OAI221_X1 g031 (n65, n69, n67, n73, n71, n74);
 NOR2_X1 g032 (n49, \ , n75);
 XOR2_X1 g033 (n60, n75, n76);
 NOR2_X1 g034 (8, n49, n77);
 AND2_X1 g035 (n77, n76, n78);
 NOR2_X1 g036 (n50, 11, n79);
 XOR2_X1 g037 (n60, n79, n80);
 NOR2_X1 g038 (21, n50, n81);
 AND2_X1 g039 (n81, n80, n82);
 INV_X1 g040 (47, n83);
 INV_X1 g041 (37, n84);
 OAI211_X1 g042 (n83, 43, n60, n53, n88);
 INV_X1 g043 (34, n89);
 INV_X1 g044 (24, n90);
 OAI211_X1 g045 (n89, 30, n60, n55, n94);
 INV_X1 g046 (73, n95);
 INV_X1 g047 (63, n96);
 NAND2_X1 g048 (69, n96, n97);
 AOI21_X1 g049 (n97, n59, n48, n99);
 OAI211_X1 g050 (n95, 69, n60, n99, n100);
 INV_X1 g051 (60, n101);
 INV_X1 g052 (50, n102);
 NAND2_X1 g053 (56, n102, n103);
 AOI21_X1 g054 (n103, n59, n48, n105);
 OAI211_X1 g055 (n101, 56, n60, n105, n106);
 NAND4_X1 g056 (n100, n94, n88, n106, n107);
 NOR4_X1 g057 (n82, n78, n74, n107, n108);
 INV_X1 g058 (n108, 329);
 XOR2_X1 g059 (n60, n70, n111);
 NOR2_X1 g060 (112, n43, n116);
 AND2_X1 g061 (n116, n64, n117);
 NOR2_X1 g062 (115, n43, n118);
 OAI211_X1 g063 (n64, n118, n117, n108, n119);
 NOR2_X1 g064 (n69, n67, n120);
 XNOR2_X1 g065 (n108, n120, n121);
 OR3_X1 g066 (n67, 105, n46, n122);
 NOR2_X1 g067 (n73, n71, n123);
 XNOR2_X1 g068 (n108, n123, n124);
 INV_X1 g069 (92, n125);
 NAND3_X1 g070 (n111, n125, 82, n126);
 OAI221_X1 g071 (n119, n122, n121, n126, n124, n127);
 XNOR2_X1 g072 (n108, n78, n128);
 NOR2_X1 g073 (14, n49, n129);
 NAND2_X1 g074 (n129, n76, n130);
 XNOR2_X1 g075 (n108, n82, n131);
 INV_X1 g076 (27, n132);
 NAND3_X1 g077 (n80, n132, 17, n133);
 OAI22_X1 g078 (n131, n133, n130, n128, n134);
 XOR2_X1 g079 (n108, n88, n135);
 INV_X1 g080 (53, n136);
 OAI211_X1 g081 (n136, 43, n60, n53, n137);
 XOR2_X1 g082 (n108, n94, n138);
 INV_X1 g083 (40, n139);
 OAI211_X1 g084 (n139, 30, n60, n55, n140);
 OAI22_X1 g085 (n138, n140, n137, n135, n141);
 XOR2_X1 g086 (n108, n100, n142);
 NOR2_X1 g087 (79, n57, n143);
 OAI21_X1 g088 (n143, n99, n60, n144);
 XOR2_X1 g089 (n108, n106, n145);
 INV_X1 g090 (66, n146);
 OAI211_X1 g091 (n146, 56, n60, n105, n147);
 OAI22_X1 g092 (n145, n147, n144, n142, n148);
 OR4_X1 g093 (n141, n134, n127, n148, 370);
 NAND2_X1 g094 (370, 14, n150);
 AOI221_X1 g095 (n49, 8, 329, \1 , 223, n151);
 OAI221_X1 g096 (56, n101, n108, n102, n60, n152);
 AOI21_X1 g097 (n152, 370, 66, n153);
 OAI221_X1 g098 (43, n83, n108, n84, n60, n154);
 AOI21_X1 g099 (n154, 370, 53, n155);
 INV_X1 g100 (86, n156);
 AOI21_X1 g101 (n45, 223, 76, n157);
 OAI21_X1 g102 (n157, n108, n156, n158);
 AOI21_X1 g103 (n158, 370, 92, n159);
 OAI221_X1 g104 (69, n95, n108, n96, n60, n160);
 AOI21_X1 g105 (n160, 370, 79, n161);
 NOR4_X1 g106 (n159, n155, n153, n161, n162);
 INV_X1 g107 (21, n163);
 AOI21_X1 g108 (n50, 223, 11, n164);
 OAI21_X1 g109 (n164, n108, n163, n165);
 AOI21_X1 g110 (n165, 370, 27, n166);
 OAI221_X1 g111 (30, n89, n108, n90, n60, n167);
 AOI21_X1 g112 (n167, 370, 40, n168);
 AOI21_X1 g113 (n43, 223, 102, n169);
 OAI21_X1 g114 (n169, n108, n62, n170);
 AOI21_X1 g115 (n170, 370, 115, n171);
 INV_X1 g116 (89, n172);
 OAI21_X1 g117 (95, n60, n172, n173);
 AOI221_X1 g118 (n173, 329, 99, 105, 370, n174);
 NOR4_X1 g119 (n171, n168, n166, n174, n175);
 AOI22_X1 g120 (n162, n175, n151, n150, 421);
 NOR4_X1 g121 (n141, n134, n127, n148, n177);
 INV_X1 g122 (n152, n178);
 OAI21_X1 g123 (n178, n177, n146, n179);
 INV_X1 g124 (n154, n180);
 OAI21_X1 g125 (n180, n177, n136, n181);
 OAI221_X1 g126 (n164, n108, n163, n132, n177, n182);
 INV_X1 g127 (n167, n183);
 OAI21_X1 g128 (n183, n177, n139, n184);
 NAND4_X1 g129 (n182, n181, n179, n184, 430);
 NAND4_X1 g130 (n161, n181, n179, n184, n186);
 NAND3_X1 g131 (n159, n181, n179, n187);
 NAND4_X1 g132 (n186, n184, n182, n187, 431);
 OAI221_X1 g133 (n157, n108, n156, n125, n177, n189);
 NAND4_X1 g134 (n184, n189, n181, n174, n190);
 AOI21_X1 g135 (n166, n184, n155, n191);
 NAND3_X1 g136 (n191, n190, n186, 432);
endmodule
