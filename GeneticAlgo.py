import operator
import copy
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt

"""
GENETIC ALGORITHM PROCESS:
**Knapsack problem genetic algorithm approach**
Goal :
    - Fill the knapsack with the highest value while being less than the maximum capacity'
    - 
"""


class Genetic:
    def __init__(self, weights: list, profits: list, capacity: int):
        # print(f"Weight len:{len(weights)}, prof len: {len(profits)}")
        assert len(weights) == len(profits), "The there should be just as many weights as there are profits"
        self.capacity = capacity
        self.weights = weights
        self.profits = profits

        self.population = []
        for i in range(100):
            self.population.append(np.random.randint(0, 2, len(profits)).tolist())

        # self.clean_up(self.population)

    def fittness(self, population: list) -> int:
        fitnesses = []
        fitness = sum(fitnesses)
        fits = 0

        for gene in population:
            total_profit = np.dot(gene, self.profits)
            total_weight = np.dot(gene, self.weights)

            # fitnesses.append(total_profit+1 if total_weight < self.capacity else 2)
            # fits += total_profit if total_weight < self.capacity else 0
            if total_weight <= self.capacity:
                fits += total_profit
            else:
                fits += 0
        return fits

    def loop(self, generations: int) -> tuple:
        # Random Selection
        fitnesses = []
        for i in range(generations):
            pop = self.population.copy()  # Keeping the initial pop
            initial_fitnesses = [(idx, self.fittness([individual])) for idx, individual in enumerate(self.population)]
            initial_fitnesses = sorted(initial_fitnesses, key=operator.itemgetter(1), reverse=True)
            most_fit = initial_fitnesses[0][1]
            print(f"Most fit: {most_fit}")
            fitnesses.append(most_fit)
            # print(most_fit)
            # print(fitnesses_)

            selected = random.sample(self.population, k=2)
            first_gene, second_gene = selected
            pop.remove(first_gene)
            pop.remove(second_gene)
            assert len(pop) == (len(self.population) - 2), "Len(pop) not less than len(Self.population)"

            # Crossover
            crossover_pop = self.crossover(selected, 1)

            # Mutation
            mutated_pop = self.mutate(crossover_pop, 1)
            # print(mutated_pop)
            # Put back into population if it increases fitness
            pop.extend(mutated_pop)
            # print(pop)
            assert len(pop) == len(self.population)

            # pop_fitness = self.fittness(pop)
            # initial_fitness = self.fittness(self.population)
            pop_fitnesses = [(idx, self.fittness([individual])) for idx, individual in enumerate(pop)]
            pop_fitnesses = sorted(pop_fitnesses, key=operator.itemgetter(1), reverse=True)
            pop_most_fit = pop_fitnesses[0][1]
            if pop_most_fit >= most_fit:
                self.population = copy.deepcopy(pop)

            # if pop_fitness > initial_fitness:
            #     self.population = pop
            #     fitnesses.append(pop_fitness)
            # self.population = pop
            # fitnesses.append(self.fittness(self.population))
            # else:
            #     self.population = self.population
            #     fitnesses.append(self.fittness(self.population))
            # fitnesses.append(0)
            # pass
            # fitnesses.append(self.fittness(self.population))

            # print(fitnesses)
        # print(sum(fitnesses))
        # print(fitnesses)

        new_pop_fitness = [(self.fittness([individual]), individual) for individual in self.population]
        new_pop_fitness = sorted(new_pop_fitness, key=operator.itemgetter(0), reverse=True)
        print(f"Best Solution: {new_pop_fitness[0]}")

        plt.grid()
        plt.plot(fitnesses)
        plt.xlabel("Generation")
        plt.ylabel("Fitness")
        plt.title('Fitnesses over generations')
        plt.show()
        plt.close()

        return fitnesses  # , self.population

        # Check

    def mutate(self, genes: list, prob: float) -> list:
        """
        A function to perform a mutation on the two genes at a probability of `prop`
        :param genes: genes to be mutated
        :param prob: probability of mutation
        :return: list of genes
        """
        assert len(genes) == 2, "The number of genes should be 2"

        first_gene, sec_gene = genes

        probability = random.random()
        if probability < prob:
            # Generate random index in
            random_index = np.random.randint(0, len(first_gene), 1).item()
            if first_gene[random_index] == 0:
                first_gene[random_index] = 1
            else:
                first_gene[random_index] = 0

            if sec_gene[random_index] == 0:
                sec_gene[random_index] = 1
            else:
                sec_gene[random_index] = 0
        # print("First gene, ", [sec_gene, first_gene])
        return [first_gene, sec_gene]

    def crossover(self, genes: list, probability: int) -> list:

        assert len(genes) == 2, "The number of genes needed should be 2"

        first_gene, sec_gene = genes
        gene_length = len(first_gene)
        prob = np.random.random()
        if prob < probability:
            gene_1 = first_gene[0:gene_length // 2] + sec_gene[gene_length // 2:]
            gene_2 = sec_gene[0:gene_length // 2] + first_gene[gene_length // 2:]
        else:
            gene_1, gene_2 = first_gene, sec_gene
        return [gene_1, gene_2]

    def get_pop(self):
        return self.population

data = [{""}]
if __name__ == "__main__":
    # gen = Genetic([1, 1, 1, 1, 32, 23433, 433324, 21, 4, 2234, 10, 3434, 342, 4, 23, 21],
    #               [1, 1, 1, 12, 4, 323, 232, 2334, 322, 2, 32, 242, 132, 23, 2314, 23], 102)
    gen = Genetic([23, 31, 29, 44, 53, 38, 63, 85, 89, 82], [92, 57, 49, 68, 60, 43, 67, 84, 87, 72], capacity=165)
    # print(f"Gen Pop before loop: {gen.population}")
    # print(gen.population)
    # print(gen.fittness(gen.population))
    # print(random.uniform(0, 1))
    # print(random.random())
    gen.loop(2000)

    # final_pop = [(idx, gen.fittness[individual]) for idx, individual in enumerate(gen.get_pop())]
    # final_pop = sorted(final_pop, key=operator.itemgetter(1), reverse=True)
    # print(final_pop)
    # print(gen.get_pop())

    # print(f"Gen pop after loop: {gen.population}")
