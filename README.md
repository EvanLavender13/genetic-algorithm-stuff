# genetic-algorithm-stuff
Playing around with genetic algorithms. Partly inspired by the mrjob library. 
Also trying to play around with functional concepts, I think. Mainly for me to 
have fun trying to write as many "pythonic" one-liners as possible!

## A Simple One Max Example
```python
class OneMax(GeneticAlgorithm):
    POPULATION_SIZE = 300
    CX_PB = 0.15
    MUT_PB = 0.05
    IND_SIZE = 10

    def init_individual(self):
        return init_individual.binary_list(size=self.IND_SIZE)

    def evaluate(self, individual):
        return sum(individual[1])

    def select(self, population):
        return selection.roulette(population)

    def cross(self, ind1, ind2):
        return crossover.single_point(ind1, ind2)

    def mutate(self, child):
        return mutation.uniform_binary(child, prob=1 / self.IND_SIZE)


if __name__ == "__main__":
    OneMax.run(num_generations=100)
```

## A Simple Traveling Salesman Problem
##### Not finished
```python
class TravelingSalesman(GeneticAlgorithm):
    POPULATION_SIZE = 10
    CX_PB = 1.0
    MUT_PB = 1.0

    def init_individual(self):
        return init_individual.integer_permutation(low=1, high=10)

    def evaluate(self, individual):
        return 1

    def select(self, population):
        return selection.roulette(population)

    def cross(self, ind1, ind2):
        return crossover.ordered(ind1, ind2)

    def mutate(self, child):
        return mutation.single_swap(child)


if __name__ == "__main__":
    TravelingSalesman.run(num_generations=100)
```