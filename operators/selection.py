from operator import itemgetter

import numpy as np


def roulette(population):
    sorted_pop = sorted(population, key=itemgetter(0))
    population_size = len(sorted_pop)
    total = sum(fit for fit, _ in sorted_pop)
    probs = [fit / total for fit, _ in sorted_pop]

    def select_generator():
        count = 0
        while count < population_size:
            count += 1
            yield (sorted_pop[np.random.choice(population_size, p=probs)][1],
                   sorted_pop[np.random.choice(population_size, p=probs)][1])

    return select_generator()
