from math import pi
from numpy import arange

R = 6.0
plotnoct_shar = 0.5
plotnoct_sverlo = 9.0
plotnoct_zhidkoct = 4.0
v_itog = (4 * pi * R ** 3) / 3
output = []
for r in arange(0.001, 6.00, 0.001):
    h = (R ** 2 - r ** 2) ** 0.5
    v_sverlo = 2 * pi * r ** 2 * h + 2 * pi * (R - h) ** 2 * (R - (R - h) / 3)
    m_itog = plotnoct_shar * (v_itog - v_sverlo) + plotnoct_sverlo * v_sverlo
    plotnoct_itog = m_itog / v_itog
    if plotnoct_itog <= plotnoct_zhidkoct:
        output.append(r)
print(max(output))