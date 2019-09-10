from genetic_algorithm import GeneticAlgorithm
from operators import individual, selection, crossover, mutation


class Test(GeneticAlgorithm):
    POPULATION_SIZE = 300
    CX_PB = 0.15
    MUT_PB = 0.05

    def init_individual(self):
        return individual.binary_list(10)

    def evaluate(self, ind):
        return sum(ind)

    def select(self, pop):
        return selection.roulette(pop)

    def cross(self, ind1, ind2):
        return crossover.single_point(ind1, ind2)

    def mutate(self, child):
        return mutation.uniform_binary(child, prob=0.05)


if __name__ == "__main__":
    Test.run(num_gens=100)
