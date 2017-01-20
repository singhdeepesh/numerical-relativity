from sympy import *
from gravipy import *


R, theta , phi = symbols("R, theta, phi")
C = Coordinates('\chi', [theta, phi])


### PRINT METRIC ###
Metric = diag(R**2, R**2*sin(theta)**2)
g = MetricTensor('g',C,Metric)
print "Metric is : " 
print g(All,All)
print "\n"


### COMPUTE CHRISTOFFEL SYMBOL ###
Ga = Christoffel('Ga',g)
#print Ga.components      ----- This command is not working for me
print "Christoffel symbol is : " 
print Ga(-All,All,All)
print "\n"


### COMPUTE RIEMANN TENSOR ###
Rm = Riemann('Rm',g)
print "Riemann tensor is : "
print Rm(-All,All,All,All)
print "\n"


### COMPUTE RICCI TENSOR AND RICCI SCALAR ###
Ri = Ricci('Ri',g)
print "Ricci tensor is : " 
print Ri(All, All)
print "\n"
print "Ricci scalar is : " , Ri.scalar()
print "\n"
