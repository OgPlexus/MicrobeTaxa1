#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from scipy.linalg import hadamard
import matplotlib.ticker as ticker
import numpy as np
import itertools
import random as rnd


for amount in range(120,450):

    rnd.seed(amount)

    size = 2 ** 10

    H = hadamard(size) 
    v = np.array([[0.5,0],[0,-1]])   
    V = v

    BS = [''.join(seq) for seq in itertools.product("01", repeat=10)]
    # BS[100].count('1') # Order

    for i in range(9):        
        V = np.kron(V,v)

    M = np.matmul(V,H) 

    Ws = [rnd.random() for i in range(size)]
    WsA = np.asarray(Ws)
    WsA_T = WsA.transpose()

    A = np.matmul(M,WsA_T)
    # B = (1/size)*A
    B = A.tolist()

    order0 = []
    order1 = []
    order2 = []
    order3 = []
    order4 = []
    order5 = []
    order6 = []
    order7 = []
    order8 = []
    order9 = []
    order10 = []

    for i in range(size):    
        if BS[i].count('1') == 0:
            order0.append(B[i])   
        if BS[i].count('1') == 1:
            order1.append(B[i])       
        if BS[i].count('1') == 2:
            order2.append(B[i])
        if BS[i].count('1') == 3:
            order3.append(B[i])
        if BS[i].count('1') == 4:
            order4.append(B[i])
        if BS[i].count('1') == 5:
            order5.append(B[i])
        if BS[i].count('1') == 6:
            order6.append(B[i])        
        if BS[i].count('1') == 7:
            order7.append(B[i])        
        if BS[i].count('1') == 8:
            order8.append(B[i])    
        if BS[i].count('1') == 9:
            order9.append(B[i])       
        if BS[i].count('1') == 10:
            order10.append(B[i])

    By_Order = []

    abs0 = list(map(abs, order0))
    avg0 = float(sum(abs0))/len(abs0)
    By_Order.append(avg0)

    abs1 = list(map(abs, order1))
    avg1 = float(sum(abs1))/len(abs1)
    By_Order.append(avg1)

    abs2 = list(map(abs, order2))
    avg2 = float(sum(abs2))/len(abs2)
    By_Order.append(avg2)

    abs3 = list(map(abs, order3))
    avg3 = float(sum(abs3))/len(abs3)
    By_Order.append(avg3)

    abs4 = list(map(abs, order4))
    avg4 = float(sum(abs4))/len(abs4)
    By_Order.append(avg4)

    abs5 = list(map(abs, order5))
    avg5 = float(sum(abs5))/len(abs5)
    By_Order.append(avg5)

    abs6 = list(map(abs, order6))
    avg6 = float(sum(abs6))/len(abs6)
    By_Order.append(avg6)

    abs7 = list(map(abs, order7))
    avg7 = float(sum(abs7))/len(abs7)
    By_Order.append(avg7)

    abs8 = list(map(abs, order8))
    avg8 = float(sum(abs8))/len(abs8)
    By_Order.append(avg8)

    abs9 = list(map(abs, order9))
    avg9 = float(sum(abs9))/len(abs9)
    By_Order.append(avg9)

    abs10 = list(map(abs, order10))
    avg10 = float(sum(abs10))/len(abs10)
    By_Order.append(avg10)

    By_Order1 = [round(x,5) for x in By_Order]
    By_Order1
    Div = sum(By_Order1)
    newList = [x / Div for x in By_Order1]
    By_Order5 = [round(x,3) for x in newList]
    print(By_Order5)
    


# In[ ]:


# Other

H = hadamard(1024)                  # Hadamard matrix of the appropriate size
v = np.array([[0.5,0],[0,-1]])      # this initializes the diagonal matrix V
V = v

for i in range(9):        #input should be n-1 where n = "word size / string length"
    V = np.kron(V,v)
    
M = np.matmul(V,H)        # here we multiply the diagonal matrix V with H
E = []

for j in range(len(W)):
    E.append([])
    for i in range(len(year)):
        E[j].append(np.array(M.dot(W[j][i])))

        
# ('bits' has length 2^(word length))
# W[j][i] has the fitness values

