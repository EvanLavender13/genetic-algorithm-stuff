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

    def prob(self):
        return np.random.random_sample()

    def execute(self):
        # initialize
        print("Initializing pop")
        population = [self.init_individual() for _ in range(self.POPULATION_SIZE)]

        # evaluate
        print("Evaluating pop")
        fitness = map(self.evaluate, population)

        # select
        print("Selecting parents")
        selected = self.select(zip(fitness, population))

        # cross
        print("Mating parents")
        offspring = [self.cross(ind1, ind2) if self.prob() < self.CX_PB else ind1 for ind1, ind2 in selected]

        # mutate
        print("Mutating children")
        any(self.mutate(child) for child in offspring if self.prob() < self.MUT_PB)

        population[:] = offspring

        print(population)

        return population
