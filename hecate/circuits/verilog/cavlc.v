// Benchmark "top" written by ABC on Sun Jun 16 00:02:50 2024

module top ( 
    \totalcoeffs[0] , \totalcoeffs[1] , \totalcoeffs[2] , \totalcoeffs[3] ,
    \totalcoeffs[4] , \ctable[0] , \ctable[1] , \ctable[2] ,
    \trailingones[0] , \trailingones[1] ,
    \coeff_token[0] , \coeff_token[1] , \coeff_token[2] , \coeff_token[3] ,
    \coeff_token[4] , \coeff_token[5] , \ctoken_len[0] , \ctoken_len[1] ,
    \ctoken_len[2] , \ctoken_len[3] , \ctoken_len[4]   );
  input  \totalcoeffs[0] , \totalcoeffs[1] , \totalcoeffs[2] ,
    \totalcoeffs[3] , \totalcoeffs[4] , \ctable[0] , \ctable[1] ,
    \ctable[2] , \trailingones[0] , \trailingones[1] ;
  output \coeff_token[0] , \coeff_token[1] , \coeff_token[2] ,
    \coeff_token[3] , \coeff_token[4] , \coeff_token[5] , \ctoken_len[0] ,
    \ctoken_len[1] , \ctoken_len[2] , \ctoken_len[3] , \ctoken_len[4] ;
  wire n21, n22, n23, n24, n25, n26, n27, n28, n29, n30, n31, n32, n33, n34,
    n35, n36, n37, n38, n39, n40, n41, n42, n43, n44, n45, n46, n47, n48,
    n49, n50, n51, n52, n53, n54, n55, n56, n57, n58, n59, n60, n61, n62,
    n63, n64, n65, n66, n67, n68, n69, n70, n71, n72, n73, n74, n75, n76,
    n77, n78, n79, n80, n81, n82, n83, n84, n85, n86, n87, n88, n89, n90,
    n91, n92, n93, n95, n96, n97, n98, n99, n100, n101, n102, n103, n104,
    n105, n106, n107, n108, n109, n110, n111, n112, n113, n114, n115, n116,
    n117, n118, n119, n120, n121, n122, n123, n124, n125, n126, n127, n128,
    n129, n130, n131, n132, n133, n134, n135, n136, n137, n138, n139, n140,
    n141, n142, n143, n144, n145, n146, n147, n148, n149, n150, n151, n152,
    n153, n154, n156, n157, n158, n159, n160, n161, n162, n163, n164, n165,
    n166, n167, n168, n169, n170, n171, n172, n173, n174, n175, n176, n177,
    n178, n179, n180, n181, n182, n183, n184, n185, n186, n187, n188, n189,
    n190, n191, n192, n193, n194, n195, n196, n197, n198, n199, n200, n201,
    n202, n203, n204, n205, n206, n207, n208, n209, n211, n212, n213, n214,
    n215, n216, n217, n218, n219, n220, n221, n222, n223, n224, n225, n226,
    n227, n228, n229, n230, n231, n232, n233, n234, n235, n236, n237, n238,
    n239, n240, n241, n242, n243, n244, n245, n246, n247, n248, n249, n250,
    n251, n252, n253, n254, n256, n257, n258, n259, n261, n262, n263, n265,
    n266, n267, n268, n269, n270, n271, n272, n273, n274, n275, n276, n277,
    n278, n279, n280, n281, n282, n283, n284, n285, n286, n287, n288, n289,
    n290, n291, n292, n293, n294, n295, n296, n297, n298, n299, n300, n301,
    n302, n303, n305, n307, n308, n309, n310, n311, n312, n313, n314, n315,
    n316, n317, n319, n320, n321, n322, n323, n324, n325, n326, n327, n328,
    n329, n330, n331, n332, n333, n334, n335, n336, n337, n338, n339, n340,
    n341, n342, n343, n344, n345, n346, n347, n348, n349, n351, n352, n353,
    n354, n355, n356, n357, n358, n359, n360, n361, n362, n363, n364, n365,
    n366, n367, n368, n369, n370, n371, n372, n373, n374, n375, n376, n377,
    n378, n379, n380, n381, n382, n383, n385, n386, n387, n388, n389, n390,
    n391, n392, n393, n394, n395, n396, n397, n398, n399, n400, n401, n402,
    n404, n405, n406;
  INV_X1    g000(.A(\ctable[1] ), .ZN(n21));
  INV_X1    g001(.A(\ctable[2] ), .ZN(n22));
  INV_X1    g002(.A(\totalcoeffs[2] ), .ZN(n23));
  INV_X1    g003(.A(\totalcoeffs[0] ), .ZN(n24));
  INV_X1    g004(.A(\totalcoeffs[1] ), .ZN(n25));
  AOI21_X1  g005(.A(n25), .B1(\trailingones[1] ), .B2(n24), .ZN(n26));
  INV_X1    g006(.A(\trailingones[1] ), .ZN(n27));
  NOR2_X1   g007(.A1(\ctable[0] ), .A2(\totalcoeffs[3] ), .ZN(n28));
  OAI21_X1  g008(.A(n28), .B1(n27), .B2(\totalcoeffs[1] ), .ZN(n29));
  AOI21_X1  g009(.A(\totalcoeffs[1] ), .B1(n27), .B2(\totalcoeffs[0] ), .ZN(n30));
  OAI21_X1  g010(.A(n22), .B1(\trailingones[1] ), .B2(n25), .ZN(n31));
  OAI22_X1  g011(.A1(n30), .A2(n31), .B1(n29), .B2(n26), .ZN(n32));
  NOR2_X1   g012(.A1(\totalcoeffs[3] ), .A2(\totalcoeffs[2] ), .ZN(n33));
  INV_X1    g013(.A(n33), .ZN(n34));
  AND2_X1   g014(.A1(\totalcoeffs[3] ), .A2(\totalcoeffs[0] ), .ZN(n35));
  AOI21_X1  g015(.A(n35), .B1(n34), .B2(\trailingones[1] ), .ZN(n36));
  OR2_X1    g016(.A1(\ctable[0] ), .A2(\totalcoeffs[2] ), .ZN(n37));
  AOI22_X1  g017(.A1(\totalcoeffs[2] ), .A2(\totalcoeffs[1] ), .B1(n24), .B2(n37), .ZN(n38));
  INV_X1    g018(.A(\totalcoeffs[3] ), .ZN(n39));
  NAND2_X1  g019(.A1(n39), .A2(\totalcoeffs[1] ), .ZN(n40));
  OAI221_X1 g020(.A(n40), .B1(n36), .B2(\totalcoeffs[1] ), .C1(\trailingones[1] ), .C2(n38), .ZN(n41));
  AOI22_X1  g021(.A1(n32), .A2(n23), .B1(n22), .B2(n41), .ZN(n42));
  NAND2_X1  g022(.A1(\trailingones[0] ), .A2(\ctable[2] ), .ZN(n43));
  NOR2_X1   g023(.A1(n43), .A2(\ctable[0] ), .ZN(n44));
  AOI21_X1  g024(.A(n44), .B1(\trailingones[1] ), .B2(n22), .ZN(n45));
  NOR2_X1   g025(.A1(\trailingones[1] ), .A2(\ctable[0] ), .ZN(n46));
  OAI21_X1  g026(.A(n46), .B1(\ctable[2] ), .B2(n25), .ZN(n47));
  OAI21_X1  g027(.A(n47), .B1(n45), .B2(n25), .ZN(n48));
  NOR2_X1   g028(.A1(\totalcoeffs[2] ), .A2(n24), .ZN(n49));
  NOR2_X1   g029(.A1(\totalcoeffs[1] ), .A2(\totalcoeffs[0] ), .ZN(n50));
  AND3_X1   g030(.A1(n50), .A2(n27), .A3(\totalcoeffs[2] ), .ZN(n51));
  AOI22_X1  g031(.A1(n49), .A2(n48), .B1(n44), .B2(n51), .ZN(n52));
  OAI22_X1  g032(.A1(n42), .A2(\trailingones[0] ), .B1(\totalcoeffs[3] ), .B2(n52), .ZN(n53));
  INV_X1    g033(.A(\trailingones[0] ), .ZN(n54));
  AOI21_X1  g034(.A(\totalcoeffs[2] ), .B1(n27), .B2(\totalcoeffs[0] ), .ZN(n55));
  XNOR2_X1  g035(.A(\trailingones[1] ), .B(\totalcoeffs[0] ), .ZN(n56));
  NAND3_X1  g036(.A1(n56), .A2(n33), .A3(\totalcoeffs[1] ), .ZN(n57));
  OAI21_X1  g037(.A(n57), .B1(n55), .B2(n21), .ZN(n58));
  AND2_X1   g038(.A1(\trailingones[1] ), .A2(\totalcoeffs[2] ), .ZN(n59));
  INV_X1    g039(.A(n59), .ZN(n60));
  NAND3_X1  g040(.A1(n27), .A2(n23), .A3(\totalcoeffs[1] ), .ZN(n61));
  OR2_X1    g041(.A1(\totalcoeffs[3] ), .A2(\totalcoeffs[0] ), .ZN(n62));
  AOI211_X1 g042(.A(n21), .B(n62), .C1(n61), .C2(n60), .ZN(n63));
  AOI21_X1  g043(.A(n63), .B1(n58), .B2(\ctable[0] ), .ZN(n64));
  INV_X1    g044(.A(\ctable[0] ), .ZN(n65));
  NOR2_X1   g045(.A1(n27), .A2(\totalcoeffs[1] ), .ZN(n66));
  NOR2_X1   g046(.A1(\totalcoeffs[2] ), .A2(\totalcoeffs[0] ), .ZN(n67));
  AOI21_X1  g047(.A(\ctable[0] ), .B1(n67), .B2(n66), .ZN(n68));
  NAND4_X1  g048(.A1(\ctable[0] ), .A2(\totalcoeffs[2] ), .A3(\totalcoeffs[1] ), .A4(n56), .ZN(n69));
  OAI21_X1  g049(.A(n69), .B1(n68), .B2(n21), .ZN(n70));
  AOI21_X1  g050(.A(\totalcoeffs[1] ), .B1(\trailingones[1] ), .B2(n24), .ZN(n71));
  NAND4_X1  g051(.A1(\totalcoeffs[2] ), .A2(n25), .A3(\totalcoeffs[0] ), .A4(n27), .ZN(n72));
  OAI21_X1  g052(.A(n72), .B1(n71), .B2(\trailingones[0] ), .ZN(n73));
  AOI22_X1  g053(.A1(n70), .A2(\trailingones[0] ), .B1(n65), .B2(n73), .ZN(n74));
  NOR2_X1   g054(.A1(\totalcoeffs[3] ), .A2(n23), .ZN(n75));
  AOI22_X1  g055(.A1(n66), .A2(n75), .B1(n54), .B2(\totalcoeffs[1] ), .ZN(n76));
  NOR2_X1   g056(.A1(\trailingones[1] ), .A2(\totalcoeffs[1] ), .ZN(n77));
  OAI21_X1  g057(.A(\totalcoeffs[3] ), .B1(n21), .B2(\totalcoeffs[2] ), .ZN(n78));
  AOI21_X1  g058(.A(n59), .B1(n78), .B2(n77), .ZN(n79));
  OAI22_X1  g059(.A1(n76), .A2(\totalcoeffs[0] ), .B1(\trailingones[0] ), .B2(n79), .ZN(n80));
  NOR3_X1   g060(.A1(\totalcoeffs[3] ), .A2(\totalcoeffs[2] ), .A3(\totalcoeffs[0] ), .ZN(n81));
  NOR3_X1   g061(.A1(\trailingones[1] ), .A2(\trailingones[0] ), .A3(\totalcoeffs[1] ), .ZN(n82));
  AOI22_X1  g062(.A1(n81), .A2(n82), .B1(n80), .B2(n65), .ZN(n83));
  OAI221_X1 g063(.A(n83), .B1(n64), .B2(n54), .C1(n39), .C2(n74), .ZN(n84));
  AOI22_X1  g064(.A1(n53), .A2(n21), .B1(n22), .B2(n84), .ZN(n85));
  NOR3_X1   g065(.A1(\trailingones[1] ), .A2(\trailingones[0] ), .A3(\ctable[1] ), .ZN(n86));
  AND3_X1   g066(.A1(\trailingones[0] ), .A2(\ctable[1] ), .A3(\totalcoeffs[4] ), .ZN(n87));
  OR2_X1    g067(.A1(n87), .A2(n86), .ZN(n88));
  MUX2_X1   g068(.S(\trailingones[1] ), .B(\totalcoeffs[4] ), .A(\ctable[1] ), .Z(n89));
  AOI21_X1  g069(.A(\trailingones[0] ), .B1(\ctable[1] ), .B2(\ctable[0] ), .ZN(n90));
  AOI22_X1  g070(.A1(n89), .A2(n90), .B1(n88), .B2(\ctable[0] ), .ZN(n91));
  NOR3_X1   g071(.A1(\totalcoeffs[3] ), .A2(\totalcoeffs[2] ), .A3(\totalcoeffs[1] ), .ZN(n92));
  NAND3_X1  g072(.A1(n92), .A2(n22), .A3(n24), .ZN(n93));
  OAI22_X1  g073(.A1(n91), .A2(n93), .B1(n85), .B2(\totalcoeffs[4] ), .ZN(\coeff_token[0] ));
  INV_X1    g074(.A(\totalcoeffs[4] ), .ZN(n95));
  AND4_X1   g075(.A1(\trailingones[0] ), .A2(\totalcoeffs[2] ), .A3(\totalcoeffs[0] ), .A4(\trailingones[1] ), .ZN(n96));
  NOR4_X1   g076(.A1(\trailingones[0] ), .A2(\totalcoeffs[2] ), .A3(\totalcoeffs[0] ), .A4(\trailingones[1] ), .ZN(n97));
  OAI21_X1  g077(.A(\ctable[0] ), .B1(n97), .B2(n96), .ZN(n98));
  OAI22_X1  g078(.A1(n54), .A2(\ctable[0] ), .B1(n21), .B2(n27), .ZN(n99));
  AND2_X1   g079(.A1(\trailingones[1] ), .A2(\ctable[1] ), .ZN(n100));
  MUX2_X1   g080(.S(\trailingones[0] ), .B(n100), .A(n46), .Z(n101));
  AOI21_X1  g081(.A(n101), .B1(n99), .B2(n24), .ZN(n102));
  OAI21_X1  g082(.A(n98), .B1(n102), .B2(n23), .ZN(n103));
  MUX2_X1   g083(.S(n54), .B(n65), .A(n95), .Z(n104));
  OAI22_X1  g084(.A1(n27), .A2(n95), .B1(\ctable[1] ), .B2(n104), .ZN(n105));
  AOI211_X1 g085(.A(\totalcoeffs[2] ), .B(\totalcoeffs[0] ), .C1(n21), .C2(\trailingones[1] ), .ZN(n106));
  AOI22_X1  g086(.A1(n105), .A2(n106), .B1(n103), .B2(n95), .ZN(n107));
  NAND2_X1  g087(.A1(\trailingones[0] ), .A2(\ctable[1] ), .ZN(n108));
  AND2_X1   g088(.A1(n108), .A2(\totalcoeffs[0] ), .ZN(n109));
  NOR4_X1   g089(.A1(\trailingones[0] ), .A2(n65), .A3(\totalcoeffs[0] ), .A4(n27), .ZN(n110));
  AOI21_X1  g090(.A(n110), .B1(n109), .B2(n99), .ZN(n111));
  NOR2_X1   g091(.A1(n54), .A2(\ctable[0] ), .ZN(n112));
  NOR2_X1   g092(.A1(\trailingones[0] ), .A2(\ctable[1] ), .ZN(n113));
  OAI21_X1  g093(.A(n23), .B1(n21), .B2(\totalcoeffs[0] ), .ZN(n114));
  AOI21_X1  g094(.A(n113), .B1(n114), .B2(n112), .ZN(n115));
  OAI22_X1  g095(.A1(n111), .A2(\totalcoeffs[2] ), .B1(\trailingones[1] ), .B2(n115), .ZN(n116));
  NOR4_X1   g096(.A1(n54), .A2(\ctable[1] ), .A3(n23), .A4(\trailingones[1] ), .ZN(n117));
  AOI21_X1  g097(.A(n117), .B1(n116), .B2(\totalcoeffs[1] ), .ZN(n118));
  OAI22_X1  g098(.A1(n107), .A2(\totalcoeffs[1] ), .B1(\totalcoeffs[4] ), .B2(n118), .ZN(n119));
  OR2_X1    g099(.A1(\trailingones[0] ), .A2(\totalcoeffs[2] ), .ZN(n120));
  MUX2_X1   g100(.S(\trailingones[0] ), .B(\ctable[0] ), .A(\totalcoeffs[3] ), .Z(n121));
  NAND2_X1  g101(.A1(n121), .A2(\totalcoeffs[0] ), .ZN(n122));
  OAI21_X1  g102(.A(n122), .B1(n120), .B2(n65), .ZN(n123));
  OAI21_X1  g103(.A(n23), .B1(n54), .B2(n39), .ZN(n124));
  NAND3_X1  g104(.A1(\trailingones[0] ), .A2(n23), .A3(\totalcoeffs[0] ), .ZN(n125));
  XNOR2_X1  g105(.A(\ctable[0] ), .B(\totalcoeffs[0] ), .ZN(n126));
  AOI21_X1  g106(.A(n25), .B1(n126), .B2(n125), .ZN(n127));
  AOI221_X1 g107(.A(n127), .B1(n123), .B2(n25), .C1(n24), .C2(n124), .ZN(n128));
  AOI21_X1  g108(.A(n23), .B1(\ctable[1] ), .B2(n25), .ZN(n129));
  NOR2_X1   g109(.A1(\trailingones[0] ), .A2(\totalcoeffs[1] ), .ZN(n130));
  NOR3_X1   g110(.A1(n130), .A2(n129), .A3(n39), .ZN(n131));
  AND2_X1   g111(.A1(\totalcoeffs[1] ), .A2(\totalcoeffs[0] ), .ZN(n132));
  NOR2_X1   g112(.A1(n54), .A2(\totalcoeffs[0] ), .ZN(n133));
  NOR2_X1   g113(.A1(\ctable[1] ), .A2(\totalcoeffs[1] ), .ZN(n134));
  NOR4_X1   g114(.A1(n133), .A2(n132), .A3(\totalcoeffs[2] ), .A4(n134), .ZN(n135));
  OAI21_X1  g115(.A(n65), .B1(n135), .B2(n131), .ZN(n136));
  OAI21_X1  g116(.A(n136), .B1(n128), .B2(\ctable[1] ), .ZN(n137));
  NAND2_X1  g117(.A1(n54), .A2(\ctable[0] ), .ZN(n138));
  NAND3_X1  g118(.A1(\totalcoeffs[3] ), .A2(\totalcoeffs[2] ), .A3(\totalcoeffs[1] ), .ZN(n139));
  OR2_X1    g119(.A1(\totalcoeffs[2] ), .A2(\totalcoeffs[1] ), .ZN(n140));
  OR3_X1    g120(.A1(n140), .A2(\trailingones[0] ), .A3(n39), .ZN(n141));
  OAI21_X1  g121(.A(n141), .B1(n65), .B2(n25), .ZN(n142));
  OAI21_X1  g122(.A(n139), .B1(n33), .B2(n65), .ZN(n143));
  AOI21_X1  g123(.A(n143), .B1(n142), .B2(\totalcoeffs[0] ), .ZN(n144));
  OAI22_X1  g124(.A1(n139), .A2(n138), .B1(n21), .B2(n144), .ZN(n145));
  MUX2_X1   g125(.S(\trailingones[1] ), .B(n145), .A(n137), .Z(n146));
  AOI22_X1  g126(.A1(n119), .A2(n39), .B1(n95), .B2(n146), .ZN(n147));
  AOI211_X1 g127(.A(\totalcoeffs[2] ), .B(n132), .C1(n27), .C2(\totalcoeffs[0] ), .ZN(n148));
  OAI21_X1  g128(.A(\totalcoeffs[2] ), .B1(\totalcoeffs[1] ), .B2(\totalcoeffs[0] ), .ZN(n149));
  NAND2_X1  g129(.A1(n149), .A2(n54), .ZN(n150));
  NAND4_X1  g130(.A1(\trailingones[0] ), .A2(n23), .A3(\totalcoeffs[1] ), .A4(n27), .ZN(n151));
  OAI21_X1  g131(.A(n151), .B1(n150), .B2(n148), .ZN(n152));
  AOI21_X1  g132(.A(n51), .B1(n152), .B2(\ctable[2] ), .ZN(n153));
  OR4_X1    g133(.A1(\ctable[0] ), .A2(\totalcoeffs[4] ), .A3(\totalcoeffs[3] ), .A4(\ctable[1] ), .ZN(n154));
  OAI22_X1  g134(.A1(n153), .A2(n154), .B1(n147), .B2(\ctable[2] ), .ZN(\coeff_token[1] ));
  OAI21_X1  g135(.A(\totalcoeffs[3] ), .B1(n54), .B2(\totalcoeffs[2] ), .ZN(n156));
  OAI21_X1  g136(.A(\totalcoeffs[3] ), .B1(\ctable[0] ), .B2(n23), .ZN(n157));
  AOI22_X1  g137(.A1(n156), .A2(\ctable[0] ), .B1(\trailingones[0] ), .B2(n157), .ZN(n158));
  OR2_X1    g138(.A1(\totalcoeffs[3] ), .A2(\totalcoeffs[1] ), .ZN(n159));
  OR4_X1    g139(.A1(\trailingones[0] ), .A2(n21), .A3(\ctable[0] ), .A4(n159), .ZN(n160));
  OAI21_X1  g140(.A(n160), .B1(n158), .B2(n25), .ZN(n161));
  NAND2_X1  g141(.A1(\trailingones[0] ), .A2(\totalcoeffs[1] ), .ZN(n162));
  AOI21_X1  g142(.A(\trailingones[1] ), .B1(n162), .B2(\ctable[1] ), .ZN(n163));
  NAND3_X1  g143(.A1(\trailingones[1] ), .A2(n54), .A3(n25), .ZN(n164));
  OAI21_X1  g144(.A(n164), .B1(n163), .B2(\totalcoeffs[2] ), .ZN(n165));
  AOI21_X1  g145(.A(n23), .B1(\trailingones[0] ), .B2(n21), .ZN(n166));
  AOI21_X1  g146(.A(n166), .B1(n124), .B2(n25), .ZN(n167));
  OAI22_X1  g147(.A1(\trailingones[0] ), .A2(n27), .B1(\totalcoeffs[3] ), .B2(n25), .ZN(n168));
  OAI211_X1 g148(.A(n21), .B(n168), .C1(n27), .C2(\totalcoeffs[3] ), .ZN(n169));
  NAND2_X1  g149(.A1(n54), .A2(\ctable[1] ), .ZN(n170));
  NAND3_X1  g150(.A1(\trailingones[1] ), .A2(n39), .A3(\totalcoeffs[1] ), .ZN(n171));
  OAI221_X1 g151(.A(n169), .B1(n167), .B2(n65), .C1(n171), .C2(n170), .ZN(n172));
  AOI221_X1 g152(.A(n172), .B1(n161), .B2(n27), .C1(\totalcoeffs[3] ), .C2(n165), .ZN(n173));
  AOI211_X1 g153(.A(\ctable[0] ), .B(n113), .C1(n27), .C2(\trailingones[0] ), .ZN(n174));
  OR3_X1    g154(.A1(n140), .A2(n95), .A3(\totalcoeffs[3] ), .ZN(n175));
  OAI22_X1  g155(.A1(n174), .A2(n175), .B1(n173), .B2(\totalcoeffs[4] ), .ZN(n176));
  NAND2_X1  g156(.A1(n65), .A2(\totalcoeffs[0] ), .ZN(n177));
  NOR2_X1   g157(.A1(\trailingones[1] ), .A2(\trailingones[0] ), .ZN(n178));
  AND3_X1   g158(.A1(\trailingones[1] ), .A2(\trailingones[0] ), .A3(\totalcoeffs[0] ), .ZN(n179));
  NOR2_X1   g159(.A1(n179), .A2(n178), .ZN(n180));
  MUX2_X1   g160(.S(\ctable[0] ), .B(n180), .A(n60), .Z(n181));
  XOR2_X1   g161(.A(\trailingones[1] ), .B(\trailingones[0] ), .Z(n182));
  OAI21_X1  g162(.A(\totalcoeffs[2] ), .B1(n182), .B2(n77), .ZN(n183));
  OAI21_X1  g163(.A(n183), .B1(n181), .B2(n25), .ZN(n184));
  OAI21_X1  g164(.A(\ctable[0] ), .B1(n39), .B2(\totalcoeffs[1] ), .ZN(n185));
  NAND3_X1  g165(.A1(n185), .A2(n178), .A3(n23), .ZN(n186));
  OR4_X1    g166(.A1(n27), .A2(n54), .A3(\totalcoeffs[1] ), .A4(n33), .ZN(n187));
  AOI21_X1  g167(.A(n24), .B1(n187), .B2(n186), .ZN(n188));
  AOI21_X1  g168(.A(n188), .B1(n184), .B2(n39), .ZN(n189));
  OR2_X1    g169(.A1(\trailingones[1] ), .A2(\trailingones[0] ), .ZN(n190));
  AND2_X1   g170(.A1(\trailingones[1] ), .A2(\totalcoeffs[1] ), .ZN(n191));
  AOI22_X1  g171(.A1(\trailingones[0] ), .A2(n25), .B1(\totalcoeffs[2] ), .B2(n191), .ZN(n192));
  OAI21_X1  g172(.A(\trailingones[0] ), .B1(\trailingones[1] ), .B2(n23), .ZN(n193));
  OAI221_X1 g173(.A(n193), .B1(n190), .B2(n23), .C1(n21), .C2(n192), .ZN(n194));
  NAND2_X1  g174(.A1(\trailingones[1] ), .A2(n25), .ZN(n195));
  NOR2_X1   g175(.A1(\trailingones[1] ), .A2(n25), .ZN(n196));
  AOI21_X1  g176(.A(n196), .B1(n195), .B2(\ctable[1] ), .ZN(n197));
  NOR2_X1   g177(.A1(\trailingones[0] ), .A2(\totalcoeffs[3] ), .ZN(n198));
  OAI21_X1  g178(.A(n198), .B1(n191), .B2(n77), .ZN(n199));
  OAI21_X1  g179(.A(n199), .B1(n197), .B2(n54), .ZN(n200));
  AOI22_X1  g180(.A1(n194), .A2(\totalcoeffs[3] ), .B1(n23), .B2(n200), .ZN(n201));
  OAI22_X1  g181(.A1(n189), .A2(\ctable[1] ), .B1(n177), .B2(n201), .ZN(n202));
  AOI22_X1  g182(.A1(n176), .A2(n24), .B1(n95), .B2(n202), .ZN(n203));
  NAND4_X1  g183(.A1(\trailingones[0] ), .A2(\ctable[2] ), .A3(\totalcoeffs[0] ), .A4(\trailingones[1] ), .ZN(n204));
  OAI21_X1  g184(.A(n204), .B1(\trailingones[1] ), .B2(\totalcoeffs[0] ), .ZN(n205));
  AND3_X1   g185(.A1(n130), .A2(n27), .A3(\totalcoeffs[0] ), .ZN(n206));
  AOI21_X1  g186(.A(n206), .B1(n205), .B2(\totalcoeffs[1] ), .ZN(n207));
  NOR2_X1   g187(.A1(\ctable[1] ), .A2(\ctable[0] ), .ZN(n208));
  NAND3_X1  g188(.A1(n208), .A2(n33), .A3(n95), .ZN(n209));
  OAI22_X1  g189(.A1(n207), .A2(n209), .B1(n203), .B2(\ctable[2] ), .ZN(\coeff_token[2] ));
  AOI21_X1  g190(.A(n39), .B1(\trailingones[1] ), .B2(n21), .ZN(n211));
  AND2_X1   g191(.A1(\ctable[1] ), .A2(\totalcoeffs[2] ), .ZN(n212));
  OAI21_X1  g192(.A(n95), .B1(n212), .B2(n211), .ZN(n213));
  AND2_X1   g193(.A1(\ctable[1] ), .A2(\ctable[0] ), .ZN(n214));
  AND2_X1   g194(.A1(\trailingones[1] ), .A2(\trailingones[0] ), .ZN(n215));
  AOI21_X1  g195(.A(n214), .B1(n215), .B2(n208), .ZN(n216));
  OR4_X1    g196(.A1(n95), .A2(\totalcoeffs[3] ), .A3(\totalcoeffs[2] ), .A4(n216), .ZN(n217));
  AOI21_X1  g197(.A(\totalcoeffs[1] ), .B1(n217), .B2(n213), .ZN(n218));
  OR3_X1    g198(.A1(\trailingones[1] ), .A2(\trailingones[0] ), .A3(\ctable[0] ), .ZN(n219));
  NAND2_X1  g199(.A1(\trailingones[0] ), .A2(\ctable[0] ), .ZN(n220));
  OR3_X1    g200(.A1(n220), .A2(n27), .A3(\ctable[1] ), .ZN(n221));
  AOI21_X1  g201(.A(n23), .B1(n221), .B2(n219), .ZN(n222));
  NAND2_X1  g202(.A1(\ctable[1] ), .A2(n65), .ZN(n223));
  AOI21_X1  g203(.A(n65), .B1(\trailingones[0] ), .B2(n21), .ZN(n224));
  OAI22_X1  g204(.A1(n223), .A2(\trailingones[0] ), .B1(n39), .B2(n224), .ZN(n225));
  OAI21_X1  g205(.A(\totalcoeffs[1] ), .B1(n225), .B2(n222), .ZN(n226));
  NAND3_X1  g206(.A1(\ctable[1] ), .A2(n65), .A3(\totalcoeffs[2] ), .ZN(n227));
  AOI21_X1  g207(.A(\totalcoeffs[4] ), .B1(n227), .B2(n226), .ZN(n228));
  OAI21_X1  g208(.A(n24), .B1(n228), .B2(n218), .ZN(n229));
  MUX2_X1   g209(.S(n23), .B(n220), .A(n121), .Z(n230));
  NOR2_X1   g210(.A1(n230), .A2(\trailingones[1] ), .ZN(n231));
  AND2_X1   g211(.A1(\trailingones[1] ), .A2(\ctable[0] ), .ZN(n232));
  AOI21_X1  g212(.A(\totalcoeffs[3] ), .B1(n232), .B2(n54), .ZN(n233));
  AOI21_X1  g213(.A(\ctable[1] ), .B1(n54), .B2(\totalcoeffs[3] ), .ZN(n234));
  NOR2_X1   g214(.A1(\ctable[0] ), .A2(n39), .ZN(n235));
  OAI22_X1  g215(.A1(n234), .A2(n235), .B1(n233), .B2(\totalcoeffs[2] ), .ZN(n236));
  OAI21_X1  g216(.A(\totalcoeffs[1] ), .B1(n236), .B2(n231), .ZN(n237));
  NOR3_X1   g217(.A1(n21), .A2(\ctable[0] ), .A3(\totalcoeffs[3] ), .ZN(n238));
  NOR4_X1   g218(.A1(\ctable[1] ), .A2(n65), .A3(\totalcoeffs[1] ), .A4(n120), .ZN(n239));
  OAI21_X1  g219(.A(n27), .B1(n239), .B2(n238), .ZN(n240));
  AOI21_X1  g220(.A(n24), .B1(n240), .B2(n237), .ZN(n241));
  NOR3_X1   g221(.A1(n33), .A2(n21), .A3(\ctable[0] ), .ZN(n242));
  NOR3_X1   g222(.A1(\ctable[1] ), .A2(n39), .A3(n23), .ZN(n243));
  OR2_X1    g223(.A1(n243), .A2(n242), .ZN(n244));
  OAI22_X1  g224(.A1(\trailingones[1] ), .A2(n223), .B1(\ctable[1] ), .B2(n39), .ZN(n245));
  AOI22_X1  g225(.A1(n244), .A2(\trailingones[1] ), .B1(n54), .B2(n245), .ZN(n246));
  OAI22_X1  g226(.A1(\trailingones[0] ), .A2(\ctable[1] ), .B1(\ctable[0] ), .B2(\trailingones[1] ), .ZN(n247));
  INV_X1    g227(.A(n191), .ZN(n248));
  OR2_X1    g228(.A1(n232), .A2(\ctable[1] ), .ZN(n249));
  AOI21_X1  g229(.A(n249), .B1(n220), .B2(n248), .ZN(n250));
  AOI21_X1  g230(.A(n250), .B1(n247), .B2(n23), .ZN(n251));
  OR4_X1    g231(.A1(\trailingones[1] ), .A2(n54), .A3(n25), .A4(n223), .ZN(n252));
  OAI221_X1 g232(.A(n252), .B1(n246), .B2(\totalcoeffs[1] ), .C1(n39), .C2(n251), .ZN(n253));
  OAI21_X1  g233(.A(n95), .B1(n253), .B2(n241), .ZN(n254));
  AOI21_X1  g234(.A(\ctable[2] ), .B1(n254), .B2(n229), .ZN(\coeff_token[3] ));
  INV_X1    g235(.A(n214), .ZN(n256));
  OR2_X1    g236(.A1(n149), .A2(\totalcoeffs[4] ), .ZN(n257));
  XNOR2_X1  g237(.A(\totalcoeffs[4] ), .B(\totalcoeffs[3] ), .ZN(n258));
  OR3_X1    g238(.A1(n258), .A2(n140), .A3(\totalcoeffs[0] ), .ZN(n259));
  AOI211_X1 g239(.A(n256), .B(\ctable[2] ), .C1(n257), .C2(n259), .ZN(\coeff_token[4] ));
  NAND4_X1  g240(.A1(\totalcoeffs[4] ), .A2(n39), .A3(n23), .A4(n50), .ZN(n261));
  NOR3_X1   g241(.A1(\totalcoeffs[2] ), .A2(\totalcoeffs[1] ), .A3(\totalcoeffs[0] ), .ZN(n262));
  OR3_X1    g242(.A1(n262), .A2(\totalcoeffs[4] ), .A3(n39), .ZN(n263));
  AOI211_X1 g243(.A(n256), .B(\ctable[2] ), .C1(n261), .C2(n263), .ZN(\coeff_token[5] ));
  OAI21_X1  g244(.A(\totalcoeffs[2] ), .B1(\ctable[0] ), .B2(\totalcoeffs[1] ), .ZN(n265));
  NAND3_X1  g245(.A1(n265), .A2(n27), .A3(n21), .ZN(n266));
  OAI21_X1  g246(.A(n266), .B1(n248), .B2(n65), .ZN(n267));
  NOR3_X1   g247(.A1(n46), .A2(n23), .A3(\totalcoeffs[0] ), .ZN(n268));
  AOI21_X1  g248(.A(n268), .B1(n267), .B2(\totalcoeffs[0] ), .ZN(n269));
  NOR2_X1   g249(.A1(n27), .A2(\totalcoeffs[0] ), .ZN(n270));
  AOI21_X1  g250(.A(n82), .B1(n270), .B2(\totalcoeffs[2] ), .ZN(n271));
  XNOR2_X1  g251(.A(\trailingones[1] ), .B(\totalcoeffs[2] ), .ZN(n272));
  OAI211_X1 g252(.A(\ctable[1] ), .B(n272), .C1(n215), .C2(n178), .ZN(n273));
  OAI221_X1 g253(.A(n273), .B1(n269), .B2(n54), .C1(n65), .C2(n271), .ZN(n274));
  NOR2_X1   g254(.A1(n23), .A2(\totalcoeffs[1] ), .ZN(n275));
  OAI21_X1  g255(.A(\trailingones[0] ), .B1(\trailingones[1] ), .B2(n22), .ZN(n276));
  AOI22_X1  g256(.A1(n275), .A2(n276), .B1(n196), .B2(n23), .ZN(n277));
  AND4_X1   g257(.A1(\trailingones[0] ), .A2(\totalcoeffs[1] ), .A3(\totalcoeffs[0] ), .A4(\trailingones[1] ), .ZN(n278));
  OAI211_X1 g258(.A(\ctable[2] ), .B(n23), .C1(n178), .C2(n278), .ZN(n279));
  OAI21_X1  g259(.A(n279), .B1(n277), .B2(\totalcoeffs[0] ), .ZN(n280));
  AOI22_X1  g260(.A1(n274), .A2(n22), .B1(n208), .B2(n280), .ZN(n281));
  OAI22_X1  g261(.A1(\trailingones[0] ), .A2(n25), .B1(n24), .B2(n108), .ZN(n282));
  AOI22_X1  g262(.A1(n132), .A2(n54), .B1(n23), .B2(n282), .ZN(n283));
  XOR2_X1   g263(.A(\trailingones[1] ), .B(\totalcoeffs[1] ), .Z(n284));
  OR2_X1    g264(.A1(n191), .A2(n82), .ZN(n285));
  NOR3_X1   g265(.A1(\trailingones[1] ), .A2(n23), .A3(n25), .ZN(n286));
  NOR3_X1   g266(.A1(n130), .A2(\ctable[1] ), .A3(\totalcoeffs[0] ), .ZN(n287));
  AOI221_X1 g267(.A(n286), .B1(n285), .B2(\totalcoeffs[0] ), .C1(n284), .C2(n287), .ZN(n288));
  OR2_X1    g268(.A1(\trailingones[0] ), .A2(\totalcoeffs[0] ), .ZN(n289));
  NAND3_X1  g269(.A1(n289), .A2(n177), .A3(n196), .ZN(n290));
  OAI221_X1 g270(.A(n290), .B1(n283), .B2(n27), .C1(\ctable[0] ), .C2(n288), .ZN(n291));
  AND3_X1   g271(.A1(n56), .A2(\ctable[0] ), .A3(n23), .ZN(n292));
  OAI21_X1  g272(.A(n21), .B1(\ctable[0] ), .B2(n23), .ZN(n293));
  AOI21_X1  g273(.A(n292), .B1(n293), .B2(n270), .ZN(n294));
  AOI21_X1  g274(.A(n179), .B1(n190), .B2(\totalcoeffs[2] ), .ZN(n295));
  OAI22_X1  g275(.A1(n294), .A2(\trailingones[0] ), .B1(n21), .B2(n295), .ZN(n296));
  INV_X1    g276(.A(n177), .ZN(n297));
  AOI21_X1  g277(.A(\trailingones[0] ), .B1(n21), .B2(n24), .ZN(n298));
  OAI211_X1 g278(.A(n27), .B(n23), .C1(n297), .C2(n298), .ZN(n299));
  NAND4_X1  g279(.A1(\trailingones[0] ), .A2(\totalcoeffs[2] ), .A3(n24), .A4(\trailingones[1] ), .ZN(n300));
  AOI21_X1  g280(.A(\totalcoeffs[1] ), .B1(n300), .B2(n299), .ZN(n301));
  AOI221_X1 g281(.A(n301), .B1(n291), .B2(\totalcoeffs[3] ), .C1(\totalcoeffs[1] ), .C2(n296), .ZN(n302));
  OAI22_X1  g282(.A1(n281), .A2(\totalcoeffs[3] ), .B1(\ctable[2] ), .B2(n302), .ZN(n303));
  AOI21_X1  g283(.A(\ctable[2] ), .B1(n261), .B2(n256), .ZN(n305));
  AOI21_X1  g284(.A(n305), .B1(n303), .B2(n95), .ZN(\ctoken_len[0] ));
  OAI22_X1  g285(.A1(n54), .A2(n24), .B1(n39), .B2(n215), .ZN(n307));
  AOI22_X1  g286(.A1(n215), .A2(n39), .B1(n21), .B2(n307), .ZN(n308));
  NOR2_X1   g287(.A1(n308), .A2(n23), .ZN(n309));
  NAND4_X1  g288(.A1(n21), .A2(\totalcoeffs[3] ), .A3(n24), .A4(\trailingones[0] ), .ZN(n310));
  AND2_X1   g289(.A1(n310), .A2(n170), .ZN(n311));
  AOI21_X1  g290(.A(n100), .B1(\trailingones[0] ), .B2(n39), .ZN(n312));
  OR2_X1    g291(.A1(n108), .A2(\trailingones[1] ), .ZN(n313));
  OAI221_X1 g292(.A(n313), .B1(n311), .B2(n27), .C1(n24), .C2(n312), .ZN(n314));
  AOI221_X1 g293(.A(n309), .B1(n86), .B2(n39), .C1(n23), .C2(n314), .ZN(n315));
  MUX2_X1   g294(.S(\trailingones[1] ), .B(\trailingones[0] ), .A(\totalcoeffs[0] ), .Z(n316));
  NOR3_X1   g295(.A1(n316), .A2(\ctable[1] ), .A3(\totalcoeffs[2] ), .ZN(n317));
  NOR3_X1   g296(.A1(n182), .A2(n21), .A3(\totalcoeffs[0] ), .ZN(n319));
  OAI21_X1  g297(.A(\totalcoeffs[3] ), .B1(n319), .B2(n317), .ZN(n320));
  MUX2_X1   g298(.S(\totalcoeffs[0] ), .B(n108), .A(n120), .Z(n321));
  OAI211_X1 g299(.A(n190), .B(\totalcoeffs[2] ), .C1(\ctable[1] ), .C2(n198), .ZN(n322));
  OAI211_X1 g300(.A(n320), .B(n322), .C1(n321), .C2(\trailingones[1] ), .ZN(n323));
  NOR4_X1   g301(.A1(\trailingones[1] ), .A2(n39), .A3(\totalcoeffs[2] ), .A4(n170), .ZN(n324));
  AOI21_X1  g302(.A(n324), .B1(n323), .B2(n25), .ZN(n325));
  OAI21_X1  g303(.A(n325), .B1(n315), .B2(n25), .ZN(n326));
  NAND2_X1  g304(.A1(n27), .A2(\ctable[0] ), .ZN(n327));
  MUX2_X1   g305(.S(n24), .B(n327), .A(n272), .Z(n328));
  OAI22_X1  g306(.A1(n138), .A2(n60), .B1(n54), .B2(n328), .ZN(n329));
  AND2_X1   g307(.A1(\ctable[0] ), .A2(\totalcoeffs[3] ), .ZN(n330));
  AOI21_X1  g308(.A(n330), .B1(n27), .B2(\totalcoeffs[2] ), .ZN(n331));
  NAND3_X1  g309(.A1(\ctable[0] ), .A2(\totalcoeffs[3] ), .A3(n23), .ZN(n332));
  OAI21_X1  g310(.A(n332), .B1(n331), .B2(\totalcoeffs[0] ), .ZN(n333));
  NOR4_X1   g311(.A1(n65), .A2(n39), .A3(\totalcoeffs[2] ), .A4(\trailingones[1] ), .ZN(n334));
  AOI221_X1 g312(.A(n334), .B1(n329), .B2(n39), .C1(n54), .C2(n333), .ZN(n335));
  NAND2_X1  g313(.A1(\totalcoeffs[3] ), .A2(\totalcoeffs[2] ), .ZN(n336));
  OAI22_X1  g314(.A1(n178), .A2(n215), .B1(n35), .B2(\totalcoeffs[2] ), .ZN(n337));
  AOI21_X1  g315(.A(n65), .B1(n337), .B2(n336), .ZN(n338));
  AND3_X1   g316(.A1(n178), .A2(n35), .A3(\totalcoeffs[2] ), .ZN(n339));
  OAI21_X1  g317(.A(n25), .B1(n339), .B2(n338), .ZN(n340));
  NAND3_X1  g318(.A1(\trailingones[1] ), .A2(\trailingones[0] ), .A3(\ctable[0] ), .ZN(n341));
  OAI221_X1 g319(.A(n340), .B1(n336), .B2(n341), .C1(n335), .C2(n25), .ZN(n342));
  AOI22_X1  g320(.A1(n326), .A2(n65), .B1(n21), .B2(n342), .ZN(n343));
  AND3_X1   g321(.A1(n182), .A2(\totalcoeffs[2] ), .A3(n24), .ZN(n344));
  NOR4_X1   g322(.A1(\trailingones[1] ), .A2(\totalcoeffs[2] ), .A3(n24), .A4(n43), .ZN(n345));
  OAI211_X1 g323(.A(n134), .B(n28), .C1(n344), .C2(n345), .ZN(n346));
  OAI21_X1  g324(.A(n346), .B1(n343), .B2(\ctable[2] ), .ZN(n347));
  NOR3_X1   g325(.A1(n37), .A2(\ctable[2] ), .A3(n95), .ZN(n348));
  NOR4_X1   g326(.A1(\totalcoeffs[3] ), .A2(\totalcoeffs[1] ), .A3(\totalcoeffs[0] ), .A4(\ctable[1] ), .ZN(n349));
  AOI22_X1  g327(.A1(n348), .A2(n349), .B1(n347), .B2(n95), .ZN(\ctoken_len[1] ));
  MUX2_X1   g328(.S(\ctable[0] ), .B(\totalcoeffs[1] ), .A(\totalcoeffs[3] ), .Z(n351));
  NAND2_X1  g329(.A1(n62), .A2(n23), .ZN(n352));
  OAI22_X1  g330(.A1(n351), .A2(n352), .B1(n177), .B2(n159), .ZN(n353));
  AOI21_X1  g331(.A(\ctable[0] ), .B1(\trailingones[0] ), .B2(n24), .ZN(n354));
  NOR4_X1   g332(.A1(n330), .A2(n23), .A3(n25), .A4(n354), .ZN(n355));
  AOI21_X1  g333(.A(n355), .B1(n353), .B2(\trailingones[0] ), .ZN(n356));
  INV_X1    g334(.A(n351), .ZN(n357));
  AOI211_X1 g335(.A(\totalcoeffs[2] ), .B(n77), .C1(\trailingones[1] ), .C2(n39), .ZN(n358));
  OAI21_X1  g336(.A(n171), .B1(n327), .B2(n140), .ZN(n359));
  OR2_X1    g337(.A1(\ctable[0] ), .A2(\totalcoeffs[1] ), .ZN(n360));
  AOI211_X1 g338(.A(\totalcoeffs[3] ), .B(n23), .C1(n284), .C2(n360), .ZN(n361));
  AOI221_X1 g339(.A(n361), .B1(n358), .B2(n357), .C1(n24), .C2(n359), .ZN(n362));
  MUX2_X1   g340(.S(\ctable[0] ), .B(\totalcoeffs[3] ), .A(\totalcoeffs[2] ), .Z(n363));
  AND3_X1   g341(.A1(n363), .A2(n156), .A3(\totalcoeffs[1] ), .ZN(n364));
  NAND4_X1  g342(.A1(\totalcoeffs[3] ), .A2(n23), .A3(n25), .A4(\trailingones[0] ), .ZN(n365));
  AOI21_X1  g343(.A(n365), .B1(\ctable[0] ), .B2(n24), .ZN(n366));
  OAI21_X1  g344(.A(\trailingones[1] ), .B1(n366), .B2(n364), .ZN(n367));
  OAI221_X1 g345(.A(n367), .B1(n356), .B2(\trailingones[1] ), .C1(\trailingones[0] ), .C2(n362), .ZN(n368));
  NAND2_X1  g346(.A1(n190), .A2(n25), .ZN(n369));
  AOI22_X1  g347(.A1(n195), .A2(\ctable[1] ), .B1(\totalcoeffs[2] ), .B2(n369), .ZN(n370));
  AOI21_X1  g348(.A(\ctable[1] ), .B1(n54), .B2(\totalcoeffs[1] ), .ZN(n371));
  OAI211_X1 g349(.A(n195), .B(\ctable[1] ), .C1(n54), .C2(n196), .ZN(n372));
  OAI221_X1 g350(.A(n372), .B1(n370), .B2(n24), .C1(n23), .C2(n371), .ZN(n373));
  AOI22_X1  g351(.A1(n368), .A2(n21), .B1(n235), .B2(n373), .ZN(n374));
  NOR3_X1   g352(.A1(\trailingones[0] ), .A2(\totalcoeffs[2] ), .A3(\totalcoeffs[0] ), .ZN(n375));
  XOR2_X1   g353(.A(\trailingones[0] ), .B(\totalcoeffs[2] ), .Z(n376));
  OR2_X1    g354(.A1(n376), .A2(\totalcoeffs[0] ), .ZN(n377));
  AND2_X1   g355(.A1(n377), .A2(n125), .ZN(n378));
  OAI22_X1  g356(.A1(n289), .A2(n60), .B1(\trailingones[1] ), .B2(n378), .ZN(n379));
  AOI22_X1  g357(.A1(n375), .A2(n191), .B1(n25), .B2(n379), .ZN(n380));
  OR3_X1    g358(.A1(\ctable[1] ), .A2(\ctable[0] ), .A3(\totalcoeffs[3] ), .ZN(n381));
  OAI22_X1  g359(.A1(n380), .A2(n381), .B1(n374), .B2(\ctable[2] ), .ZN(n382));
  AND4_X1   g360(.A1(n28), .A2(n22), .A3(\totalcoeffs[4] ), .A4(n262), .ZN(n383));
  AOI21_X1  g361(.A(n383), .B1(n382), .B2(n95), .ZN(\ctoken_len[2] ));
  AOI21_X1  g362(.A(n100), .B1(n249), .B2(n133), .ZN(n385));
  NOR2_X1   g363(.A1(n208), .A2(n95), .ZN(n386));
  MUX2_X1   g364(.S(n39), .B(n386), .A(n385), .Z(n387));
  OR2_X1    g365(.A1(n46), .A2(\totalcoeffs[3] ), .ZN(n388));
  OAI21_X1  g366(.A(\totalcoeffs[2] ), .B1(n232), .B2(\trailingones[0] ), .ZN(n389));
  OAI22_X1  g367(.A1(n388), .A2(n389), .B1(n387), .B2(\totalcoeffs[2] ), .ZN(n390));
  INV_X1    g368(.A(n369), .ZN(n391));
  OAI211_X1 g369(.A(\trailingones[0] ), .B(n24), .C1(n39), .C2(n100), .ZN(n392));
  AOI21_X1  g370(.A(\totalcoeffs[2] ), .B1(n392), .B2(n388), .ZN(n393));
  AOI21_X1  g371(.A(\ctable[0] ), .B1(\trailingones[1] ), .B2(\trailingones[0] ), .ZN(n394));
  AOI21_X1  g372(.A(\totalcoeffs[3] ), .B1(n341), .B2(n21), .ZN(n395));
  AOI211_X1 g373(.A(n393), .B(n395), .C1(n394), .C2(n243), .ZN(n396));
  AOI21_X1  g374(.A(\ctable[2] ), .B1(n243), .B2(n297), .ZN(n397));
  OR2_X1    g375(.A1(n92), .A2(\ctable[2] ), .ZN(n398));
  OAI21_X1  g376(.A(n65), .B1(\totalcoeffs[3] ), .B2(n23), .ZN(n399));
  OAI22_X1  g377(.A1(n75), .A2(n22), .B1(n95), .B2(n92), .ZN(n400));
  AOI221_X1 g378(.A(n400), .B1(n398), .B2(\totalcoeffs[0] ), .C1(\ctable[1] ), .C2(n399), .ZN(n401));
  OAI221_X1 g379(.A(n401), .B1(n396), .B2(n25), .C1(n391), .C2(n397), .ZN(n402));
  AOI21_X1  g380(.A(n402), .B1(n390), .B2(n25), .ZN(\ctoken_len[3] ));
  OAI22_X1  g381(.A1(n270), .A2(n25), .B1(\trailingones[0] ), .B2(n30), .ZN(n404));
  NAND4_X1  g382(.A1(n95), .A2(\totalcoeffs[3] ), .A3(\totalcoeffs[2] ), .A4(n404), .ZN(n405));
  OR3_X1    g383(.A1(\ctable[2] ), .A2(\ctable[1] ), .A3(\ctable[0] ), .ZN(n406));
  AOI21_X1  g384(.A(n406), .B1(n405), .B2(n261), .ZN(\ctoken_len[4] ));
endmodule


