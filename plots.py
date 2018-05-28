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

# print(CP.PropsSI('S', ))

