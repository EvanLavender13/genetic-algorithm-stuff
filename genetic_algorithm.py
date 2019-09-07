import numpy as np


def prob():
    return np.random.random_sample()


class GeneticAlgorithm:
    POPULATION_SIZE = None
    CX_PB = 1.0
    MUT_PB = 1.0

    def init_individual(self):
        raise NotImplementedError

    def evaluate(self, ind):
        raise NotImplementedError

    def select(self, pop):
        raise NotImplementedError

    def cross(self, ind1, ind2):
        raise NotImplementedError

    def mutate(self, child):
        raise NotImplementedError

    @classmethod
    def run(cls, num_gens):
        algorithm = cls()
        result = algorithm.execute(num_gens)

        print("Final population ...")
        print(sum(sum(result)))

    def execute(self, num_gens):
        # initialize
        print("Initializing pop")
        population = [self.init_individual() for _ in range(self.POPULATION_SIZE)]

        print(sum(sum(population)))

        for gen in range(num_gens):
            # evaluate
            # print("Evaluating pop")
            fitness = map(self.evaluate, population)

            # select
            # print("Selecting parents")
            selected = self.select(zip(fitness, population))

            # cross
            # print("Mating parents")
            offspring = [self.cross(ind1, ind2) if prob() < self.CX_PB else ind1 for ind1, ind2 in selected]

            # mutate
            # print("Mutating children")
            any(self.mutate(child) for child in offspring if prob() < self.MUT_PB)

            population[:] = offspring

        return population
