# coding:utf-8

import numpy as np

def run():
    '''テキトゥー'''
    for r in make_rand_seed():
        print(r)


def make_rand_seed():
    for i in range(10):
        yield np.random.rand(3)


if __name__ == '__main__':
    run()
