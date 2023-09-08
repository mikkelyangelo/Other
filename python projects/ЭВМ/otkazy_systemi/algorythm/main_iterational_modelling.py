import time

import sympy
from scipy.integrate import odeint
from math import factorial, exp, sqrt
import matplotlib.pyplot as plt
import numpy as np
import random


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


STATES = {
    "S_32_22": 1,
    "S_22_22": 2,
    "S_32_21": 3,
    "S_12_22": 4,
    "S_22_21": 5,
    "S_32_20": 6,
    "S_11_22": 7,
    "S_12_21": 8,
    "S_22_20": 9,
    "S_32_10": 16,
    "S_10_22": 10,
    "S_11_21": 11,
    "S_12_20": 12,
    "S_22_10": 17,
    "S_00_22": 18,
    "S_10_21": 13,
    "S_11_20": 14,
    "S_12_10": 19,
    "S_00_21": 20,
    "S_10_20": 15,
    "S_11_10": 21,
    "S_00_20": 22,
    "S_10_10": 23,
}

if __name__ == "__main__":
    # Имитационное моделирование системы в терминах непрерывных марковских цепей
    random.seed(time.time())
    maxLen = 0
    times = []

    ITERATIONS = 100
    ways = []
    longestWayLen = 0
    latestTime = 0
    for i in range(ITERATIONS):
        LA = 3
        LB = 4
        work_A = 3
        work_B = 2
        reserve_A = 2
        reserve_B = 2
        time_destroy_A = 0.0
        time_destroy_B = 0.0
        cur_time = 0.0
        way = [[1, 0]]
        while work_A >= 1 and work_B >= 2:  # пока в рабочем состоянии
            total_intensity = work_A * LA + work_B * LB

            time_destroy = random.expovariate(total_intensity)
            cur_time += time_destroy

            destroyed = np.random.choice(['A', 'B'], p=[work_A / (work_A + work_B), work_B / (work_A + work_B)])
            if destroyed == 'A':
                work_A -= 1
                if (work_A < 1) and (reserve_A > 0):
                    work_A += 1
                    reserve_A -= 1
            else:
                work_B -= 1
                if (work_B < 2) and (reserve_B > 0):
                    work_B += 1
                    reserve_B -= 1
            way.append([STATES[f"S_{work_A}{reserve_A}_{work_B}{reserve_B}"], cur_time])
        times.append(cur_time)
        ways.append(way)
        longestWayLen = max(longestWayLen, len(way))
        latestTime = max(latestTime, cur_time)
    print(times)
    print(ways)

    # Подготавливаем данные для ступенчатого графика
    x_graph_values = np.arange(0, latestTime, 0.001)
    y_graph_values = []
    for way in ways:
        y = [1]
        lastYVal = 1
        for i in range(len(x_graph_values) - 1):
            for pair in way:
                if x_graph_values[i] < pair[1] < x_graph_values[i+1]:
                    lastYVal = pair[0]
            y.append(lastYVal)
        y_graph_values.append(y)

    # График переходов
    for y in y_graph_values:
        plt.plot(x_graph_values, y)
    plt.show()
    plt.savefig('./res/imitational_modelling.png')

    # Среднее выборочное значение
    mean_time = np.mean(times)
    print("MEAN:", mean_time)

    # Стандартное отклонение времени безотказной работы системы
    std_dev = sqrt(sum((times[i] - mean_time) ** 2 for i in range(ITERATIONS)) / (ITERATIONS - 1))
    print("STD_DEV:", std_dev)

