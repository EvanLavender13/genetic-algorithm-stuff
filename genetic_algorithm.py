import tools


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
        for i in result:
            print(i, type(i))

    def execute(self, num_gens):
        # initialize
        print("Initializing pop")
        population = [self.init_individual() for _ in range(self.POPULATION_SIZE)]

        for i in population:
            print(i, type(i))

        for gen in range(num_gens):
            # evaluate
            # print("Evaluating pop")
            fitness = map(self.evaluate, population)

            # select
            # print("Selecting parents")
            selected = self.select(zip(fitness, population))

            # cross
            # print("Mating parents")
            offspring = [self.cross(ind1, ind2) if tools.prob() < self.CX_PB else ind1 for ind1, ind2 in selected]

            # mutate
            # print("Mutating children")
            mutants = [self.mutate(child) if tools.prob() < self.MUT_PB else child for child in offspring]

            population[:] = mutants

        return population
