import numpy as np
from TropicalNumbers import TropicalNumber
from typing import Union

def _checkShape(a: TropicalNumber,
                b: TropicalNumber) -> None:
    if isinstance(a.arr, np.ndarray) and \
        isinstance(b.arr, np.ndarray):
        assert a.arr.shape == b.arr.shape, \
                f"Shape does not match. Given shape: {a.arr.shape}"\
                + f" and {b.arr.shape}"
    else:
        pass

def TropicalMetric(x: TropicalNumber,
                   y: TropicalNumber) -> float:
    _checkShape(x, y)
    return np.max(x.arr - y.arr) - np.min(x.arr - y.arr)

def TropicalNorm(x: TropicalNumber) -> float:
    _checkShape(x, y)
    return np.max(x) - np.min(x)

def TropicalMinDistance(
                        a: TropicalNumber,
                        b: TropicalNumber,
                        axis: Union[int, list] = 0
                        ) -> float:
    _checkShape(a, b)
    diff = np.sum(b.arr - a.arr, axis=axis)
    n = np.prod(a.arr.shape, axis=axis)
    return diff - n * np.min(b.arr - a.arr, axis=axis)

def TropicalMaxDistance(
                        a: TropicalNumber,
                        b: TropicalNumber,
                        axis: Union[int, list] = 0
                        ) -> float:
    _checkShape(a, b)
    diff = np.sum(b.arr - a.arr, axis=axis)
    n = np.prod(a.arr.shape, axis=axis)
    return n * np.max(b.arr - a.arr, axis=axis) - diff

