# -*- coding: utf-8 -*-
from GA import GA
import pickle
from chromosome import Chromosome
import matplotlib.pyplot as plt
import numpy as np
import time


def random_restart(tsp_file_path, saving_file_name, pop_size=10000, generations=100):
    pass


def update_plot(chrom):
    # global matplot lib variables
    global plt, fig, ax

    # city positions
    x, y = np.array([c.y for c in chrom.city_list]), np.array([c.x for c in chrom.city_list])
    x -= np.min(x)
    y -= np.min(y)

    # plot
    ax.clear()
    ax.plot(x, y, 'ro')
    ax.fill(x, y, edgecolor='b', fill=False)
    fig.canvas.draw()
    plt.show()


# slove TSP problem while show the evolution
def graphical_mode(tsp_file_path='./data/dj.txt', pop_size=10000, generations=100):
    global plt, fig, ax

    # matplotlib init
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # make ga solver
    my_ga = GA(file_path=tsp_file_path, pop_size=pop_size, generations=generations)
    my_ga.start()
    while my_ga.isAlive():
        update_plot(my_ga.best_tour)
        print('update plot')
    time.sleep(15)

    # saving model
    with open('saving.pkl', 'wr+') as f:
        pickle.dump(my_ga.best_tour, f)

    return my_ga.best_tour


# depict saved models
def depict_model(model_file_path='saving.pkl'):
    with open(model_file_path, 'r') as f:
        bt = pickle.load(f)

    # city positions
    x, y = np.array([c.y for c in bt.city_list]), np.array([c.x for c in bt.city_list])
    x -= np.min(x)
    y -= np.min(y)

    # plot
    plt.figure(1)
    plt.plot(x, y, 'ro')
    plt.fill(x, y, edgecolor='b', fill=False)
    plt.show()

if(__name__ == '__main__'):
    #bt = graphical_mode()
    depict_model('dj38.pkl')
