import bisect
import itertools

import numpy as np


def select_generator(pop, func, *args):
    size = len(pop)
    count = 0

    while count < size:
        count += 1

        yield pop[func(*args)][1], pop[func(*args)][1]


# still want to redo this

# need to rethink this

def roulette(population):
    size = len(population)
    fitnesses = [fitness for fitness, _ in population]
    total = sum(fitnesses)
    roulette_wheel = list(itertools.accumulate(fitnesses))

    count = 0
    while count < size:
        slot1 = np.random.randint(0, total + 1)
        index1 = bisect.bisect_left(roulette_wheel, slot1)
        slot2 = np.random.randint(0, total + 1)
        index2 = bisect.bisect_left(roulette_wheel, slot2)

        count += 1

        yield population[index1][1], population[index2][1]

# redo this

# def roulette(population):
#     sorted_pop = tools.sort(population, reverse=True)
#     total = sum(fit for fit, _ in sorted_pop)
#     probs = [fit / total for fit, _ in sorted_pop]
#     size = len(sorted_pop)
#
#     return select_generator(sorted_pop, lambda x, y: np.random.choice(x, p=y), size, probs)
