import CoolProp.CoolProp as CP
import math
import CoolProp
from CoolProp.Plots import PropertyPlot



T1 = 290
T2 = 140
G2 = 4
p=6 * 10**6
H1 = CP.PropsSI('H','T',T1,'P',p,'He')
print(H1)

H2 = CP.PropsSI('H','T',T2,'P',p,'He')
print('h2=',H2)

h3 = 630300
T3 = CP.PropsSI('T','H',h3,'P',p,'He')
print('T3=',T3)



#ЗАДАЧА 2
print("\n\nZADACHA2")
P1 = 0.25*10**6
P2 = 1 * 10**6
T1 = 250
gas = 'Air'

R_air = CP.PropsSI('GAS_CONSTANT', gas)/CP.PropsSI('M',gas)
print('R_air = ', R_air)

s1 = CP.PropsSI('S', 'P',P1, 'T', T1, gas)
print("s1 = ", s1)

s2 = CP.PropsSI('S', 'P',P2, 'T', T1, gas)
print("s2 = ", s2)

ds = s2-s1
print (ds)

print(R_air*math.log(P1/P2, math.e))

h1 = CP.PropsSI('H', 'P',P1, 'T', T1, gas)
print("h1 = ", h1)

h2 = CP.PropsSI('H', 'P',P2, 'T', T1, gas)
print("h2 = ", h2)



# ЗАДАЧА 3

P1 = 0.2 * 10**6
T_os = 300
T1 = 250
T2 = 180
gas = 'Air'

print("\n\nZADACHA 3") # исправить даление p2 на p1.
s1 = CP.PropsSI('S', 'P',P1, 'T', T1, gas)
print("s1 = ", s1)

s2 = CP.PropsSI('S', 'P',P2, 'T', T2, gas)
print("s2 = ", s2)

h1 = CP.PropsSI('H', 'P',P1, 'T', T1, gas)
print("h1 = ", h1)

h2 = CP.PropsSI('H', 'P',P2, 'T', T2, gas)
print("h2 = ", h2)

D1 = CP.PropsSI('D', 'H',h1, 'S', s1, gas)
print('v1=',1/D1)

h2 = CP.PropsSI('H', 'D',D1, 'T', T2, gas)
print("h2 = ", h2)

s2 = CP.PropsSI('S', 'D',D1, 'T', T2, gas)
print("s2 = ", s2)

# ЗАДАЧА 4
print("\n\nZADACHA 4")

T1 = 200
T2=150
gas1='Oxygen'
gas2='Air'
P1 = 0.5*10**6
G1 = 10
P2 = 1*10**6
G2 = 9
dT = 5

h1 = CP.PropsSI('H', 'P',P1, 'T', T1, gas1)
print("h1 = ", h1)

h2 = CP.PropsSI('H', 'P',P2, 'T', T2, gas2)
print("h2 = ", h2)

Cp1 = CP.PropsSI('CPMASS', 'P',P1, 'T', T1, gas1)
print("Cp1 = ", Cp1)

Cp2 = CP.PropsSI('CPMASS', 'P',P2, 'T', T2, gas2)
print("Cp2 = ", Cp2)

W1 = Cp1*G1
W2 = Cp2*G2
print("W1 = ", W1)
print("W2 = ", W2)

#ЗАДАЧА 5
print('\n\nZADACHA 5')

T1max = 200
T1min = 150
gas = 'Air'
P1 = 2.5*10**6
P2 = 0.2*10**6
k = 1.4


eps = P2/P1
T1 = [150,160,170,180,190,200]
T2 = [72.893,77.753,82.613,88,92.332, 97.191]
h1 = []
h2 = []
for t in T1:
    h1.append( CP.PropsSI('H', 'P',P1, 'T', t, gas) )
print('h1 = ',h1)


for t2 in T2:
    h2.append( CP.PropsSI('H', 'P',P2, 'T', t2, gas) )
print('h2 = ',h2)

T2 = []
for h in h1:
    T2.append(CP.PropsSI('T', 'H',h, 'P', P2, gas))
print('T2 = ', T2)

V1=[]
for h in h1:
    V1.append(1/CP.PropsSI('D', 'H',h, 'P', P1, gas) )
print('v1=',V1)

V2=[]
for h in h1: # не h2 а h1......
    V2.append(1/CP.PropsSI('D', 'H',h, 'P', P2, gas) )
print('v2=',V2)


#Задача 6
print('\n\nZADACHA 6')
T1=200
P1max = 5 * 10**6
P1min = 0.5 * 10**6
gas = 'Air'
eps = 2.5
k = 1.4

T2 = T1*(1/eps)**((k-1)/k)
print(T2)
P1=[]
for i in range(10):
    P1.append(P1min+i*0.5*10**6)

h1 = []
for p in P1:
    h1.append(CP.PropsSI('H', 'P',p, 'T', T1, gas))
print('h1 = ', h1)

P2 = []
for p in P1:
    P2.append(p/2.5)
print('P2=', P2)

h2 =[]
for p in P2:
    h2.append(CP.PropsSI('H', 'P',p, 'T', T2, gas))
print('h2=',h2)



dT = []
for i in range(10):
    dT.append(T1*(1-0.4**((k-1))/k))
print('dT=',dT)

T2=[]
for i in range(10):
    T2.append(CP.PropsSI('T', 'H',h1[i], 'P', P2[i], gas))
print('T2=', T2)

V1=[]
for i in range(10):
    V1.append(1/CP.PropsSI('D', 'H',h1[i], 'P', P1[i], gas) )
print('v1=',V1)

V2=[]
for i in range(10):
    V2.append(1/CP.PropsSI('D', 'H',h1[i], 'P', P2[i], gas) )
print('v2=',V2)

l = []
for i in range(10):
    l.append(P1[i]*V1[i]- P2[i]*V2[i])
print(l)