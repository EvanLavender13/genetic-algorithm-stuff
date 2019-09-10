from genetic_algorithm import GeneticAlgorithm
from operators import init_individual, selection, crossover, mutation


class Test(GeneticAlgorithm):
    POPULATION_SIZE = 300
    CX_PB = 0.15
    MUT_PB = 0.05

    def init_individual(self):
        return init_individual.binary_list(10)

    def evaluate(self, individual):
        return sum(individual)

    def select(self, population):
        return selection.roulette(population)

    def cross(self, ind1, ind2):
        return crossover.single_point(ind1, ind2)

    def mutate(self, child):
        return mutation.uniform_binary(child, prob=0.05)


if __name__ == "__main__":
    Test.run(num_generations=100)
