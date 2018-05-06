from CoolProp.Plots import PropertyPlot, SimpleCompressionCycle, SimpleCycles
import CoolProp
import CoolProp.CoolProp as CP
import math

print("CoolProp version:", CP.get_global_param_string("version"))

# P1 = 0.25*10**6
# P2 = 1 * 10**6
# T1 = 250
# gas = 'Air'
#
# h1 = CP.PropsSI('H', 'P',P1, 'T', T1, gas)
# print("h1 = ", h1)
#
# h2 = CP.PropsSI('H', 'P',P2, 'T', T1, gas)
# print("h2 = ", h2)
#
# plot = PropertyPlot('Air', 'TS', unit_system='SI', tp_limits='ACHP')
# plot.calc_isolines(CoolProp.iP, iso_range=[P1,P2], num=5, rounding=True)
# plot.calc_isolines(CoolProp.iHmass, iso_range=[h1,h2], num = 5 )
# plot.show()

print(math.log(15/4,math.e))

h3 = 184590
p = 1 * 10**6
print(CP.PropsSI('T','H',h3,'P',p,'Nitrogen'))
print(CP.PropsSI('GAS_CONSTANT', 'Nitrogen'))


# plot = PropertyPlot('Air', 'TS', unit_system='SI', tp_limits='ACHP')
# plot.set_axis_limits()

import numpy as np
import matplotlib.pyplot as plt
# x=np.arange(-10,10.01,0.01) #Массив значений аргумента
x1 = [1,2,3,4,5,6]
y1 = [1,4,9,16,25,36]
#
# x = np.add(x1,x1)
#
# plt.plot(x1,y1) #Построение графика
# plt.xlabel(r'$x$') #Метка по оси x в формате TeX
# plt.ylabel(r'$f(x)$') #Метка по оси y в формате TeX
# plt.title(r'$y=x^2$') #Заголовок в формате TeX
# plt.grid(True) #Сетка
# plt.show() #Показать график

plt.su
plt.plot(x1, y1)
plt.twinx()
plt.show()

x = [x for x in range(100,210,10)]
print(x)

