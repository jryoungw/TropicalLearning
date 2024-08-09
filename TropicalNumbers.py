from abc import ABC, abstractmethod
import numpy as np
from typing import Any, Self

class BaseTropicalClass(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def _checkTN(self):
        pass

    @abstractmethod
    def __add__(self):
        pass

    @abstractmethod
    def __radd__(self):
        pass

    @abstractmethod
    def __mul__(self):
        pass

    @abstractmethod
    def __rmul__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

class TropicalNumber(BaseTropicalClass):
    def __init__(self, arr: Any) -> None:
        super().__init__()
        self.arr = arr

    def _checkTN(self, other: Any) -> None:
        assert isinstance(other, TropicalNumber), \
            "Operation is only supported between two TropicalNumbers." + \
            f"Given data types: TropicalNumber and {type(other)}."
        
    def __add__(self, other: Any) -> Self:
        self._checkTN(other)
        if isinstance(other.arr, np.ndarray) or \
            isinstance(self.arr, np.ndarray):
            return TropicalNumber(np.maximum(self.arr, other.arr))
        else:
            try:
                return TropicalNumber(
                    np.max(np.array(self.arr), np.array(other.arr))
                    )
            except:
                return TropicalNumber(max(self.arr, other.arr))
    
    def __radd__(self, other: Any) -> Self:
        self._checkTN(other)
        return self.__add__(other)
    
    def __mul__(self, other: Any) -> Self:
        self._checkTN(other)
        return TropicalNumber(self.arr + other.arr)
    
    def __rmul__(self, other: Any) -> Self:
        self._checkTN(other)
        return self.__mul__(other)
    
    def __repr__(self):
        return f"{self.arr}"
    
class TropicalTorusNumber(TropicalNumber):
    def __init__(self, arr: Any) -> None:
        super().__init__(arr)

    def __eq__(self, other: Any):
        self._checkTN(other)
        if len(np.unique(self.arr - other.arr))==1:
            return True
        else:
            return False
