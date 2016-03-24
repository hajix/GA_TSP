# -*- coding: utf-8 -*-
from copy import deepcopy
import chromosome
from city import City
import random
import threading


class GA(threading.Thread):

    def __init__(self, file_path='./data/dj.txt', pop_size=10000, generations=100):
        super(GA, self).__init__()
        # read file and make base city list
        with open(file_path, 'r') as f:
            city_lines = [i.strip() for i in f.readlines() if i[0].isdigit()]
        self.base_city_list = [City(i.split()[0], float(i.split()[1]), float(i.split()[2])) for i in city_lines]
        City.make_table()

        # generate initial population
        self.pop_size = pop_size
        self.pop = []
        #print('-------------------generate pop-------------------')
        for i in range(self.pop_size):
            #print(i * 100.0 / self.pop_size)
            self.pop.append(chromosome.Chromosome(self.generate_city_permutation(self.base_city_list)))

        # keep the best solution
        self.best_tour = deepcopy(chromosome.Chromosome(self.base_city_list))
        self.tsp_size = len(self.best_tour.city_list)
        #print('tsp size {}'.format(self.tsp_size))

        # how many generations?
        self.generations = generations

    def generate_city_permutation(self, city_list):
        tmp = deepcopy(city_list)
        random.shuffle(tmp)
        return tmp

    def tournament_selection(self, tournament_size=4):
        # save best solution
        tmp = sorted(self.pop, key=lambda item: item.fitness)[0]
        if(tmp.fitness < self.best_tour.fitness):
            self.best_tour = deepcopy(tmp)
        #print(self.best_ans)
        # do tournament selection
        selected_pop = []
        for i in range(self.pop_size):
            selected_pop.append(sorted(random.sample(self.pop, tournament_size), key=lambda item: item.fitness)[0])
        # update population
        self.pop = selected_pop

    def crossover(self, p_xover=0.95, p_mu=0.4):
        next_gen = []
        for ind, v1 in enumerate(self.pop[::2]):
            # make permutation from chromosome
            v1 = [int(i.name) - 1 for i in v1.city_list]
            v2 = [int(i.name) - 1 for i in self.pop[2 * ind + 1].city_list]
            # order xover
            if(random.random() < p_xover):
                r1, r2 = self.OX(v1, v2)
            else:
                r1, r2 = v1, v2
            # mutation
            if(random.random() < p_mu):
                s, d = random.randint(1, self.tsp_size - 1), random.randint(1, self.tsp_size - 1)
                r1[s], r1[d] = r1[d], r1[s]
            if(random.random() < p_mu):
                s, d = random.randint(1, self.tsp_size - 1), random.randint(1, self.tsp_size - 1)
                r2[s], r2[d] = r2[d], r2[s]
            # make chromosome from permutation
            child1, child2 = chromosome.Chromosome([self.base_city_list[i] for i in r1]), chromosome.Chromosome([self.base_city_list[i] for i in r2])
            next_gen.append(child1)
            next_gen.append(child2)
        self.pop = next_gen

    def OX(self, v1, v2):
        point = random.randint(1, self.tsp_size - 1)
        result1, result2 = v1[point:], v2[point:]
        for i, j in zip(v1[::-1], v2[::-1]):
            try:
                result1.index(j)
            except:
                result1.insert(0, j)
            try:
                result2.index(i)
            except:
                result2.insert(0, i)
        return result1, result2

    def solver(self):
        print('-------------------solving TSP-------------------')
        for i in range(self.generations):
            self.tournament_selection()
            self.crossover()
            print('progress:{}, best tour length {}'.format((i + 1) * 100.0 / self.generations, self.best_tour.fitness))
        print('\n\nbest solution\n{}'.format(self.best_tour))
        return self.best_tour

    def run(self):
        print('-------------------solving TSP @thread-------------------')
        for i in range(self.generations):
            self.tournament_selection()
            self.crossover()
            print('progress:{}, best tour length {}'.format((i + 1) * 100.0 / self.generations, self.best_tour.fitness))
        print('\n\nbest solution\n{}'.format(self.best_tour))
        return self.best_tour

if(__name__ == '__main__'):
    my_ga = GA()
    my_ga.solver()
