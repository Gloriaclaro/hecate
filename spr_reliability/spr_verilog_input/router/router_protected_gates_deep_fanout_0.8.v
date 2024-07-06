// Benchmark "top" written by ABC on Sun Jun 16 00:05:26 2024

module top ( 
    \dest_x[0] , \dest_x[1] , \dest_x[2] , \dest_x[3] , \dest_x[4] ,
    \dest_x[5] , \dest_x[6] , \dest_x[7] , \dest_x[8] , \dest_x[9] ,
    \dest_x[10] , \dest_x[11] , \dest_x[12] , \dest_x[13] , \dest_x[14] ,
    \dest_x[15] , \dest_x[16] , \dest_x[17] , \dest_x[18] , \dest_x[19] ,
    \dest_x[20] , \dest_x[21] , \dest_x[22] , \dest_x[23] , \dest_x[24] ,
    \dest_x[25] , \dest_x[26] , \dest_x[27] , \dest_x[28] , \dest_x[29] ,
    \dest_y[0] , \dest_y[1] , \dest_y[2] , \dest_y[3] , \dest_y[4] ,
    \dest_y[5] , \dest_y[6] , \dest_y[7] , \dest_y[8] , \dest_y[9] ,
    \dest_y[10] , \dest_y[11] , \dest_y[12] , \dest_y[13] , \dest_y[14] ,
    \dest_y[15] , \dest_y[16] , \dest_y[17] , \dest_y[18] , \dest_y[19] ,
    \dest_y[20] , \dest_y[21] , \dest_y[22] , \dest_y[23] , \dest_y[24] ,
    \dest_y[25] , \dest_y[26] , \dest_y[27] , \dest_y[28] , \dest_y[29] ,
    \outport[0] , \outport[1] , \outport[2]   );
  input  \dest_x[0] , \dest_x[1] , \dest_x[2] , \dest_x[3] , \dest_x[4] ,
    \dest_x[5] , \dest_x[6] , \dest_x[7] , \dest_x[8] , \dest_x[9] ,
    \dest_x[10] , \dest_x[11] , \dest_x[12] , \dest_x[13] , \dest_x[14] ,
    \dest_x[15] , \dest_x[16] , \dest_x[17] , \dest_x[18] , \dest_x[19] ,
    \dest_x[20] , \dest_x[21] , \dest_x[22] , \dest_x[23] , \dest_x[24] ,
    \dest_x[25] , \dest_x[26] , \dest_x[27] , \dest_x[28] , \dest_x[29] ,
    \dest_y[0] , \dest_y[1] , \dest_y[2] , \dest_y[3] , \dest_y[4] ,
    \dest_y[5] , \dest_y[6] , \dest_y[7] , \dest_y[8] , \dest_y[9] ,
    \dest_y[10] , \dest_y[11] , \dest_y[12] , \dest_y[13] , \dest_y[14] ,
    \dest_y[15] , \dest_y[16] , \dest_y[17] , \dest_y[18] , \dest_y[19] ,
    \dest_y[20] , \dest_y[21] , \dest_y[22] , \dest_y[23] , \dest_y[24] ,
    \dest_y[25] , \dest_y[26] , \dest_y[27] , \dest_y[28] , \dest_y[29] ;
  output \outport[0] , \outport[1] , \outport[2] ;
  wire n90, n91, n92, n93, n94, n95, n96, n97, n98, n99, n100, n101, n102,
    n103, n104, n105, n106, n107, n108, n109, n110, n111, n112, n113, n114,
    n115, n116, n117, n118, n119, n120, n121, n122, n123, n124, n125, n126,
    n127, n128, n129, n130, n131, n132, n133, n134, n135, n136, n137, n138,
    n139, n140, n141, n142, n143, n144, n145, n146, n147, n148, n149, n150,
    n151, n152, n153, n154, n155, n156, n157, n158, n159, n160, n161, n162,
    n163, n164, n165, n166, n167, n168, n169, n170, n171, n172, n174, n175,
    n176, n177, n178, n179, n180, n181, n182, n183, n184, n185, n186, n187,
    n188, n189, n190, n191, n192, n193, n194, n195, n196, n197, n198, n199,
    n200, n201, n202, n203, n204, n205, n206, n207, n208, n209, n210, n211,
    n212, n213, n214, n215, n216, n217, n218, n219, n220, n221, n222, n223,
    n224, n225, n226, n227, n228, n229, n230, n231, n232, n233, n234, n235,
    n236, n237, n238, n239, n240, n241, n242, n243, n244, n245, n246, n247,
    n248, n249, n250, n251, n252, n253, n254, n255, n256, n258;
  wire n90, n91, n92, n93, n94, n95, n96, n97, n98, n99, n100, n101, n102,
    n103, n104, n105, n106, n107, n108, n109, n110, n111, n112, n113, n114,
    n115, n116, n117, n118, n119, n120, n121, n122, n123, n124, n125, n126,
    n127, n128, n129, n130, n131, n132, n133, n134, n135, n136, n137, n138,
    n139, n140, n141, n142, n143, n144, n145, n146, n147, n148, n149, n150,
    n151, n152, n153, n154, n155, n156, n157, n158, n159, n160, n161, n162,
    n163, n164, n165, n166, n167, n168, n169, n170, n171, n172, n174, n175,
    n176, n177, n178, n179, n180, n181, n182, n183, n184, n185, n186, n187,
    n188, n189, n190, n191, n192, n193, n194, n195, n196, n197, n198, n199,
    n200, n201, n202, n203, n204, n205, n206, n207, n208, n209, n210, n211,
    n212, n213, n214, n215, n216, n217, n218, n219, n220, n221, n222, n223,
    n224, n225, n226, n227, n228, n229, n230, n231, n232, n233, n234, n235,
    n236, n237, n238, n239, n240, n241, n242, n243, n244, n245, n246, n247,
    n248, n249, n250, n251, n252, n253, n254, n255, n256, n258;
INV_X1_p g000(.A(\dest_x[26] ), .ZN(n90));
INV_X1_p g001(.A(\dest_x[27] ), .ZN(n91));
INV_X1_p g002(.A(\dest_x[28] ), .ZN(n92));
  INV_X1    g003(.A(\dest_x[23] ), .ZN(n93));
  INV_X1    g004(.A(\dest_x[24] ), .ZN(n94));
  INV_X1    g005(.A(\dest_x[25] ), .ZN(n95));
  INV_X1    g006(.A(\dest_x[18] ), .ZN(n96));
  INV_X1    g007(.A(\dest_x[19] ), .ZN(n97));
  INV_X1    g008(.A(\dest_x[20] ), .ZN(n98));
  INV_X1    g009(.A(\dest_x[14] ), .ZN(n99));
  INV_X1    g010(.A(\dest_x[15] ), .ZN(n100));
  INV_X1    g011(.A(\dest_x[12] ), .ZN(n101));
  INV_X1    g012(.A(\dest_x[13] ), .ZN(n102));
  OAI21_X1  g013(.A(\dest_x[11] ), .B1(\dest_x[10] ), .B2(\dest_x[9] ), .ZN(n103));
  AND3_X1   g014(.A1(n103), .A2(n102), .A3(n101), .ZN(n104));
  NOR3_X1   g015(.A1(n104), .A2(n100), .A3(n99), .ZN(n105));
  OAI21_X1  g016(.A(\dest_x[17] ), .B1(n105), .B2(\dest_x[16] ), .ZN(n106));
  AOI211_X1 g017(.A(n98), .B(n97), .C1(n96), .C2(n106), .ZN(n107));
  NOR3_X1   g018(.A1(n107), .A2(\dest_x[22] ), .A3(\dest_x[21] ), .ZN(n108));
OR4_X1_p g019(.A1(n95), .A2(n94), .A3(n93), .A4(n108), .ZN(n109));
AOI211_X1_p g020(.A(n92), .B(n91), .C1(n90), .C2(n109), .ZN(n110));
  XNOR2_X1  g021(.A(n110), .B(\dest_x[29] ), .ZN(n111));
  NOR4_X1   g022(.A1(n95), .A2(n94), .A3(n93), .A4(n108), .ZN(n112));
  OAI21_X1  g023(.A(\dest_x[27] ), .B1(n112), .B2(\dest_x[26] ), .ZN(n113));
  XNOR2_X1  g024(.A(n113), .B(n92), .ZN(n114));
  NOR2_X1   g025(.A1(n112), .A2(\dest_x[26] ), .ZN(n115));
  XNOR2_X1  g026(.A(n115), .B(n91), .ZN(n116));
  XNOR2_X1  g027(.A(n112), .B(\dest_x[26] ), .ZN(n117));
  NOR3_X1   g028(.A1(n108), .A2(n94), .A3(n93), .ZN(n118));
  XNOR2_X1  g029(.A(n118), .B(n95), .ZN(n119));
  NOR2_X1   g030(.A1(n108), .A2(n93), .ZN(n120));
  XNOR2_X1  g031(.A(n120), .B(n94), .ZN(n121));
  XNOR2_X1  g032(.A(n108), .B(\dest_x[23] ), .ZN(n122));
  NOR2_X1   g033(.A1(n107), .A2(\dest_x[21] ), .ZN(n123));
  XOR2_X1   g034(.A(n123), .B(\dest_x[22] ), .Z(n124));
  XNOR2_X1  g035(.A(n107), .B(\dest_x[21] ), .ZN(n125));
  AOI21_X1  g036(.A(n97), .B1(n106), .B2(n96), .ZN(n126));
  XNOR2_X1  g037(.A(n126), .B(n98), .ZN(n127));
  INV_X1    g038(.A(\dest_x[16] ), .ZN(n128));
  INV_X1    g039(.A(\dest_x[17] ), .ZN(n129));
  OR3_X1    g040(.A1(n104), .A2(n100), .A3(n99), .ZN(n130));
  AOI21_X1  g041(.A(n129), .B1(n130), .B2(n128), .ZN(n131));
  NOR2_X1   g042(.A1(n131), .A2(\dest_x[18] ), .ZN(n132));
  XNOR2_X1  g043(.A(n132), .B(\dest_x[19] ), .ZN(n133));
  XNOR2_X1  g044(.A(n131), .B(\dest_x[18] ), .ZN(n134));
  NOR2_X1   g045(.A1(n105), .A2(\dest_x[16] ), .ZN(n135));
  XNOR2_X1  g046(.A(n135), .B(\dest_x[17] ), .ZN(n136));
  XNOR2_X1  g047(.A(n105), .B(\dest_x[16] ), .ZN(n137));
  NOR2_X1   g048(.A1(n104), .A2(n99), .ZN(n138));
  XNOR2_X1  g049(.A(n138), .B(n100), .ZN(n139));
  XNOR2_X1  g050(.A(n104), .B(n99), .ZN(n140));
  AND2_X1   g051(.A1(n103), .A2(n101), .ZN(n141));
  XNOR2_X1  g052(.A(n141), .B(\dest_x[13] ), .ZN(n142));
  XNOR2_X1  g053(.A(n103), .B(\dest_x[12] ), .ZN(n143));
  OR3_X1    g054(.A1(\dest_x[11] ), .A2(\dest_x[10] ), .A3(\dest_x[9] ), .ZN(n144));
  NAND2_X1  g055(.A1(n144), .A2(n103), .ZN(n145));
  INV_X1    g056(.A(\dest_x[0] ), .ZN(n146));
  NAND4_X1  g057(.A1(\dest_x[3] ), .A2(\dest_x[2] ), .A3(\dest_x[1] ), .A4(\dest_x[4] ), .ZN(n147));
  OR3_X1    g058(.A1(n147), .A2(\dest_x[9] ), .A3(n146), .ZN(n148));
  XOR2_X1   g059(.A(\dest_x[10] ), .B(\dest_x[9] ), .Z(n149));
  NAND4_X1  g060(.A1(\dest_x[7] ), .A2(\dest_x[6] ), .A3(\dest_x[5] ), .A4(\dest_x[8] ), .ZN(n150));
  OR4_X1    g061(.A1(n149), .A2(n148), .A3(n145), .A4(n150), .ZN(n151));
  NOR4_X1   g062(.A1(n143), .A2(n142), .A3(n140), .A4(n151), .ZN(n152));
  AND4_X1   g063(.A1(n139), .A2(n137), .A3(n136), .A4(n152), .ZN(n153));
  AND4_X1   g064(.A1(n134), .A2(n133), .A3(n127), .A4(n153), .ZN(n154));
AND4_X1_p g065(.A1(n125), .A2(n124), .A3(n122), .A4(n154), .ZN(n155));
NAND4_X1_p g066(.A1(n121), .A2(n119), .A3(n117), .A4(n155), .ZN(n156));
OR4_X1_p g067(.A1(n116), .A2(n114), .A3(n111), .A4(n156), .ZN(n157));
NAND2_X1_p g068(.A1(n110), .A2(\dest_x[29] ), .ZN(n158));
AND2_X1_p g069(.A1(n158), .A2(n157), .ZN(n159));
  XNOR2_X1  g070(.A(n115), .B(\dest_x[27] ), .ZN(n160));
  INV_X1    g071(.A(n140), .ZN(n161));
  OR4_X1    g072(.A1(\dest_x[5] ), .A2(\dest_x[4] ), .A3(\dest_x[3] ), .A4(\dest_x[6] ), .ZN(n162));
  NOR2_X1   g073(.A1(\dest_x[8] ), .A2(\dest_x[7] ), .ZN(n163));
  NAND3_X1  g074(.A1(n163), .A2(n149), .A3(\dest_x[9] ), .ZN(n164));
  NOR4_X1   g075(.A1(n162), .A2(\dest_x[2] ), .A3(\dest_x[1] ), .A4(n164), .ZN(n165));
  NAND4_X1  g076(.A1(n145), .A2(n143), .A3(n142), .A4(n165), .ZN(n166));
  OR4_X1    g077(.A1(n161), .A2(n139), .A3(n137), .A4(n166), .ZN(n167));
  OR4_X1    g078(.A1(n136), .A2(n134), .A3(n133), .A4(n167), .ZN(n168));
OR4_X1_p g079(.A1(n127), .A2(n125), .A3(n124), .A4(n168), .ZN(n169));
OR4_X1_p g080(.A1(n122), .A2(n121), .A3(n119), .A4(n169), .ZN(n170));
NOR3_X1_p g081(.A1(n170), .A2(n117), .A3(n160), .ZN(n171));
AOI21_X1_p g082(.A(n158), .B1(n171), .B2(n114), .ZN(n172));
OR2_X1_p g083(.A1(n172), .A2(n159), .ZN(\outport[0] ));
  INV_X1    g084(.A(\dest_y[26] ), .ZN(n174));
  INV_X1    g085(.A(\dest_y[27] ), .ZN(n175));
  INV_X1    g086(.A(\dest_y[23] ), .ZN(n176));
  INV_X1    g087(.A(\dest_y[24] ), .ZN(n177));
  INV_X1    g088(.A(\dest_y[25] ), .ZN(n178));
  INV_X1    g089(.A(\dest_y[18] ), .ZN(n179));
  INV_X1    g090(.A(\dest_y[19] ), .ZN(n180));
  INV_X1    g091(.A(\dest_y[20] ), .ZN(n181));
  INV_X1    g092(.A(\dest_y[14] ), .ZN(n182));
  INV_X1    g093(.A(\dest_y[15] ), .ZN(n183));
  INV_X1    g094(.A(\dest_y[12] ), .ZN(n184));
  INV_X1    g095(.A(\dest_y[13] ), .ZN(n185));
  OAI21_X1  g096(.A(\dest_y[11] ), .B1(\dest_y[10] ), .B2(\dest_y[9] ), .ZN(n186));
  AND3_X1   g097(.A1(n186), .A2(n185), .A3(n184), .ZN(n187));
  NOR3_X1   g098(.A1(n187), .A2(n183), .A3(n182), .ZN(n188));
  OAI21_X1  g099(.A(\dest_y[17] ), .B1(n188), .B2(\dest_y[16] ), .ZN(n189));
  AOI211_X1 g100(.A(n181), .B(n180), .C1(n179), .C2(n189), .ZN(n190));
  NOR3_X1   g101(.A1(n190), .A2(\dest_y[22] ), .A3(\dest_y[21] ), .ZN(n191));
  OR4_X1    g102(.A1(n178), .A2(n177), .A3(n176), .A4(n191), .ZN(n192));
  AOI21_X1  g103(.A(n175), .B1(n192), .B2(n174), .ZN(n193));
  NAND3_X1  g104(.A1(n193), .A2(\dest_y[29] ), .A3(\dest_y[28] ), .ZN(n194));
  XNOR2_X1  g105(.A(n193), .B(\dest_y[28] ), .ZN(n195));
  NOR4_X1   g106(.A1(n178), .A2(n177), .A3(n176), .A4(n191), .ZN(n196));
  NOR2_X1   g107(.A1(n196), .A2(\dest_y[26] ), .ZN(n197));
  XNOR2_X1  g108(.A(n197), .B(n175), .ZN(n198));
  XNOR2_X1  g109(.A(n196), .B(n174), .ZN(n199));
  NOR3_X1   g110(.A1(n191), .A2(n177), .A3(n176), .ZN(n200));
  XNOR2_X1  g111(.A(n200), .B(n178), .ZN(n201));
  NOR2_X1   g112(.A1(n191), .A2(n176), .ZN(n202));
  XNOR2_X1  g113(.A(n202), .B(n177), .ZN(n203));
  XNOR2_X1  g114(.A(n191), .B(\dest_y[23] ), .ZN(n204));
  NOR2_X1   g115(.A1(n190), .A2(\dest_y[21] ), .ZN(n205));
  XNOR2_X1  g116(.A(n205), .B(\dest_y[22] ), .ZN(n206));
  XOR2_X1   g117(.A(n190), .B(\dest_y[21] ), .Z(n207));
  AOI21_X1  g118(.A(n180), .B1(n189), .B2(n179), .ZN(n208));
  XNOR2_X1  g119(.A(n208), .B(\dest_y[20] ), .ZN(n209));
  INV_X1    g120(.A(\dest_y[16] ), .ZN(n210));
  INV_X1    g121(.A(\dest_y[17] ), .ZN(n211));
  OR3_X1    g122(.A1(n187), .A2(n183), .A3(n182), .ZN(n212));
  AOI21_X1  g123(.A(n211), .B1(n212), .B2(n210), .ZN(n213));
  NOR2_X1   g124(.A1(n213), .A2(\dest_y[18] ), .ZN(n214));
  XNOR2_X1  g125(.A(n214), .B(\dest_y[19] ), .ZN(n215));
  XNOR2_X1  g126(.A(n213), .B(\dest_y[18] ), .ZN(n216));
  NOR2_X1   g127(.A1(n188), .A2(\dest_y[16] ), .ZN(n217));
  XNOR2_X1  g128(.A(n217), .B(\dest_y[17] ), .ZN(n218));
  XNOR2_X1  g129(.A(n188), .B(n210), .ZN(n219));
  NOR2_X1   g130(.A1(n187), .A2(n182), .ZN(n220));
  XNOR2_X1  g131(.A(n220), .B(\dest_y[15] ), .ZN(n221));
  XNOR2_X1  g132(.A(n187), .B(\dest_y[14] ), .ZN(n222));
  INV_X1    g133(.A(n222), .ZN(n223));
  AND2_X1   g134(.A1(n186), .A2(n184), .ZN(n224));
  XNOR2_X1  g135(.A(n224), .B(n185), .ZN(n225));
  XNOR2_X1  g136(.A(n186), .B(n184), .ZN(n226));
  NOR2_X1   g137(.A1(\dest_y[10] ), .A2(\dest_y[9] ), .ZN(n227));
  XNOR2_X1  g138(.A(n227), .B(\dest_y[11] ), .ZN(n228));
  OR4_X1    g139(.A1(\dest_y[5] ), .A2(\dest_y[4] ), .A3(\dest_y[3] ), .A4(\dest_y[6] ), .ZN(n229));
  INV_X1    g140(.A(\dest_y[9] ), .ZN(n230));
  OR4_X1    g141(.A1(n230), .A2(\dest_y[8] ), .A3(\dest_y[7] ), .A4(\dest_y[10] ), .ZN(n231));
  OR4_X1    g142(.A1(n229), .A2(\dest_y[2] ), .A3(\dest_y[1] ), .A4(n231), .ZN(n232));
  NOR4_X1   g143(.A1(n228), .A2(n226), .A3(n225), .A4(n232), .ZN(n233));
  NAND4_X1  g144(.A1(n223), .A2(n221), .A3(n219), .A4(n233), .ZN(n234));
  NOR4_X1   g145(.A1(n218), .A2(n216), .A3(n215), .A4(n234), .ZN(n235));
  NAND4_X1  g146(.A1(n209), .A2(n207), .A3(n206), .A4(n235), .ZN(n236));
  NOR4_X1   g147(.A1(n204), .A2(n203), .A3(n201), .A4(n236), .ZN(n237));
  AND4_X1   g148(.A1(n199), .A2(n198), .A3(n195), .A4(n237), .ZN(n238));
  OR2_X1    g149(.A1(n238), .A2(n194), .ZN(n239));
  INV_X1    g150(.A(\dest_y[0] ), .ZN(n240));
  AOI21_X1  g151(.A(n194), .B1(n240), .B2(n146), .ZN(n241));
  XNOR2_X1  g152(.A(n208), .B(n181), .ZN(n242));
  AND4_X1   g153(.A1(\dest_y[4] ), .A2(\dest_y[3] ), .A3(\dest_y[2] ), .A4(\dest_y[5] ), .ZN(n243));
  AND4_X1   g154(.A1(n230), .A2(\dest_y[8] ), .A3(\dest_y[0] ), .A4(\dest_y[29] ), .ZN(n244));
  XNOR2_X1  g155(.A(\dest_y[10] ), .B(\dest_y[9] ), .ZN(n245));
  AND4_X1   g156(.A1(\dest_y[7] ), .A2(\dest_y[6] ), .A3(\dest_y[1] ), .A4(n245), .ZN(n246));
  AND4_X1   g157(.A1(n244), .A2(n243), .A3(n228), .A4(n246), .ZN(n247));
  NAND4_X1  g158(.A1(n226), .A2(n225), .A3(n222), .A4(n247), .ZN(n248));
  NOR3_X1   g159(.A1(n248), .A2(n221), .A3(n219), .ZN(n249));
  AND3_X1   g160(.A1(n249), .A2(n218), .A3(n216), .ZN(n250));
  NAND3_X1  g161(.A1(n250), .A2(n215), .A3(n242), .ZN(n251));
  NOR3_X1   g162(.A1(n251), .A2(n207), .A3(n206), .ZN(n252));
  NAND4_X1  g163(.A1(n204), .A2(n203), .A3(n201), .A4(n252), .ZN(n253));
  NOR4_X1   g164(.A1(n199), .A2(n198), .A3(n195), .A4(n253), .ZN(n254));
  NOR2_X1   g165(.A1(n254), .A2(n241), .ZN(n255));
AOI221_X1_p g166(.A(n159), .B1(n194), .B2(\dest_x[0] ), .C1(n255), .C2(n239), .ZN(n256));
NOR2_X1_p g167(.A1(n256), .A2(n172), .ZN(\outport[1] ));
  OR3_X1    g168(.A1(n194), .A2(n240), .A3(n146), .ZN(n258));
AOI211_X1_p g169(.A(n172), .B(n159), .C1(n239), .C2(n258), .ZN(\outport[2] ));
