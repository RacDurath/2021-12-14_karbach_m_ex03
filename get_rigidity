# 2021-12-17_ex03
# Marcel Karbach, 4000031
# Course: Applications of Accelerators

import numpy as np
import math

def get_rigidity(AE, Q, m_0, C):

	global e_0
	global c_0
	q = (Q * e_0)
	mkg = (m_0 * ukg)
	Ekin = (m_0 * AE)
	gamma = ((Ekin) / (m_0 * c_mev) + 1)
	gamma2 = pow(gamma, 2)
	v = math.sqrt((1 - (1 / gamma2)))
	vabs = (v * c_0)
	rho = (C / (2 * pi))
	B = ((gamma  * vabs * (mkg/q)/rho))
	rigidity = (B * rho)

	return rigidity, Ekin, gamma, v, vabs, rho, B, mkg

c_0 = int(299792458)
c_mev = float(931.5)
e_0 = float(1.602E-19)
ukg = float(1.66E-27)
pi = math.pi

# input of data
print ('For calculating the magnetic rigidity some parameter are needed. Please enter these here. ')
AE = int(input('Enter energy per nucleon [MeV]: ')) 
Q = int(input('Enter charge of particle [+/-(Number)]:'))
m_0 = int(input('Enter mass of particle [u]: ')) 
C = int(input('Enter circumference [m]: '))

result, Ekin, gamma, v, vabs, rho, B, mkg = get_rigidity(AE, Q, m_0, C)

print ('')
print ('The magnetic rigidity is '+ str(result), '[Tm]') 
print ('') 
print ('Parameter:') 
print ('E_kin = '+ str(Ekin), '[MeV]')
print ('B = '+ str(B), '[T]')
print ('rho = '+ str(rho), '[m]')

print ('rel. gamma = '+ str(gamma)) 
print ('v = '+ str(v), '[*c]')
print ('v_abs = '+ str(v * c_0), '[m/s]')
