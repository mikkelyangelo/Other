import sympy
from math import exp
import matplotlib.pyplot as plt
import numpy as np


m = [
[-17,   0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[9,	-14,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[8,	0,	-17,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	6,	0,	-11,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	8,	9,	0,	-14,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	8,	0,	0,	-17,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	3,	0,	0,	-11,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	8,	6,	0,	0,	-11,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	8,	9,	0,	0,	-11,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	3,	0,	0,	-11,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	8,	3,	0,	0,	-11,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	8,	3,	0,	0,	-11,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	8,	3,	0,	-11,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	8,	3,	0,	-11,	0,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	8,	3,	-11,	0,	0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	8,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	    0,	0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	8,	0,	0,	0,	0,	0,	0,	0,	0,	    0,	0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	3,	0,	0,	0,	0,	0,	0,	0,	0,	    0,	0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	8,	0,	0,	0,	0,	0,	0,	0,	    0,	0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	3,	0,	0,	0,	0,	0,	0,	0,	    0,	0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	8,	0,	0,	0,	0,	0,	0,	0,	    0,	0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	3,	0,	0,	0,	0,	0,	0,	0,	    0],
[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	8,	0,	0,	0,	0,	0,	0,	0, 0     ],
]

SIZE = len(m)
STABLE_SIZE = 15


if __name__ == "__main__":
    # Составляем дифференциальные уравнения
    t = sympy.symbols('t')
    listOfP = sympy.symbols('p1 p2 p3 p4 p5 p6 p7 p8 p9 p10 p11 p12 p13 p14 p15 p16 p17 p18 p19 p20 p21 p22 p23', cls=sympy.Function)
    (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23) = listOfP
    listOfP = list(listOfP)

    eqs = []
    startVals = {}
    for i in range(SIZE):
        leftSide = listOfP[i](t).diff(t)
        rightSide = 0
        for j in range(SIZE):
            rightSide += listOfP[j](t) * m[i][j]
        eqs.append(sympy.Eq(leftSide, rightSide))

        startVals[listOfP[i](0)] = 0
    startVals[listOfP[0](0)] = 1

    listOfP_t = [listOfP[i](t) for i in range(SIZE)]

    # Решаем дифференциальные уравнения
    solutions = sympy.dsolve(eqs, listOfP_t, ics=startVals)

    print("DIFFS:", solutions)

    # solutions = [
    #     sympy.Eq(p1(t), exp(-17*t)),
    #     sympy.Eq(p2(t), 3*exp(-14*t) - 3*exp(-17*t)),
    #     sympy.Eq(p3(t), 8*t*exp(-17*t)),
    #     sympy.Eq(p4(t), 3*exp(-11*t) - 6*exp(-14*t) + 3*exp(-17*t)),
    #     sympy.Eq(p5(t), 24*t*exp(-14*t) - 24*t*exp(-17*t)),
    #     sympy.Eq(p6(t), 32*t**2*exp(-17*t)),
    #     sympy.Eq(p7(t), 9*t*exp(-11*t) - 9*exp(-11*t)/2 + 6*exp(-14*t) - 3*exp(-17*t)/2),
    #     sympy.Eq(p8(t), 24*t*exp(-11*t) - 48*t*exp(-14*t) + 24*t*exp(-17*t)),
    #     sympy.Eq(p9(t), -48*t**2*exp(-17*t) - 64*t*exp(-14*t) + 16*t*exp(-17*t) + 56*exp(-11*t)/3 - 64*exp(-14*t)/3 + 8*exp(-17*t)/3),
    #     sympy.Eq(p10(t), 27*t**2*exp(-11*t)/2 - 27*t*exp(-11*t)/2 + 21*exp(-11*t)/4 - 6*exp(-14*t) + 3*exp(-17*t)/4),
    #     sympy.Eq(p11(t), 72*t**2*exp(-11*t) - 36*t*exp(-11*t) + 48*t*exp(-14*t) - 12*t*exp(-17*t)),
    #     sympy.Eq(p12(t), 96*t**2*exp(-11*t) + 24*t**2*exp(-17*t) + 56*t*exp(-11*t) + 192*t*exp(-14*t) - 32*t*exp(-17*t) - 236*exp(-11*t)/3 + 256*exp(-14*t)/3 - 20*exp(-17*t)/3),
    #     sympy.Eq(p13(t), 108*t**3*exp(-11*t) - 108*t**2*exp(-11*t) + 42*t*exp(-11*t) - 48*t*exp(-14*t) + 6*t*exp(-17*t)),
    #     sympy.Eq(p14(t), 288*t**3*exp(-11*t) - 60*t**2*exp(-11*t) - 12*t**2*exp(-17*t) - 236*t*exp(-11*t) - 320*t*exp(-14*t) + 28*t*exp(-17*t) + 184*exp(-11*t) - 192*exp(-14*t) + 8*exp(-17*t)),
    #     sympy.Eq(p15(t), 432*t**4*exp(-11*t) - 348*t**3*exp(-11*t) - 186*t**2*exp(-11*t) + 6*t**2*exp(-17*t) + 552*t*exp(-11*t) + 448*t*exp(-14*t) - 20*t*exp(-17*t) - 334*exp(-11*t) + 1024*exp(-14*t)/3 - 22*exp(-17*t)/3),
    #     sympy.Eq(p16(t), -256*t**2*exp(-17*t)/17 - 512*t*exp(-17*t)/289 + 512/4913 - 512*exp(-17*t)/4913),
    #     sympy.Eq(p17(t), 384*t**2*exp(-17*t)/17 + 256*t*exp(-14*t)/7 - 1408*t*exp(-17*t)/289 + 832896/2648107 - 448*exp(-11*t)/33 + 2176*exp(-14*t)/147 - 22720*exp(-17*t)/14739),
    #     sympy.Eq(p18(t), -81*t**2*exp(-11*t)/22 + 729*t*exp(-11*t)/242 + 729/158389 - 6165*exp(-11*t)/5324 + 9*exp(-14*t)/7 - 9*exp(-17*t)/68),
    #     sympy.Eq(p19(t), -768*t**2*exp(-11*t)/11 - 192*t**2*exp(-17*t)/17 - 6464*t*exp(-11*t)/121 - 768*t*exp(-14*t)/7 + 3968*t*exp(-17*t)/289 + 95520384/320420947 + 209056*exp(-11*t)/3993 - 8320*exp(-14*t)/147 + 58144*exp(-17*t)/14739),
    #     sympy.Eq(p20(t), -324*t**3*exp(-11*t)/11 + 2592*t**2*exp(-11*t)/121 - 10062*t*exp(-11*t)/1331 + 72*t*exp(-14*t)/7 - 18*t*exp(-17*t)/17 + 3076380/207331201 - 10062*exp(-11*t)/14641 + 36*exp(-14*t)/49 - 18*exp(-17*t)/289),
    #     sympy.Eq(p21(t), -2304*t**3*exp(-11*t)/11 - 1632*t**2*exp(-11*t)/121 + 96*t**2*exp(-17*t)/17 + 225184*t*exp(-11*t)/1331 + 1280*t*exp(-14*t)/7 - 3616*t*exp(-17*t)/289 + 574563456/3524630417 - 1734048*exp(-11*t)/14641 + 6016*exp(-14*t)/49 - 22112*exp(-17*t)/4913),
    #     sympy.Eq(p22(t), -1296*t**4*exp(-11*t)/11 + 6300*t**3*exp(-11*t)/121 + 86418*t**2*exp(-11*t)/1331 - 18*t**2*exp(-17*t)/17 - 2031300*t*exp(-11*t)/14641 - 96*t*exp(-14*t) + 984*t*exp(-17*t)/289 + 21730032/791243563 + 12638982*exp(-11*t)/161051 - 80*exp(-14*t) + 7342*exp(-17*t)/4913),
    #     sympy.Eq(p23(t), -3456*t**4*exp(-11*t)/11 + 16800*t**3*exp(-11*t)/121 + 230448*t**2*exp(-11*t)/1331 - 48*t**2*exp(-17*t)/17 - 5416800*t*exp(-11*t)/14641 - 256*t*exp(-14*t) + 2624*t*exp(-17*t)/289 + 57946752/791243563 + 33703952*exp(-11*t)/161051 - 640*exp(-14*t)/3 + 58736*exp(-17*t)/14739)
    # ]

    # Графики вероятности нахождения в каждом из состояний
    x_values = np.arange(0, 0.3, 0.3e-2)
    for i in range(19):
        y_values = np.zeros(len(x_values))
        for j in range(len(x_values)):
            y_values[j] = solutions[i].subs(t, x_values[j]).rhs
        plt.plot(x_values, y_values)
    plt.legend(range(19))
    plt.show()
    plt.savefig('./res/states_ver.png')

    # График функции надёжности системы
    x_values = np.arange(0, 0.3, 0.3e-2)
    y_values = np.zeros(len(x_values))
    for i in range(STABLE_SIZE):
        for j in range(len(x_values)):
            y_values[j] += solutions[i].subs(t, x_values[j]).rhs
    plt.plot(x_values, y_values)
    plt.show()
    plt.savefig('./res/stable_function.png')

    # Аналитическое выражение функции надежности
    total_solution = sum(solutions[i].rhs for i in range(STABLE_SIZE))
    print("TOTAL:", total_solution)

    # Математическое ожидание времени безотказной работы
    mat = sympy.integrate(total_solution, (t, 0, sympy.oo)).evalf()
    print("MAT:", mat)

