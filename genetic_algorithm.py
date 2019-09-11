import tools


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
    def run(cls, num_generations):
        algorithm = cls()

        return algorithm.execute(num_generations)

    def execute(self, num_generations):
        # initialize
        print("Initializing pop ...")
        initial_population = [self.init_individual() for _ in range(self.POPULATION_SIZE)]

        print(initial_population)

        # for i in population:
        #     print(i, type(i))

        population = initial_population

        metrics = {}

        for gen in range(num_generations):
            # evaluate
            # print("Evaluating pop")
            evaluated_pop = list(zip(map(self.evaluate, population), population))

            mean = tools.mean(evaluated_pop)
            best = tools.best(evaluated_pop)

            metrics[gen] = {
                "mean": mean,
                "best": best
            }

            # select, cross, mutate
            # need to tighten this up; some looping seems unnecessary
            selected = self.select(evaluated_pop)
            offspring = [self.cross(ind1, ind2) if tools.prob() < self.CX_PB else ind1 for ind1, ind2 in selected]
            mutants = [self.mutate(child) if tools.prob() < self.MUT_PB else child for child in offspring]

            population[:] = mutants

        return population, metrics
