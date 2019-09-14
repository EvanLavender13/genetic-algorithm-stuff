import tools
from genetic_algorithm import GeneticAlgorithm
from operators import init_individual, selection, crossover, mutation


class TravelingSalesman(GeneticAlgorithm):
    POPULATION_SIZE = 100
    CX_PB = 0.25
    MUT_PB = 0.10

    def init(self):
        # random adjacency matrix
        self.adjacency_matrix = [
            [0, 10, 20, 6, 12, 5, 32, 45, 17, 25],
            [10, 0, 18, 19, 34, 22, 89, 23, 9, 11],
            [20, 18, 0, 22, 9, 18, 7, 44, 10, 65],
            [6, 19, 22, 0, 16, 23, 100, 17, 34, 29],
            [12, 34, 9, 16, 0, 75, 8, 13, 24, 4],
            [5, 22, 18, 23, 75, 0, 8, 18, 28, 38],
            [32, 89, 7, 100, 8, 8, 0, 3, 9, 27],
            [45, 23, 44, 17, 13, 18, 3, 0, 16, 64],
            [17, 9, 10, 34, 24, 28, 9, 16, 0, 25],
            [25, 11, 65, 29, 4, 38, 27, 64, 25, 0]
        ]

    def evaluate(self, individual):
        route = individual
        distance = 0

        for x, y in zip(route[:-1], route[1:]):
            distance += self.adjacency_matrix[x - 1][y - 1]

        distance += self.adjacency_matrix[route[-1] - 1][route[0] - 1]

        return distance

    def init_individual(self):
        return init_individual.integer_permutation(low=1, high=10)

    def select(self, population):
        return selection.roulette(population)

    def cross(self, ind1, ind2):
        return crossover.ordered(ind1, ind2)

    def mutate(self, child):
        return mutation.single_swap(child)


class OneMax(GeneticAlgorithm):
    POPULATION_SIZE = 100
    CX_PB = 1.0
    MUT_PB = 0.5
    IND_SIZE = 25

    def exit(self, population):
        return tools.best(population)[0] == self.IND_SIZE

    def init_individual(self):
        return init_individual.binary_list(size=self.IND_SIZE)

    def evaluate(self, individual):
        return sum(individual)

    def select(self, population):
        return selection.roulette(population)

    def cross(self, ind1, ind2):
        return crossover.single_point(ind1, ind2)

    def mutate(self, child):
        return mutation.uniform_binary(child, prob=(1 / self.IND_SIZE))


if __name__ == "__main__":
    result, metrics = OneMax.run(num_generations=1000)
    # result, metrics = TravelingSalesman.run(num_generations=300)

    print("Number of generations = %s" % max(metrics.keys()))

    # for key, value in metrics.items():
    #     print("gen %s mean = %s, best = %s" % (key, value["mean"], value["best"]))
