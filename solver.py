#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
from operator import attrgetter
Item = namedtuple("Item", ['index', 'value', 'weight', 'density'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    
    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        v,w = int(parts[0]), int(parts[1])
        items.append(Item( i-1,v,w,1.0* v/w ))

    

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full

    n=len(items)
    values = [[0 for j in range (capacity+1)] for i in range(n+1)]
    taken = [0]* len(items)

    for i in range(n + 1):
        if i > 0:
            value = items[i - 1].value
            weight = items[i - 1].weight
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                continue
            elif weight > j:
                values[i][j] = values[i - 1][j]
            else:
                vTake = values[i - 1][j - weight] + value
                vKeep = values[i - 1][j]
                values[i][j] = max(vTake, vKeep)

    totalWeight = capacity
    for i in reversed(range(n)):
        if values[i][totalWeight] == values[i + 1][totalWeight]:
            continue
        else:
            taken[i] = 1
            totalWeight -= items[i].weight    
        
            
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

