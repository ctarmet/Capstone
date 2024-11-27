# Polytope_GCG
### Christoffer Tarmet

## ChaosColor programs
 Description:  Plays a GCG in 2- and 3-dimensional polygons and plots the result. At the bottom of the program, change the number of vertices of the polytope by changing the first argument. Change the ratio moved towards the randomly selected vertex by changing the second argument. Change the number of iterations by modifying the third argument. 

## Figure8.py
Creates Figure 8 in the paper.

## Figures6_7_9_10
Creates Figures 6, 7, 9, 10 in the paper. To recreate, you must first download manim. Then, run the program and select the prefered scene. 

## Overlap_testing programs
Programs that iteritively finds an estimate to the optimal ratio, as well as finding delta_parallel and the edge length. Select the number of vertices of the polytope by modifying the first argument of the overlap_test function at the bottom of the program. The second argument is the start point for the r-value. To minimize the run time it is recommended that this argument is relatively close to the conjectured optimal ratio. The program will stop when the computed optimal ratio has at least 5 correct decimals.