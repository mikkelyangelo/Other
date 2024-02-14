

from io import IOBase
from typing import List, Set, Union, Tuple

import numpy as np

class Matrix(object):
    def __init__(self, mtx: List[List[int]]):
        self._mtx: List[List[int]] = mtx
        self._n: int = len(mtx)

        self._degrees: List = [None] * self._n 
        self._cross_list: List[Set[int]] = [set()] * self._n

        max = self._mtx[0][0]

        for i, row in enumerate(self._mtx):
            for j, x in enumerate(row):
                if x > 0:
                    self._cross_list[i].add(j)
                    self._cross_list[j].add(i)
                if x > max:
                    max = x
                    self._max_idx = [i, j]
            self._degrees[i] = sum(row)

    @property
    def n(self) -> int: return self._n

    @property
    def mtx(self) -> List[List[int]]: return self._mtx

    @property
    def cross_list(self) -> List[Set[int]]: return self._cross_list
 
    @property
    def degrees(self) -> List[int]: return self._degrees

    def crosses(self, x: int) -> Set[int]: return self._cross_list[x]

    def swap_cols(self, x: int, y: int) -> None:
        for i in range(self.n):
            self._mtx[i][x], self._mtx[i][y] = self._mtx[i][y], self._mtx[i][x]

    def swap_rows(self, x: int, y: int) -> None:
        self._mtx[x], self._mtx[y] = self._mtx[y], self._mtx[x]

    def swap_nodes(self, x: int, y: int) -> None:
        self.swap_cols(x, y)
        self.swap_rows(x, y)

class StreamMatrix(Matrix):
    def __init__(self, stream: IOBase):
        mtx = []
        while stream.readable():
            line = stream.readline()
            if line is None or line == '':
                break
            row = list(map(int, line.replace(' ', '').split(',')))
            mtx.append(row)
    
        super().__init__(mtx=mtx)
