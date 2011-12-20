'batch_args \-m
=T-DEPL parm=(centrm,check)
CHANGED FUEL MAP TO TEST DANCOFF LOGIC
'49gxlib
v7-238
' brian j. ade - updated 2/3/2010
' data taken from:
'    [1] core design and operating data for cycles 1 and 2
'        of peach bottom 2, n. h. larson, electric power
'        research institute.
'    [2] b.j. ade, fueltemp.nb - mathematica notebook for
'        fuel temperature estimates based on moderator
'        temperature.
'    [3] n.e. todreas and m.s. kazimi, nuclear systems i -
'        thermal hydraulic fundamentals, taylor and francis
'        group, new york, 1990.
'    [4] y.a. cengel and m.a. boles, thermodynamics -
'        an engineering approch, steam tables, mcgraw hill,
'        new york, 2006.
'------------------define alias--------------------------
' assembly layout
'              11  12  13  14  15  16  17
'                  22  23  24  25  26  27
'                      33  34  35  36  37
'                          44  45  46  47
'                              55  56  57
'                                  66  67
'                                      77
read comp
' w/o U234 .0089*U235, w/o U236 0.0046*U235
' 7X7 fuel pins
'
' Data for fuel pins taken from [1]
' Density: 10.32 g/cc from "Stack Density" tables 4-9 of [1]
' Enrichment: 2.93% enr from "U-235 wt%" figures 1-8 of [1]
' Temp: 948.45 K calculated in [2] from eqn. 8-119 of [3]
uo2 1 den=10.320 1.00 948.45 92235 2.93 92234 0.0261 92236 0.0135 92238 97.0304 end
' Data for fuel pins taken from [1]
' Density: 10.32 g/cc from "Stack Density" tables 4-9 of [1]
' Enrichment: 2.93% enr from "U-235 wt%" figures 1-8 of [1]
' Temp: 948.45 K calculated in [2] from eqn. 8-119 of [3]
uo2 201 den=10.320 1.00 948.45 92235 2.93 92234 0.0261 92236 0.0135 92238 97.0304 end
' Data for fuel pins taken from [1]
' Density: 10.32 g/cc from "Stack Density" tables 4-9 of [1]
' Enrichment: 2.93% enr from "U-235 wt%" figures 1-8 of [1]
' Temp: 948.45 K calculated in [2] from eqn. 8-119 of [3]
uo2 2 den=10.320 1.00 948.45 92235 1.94 92234 0.0173 92236 0.0089 92238 98.0338 end
' Data for fuel pins taken from [1]
' Density: 10.32 g/cc from "Stack Density" tables 4-9 of [1]
' Enrichment: 2.93% enr from "U-235 wt%" figures 1-8 of [1]
' Temp: 948.45 K calculated in [2] from eqn. 8-119 of [3]
uo2 202 den=10.320 1.00 948.45 92235 1.94 92234 0.0173 92236 0.0089 92238 98.0338 end
' Data for fuel pins taken from [1]
' Density: 10.32 g/cc from "Stack Density" tables 4-9 of [1]
' Enrichment: 2.93% enr from "U-235 wt%" figures 1-8 of [1]
' Temp: 948.45 K calculated in [2] from eqn. 8-119 of [3]
uo2 212 den=10.320 1.00 948.45 92235 1.94 92234 0.0173 92236 0.0089 92238 98.0338 end
' Data for fuel pins taken from [1]
' Density: 10.32 g/cc from "Stack Density" tables 4-9 of [1]
' Enrichment: 2.93% enr from "U-235 wt%" figures 1-8 of [1]
' Temp: 948.45 K calculated in [2] from eqn. 8-119 of [3]
uo2 203 den=10.320 1.00 948.45 92235 1.69 92234 0.0150 92236 0.0078 92238 98.2872 end
' Data for fuel pins taken from [1]
' Density: 10.32 g/cc from "Stack Density" tables 4-9 of [1]
' Enrichment: 2.93% enr from "U-235 wt%" figures 1-8 of [1]
' Temp: 948.45 K calculated in [2] from eqn. 8-119 of [3]
uo2 213 den=10.320 1.00 948.45 92235 1.69 92234 0.0150 92236 0.0078 92238 98.2872 end
' Data for fuel pins taken from [1]
' Density: 10.32 g/cc from "Stack Density" tables 4-9 of [1]
' Enrichment: 2.93% enr from "U-235 wt%" figures 1-8 of [1]
' Temp: 948.45 K calculated in [2] from eqn. 8-119 of [3]
uo2 4 den=10.320 1.00 948.45 92235 1.33 92234 0.0118 92236 0.0061 92238 98.6520 end
' Data for fuel pins taken from [1]
' Density: 10.19 g/cc from "Stack Density" of type 5A tables 4-9 of [1]
' Enrichment: 2.93% enr + 3 wt% Gd2O3 from figures 1-8 of [1]
' Temp: 948.45 K calculated in [2] from eqn. 8-119 of [3]
uo2 500 den=10.19 0.97 948.45 92235 2.93 92234 0.0261 92236 0.0135 92238 97.0304 end
uo2 501 den=10.19 0.97 948.45 92235 2.93 92234 0.0261 92236 0.0135 92238 97.0304 end
uo2 502 den=10.19 0.97 948.45 92235 2.93 92234 0.0261 92236 0.0135 92238 97.0304 end
uo2 503 den=10.19 0.97 948.45 92235 2.93 92234 0.0261 92236 0.0135 92238 97.0304 end
uo2 504 den=10.19 0.97 948.45 92235 2.93 92234 0.0261 92236 0.0135 92238 97.0304 end
uo2 505 den=10.19 0.97 948.45 92235 2.93 92234 0.0261 92236 0.0135 92238 97.0304 end
uo2 506 den=10.19 0.97 948.45 92235 2.93 92234 0.0261 92236 0.0135 92238 97.0304 end
uo2 507 den=10.19 0.97 948.45 92235 2.93 92234 0.0261 92236 0.0135 92238 97.0304 end
gd2o3 500 den=10.19 0.03 948.45 end
gd2o3 501 den=10.19 0.03 948.45 end
gd2o3 502 den=10.19 0.03 948.45 end
gd2o3 503 den=10.19 0.03 948.45 end
gd2o3 504 den=10.19 0.03 948.45 end
gd2o3 505 den=10.19 0.03 948.45 end
gd2o3 506 den=10.19 0.03 948.45 end
gd2o3 507 den=10.19 0.03 948.45 end
'
' Clad
' Data for fuel clad taken from [1]
' Material: Zirc-2 from "Cladding" of tables 4-9 of [1]
' Density: 6.56 g/cc SCALE standard density assumed
' Temp: 578.71 K calculated in [2] from eqn. 8-119 of [3]
zirc2 101 den=6.56 1 578.71 end
zirc2 102 den=6.56 1 578.71 end
zirc2 103 den=6.56 1 578.71 end
zirc2 104 den=6.56 1 578.71 end
zirc2 105 den=6.56 1 578.71 end
zirc2 301 den=6.56 1 578.71 end
zirc2 302 den=6.56 1 578.71 end
zirc2 303 den=6.56 1 578.71 end
zirc2 304 den=6.56 1 578.71 end
zirc2 305 den=6.56 1 578.71 end
' Channel box
' Data for fuel clad taken from [1]
' Material: Zirc-4 from "Channel" of tables 1 and 2 of [1]
' Density: 6.56 g/cc SCALE standard density assumed
' Temp: 557.96 K Moderator temperature, Tsat @ 1000 psia, [1]
zirc4 630 den=6.56 1 557.96 end
'
' Control rod blades
' Material: B4C from Table 11 of [1]
' ss304 from Table 11 of [1]
' Density: 70% TD from Table 11 of [1]
' 7.94 g/cc SCALE default density
' Temperature: 557.96 K Moderator temperature, Tsat @ 1000 psia, [1]
ss304 645 den=7.94 1.0000 557.96 end
b4c 646 den=1.764 1.0000 557.96 end
'
' Water Moderator 0% Void
' Pressure: 1000 pisa assumed from table 15 of [1], Feedwater outlet, turbin inlet
' Density: calculated with => rho2p = rhof*(1-VF) + rhog*(VF)
' rhof and rhog taken from saturate liquid water table @ 1000 psia [4]
' 0.738079 g/cc from sat. liquid density @ 1000 psia, 00V
' 0.457211 g/cc from sat. liquid density @ 1000 psia, 40V
' 0.176345 g/cc from sat. liquid density @ 1000 psia, 80V
' 0.035913 g/cc from sat. liquid density @ 1000 psia, 100V
' Temperature: 557.95 g/cc from tsat @ 1000 psia [4]
h2o 111 den=0.738079 1.0000 557.96 end
h2o 112 den=0.738079 1.0000 557.96 end
h2o 113 den=0.738079 1.0000 557.96 end
h2o 114 den=0.738079 1.0000 557.96 end
h2o 115 den=0.738079 1.0000 557.96 end
h2o 311 den=0.738079 1.0000 557.96 end
h2o 312 den=0.738079 1.0000 557.96 end
h2o 313 den=0.738079 1.0000 557.96 end
h2o 314 den=0.738079 1.0000 557.96 end
h2o 315 den=0.738079 1.0000 557.96 end
zirc4 111 den=0.046488 1.0000 557.96 end
zirc4 112 den=0.046488 1.0000 557.96 end
zirc4 113 den=0.046488 1.0000 557.96 end
zirc4 114 den=0.046488 1.0000 557.96 end
zirc4 115 den=0.046488 1.0000 557.96 end
zirc4 311 den=0.046488 1.0000 557.96 end
zirc4 312 den=0.046488 1.0000 557.96 end
zirc4 313 den=0.046488 1.0000 557.96 end
zirc4 314 den=0.046488 1.0000 557.96 end
zirc4 315 den=0.046488 1.0000 557.96 end
inconel 111 den=0.008873 1.0000 557.96 end
inconel 112 den=0.008873 1.0000 557.96 end
inconel 113 den=0.008873 1.0000 557.96 end
inconel 114 den=0.008873 
1.0000 557.96
 end
inconel 115 den=0.008873 1.0000 557.96 end
inconel 311 den=0.008873 1.0000 557.96 end
inconel 312 den=0.008873 1.0000 557.96 end
inconel 313 den=0.008873 1.0000 557.96 end
inconel 314 den=0.008873 1.0000 557.96 end
inconel 315 den=0.008873 1.0000 557.96 end
h2o 620 den=0.738079 1.0000 557.96 end
h2o 656 den=0.738079 1.0000 557.96 end
h2o 655 den=0.738079 1.0000 557.96 end
'
' Gap, he
' Density: 2.2218E-4 g/cc calculated from the ideal gas law assuming
' 5 psig from II.e 0-10 psig and 70 F [1]
' from II.e 0-10 psig [1]
' Temperature: 711.15 K calculated in [2] from eqn. 8-119 of [3]
he 121 den=2.2218E-4 1.0000 711.15 end
he 122 den=2.2218E-4 1.0000 711.15 end
he 123 den=2.2218E-4 1.0000 711.15 end
he 124 den=2.2218E-4 1.0000 711.15 end
he 125 den=2.2218E-4 1.0000 711.15 end
he 321 den=2.2218E-4 1.0000 711.15 end
he 322 den=2.2218E-4 1.0000 711.15 end
he 323 den=2.2218E-4 1.0000 711.15 end
he 324 den=2.2218E-4 1.0000 711.15 end
he 325 den=2.2218E-4 1.0000 711.15 end
'
' Detector Materials
h2o 999 den=0.738079 1.0000 557.96 end 
u-235 999 den=0.738079 1.e-10 557.96 end 
end comp
'------------------define celldata-----------------------
' pitch:       1.87452 cm   from table 1 of [1], fuel rod pitch
' fuel radius: 0.60579 cm   from table 5 of [1], pellet o.d. .477"
' gap radius:  0.62103 cm   from table 5 of [1], clad o.d. - 0.037" wall
' clad radius: 0.71501 cm   from table 5 of [1], clad o.d. .563"
' dancoff factors:          calculated from mcdancoff simulation.
'               0% void
'                corner average: 0.144
'                edge average:   0.194
'                0.1428 0.1919 0.1966 0.1935 0.1953 0.1910 0.1417
'                       0.2526 0.2607 0.2554 0.2596 0.2528 0.1943
'                                  gd 0.2589 0.2617     gd 0.1934
'                                     0.2553 0.2626 0.2557 0.1935
'                                                gd 0.2562 0.1940
'                                                   0.2559 0.1975
'                                                          0.1464
'              20% void
'                corner average: 0.164
'                edge average:   0.226
'                0.1635 0.2234 0.2295 0.2259 0.2273 0.2223 0.1621
'                       0.2983 0.3083 0.3025 0.3066 0.2986 0.2256
'                              0.3104 0.3078 0.3123 0.3111 0.2255
'                                     0.3034 0.3107 0.3042 0.2258
'                                            0.3095 0.3046 0.2261
'                                                   0.3001 0.2292
'                                                          0.1677
'              40% void
'                corner average: 0.191
'                edge average:   0.269
'                0.1907 0.2650 0.2731 0.2692 0.2698 0.2637 0.1891
'                       0.3593 0.3723 0.3661 0.3698 0.3597 0.2669
'                                  gd 0.3737 0.3766     gd 0.2683
'                                     0.3699 0.3771 0.3668 0.2687
'                                                gd 0.3674 0.2696
'                                                   0.3633 0.2711
'                                                          0.1936
'              60% void
'                corner average: 0.227
'                edge average:   0.325
'                0.2263 0.3196 0.3308 0.3268 0.3263 0.3181 0.2244
'                       0.4404 0.4580 0.4522 0.4546 0.4409 0.3210
'                              0.4660 0.4642 0.4686 0.4595 0.3250
'                                     0.4603 0.4665 0.4539 0.3261
'                                            0.4652 0.4542 0.3266
'                                                   0.4425 0.3263
'                                                          0.2302
'              80% void
'                corner average: 0.277
'                edge average:   0.405
'                0.2771 0.3973 0.4139 0.4104 0.4080 0.3959 0.2748
'                       0.5568 0.5824 0.5783 0.5780 0.5573 0.3981
'                                  gd 0.5974 0.5994     gd 0.4068
'                                     0.5959 0.5997 0.5786 0.4091
'                                                gd 0.5783 0.4103
'                                                   0.5609 0.4045
'                                                          0.2779
'             100% void
'                corner average: 0.353
'                edge average:   0.529
'                0.3540 0.5144 0.5405 0.5391 0.5330 0.5139 0.3514
'                       0.7325 0.7720 0.7739 0.7686 0.7328 0.5137
'                                  gd 0.8067 0.8066     gd 0.5324
'                                     0.8101 0.8080 0.7730 0.5377
'                                                gd 0.7702 0.5382
'                                                   0.7366 0.5229
'                                                          0.3522
read celldata
latticecell squarep pitch=1.87452 111 fuelr=0.60579 1 gapr=0.62103 121 cladr=0.71501 101 end
latticecell squarep pitch=1.87452 112 fuelr=0.60579 2 gapr=0.62103 122 cladr=0.71501 102 end
latticecell squarep pitch=1.87452 114 fuelr=0.60579 4 gapr=0.62103 124 cladr=0.71501 104 end
'centrmdata alump=0.3 pmc_omit=1 dan2pitch(4)=0.144 end centrmdata
latticecell squarep pitch=1.87452 311 fuelr=0.60579 201 gapr=0.62103 321 cladr=0.71501 301 end
'centrmdata alump=0.3 pmc_omit=1 dan2pitch(201)=0.194 end centrmdata
latticecell squarep pitch=1.87452 312 fuelr=0.60579 202 gapr=0.62103 322 cladr=0.71501 302 end
'centrmdata alump=0.3 pmc_omit=1 dan2pitch(202)=0.194 end centrmdata
latticecell squarep pitch=1.87452 313 fuelr=0.60579 203 gapr=0.62103 323 cladr=0.71501 303 end
'centrmdata alump=0.3 pmc_omit=1 dan2pitch(203)=0.194 end centrmdata
latticecell squarep pitch=1.87452 314 fuelr=0.60579 212 gapr=0.62103 324 cladr=0.71501 304 end
'centrmdata alump=0.3 pmc_omit=1 dan2pitch(212)=0.144 end centrmdata
latticecell squarep pitch=1.87452 315 fuelr=0.60579 213 gapr=0.62103 325 cladr=0.71501 305 end
'centrmdata alump=0.3 pmc_omit=1 dan2pitch(213)=0.144 end centrmdata
multiregion cylindrical right_bdy=white end
500 0.21418 501 0.30290 502 0.37097 503 0.42836 504 0.47892 505 0.52463 506 0.56666 507 0.60579 125 0.62103 105 0.71501 115 1.05758 end zone
end celldata
'--------------------END CELLDATA-----------------------                                                                                                                                                                                                    
'------------------DEFINE BRANCHES----------------------                                                                                                                                                                                                    
' Branches contained in separate tree files.  Branches loosely taken from                                                                                                                                                                                   
' previously used HELIOS branches by UM in HELIOS-PARCS PB C1 validation.                                                                                                                                                                                   
'read branch                                                                                                                                                                                                                                                 
'define fuel 1 2 4 500 501 502 503 504 505 506 507 23 24 25 26 34 35 44 45 46 55 56 66 22 11 33 36 331 361 332 362 333 363 334 364 335 365 336 366 337 367 201 202 212 203 213 37 47 57 14 15 16 27 67 77 12 13 17 end
'define mod 111 112 113 114 115 311 312 313 314 315 end
'define crin 645 646 end
'define crout 655 656 end
'define d2pset 100 4 0.353 201 0.529 202 0.529 203 0.529 212 0.353 213 0.353 end
'define d2pset 80 4 0.277 201 0.405 202 0.405 203 0.405 212 0.277 213 0.277 end
'define d2pset 60 4 0.227 201 0.325 202 0.325 203 0.325 212 0.227 213 0.227 end
'define d2pset 40 4 0.191 201 0.269 202 0.269 203 0.269 212 0.191 213 0.191 end
'define d2pset 20 4 0.164 201 0.226 202 0.226 203 0.226 212 0.164 213 0.164 end
'define d2pset 1 4 0.144 201 0.194 202 0.194 203 0.194 212 0.144 213 0.144 end
'end branch
'------------------END BRANCHES-----------------------                                                                                                                                                                                                      
'---------DEFINE DEPLETION and BURNUP-----------------                                                                                                                                                                                                      
' Deplete all fuels, assign 1fuels to all applicable fuels to save XS processing time.                                                                                                                                                                      
read depletion 23 24 25 26 34 35 44 45 46 55 56 66 22 11 37 47 57 14 15 16 27 67 77 12 13 17 flux 33 36 331 361 332 362 333 363 334 364 335 365 336 366 337 367 end assign 1 23 24 25 26 34 35 44 45 46 55 56 66 end assign 2 22 end assign 4 11 end assign 
201 37 47 57 end assign 202 14 15 16 27 67 end assign 212 77 end assign 203 12 13 end assign 213 17 end assign 500 33 36 end assign 501 331 361 end assign 502 332 362 end assign 503 333 363 end assign 504 334 364 end assign 505 335 365 end assign 506  
336 366 end assign 507 337 367 end end depletion                                                                                                                                                                                                            
'                                                                                                                                                                                                                                                           
read burndata                                                                                                                                                                                                                                               
' Generate cross sections at burnups of:                                                                                                                                                                                                                    
'     0.0000   0.0461   0.3602   0.6744   0.9885   1.3026   1.6168                                                                                                                                                                                          
'     1.9309   2.2451   2.5592   2.8733   3.1875   3.5016   4.0501                                                                                                                                                                                          
'     4.5986   5.1471   5.6956   6.2441   6.7926   7.3411   7.8896                                                                                                                                                                                          
'     8.4381   8.9866   9.5351   10.0836  10.6321  11.1806  11.7291                                                                                                                                                                                         
'     12.2776  12.8261  13.3746  13.9231  14.4716  15.0201  16.2268                                                                                                                                                                                         
'     18.5304  20.8341  23.1378  25.4415  27.7452  31.5847  35.4242                                                                                                                                                                                         
'     39.2637  43.1031  46.9426  50.7821                                                                                                                                                                                                                    
power=23.037 burn=   2  down=0  nlib= 0  end                                                                                                                                                                                                                
power=23.037 burn= 150  down=0  nlib=10  end                                                                                                                                                                                                                
power=23.037 burn= 500  down=0  nlib=20  end                                                                                                                                                                                                                
power=23.037 burn= 600  down=0  nlib= 5  end                                                                                                                                                                                                                
power=23.037 burn=1000  down=0  nlib= 5  end                                                                                                                                                                                                                
end burndata                                                                                                                                                                                                                                                
'------------DEFINE NEWT MODEL--------------------                                                                                                                                                                                                          
read model                                                                                                                                                                                                                                                  
PB CYCLE1
'-------NEWT PARAMETER INPUT BLOCK-------                                                                                                                                                                                                                   
read parm                                                                                                                                                                                                                                                   
echo=yes drawit=yes run=yes prtflux=no solntype=b1                                                                                                                                                                                                          
'cmfd=1 
epsilon=1e-5 converg=mix inners=2 therm=yes 
'therms=1 
outers=9999 xycmfd=1                                                                                                                                                                            
det=999                                                                                                                                                                                                                                                     
end parm                                                                                                                                                                                                                                                    
read materials
mix= 23 pn=1 com='2.93% UO2' end
mix= 24 pn=1 com='2.93% UO2' end
mix= 25 pn=1 com='2.93% UO2' end
mix= 26 pn=1 com='2.93% UO2' end
mix= 34 pn=1 com='2.93% UO2' end
mix= 35 pn=1 com='2.93% UO2' end
mix= 44 pn=1 com='2.93% UO2' end
mix= 45 pn=1 com='2.93% UO2' end
mix= 46 pn=1 com='2.93% UO2' end
mix= 55 pn=1 com='2.93% UO2' end
mix= 56 pn=1 com='2.93% UO2' end
mix= 66 pn=1 com='2.93% UO2' end
mix= 22 pn=1 com='1.94% UO2' end
mix= 11 pn=1 com='1.33% UO2' end
mix= 33 pn=1 com='2.93% UO2 (3% Gd)' end
mix= 36 pn=1 com='2.93% UO2 (3% Gd)' end
mix= 331 pn=1 com='2.93% UO2 (3% Gd)' end
mix= 361 pn=1 com='2.93% UO2 (3% Gd)' end
mix= 332 pn=1 com='2.93% UO2 (3% Gd)' end
mix= 362 pn=1 com='2.93% UO2 (3% Gd)' end
mix= 333 pn=1 com='2.93% UO2 (3% Gd)' end
mix= 363 pn=1 com='2.93% UO2 (3% Gd)' end
mix= 334 pn=1 com='2.93% UO2 (3% Gd)' end
mix= 364 pn=1 com='2.93% UO2 (3% Gd)' end
mix= 335 pn=1 com='2.93% UO2 (3% Gd)' end
mix= 365 pn=1 com='2.93% UO2 (3% Gd)' end
mix= 336 pn=1 com='2.93% UO2 (3% Gd)' end
mix= 366 pn=1 com='2.93% UO2 (3% Gd)' end
mix= 337 pn=1 com='2.93% UO2 (3% Gd)' end
mix= 367 pn=1 com='2.93% UO2 (3% Gd)' end
mix= 37 pn=1 com='2.93% UO2, edge' end
mix= 47 pn=1 com='2.93% UO2, edge' end
mix= 57 pn=1 com='2.93% UO2, edge' end
mix= 14 pn=1 com='1.94% UO2, edge' end
mix= 15 pn=1 com='1.94% UO2, edge' end
mix= 16 pn=1 com='1.94% UO2, edge' end
mix= 27 pn=1 com='1.94% UO2, edge' end
mix= 67 pn=1 com='1.94% UO2, edge' end
mix= 77 pn=1 com='1.94% UO2, corner' end
mix= 12 pn=1 com='1.69% UO2, edge' end
mix= 13 pn=1 com='1.69% UO2, edge' end
mix= 17 pn=1 com='1.69% UO2, corner' end
mix= 111 pn=2 com='H2O(void)' end
mix= 112 pn=2 com='H2O(void)' end
mix= 113 pn=2 com='H2O(void)' end
mix= 114 pn=2 com='H2O(void)' end
mix= 115 pn=2 com='H2O(void)' end
mix= 311 pn=2 com='H2O(void)' end
mix= 312 pn=2 com='H2O(void)' end
mix= 313 pn=2 com='H2O(void)' end
mix= 314 pn=2 com='H2O(void)' end
mix= 315 pn=2 com='H2O(void)' end
mix= 101 pn=1 com='Zirc2' end
mix= 102 pn=1 com='Zirc2' end
mix= 103 pn=1 com='Zirc2' end
mix= 104 pn=1 com='Zirc2' end
mix= 105 pn=1 com='Zirc2' end
mix= 301 pn=1 com='Zirc2' end
mix= 302 pn=1 com='Zirc2' end
mix= 303 pn=1 com='Zirc2' end
mix= 304 pn=1 com='Zirc2' end
mix= 305 pn=1 com='Zirc2' end
mix= 121 pn=1 com='Helium' end
mix= 122 pn=1 com='Helium' end
mix= 123 pn=1 com='Helium' end
mix= 124 pn=1 com='Helium' end
mix= 125 pn=1 com='Helium' end
mix= 321 pn=1 com='Helium' end
mix= 322 pn=1 com='Helium' end
mix= 323 pn=1 com='Helium' end
mix= 324 pn=1 com='Helium' end
mix= 325 pn=1 com='Helium' end
mix= 620 pn=2 com='H2O(solid)' end
mix= 630 pn=1 com='Zirc4' end
mix= 645 pn=1 com='SS304' end
mix= 646 pn=1 com='Absorber' end
mix= 655 pn=2 com='SS304(swap)' end
mix= 656 pn=2 com='Absorber(swap)' end
mix=999 pn=2 com='Detector' end
end mate
'--NEWT GEOMETRY                                                                                                                                                                                                                                            
' Pitch:       1.87452 cm   from Table 1 of [1], Fuel Rod Pitch                                                                                                                                                                                             
' Fuel Radius: 0.60579 cm   from Table 5 of [1], Pellet o.d. .477"                                                                                                                                                                                          
' Gap Radius:  0.62103 cm   from Table 5 of [1], Clad o.d. - 0.037" wall                                                                                                                                                                                    
' Clad radius: 0.71501 cm   from Table 5 of [1], Clad o.d. .563"                                                                                                                                                                                            
' Model Refinement:                                                                                                                                                                                                                                         
' 1. 0.7 cm ring of water around normal fuel pins for enhanced flux shape near pins                                                                                                                                                                         
' 2. (3) 0.3 cm rings of water around Gd-bearing fuel pins for enhanced flux shape                                                                                                                                                                          
read geom                                                                                                                                                                                                                                                   
' lattice position   11                                                                                                                                                                                                                                     
unit   11                                                                                                                                                                                                                                                   
'cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 1   6.0579e-1
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726
'cuboid   5  0.93726 -.93726  .93726  -0.93726                                                                                                                                                                                                                                        
media  11 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' lattice position   12                                                                                                                                                                                                                                     
unit   12                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  12 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' lattice position   13                                                                                                                                                                                                                                     
unit   13                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  13 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' lattice position   14                                                                                                                                                                                                                                     
unit   14                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  14 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' lattice position   15                                                                                                                                                                                                                                     
unit   15                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  15 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' lattice position   16                                                                                                                                                                                                                                     
unit   16                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  16 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' lattice position   17                                                                                                                                                                                                                                     
unit   17                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  17 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' lattice position   22                                                                                                                                                                                                                                     
unit   22                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  22 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' lattice position   23                                                                                                                                                                                                                                     
unit   23                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  23 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' lattice position   24                                                                                                                                                                                                                                     
unit   24                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  24 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' lattice position   25                                                                                                                                                                                                                                     
unit   25                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  25 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' lattice position   26                                                                                                                                                                                                                                     
unit   26                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  26 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' lattice position   27                                                                                                                                                                                                                                     
unit   27                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  27 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' lattice position   33                                                                                                                                                                                                                                     
unit   33                                                                                                                                                                                                                                                   
cylinder 1    0.21418                                                                                                                                                                                                                                       
cylinder 2    0.30290                                                                                                                                                                                                                                       
cylinder 3    0.37097                                                                                                                                                                                                                                       
cylinder 4    0.42836                                                                                                                                                                                                                                       
cylinder 5    0.47892                                                                                                                                                                                                                                       
cylinder 6    0.52463                                                                                                                                                                                                                                       
cylinder 7    0.56666                                                                                                                                                                                                                                       
cylinder 8    0.60579                                                                                                                                                                                                                                       
cylinder 9    0.62103                                                                                                                                                                                                                                       
cylinder 10   0.71501                                                                                                                                                                                                                                       
cylinder 11   0.74501                                                                                                                                                                                                                                       
cylinder 12   0.77501                                                                                                                                                                                                                                       
cylinder 13   0.80501                                                                                                                                                                                                                                       
cuboid   14 4p0.93726                                                                                                                                                                                                                                       
media  33 1 1                                                                                                                                                                                                                                               
media 331 1 2  -1                                                                                                                                                                                                                                           
media 332 1 3  -2                                                                                                                                                                                                                                           
media 333 1 4  -3                                                                                                                                                                                                                                           
media 334 1 5  -4                                                                                                                                                                                                                                           
media 335 1 6  -5                                                                                                                                                                                                                                           
media 336 1 7  -6                                                                                                                                                                                                                                           
media 337 1 8  -7                                                                                                                                                                                                                                           
media 121 1 9  -8                                                                                                                                                                                                                                           
media 101 1 10 -9                                                                                                                                                                                                                                           
media 111 1 11 -10                                                                                                                                                                                                                                          
media 111 1 12 -11                                                                                                                                                                                                                                          
media 111 1 13 -12                                                                                                                                                                                                                                          
media 111 1 14 -13                                                                                                                                                                                                                                          
boundary    14  4 4                                                                                                                                                                                                                                         
' lattice position   34                                                                                                                                                                                                                                     
unit   34                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  34 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' lattice position   35                                                                                                                                                                                                                                     
unit   35                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  35 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' lattice position   36                                                                                                                                                                                                                                     
unit   36                                                                                                                                                                                                                                                   
cylinder 1    0.21418                                                                                                                                                                                                                                       
cylinder 2    0.30290                                                                                                                                                                                                                                       
cylinder 3    0.37097                                                                                                                                                                                                                                       
cylinder 4    0.42836                                                                                                                                                                                                                                       
cylinder 5    0.47892                                                                                                                                                                                                                                       
cylinder 6    0.52463                                                                                                                                                                                                                                       
cylinder 7    0.56666                                                                                                                                                                                                                                       
cylinder 8    0.60579                                                                                                                                                                                                                                       
cylinder 9    0.62103                                                                                                                                                                                                                                       
cylinder 10   0.71501                                                                                                                                                                                                                                       
cylinder 11   0.74501                                                                                                                                                                                                                                       
cylinder 12   0.77501                                                                                                                                                                                                                                       
cylinder 13   0.80501                                                                                                                                                                                                                                       
cuboid   14 4p0.93726                                                                                                                                                                                                                                       
media  36 1 1                                                                                                                                                                                                                                               
media 361 1 2  -1                                                                                                                                                                                                                                           
media 362 1 3  -2                                                                                                                                                                                                                                           
media 363 1 4  -3                                                                                                                                                                                                                                           
media 364 1 5  -4                                                                                                                                                                                                                                           
media 365 1 6  -5                                                                                                                                                                                                                                           
media 366 1 7  -6                                                                                                                                                                                                                                           
media 367 1 8  -7                                                                                                                                                                                                                                           
media 121 1 9  -8                                                                                                                                                                                                                                           
media 101 1 10 -9                                                                                                                                                                                                                                           
media 111 1 11 -10                                                                                                                                                                                                                                          
media 111 1 12 -11                                                                                                                                                                                                                                          
media 111 1 13 -12                                                                                                                                                                                                                                          
media 111 1 14 -13                                                                                                                                                                                                                                          
boundary    14  4 4                                                                                                                                                                                                                                         
' lattice position   37                                                                                                                                                                                                                                     
unit   37                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  37 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4 

' CHANGING THIS ONE TO HAVE NO FUEL FOR TESTING
' lattice position   44                                                                                                                                                                                                                                     
unit   44                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
'media  44 1 1 
'media 121 1 2 -1 
'media 101 1 3 -2 
' Making them water
media 111 1 1 
media 111 1 2 -1 
media 111 1 3 -2 
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4 

' lattice position   45                                                                                                                                                                                                                                     
unit   45                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  45 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' lattice position   46                                                                                                                                                                                                                                     
unit   46                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  46 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' lattice position   47                                                                                                                                                                                                                                     
unit   47                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  47 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' lattice position   55                                                                                                                                                                                                                                     
unit   55                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  55 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' lattice position   56                                                                                                                                                                                                                                     
unit   56                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  56 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' lattice position   57                                                                                                                                                                                                                                     
unit   57                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  57 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' lattice position   66                                                                                                                                                                                                                                     
unit   66                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  66 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' lattice position   67                                                                                                                                                                                                                                     
unit   67                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  67 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' lattice position   77                                                                                                                                                                                                                                     
unit   77                                                                                                                                                                                                                                                   
cylinder 1   0.60579                                                                                                                                                                                                                                        
cylinder 2   0.62103                                                                                                                                                                                                                                        
cylinder 3   0.71501                                                                                                                                                                                                                                        
cylinder 4   0.78501                                                                                                                                                                                                                                        
cuboid   5 4p0.93726                                                                                                                                                                                                                                        
media  77 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
boundary    5  4 4                                                                                                                                                                                                                                          
' Channel corners                                                                                                                                                                                                                                           
' Channel corners placed in geometry by using a hole.                                                                                                                                                                                                       
' Thickness:  0.2032 cm   from 0.080" in Table 1 of [1] - same as channel                                                                                                                                                                                   
' Radius:     0.9652 cm   from 0.380" in Table 1 of [1]                                                                                                                                                                                                     
' Northeast Corner                                                                                                                                                                                                                                          
unit   80                                                                                                                                                                                                                                                   
cylinder 1   0.60579  chord +x=0.0    chord +y=0.0     origin x=-0.1143 y=-0.1143                                                                                                                                                                           
cylinder 2   0.62103  chord +x=0.0    chord +y=0.0     origin x=-0.1143 y=-0.1143                                                                                                                                                                           
cylinder 3   0.71501  chord +x=0.0    chord +y=0.0     origin x=-0.1143 y=-0.1143                                                                                                                                                                           
cylinder 4   0.78501  chord +x=0.0    chord +y=0.0     origin x=-0.1143 y=-0.1143                                                                                                                                                                           
cylinder 5   0.9652   chord +x=0.0    chord +y=0.0                                                                                                                                                                                                          
cylinder 6   1.1684   chord +x=0.0    chord +y=0.0                                                                                                                                                                                                          
cuboid   7   1.2 0.0  1.2 0.0                                                                                                                                                                                                                               
media  17 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
media 630 1 6 -5                                                                                                                                                                                                                                            
media 620 1 7 -6                                                                                                                                                                                                                                            
boundary    7  2 2                                                                                                                                                                                                                                          
' Southeast Corner                                                                                                                                                                                                                                          
unit   81                                                                                                                                                                                                                                                   
cylinder 1   0.60579  chord +x=0.0    chord +y=0.0     origin x=-0.1143 y=-0.1143                                                                                                                                                                           
cylinder 2   0.62103  chord +x=0.0    chord +y=0.0     origin x=-0.1143 y=-0.1143                                                                                                                                                                           
cylinder 3   0.71501  chord +x=0.0    chord +y=0.0     origin x=-0.1143 y=-0.1143                                                                                                                                                                           
cylinder 4   0.78501  chord +x=0.0    chord +y=0.0     origin x=-0.1143 y=-0.1143                                                                                                                                                                           
cylinder 5   0.9652   chord +x=0.0    chord +y=0.0                                                                                                                                                                                                          
cylinder 6   1.1684   chord +x=0.0    chord +y=0.0                                                                                                                                                                                                          
cuboid   7   1.2 0.0  1.2 0.0                                                                                                                                                                                                                               
media  11 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
media 630 1 6 -5                                                                                                                                                                                                                                            
media 620 1 7 -6                                                                                                                                                                                                                                            
boundary    7  2 2                                                                                                                                                                                                                                          
' Southwest Corner                                                                                                                                                                                                                                          
unit   82                                                                                                                                                                                                                                                   
cylinder 1   0.60579  chord +x=0.0    chord +y=0.0     origin x=-0.1143 y=-0.1143                                                                                                                                                                           
cylinder 2   0.62103  chord +x=0.0    chord +y=0.0     origin x=-0.1143 y=-0.1143                                                                                                                                                                           
cylinder 3   0.71501  chord +x=0.0    chord +y=0.0     origin x=-0.1143 y=-0.1143                                                                                                                                                                           
cylinder 4   0.78501  chord +x=0.0    chord +y=0.0     origin x=-0.1143 y=-0.1143                                                                                                                                                                           
cylinder 5   0.9652   chord +x=0.0    chord +y=0.0                                                                                                                                                                                                          
cylinder 6   1.1684   chord +x=0.0    chord +y=0.0                                                                                                                                                                                                          
cuboid   7   1.2 0.0  1.2 0.0                                                                                                                                                                                                                               
media  17 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
media 630 1 6 -5                                                                                                                                                                                                                                            
media 620 1 7 -6                                                                                                                                                                                                                                            
boundary    7  2 2                                                                                                                                                                                                                                          
' Northwest Corner                                                                                                                                                                                                                                          
unit   83                                                                                                                                                                                                                                                   
cylinder 1   0.60579  chord +x=0.0    chord +y=0.0     origin x=-0.1143 y=-0.1143                                                                                                                                                                           
cylinder 2   0.62103  chord +x=0.0    chord +y=0.0     origin x=-0.1143 y=-0.1143                                                                                                                                                                           
cylinder 3   0.71501  chord +x=0.0    chord +y=0.0     origin x=-0.1143 y=-0.1143                                                                                                                                                                           
cylinder 4   0.78501  chord +x=0.0    chord +y=0.0     origin x=-0.1143 y=-0.1143                                                                                                                                                                           
cylinder 5   0.9652   chord +x=0.0    chord +y=0.0                                                                                                                                                                                                          
cylinder 6   1.1684   chord +x=0.0    chord +y=0.0                                                                                                                                                                                                          
cuboid   7   1.2 0.0  1.2 0.0                                                                                                                                                                                                                               
media  77 1 1                                                                                                                                                                                                                                               
media 121 1 2 -1                                                                                                                                                                                                                                            
media 101 1 3 -2                                                                                                                                                                                                                                            
media 111 1 4 -3                                                                                                                                                                                                                                            
media 111 1 5 -4                                                                                                                                                                                                                                            
media 630 1 6 -5                                                                                                                                                                                                                                            
media 620 1 7 -6                                                                                                                                                                                                                                            
boundary    7  2 2                                                                                                                                                                                                                                          
' Control Rod Blades                                                                                                                                                                                                                                        
' Control rod blades placed in the geometry using a hole                                                                                                                                                                                                    
' Tube o.r.:         0.23876 cm  from Table 11 "Tube Dimensions", 0.188" o.d. [1]                                                                                                                                                                           
' Tube i.r.:         0.17526 cm  from Table 11 "Tube Dimensions", 0.025" wall thickness [1]                                                                                                                                                                 
' Blade Thickness:   0.39624 cm  from Table 11 "Control Blade Full Thickness",                                                                                                                                                                              
'                                0.3120" wall thickness [1]                                                                                                                                                                                                 
' Sheath Thickness: 0.14224 cm  from Table 11 "Sheath Thickness" 0.056" [1]                                                                                                                                                                                 
' Blade Half Span:  12.38250 cm  from Table 11 "Blade Half Span" 4.875" [1]                                                                                                                                                                                 
' Central Support:   1.98501 cm  from Table 11 "Central Structure Wing Length" 0.7815" [1]                                                                                                                                                                  
' Number of Tubes:  84           from Table 11 "Number of Control Material Tubes per Rod" [1]                                                                                                                                                               
' Assumed that absorber tubes touch adjacent absorber tubes                                                                                                                                                                                                 
' Assumed rounded blade tip was negligable - modeled as a square                                                                                                                                                                                            
unit 200                                                                                                                                                                                                                                                    
com='control wing half-pellet'                                                                                                                                                                                                                              
cylinder 10  0.17526 chord -y=0                                                                                                                                                                                                                             
cylinder 20  0.23876 chord -y=0                                                                                                                                                                                                                             
cuboid   40    0.23876 -0.23876  0 -0.25400                                                                                                                                                                                                                 
media  656  1  10                                                                                                                                                                                                                                           
media  655  1 -10  20                                                                                                                                                                                                                                       
media  620  1 -20  40                                                                                                                                                                                                                                       
boundary 40 2 1                                                                                                                                                                                                                                             
unit 201                                                                                                                                                                                                                                                    
com='control wing half-pellet'                                                                                                                                                                                                                              
cylinder 10  0.17526 chord +x=0                                                                                                                                                                                                                             
cylinder 20  0.23876 chord +x=0                                                                                                                                                                                                                             
cuboid   40  0.25400 0.0  0.23876 -0.23876                                                                                                                                                                                                                  
media  656  1  10                                                                                                                                                                                                                                           
media  655  1 -10  20                                                                                                                                                                                                                                       
media  620  1 -20  40                                                                                                                                                                                                                                       
boundary 40 1 2
   
unit 202                                                                                                                                                                                                                                                    
com='control blade wing'                                                                                                                                                                                                                                    
cuboid   10  10.17016 0.0  0.0 -0.39625                                                                                                                                                                                                                      
array 200 10 place 1 1  .23876  0.0                                                                                                                                                                                                                         
media  655  1 10                                                                                                                                                                                                                                            
boundary 10

unit 203                                                                                                                                                                                                                                                    
com='control blade wing'                                                                                                                                                                                                                                    
cuboid   10   0.39625 0.0  0.0 -10.17016                                                                                                                                                                                                                    
array 201 10 place 1 1   0.0 -9.78916                                                                                                                                                                                                                       
media  655  1 10                                                                                                                                                                                                                                            
boundary 10

unit 205                                                                                                                                                                                                                                                    
com='control blade central support'                                                                                                                                                                                                                         
cuboid   10   2.21234 0.0  0.0 -0.39625                                                                                                                                                                                                                     
media  655  1 10                                                                                                                                                                                                                                            
boundary 10

' !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
' Need another unit to describe the other part of the control blade central support
unit 206
com='control blade central support - vertical part'                                                                                                                                                                                                                         
cuboid  10  0.39625  0.0  -0.39625 -2.21234
media  655  1 10                                                                                                                                                                                                                                            
boundary  10
                                                                                                                                                                                                                                                 
' Detector Unit                                                                                                                                                                                                                                             
'unit 300                                                                                                                                                                                                                                                    
'com='LPRM detector model'                                                                                                                                                                                                                                   
'cylinder 10 0.64516 chord -x=0 chord +y=0                                                                                                                                                                                                                   
'media  999  1 10                                                                                                                                                                                                                                            
'boundary 10 2 2

' Global unit                                                                                                                                                                                                                                               
' Channel                                                                                                                                                                                                                                                   
' Thickness:       0.2032 cm   from 0.080" in Table 1 of [1] - same as channel                                                                                                                                                                              
' Assembly Pitch: 15.24 cm     from control blade pitch, Table 11, 12.0" [1]                                                                                                                                                                                
' Rounded channel corners, partial pins with the corners, and control blades                                                                                                                                                                                
'   are placed using holes.                                                                                                                                                                                                                                 
global unit 100                                                                                                                                                                                                                                             
cuboid  1   6.94182 -6.46430  6.46430 -6.94182                                                                                                                                                                                                              
array 1 1  place 4 4  0.23876 -0.23876                                                                                                                                                                                                                      
cuboid  2   7.14502 -6.66750  6.66750 -7.14502                                                                                                                                                                                                              
cuboid  10  4p7.62                                                                                                                                                                                                                                          
media   111 1 1                                                                                                                                                                                                                                             
media   630 1 2 -1                                                                                                                                                                                                                                          
media   620 1 10 -2                                                                                                                                                                                                                                         
hole 80  origin x= 5.97662 y= 5.49910                                                                                                                                                                                                                       
hole 81  origin x=-5.49910 y= 5.49910  rotate a1= 90                                                                                                                                                                                                        
hole 82  origin x=-5.49910 y=-5.97662  rotate a1=180                                                                                                                                                                                                        
hole 83  origin x= 5.97662 y=-5.97662  rotate a1=270                                                                                                                                                                                                        
hole 202 origin x=-5.40766 y= 7.62                                                                                                                                                                                                                          
hole 203 origin x=-7.62    y= 5.40766                                                                                                                                                                                                                       
hole 205 origin x=-7.62    y= 7.62                                                                                                                                                                                                                          
'hole 205 origin x=-7.22375 y= 7.62    rotate a1=270
hole 206 origin x=-7.62    y= 7.62
'hole 300 origin x=7.62     y=-7.62                                                                                                                                                                                                                          
boundary 10 12 12
end geom                                                                                                                                                                                                                                                    
' ---------ARRAYS--------                                                                                                                                                                                                                                   
read array                                                                                                                                                                                                                                                  
ara=1 nux=7 nuy=7 pinpow    no typ=cuboidal                                                                                                                                                                                                                              
fill                                                                                                                                                                                                                                                        
17  17  17  17  17  17  17
17  17  17  17  17  44  17
17  17  17  17  17  44  17
17  17  17  17  17  17  17
17  17  17  17  17  44  17
17  17  17  17  17  17  17                                                                                                                                                                                                                              
17  17  17  17  17  17  17 end fill                                                                                                                                                                                                                         
ara=200 nux=21 nuy=1                                                                                                                                                                                                                                        
fill 21r200  end fill                                                                                                                                                                                                                                       
ara=201 nux=1  nuy=21                                                                                                                                                                                                                                       
fill 21r201  end fill                                                                                                                                                                                                                                       
end array                                                                                                                                                                                                                                                   
' --------BOUNDARY CONDITIONS--------                                                                                                                                                                                                                       
read bounds                                                                                                                                                                                                                                                 
all=refl                                                                                                                                                                                                                                                   
end bounds                                                                                                                                                                                                                                                  
read collapse                                                                                                                                                                                                                                               
' 2-group collapse (Eth=0.625eV)                                                                                                                                                                                                                            
 199r1  39r2
end collapse                                                                                                                                                                                                                                                
read homog                                                                                                                                                                                                                                                  
900 pbt2b     11  12  13  14  15  16  17                                                                                                                                                                                                                    
22  23  24  25  26  27                                                                                                                                                                                                                                      
33  34  35  36  37                                                                                                                                                                                                                                          
331         361                                                                                                                                                                                                                                             
332         362                                                                                                                                                                                                                                             
333         363                                                                                                                                                                                                                                             
334         364                                                                                                                                                                                                                                             
335         365                                                                                                                                                                                                                                             
336         366                                                                                                                                                                                                                                             
337         367                                                                                                                                                                                                                                             
44  45  46  47                                                                                                                                                                                                                                              
55  56  57                                                                                                                                                                                                                                                  
66  67                                                                                                                                                                                                                                                      
77                                                                                                                                                                                                                                                          
101                                                                                                                                                                                                                                                         
111                                                                                                                                                                                                                                                         
121                                                                                                                                                                                                                                                         
620                                                                                                                                                                                                                                                         
630                                                                                                                                                                                                                                                         
645                                                                                                                                                                                                                                                         
646                                                                                                                                                                                                                                                         
655                                                                                                                                                                                                                                                         
656                                                                                                                                                                                                                                                         
999  end                                                                                                                                                                                                                                                    
end homog                                                                                                                                                                                                                                                   
read adf                                                                                                                                                                                                                                                    
1 900 n= 7.62  s=-7.62  e= 7.62 w=-7.62                                                                                                                                                                                                                     
end adf                                                                                                                                                                                                                                                     
end model
end
