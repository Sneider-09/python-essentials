from sys import path
import os

path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'packages')
))

import extra.iota
print(extra.iota.funI())

from extra.iota import funI
print(funI())

# Final del árbol
import extra.good.best.sigma
from extra.good.best.tau import funT
 
print(extra.good.best.sigma.funS())
print(funT())

# Usando un alias
import extra.good.best.sigma as sig
import extra.good.alpha as alp
 
print(sig.funS())
print(alp.funA())

