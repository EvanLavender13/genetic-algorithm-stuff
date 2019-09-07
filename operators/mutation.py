import numpy as np

# look into using map/any for this
def uniform(child, prob, func, *args):
    size = len(child)

    for i in range(size):
        if np.random.random_sample() < prob:
            child[i] = func(child[i], *args)


def uniform_binary(child, prob):
    uniform(child, prob, lambda x: 1 - x)


def uniform_integer(child, low, high, prob):
    uniform(child, prob, lambda _: np.random.random_integers(low, high))
