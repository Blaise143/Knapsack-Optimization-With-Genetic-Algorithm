import operator
import copy
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt

from problems import *


class Genetic:
    def __init__(self, weights: list, profits: list, capacity: int) -> None:
        self.best_value = None
        self.best_combination = None
        assert len(weights) == len(profits), "The there should be just as many weights as there are profits"
        self.capacity = capacity
        self.weights = weights
        self.profits = profits

        self.population = []
        for i in range(100):
            self.population.append(np.random.randint(0, 2, len(profits)).tolist())

    def fittness(self, population: list) -> int:
        fits = 0

        for gene in population:
            total_profit = np.dot(gene, self.profits)
            total_weight = np.dot(gene, self.weights)

            if total_weight <= self.capacity:
                fits += total_profit
            else:
                fits += 0
        return fits

    def loop(self, generations: int) -> list:
        # Random Selection
        fitnesses = []
        for i in range(generations):
            pop = self.population.copy()  # Keeping the initial pop
            initial_fitnesses = [(idx, self.fittness([individual])) for idx, individual in enumerate(self.population)]
            initial_fitnesses = sorted(initial_fitnesses, key=operator.itemgetter(1), reverse=True)
            most_fit = initial_fitnesses[0][1]
            fitnesses.append(most_fit)

            selected = random.sample(self.population, k=2)
            first_gene, second_gene = selected
            pop.remove(first_gene)
            pop.remove(second_gene)
            assert len(pop) == (len(self.population) - 2), "Len(pop) not less than len(Self.population)"

            # Crossover
            crossover_pop = self.crossover(selected, 1)

            # Mutation
            mutated_pop = self.mutate(crossover_pop, 1)
            # Put back into population if it increases fitness
            pop.extend(mutated_pop)
            assert len(pop) == len(self.population)

            pop_fitnesses = [(idx, self.fittness([individual])) for idx, individual in enumerate(pop)]
            pop_fitnesses = sorted(pop_fitnesses, key=operator.itemgetter(1), reverse=True)
            pop_most_fit = pop_fitnesses[0][1]
            if pop_most_fit >= most_fit:
                self.population = copy.deepcopy(pop)

        new_pop_fitness = [(self.fittness([individual]), individual) for individual in self.population]
        new_pop_fitness = sorted(new_pop_fitness, key=operator.itemgetter(0), reverse=True)
        self.best_combination = new_pop_fitness[0][1]
        self.best_value = np.dot(self.best_combination, self.profits)

        plt.grid()
        plt.plot(fitnesses)
        plt.xlabel("Generation")
        plt.ylabel("Fitness")
        plt.title('Fitnesses over generations')
        plt.show()
        plt.close()

        return fitnesses  # , self.population

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

    @staticmethod
    def crossover(genes: list, probability: float) -> list:

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


if __name__ == "__main__":
    gen = Genetic(p8["weights"], p8["profits"], capacity=p8["capacity"])
    gen.loop(2000)
    print(f"Best Solution: {gen.best_combination}, Best Value: {gen.best_value}")
    print(f"Actual Solution: {p8['optimal']}, Actual best: {p8['best']}")
