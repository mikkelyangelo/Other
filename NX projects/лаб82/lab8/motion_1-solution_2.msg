


  ************************************************************
  *                                                          *
  *                         RecurDyn                         *
  *                                                          *
  *             Recursive Dynamics Analysis Program          *
  *                                                          *
  ************************************************************
  *                                                          *
  *                Solver Version : SDK 7.25.0               *
  *                                                          *
  *                Build Date : Jul 15 2014                  *
  *                Build Time :    13:58:13                  *
  *                Build Platform : Window 64                *
  *                                                          *
  *                Copyright (C) 1997 - 2014                 *
  *                                                          *
  *                    Function Bay, Inc.                    *
  *                                                          *
  ************************************************************


 << RECURDYN/CONVERTER PROCESSING >>

    READING THE RMD FILE 
      NO. PART = 7
      NO. DUMMY PART = 0
      NO. JOINT = 6

    SPANNING TREE 
      NO. JOINT BEFORE SPANNING = 6
      NO. VIRTUALJOINT BEFORE SPANNING = 0
      NO. CUTJOINT BEFORE SPANNING = 0
      NO. JOINT AFTER SPANNING = 6
      NO. VIRTUALJOINT AFTER SPANNING = 0
      NO. CUTJOINT AFTER SPANNING = 0

    CHECKING CUTJOINT 
 ======================================================================== 
               CONVERT-PROCESSING IS SUCCESSFULLY FINISHED
 ======================================================================== 

 << RECURDYN/SOLVER PROCESSING >>

 
 ============================================================
 >> BUILDING THE RD/SOLVER STRUCTURE
 ============================================================
 ============================================================
 >> THE SIZE OF USED INBODY ARRAY =           7
 ------------------------------------------------------------
 >> THE SIZE OF USED JOINT ARRAY =          60
 ------------------------------------------------------------
 >> THE SIZE OF USED JOINTIV ARRAY                 =                0
 ------------------------------------------------------------
 >> THE SIZE OF USED EXTPARIV ARRAY                =                0
 ------------------------------------------------------------
 >> THE SIZE OF USED CUTJOINT ARRAY =           6
 ------------------------------------------------------------
 >> THE SIZE OF USED FLEXBODY ARRAY =           0
 ============================================================
 ========================================================================
 >> THE SIZE OF USED N120 ARRAY                    =             3600
 ------------------------------------------------------------------------
 >> THE SIZE OF USED IPN16_1 ARRAY                 =              200
 ------------------------------------------------------------------------
 >> THE SIZE OF USED IPN17 ARRAY                   =              100
 ------------------------------------------------------------------------
 >> THE SIZE OF USED IPN18 ARRAY                   =              200
 ========================================================================
 ========================================================================
 >> THE SIZE OF USED N90 ARRAY                     =             4924
 ------------------------------------------------------------------------
 >> THE SIZE OF USED N90n1 ARRAY                   =             3592
 ------------------------------------------------------------------------
 >> THE SIZE OF USED N90n2 ARRAY                   =             1000
 ------------------------------------------------------------------------
 >> THE SIZE OF USED N90n3 ARRAY                   =             1000
 ========================================================================
 ============================================================
 >> THE SIZE OF USED RBUS ARRAY =       26091
 ------------------------------------------------------------
 >> THE SIZE OF USED IBUS ARRAY =        1717
 ------------------------------------------------------------
 >> THE SIZE OF USED LBUS ARRAY =        1621
 ------------------------------------------------------------
 >> THE SIZE OF USED MGRBUS ARRAY =         196
 ------------------------------------------------------------
 >> THE SIZE OF USED OBUS ARRAY                    =              352
 ========================================================================
 >>> SUCCESSFULLY BUILT THE RD/SOLVER STRUCTURE


                         JOINT INFORMATION 
      =======================================================
        JOINT ID  ACTION MARKER    BASE MARKER     TYPE
      =======================================================
           21          30              31          FIXED    
           85          94              95          FIXED    
           65          74              75      TRANSLATIONAL
          102         111             112      TRANSLATIONAL
          145         155             154        REVOLUTE   
          170         179             180          FIXED    
      =======================================================
 
                          CONSTRAINT INFORMATION
 ========================================================================
         CONSTRAINT ID   ACTION MARKER   BASE MARKER    TYPE
 ========================================================================
             127             138            139     POINT TO CURVE 
             187             196            198     POINT ON SURFAC
 ========================================================================
 
         CONSTRAINT ID    JOINT1    JOINT2    JOINT3    TYPE
 ========================================================================
      1000000           65                          MOTION
 ========================================================================
 
 
 ======================================================================
 *** WHAT = 
 sim/pos,end=0.000000,step=100                                                  
  
 ======================================================================
 *** TOKEN SIMULATION TYPE = pos
 *** TOKEN ENDTIME =  0.000000000000000E+000   1.00000000000000     
 *** TOKEN PLOT STEPSIZE =         100          30
 
 ========================================================================
 >> POSITION ANALYSIS
 ========================================================================


                  INITIAL POSITION CONSTRAINT VIOLATION
 ========================================================================
        ID JOINT               ELEMENT                    VIOLATION
 ========================================================================
        21 FIXED               TRANSLATION ALONG X        0.000000E+00
                               TRANSLATION ALONG Y        0.000000E+00
                               TRANSLATION ALONG Z        0.000000E+00
                               ROTATION ABOUT Z          -3.469447E-18
                               ROTATION ABOUT Y           5.273559E-16
                               ROTATION ABOUT X          -2.320193E-17
 ========================================================================
        85 FIXED               TRANSLATION ALONG X        0.000000E+00
                               TRANSLATION ALONG Y        0.000000E+00
                               TRANSLATION ALONG Z        0.000000E+00
                               ROTATION ABOUT Z           0.000000E+00
                               ROTATION ABOUT Y           0.000000E+00
                               ROTATION ABOUT X           0.000000E+00
 ========================================================================
        65 TRANSLATIONAL       ROTATION ABOUT Y          -1.776357E-14
                               ROTATION ABOUT X           0.000000E+00
                               TRANSLATION ALONG X        0.000000E+00
                               TRANSLATION ALONG Y        0.000000E+00
                               ROTATION ABOUT Z           0.000000E+00
 ========================================================================
       102 TRANSLATIONAL       ROTATION ABOUT Y           1.787499E-14
                               ROTATION ABOUT X          -6.310887E-29
                               TRANSLATION ALONG X        0.000000E+00
                               TRANSLATION ALONG Y        0.000000E+00
                               ROTATION ABOUT Z          -6.213038E-29
 ========================================================================
       145 REVOLUTE            TRANSLATION ALONG X        0.000000E+00
                               TRANSLATION ALONG Y        0.000000E+00
                               TRANSLATION ALONG Z        0.000000E+00
                               ROTATION ABOUT Y           2.005340E-15
                               ROTATION ABOUT X           1.026257E-28
 ========================================================================
       170 FIXED               TRANSLATION ALONG X        0.000000E+00
                               TRANSLATION ALONG Y        0.000000E+00
                               TRANSLATION ALONG Z        0.000000E+00
                               ROTATION ABOUT Z           0.000000E+00
                               ROTATION ABOUT Y          -4.822531E-15
                               ROTATION ABOUT X           7.155734E-18
 ========================================================================
       127 POINT TO CURV       TRANSLATION ALONG X       -1.200256E-07
 ========================================================================
                               TRANSLATION ALONG Y       -1.321509E+01
 ========================================================================
                               TRANSLATION ALONG Z       -2.310656E+01
 ========================================================================
       187 POINT ON SURF       TRANSLATION ALONG X       -5.319814E+00
 ========================================================================
                               TRANSLATION ALONG Y        2.491833E-01
 ========================================================================
                               TRANSLATION ALONG Z       -1.221244E+00
 ========================================================================
   1000000 MOTION                                         0.000000E+00
 ========================================================================
 >> WARNING : THE INITIAL POSITION CONSTRAINTVIOLATIONS ARE GREAT.
 >>> CHECK THE INITIAL CONDITIONS.
 ** CONVERGENCY IS FAILED IN POSITION ANALYSIS. **
 *** CHECK YOUR MODEL. ***
 
 --<< ERROR >>--
 >> ......................................#004003003 
