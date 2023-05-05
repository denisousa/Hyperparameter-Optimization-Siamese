'''
NOTE: Only Works with pip install "numpy<1.24.0"
'''

from skopt import gp_minimize
from skopt.space import Integer
from skopt.utils import use_named_args
import numpy as np
import random 


def run_tool(X, Y):
    return random.randint(1, 10000), random.randint(1, 10000), random.randint(1, 10000)

@use_named_args(dimensions)
def evaluate_tool(**parms):
    recall, precision, f1_score = run_tool(parms['X'], parms['Y'])
    check.append([f1_score, parms['X'], parms['Y']])
    loss = -f1_score

    return loss

def prove_algorithm(check):
    max_score,max_x, max_y = 0,0,0
    for score, x, y in check:
        if score > max_score:
            max_score, max_x, max_y = score, x, y

    print(max_score, max_x, max_y)

check = []
dimensions=[Integer(1, 10000, name='X'), Integer(1, 10000, name='Y')]

# Calls Bayesian Optimization
result = gp_minimize(evaluate_tool, dimensions=dimensions, n_calls=20, random_state=42)

best_X = result.x[0]
best_Y = result.x[1]

print("Melhores hiperparâmetros encontrados:")
print("X: ", best_X)
print("Y: ", best_Y)

prove_algorithm(check)
