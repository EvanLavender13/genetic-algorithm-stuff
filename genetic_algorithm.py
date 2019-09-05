import numpy as np


class GeneticAlgorithm:
    POPULATION_SIZE = None

    CX_PB = 1.0
    MUT_PB = 1.0

    def init_individual(self):
        raise NotImplementedError

    def evaluate(self, individual):
        raise NotImplementedError

    def select(self, population):
        raise NotImplementedError

    def cross(self, ind1, ind2):
        raise NotImplementedError

    def mutate(self, child):
        raise NotImplementedError

    @classmethod
    def run(cls):
        algorithm = cls()
        algorithm.execute()

    def execute(self):
        # initialize
        population = [self.init_individual() for _ in range(self.POPULATION_SIZE)]

        # evaluate
        fitness = map(self.evaluate, population)

        # select
        selected = self.select(zip(fitness, population))

        # cross
        prob = np.random.random_sample()
        offspring = [self.cross(ind1, ind2) if prob < self.CX_PB else ind1 for ind1, ind2 in selected]

        # mutate
        prob = np.random.random_sample()
        any(self.mutate(child) for child in offspring if prob < self.MUT_PB)

        population[:] = offspring

        print(population)

        return population
