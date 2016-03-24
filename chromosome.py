# -*- coding: utf-8 -*-
import city
from city import City


class Chromosome(object):

    def __init__(self, city_list=[]):
        self.city_list = city_list
        self.city_list_len = len(city_list)
        self.fitness = self.eval_fitness()

    def eval_fitness(self):
        result = City.distance(self.city_list[0].name, self.city_list[-1].name)
        for ind, city1 in enumerate(self.city_list[:-1]):
            city2 = self.city_list[ind + 1]
            result += City.distance(city1.name, city2.name)
        return result

    def is_edge(self, city1, city2):
        ind1 = self.city_list.index(city1)
        ind2 = self.city_list.index(city2)
        if((abs(ind1 - ind2) == 1) or (abs(ind1 - ind2) == self.city_list_len - 1)):
            return True
        return False

    def __str__(self):
        result = ''
        for i in self.city_list:
            result += i.__str__() + '\n'
        return result + 'fitness {}'.format(self.fitness)

    def __repr__(self):
        return 'chromosome object:\n' + self.__str__()

if(__name__ == '__main__'):
    c1 = city.City('teh', 0., 0.)
    c2 = city.City('ker', 10., 0.)
    c3 = city.City('mas', 10., 10.)
    c4 = city.City('mas', 0., 10.)

    my_ch = Chromosome([c1, c2, c3, c4])
    print(my_ch.fitness)
    print(my_ch.is_edge(c1, c2))
    print(my_ch.is_edge(c1, c3))
