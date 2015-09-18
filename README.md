# Bat Algorithm in Python

## Objective
The main objective is to create an implementation of bat algorithm in Python programming language.

## Installation

    pip install BatAlgorithm

### Example
The following example presents a simple use of bat algorithm. `Fun()` denotes the objective function that may be changed by the user. Control parameters should be defined within `BatAlgorithm()` constructor. Order of parameters is as
follows: `BatAlgorithm(D, NP, N_Gen, A, r, Qmin, Qmax, Lower, Upper, function)` where:

- `D`  denotes dimension of the problem,
- `NP` denotes population size,
- `N_Gen`  denotes number of generations (iterations),
- `A` parameter denotes loudness,
- `r` parameter denotes pulse rate,
- `Qmin` parameter denotes frequency minimum,
- `Qmax` parameter denotes frequency maximum,
- `Lower` denotes lower bound,
- `Upper` denotes upper bound and
- `function` passes objective function.

## CODE EXAMPLE:

```python
import random
from BatAlgorithm import *

def Fun(D, sol):
    val = 0.0
    for i in range(D):
        val = val + sol[i] * sol[i]
    return val

# For reproducive results
#random.seed(5)

for i in range(10):
    Algorithm = BatAlgorithm(10, 40, 1000, 0.5, 0.5, 0.0, 2.0, -10.0, 10.0, Fun)
    Algorithm.move_bat()
```

## Bugs
Bugs and extension should be send via Github.

## Authors
Iztok Fister Jr. and Marko Burjek

## References

Yang, X.-S. "A new metaheuristic bat-inspired algorithm." Nature inspired cooperative strategies for optimization (NICSO 2010). Springer
Berlin Heidelberg, 2010. 65-74.

Fister, I. Jr., Fister, I., Yang, X.-S., Fong, S., Zhuang, Y. "Bat algorithm: Recent advances." IEEE 15th International Symposium on Computational Intelligence and Informatics (CINTI), IEEE, 2014. 163-167.
