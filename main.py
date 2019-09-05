from operator import itemgetter

import numpy as np

from genetic_algorithm import GeneticAlgorithm
from operators import individual


class Test(GeneticAlgorithm):
    POPULATION_SIZE = 10
    CX_PB = 0.50
    MUT_PB = 0.50

    def init_individual(self):
        return individual.binary_list(10)

    def evaluate(self, individual):
        return sum(individual)

    def select(self, population):
        sorted_pop = sorted(population, key=itemgetter(0))
        total = sum(fit for fit, _ in sorted_pop)
        probs = [fit / total for fit, _ in sorted_pop]

        def select_generator():
            count = 0
            while count < self.POPULATION_SIZE:
                count += 1
                yield (sorted_pop[np.random.choice(self.POPULATION_SIZE, p=probs)],
                       sorted_pop[np.random.choice(self.POPULATION_SIZE, p=probs)])

        return select_generator()

    def cross(self, ind1, ind2):
        size = len(ind1[1])
        point = np.random.randint(1, size - 1)

        print("CROSS!")

        return 0, np.concatenate([ind1[1][:point], ind2[1][point:]])

    def mutate(self, child):
        print("MUTATE")


if __name__ == "__main__":
    Test.run()
