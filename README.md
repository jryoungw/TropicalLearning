# TropicalLearning

Implementation of [Tropical Gradient Descent](https://arxiv.org/abs/2405.19551).

## Usage

### Tropical Algebra

```
from TropicalNumbers import TropicalNumber
import numpy as np

tn1 = TropicalNumber(1)
tn2 = TropicalNumber(3)

print(tn1 + tn2, tn1 * tn2) # 3, 4
```

### Algebra on Tropical Projective Torus
```
from TropicalNumbers import TropicalNumber, TropicalTorusNumber
import numpy as np

ttn1 = TropicalTorusNumber(np.array([1,2,3]))
ttn2 = TropicalTorusNumber(np.array([2,3,5]))

print(ttn1 == ttn2) # False

ttn1 = TropicalTorusNumber(np.array([1,2,3]))
ttn2 = TropicalTorusNumber(np.array([2,3,4]))

print(ttn1 == ttn2) # True
```
