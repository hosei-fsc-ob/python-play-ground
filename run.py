# coding:utf-8

import numpy as np

def run():
    '''テキトゥー'''
    for r in make_rand_matrix():
        print(r)


def make_rand_matrix():
    for i in range(10):
        yield np.random.rand(3)


if __name__ == '__main__':
    run()
