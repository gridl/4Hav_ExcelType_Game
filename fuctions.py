from random import randint as rnd
from random import shuffle as shf

def make_value_list(size=5):
    # Make empty list
    square = size ** 2
    line = [0] * square
    
    # Make fitted list
    for i in range(len(line)):
        count = i + 1
        line[i] = count
    
    # Make shuffle list
    shf(line)
    
    # Make fitted array
    area = []
    row = []
    
    for i in range(len(line)):
        count = i + 1
        cond = count % size
        row.append(line[i])
        
        if cond == 0:
            area.append(row)
            row = []
    
    return area

def find_values(area, value=10):
    area_new = area.copy()
    
    for irow in range(len(area_new)):
        for icol in range(len(area_new[irow])):
            if area_new[irow][icol] > value:
                area_new[irow][icol] = None
    
    return area_new

area = make_value_list(size=5)
area_new = find_values(area, value=10)
print(area_new)