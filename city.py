# -*- coding: utf-8 -*-
import math


class City(object):
    city_name_list = []
    city_cord_list = []
    city_table = {}

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        # check if city has been seen
        try:
            City.city_name_list[name]
        # add city name & cords if not
        except:
            City.city_name_list.append(name)
            City.city_cord_list.append((x, y))

    def __str__(self):
        return 'name:{} x:{} y:{}'.format(str(self.name), str(self.x), str(self.y))

    def __repr__(self):
        return 'city object:\n' + self.__str__()

    @classmethod
    def make_table(cls):
        for n1, (x1, y1) in zip(cls.city_name_list, cls.city_cord_list):
            cls.city_table[n1] = {}
            for n2, (x2, y2) in zip(cls.city_name_list, cls.city_cord_list):
                cls.city_table[n1][n2] = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                #print('n1 {}, n2 {} -> {}'.format(n1, n2, cls.city_table[n1][n2]))

    @classmethod
    def distance(cls, n1, n2):
        return cls.city_table[n1][n2]
