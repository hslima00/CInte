"""
Created on Fri Oct 28 11:25:48 2022

@author: Resende, Lima
"""
def evaluatecostvariable(individual, CustDist, CustOrd_list):
    total_distance = 0 
    load = 1000 
    
    
    for i in range(0, len(individual)):
        individual[i] = individual[i] + 1
    
    
    #falta ele ir ter de descarregar na última cena (corrigir)
    for i in range(0, len(individual)):
        #doesnt have enough load 
        if(load < CustOrd_list[individual[i]][0]):
            #last location -> central
            total_distance = total_distance + CustDist[0][individual[i-1]]
            load = 1000
            
            #central -> next location
            total_distance = total_distance + CustDist[0][individual[i]]
            load = load - CustOrd_list[individual[i]][0]
            
        
        #last client
        if(i == (len(individual) - 1)):
            #last location -> next location
            total_distance = total_distance + CustDist[individual[i]][individual[i-1]]
            load = load - CustOrd_list[individual[i]][0]
            #next location -> warehouse
            total_distance = total_distance + CustDist[individual[i]][0]
        
        #first client
        if(i == 0):
            #warehouse -> next location
            total_distance = total_distance + CustDist[0][individual[i]]
            load = load - CustOrd_list[individual[i]][0]
        
        #has enough load 
        else: 
            #last location -> next location
            total_distance = total_distance + CustDist[individual[i]][individual[i-1]]
            load = load - CustOrd_list[individual[i]][0]
            
    for i in range(0, len(individual)):
        individual[i] = individual[i] - 1
            
    return total_distance,


def evaluatecostfixed(individual, CustDist, CustOrd_list):
    total_distance = 0 
    load = 1000 
    
    for i in range(0, len(individual)):
        individual[i] = individual[i] + 1
        
    #falta ele ir ter de descarregar na última cena (corrigir)
    for i in range(0, len(individual)):
        #doesnt have enough load 
        if(load < 50):
            #last location -> central
            total_distance = total_distance + CustDist[0][individual[i-1]]
            load = 1000
            
            #central -> next location
            total_distance = total_distance + CustDist[0][individual[i]]
            load = load - 50
            
        
        #last client
        if(i == (len(individual) - 1)):
            #last location -> next location
            total_distance = total_distance + CustDist[individual[i]][individual[i-1]]
            load = load - 50
            #next location -> warehouse
            total_distance = total_distance + CustDist[individual[i]][0]
        
        #first client
        if(i == 0):
            #warehouse -> next location
            total_distance = total_distance + CustDist[0][individual[i]]
            load = load - 50
        
        #has enough load 
        else: 
            #last location -> next location
            total_distance = total_distance + CustDist[individual[i]][individual[i-1]]
            load = load - 50
            
    for i in range(0 ,len(individual)):
        individual[i] = individual[i] - 1
            
    return total_distance, 



#get the route with the goings to the warehouse 
def get_route(indiv, Orders, Number_Customers):
    
    route = [0]
    cargo = 1000

    try:
        for i in range(Number_Customers):
            indiv[i] = indiv[i]
            if cargo > Orders[indiv[i]][0]:
                route.append(indiv[i])
                cargo = cargo - Orders[indiv[i]][0]
            else:
                route.append(0)
                route.append(indiv[i])
                cargo = 1000  
    except:
            Orders = 50
            for i in range(Number_Customers):
                indiv[i] = indiv[i]

                if cargo > Orders:
                    route.append(indiv[i])
                    cargo = cargo - Orders
                else:
                    route.append(0)
                    route.append(indiv[i])
                    cargo = 1000


    
    route.append(0)
    
    return route 

import matplotlib.pyplot as plt

def plot_best_route_on_grid(best_ind_plot, CustPos_list, dist, nr_customers): # receives the best individual and plots it on the grid
# plot the best route on the grid
    final_sol = best_ind_plot
    
    plt.figure(figsize=(10,10)) 

    # scatter plot of the customers and the warehouse until nr_customers+1
    plt.scatter([CustPos_list[i][0] for i in range(nr_customers+1)], 
                [CustPos_list[i][1] for i in range(nr_customers+1)], 
                color='g', s=50, marker='o', label='Customers')
    # plt.scatter([x[0] for x in CustPos_list until nr_customers], 
    #             [x[1] for x in CustPos_list until nr_customers], 
    #             s=50, c='g') # adds a green dot at costumers locations
    # add number to each costumer
    for i in range(nr_customers+1):
        plt.text(CustPos_list[i][0], CustPos_list[i][1], str(i), fontsize=15)
    
    plt.scatter(CustPos_list[0][0], CustPos_list[0][1], s=10, c='r')
    plt.scatter(CustPos_list[0][0], CustPos_list[0][1], s=10, c='w')
    plt.text(CustPos_list[0][0], CustPos_list[0][1], 'WH', fontsize=10)
    plt.grid()
    for p in range(len(final_sol) - 1):
        i = final_sol[p]
        j = final_sol[p+1]
        # if next customer is the warehouse change color to red
        if j == 0:
            color = 'red'
        else:
            color = 'black'       
        plt.arrow(CustPos_list[i][0], 
                CustPos_list[i][1],
                CustPos_list[j][0] - CustPos_list[i][0], 
                CustPos_list[j][1] - CustPos_list[i][1], 
                color=color)
    plt.title('Best route, distance: ' + str(dist)+ 'km')
    plt.show()

# inverse mutation for TSP
def invmutTSP(individual):
    import random
    # Choose two cities along the list at random and invert the segment between those cities.

    # Choose two cities along the list at random
    city1 = random.randint(0, len(individual) - 1)
    city2 = random.randint(0, len(individual) - 1)

    # Invert the segment between those cities
    if city1 < city2:
        individual[city1:city2] = individual[city1:city2][::-1]
    elif city1 > city2:
        individual[city2:city1] = individual[city2:city1][::-1]
    return individual,


def convergence_plot(c_10_1, c_10_2, c_10_3, c_10_4, c_30_1, c_30_2, c_30_3, c_30_4, c_50_1, c_50_2, c_50_3, c_50_4):
    import numpy as np
    # generate 3 graphs
    # one graph per number of customers

    # superimpose the graphs
    # one graph per number of customers

    # generate x axis 
    x = np.arange(0, 100, 1)
    # subplots for each number of customers
    fig, (c_10, c_30, c_50) = plt.subplots(1, 3, figsize=(15, 5))

    # plot the graphs
    c_10.plot(x, c_10_1, label='Central, Variable Orders')
    c_10.plot(x, c_10_2, label='Central, Fixed Orders')
    c_10.plot(x, c_10_3, label='Corner, Variable Orders')
    c_10.plot(x, c_10_4, label='Corner, Fixed Orders')
    c_10.set_title('10 customers')
    c_10.set_xlabel('Generation')
    c_10.set_ylabel('Distance')
    c_10.legend()

    c_30.plot(x, c_30_1, label='Central, Variable Orders')
    c_30.plot(x, c_30_2, label='Central, Fixed Orders')
    c_30.plot(x, c_30_3, label='Corner, Variable Orders')
    c_30.plot(x, c_30_4, label='Corner, Fixed Orders')
    c_30.set_title('30 customers')
    c_30.set_xlabel('Generation')
    c_30.set_ylabel('Distance')
    c_30.legend()

    c_50.plot(x, c_50_1, label='Central, Variable Orders')
    c_50.plot(x, c_50_2, label='Central, Fixed Orders')
    c_50.plot(x, c_50_3, label='Corner, Variable Orders')
    c_50.plot(x, c_50_4, label='Corner, Fixed Orders')
    c_50.set_title('50 customers')
    c_50.set_xlabel('Generation')
    c_50.set_ylabel('Distance')
    c_50.legend()

    plt.show()
    





