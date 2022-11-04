
import matplotlib.pyplot as plt


def MO_evaluatecostvariable(individual, CustDist, CustOrd_list):
    total_distance = 0 
    load = 1000 
    total_cost = 0
    
    for i in range(len(individual)):
        individual[i] = individual[i] + 1
    
    
    #falta ele ir ter de descarregar na última cena (corrigir)
    for i in range(len(individual)):
        #doesnt have enough load 
        if(load < CustOrd_list[individual[i]][0]):
            #last location -> central
            total_distance = total_distance + CustDist[0][individual[i-1]]
            total_cost = total_cost + load * CustDist[0][individual[i-1]]
            load = 1000
            
            #central -> next location
            total_distance = total_distance + CustDist[0][individual[i]]
            total_cost = total_cost + load * CustDist[0][individual[i]]
            load = load - CustOrd_list[individual[i]][0]
            
        
        #last client
        if(i == (len(individual) - 1)):
            #last location -> next location
            total_distance = total_distance + CustDist[individual[i]][individual[i-1]]
            total_cost = total_cost + load * CustDist[individual[i]][individual[i-1]]
            load = load - CustOrd_list[individual[i]][0]
            #next location -> warehouse
            total_distance = total_distance + CustDist[individual[i]][0]
            total_cost = total_cost + load * CustDist[individual[i]][0]
        
        #first client
        if(i == 0):
            #warehouse -> next location
            total_distance = total_distance + CustDist[0][individual[i]]
            total_cost = total_cost + load * CustDist[0][individual[i]]
            load = load - CustOrd_list[individual[i]][0]
        
        #has enough load 
        else: 
            #last location -> next location
            total_distance = total_distance + CustDist[individual[i]][individual[i-1]]
            total_cost = total_cost + load * CustDist[individual[i]][individual[i-1]]
            load = load - CustOrd_list[individual[i]][0]
        
        
    for i in range(len(individual)):
        individual[i] = individual[i] - 1
            
        
    return total_distance, total_cost,


def plot_pareto_frontier(Xs, Ys, maxX=True, maxY=True):
    '''Pareto frontier selection process'''
    sorted_list = sorted([[Xs[i], Ys[i]] for i in range(len(Xs))], reverse=maxX)
    pareto_front = [sorted_list[0]]
    for pair in sorted_list[1:]:
        if maxY:
            if pair[1] >= pareto_front[-1][1]:
                pareto_front.append(pair)
        else:
            if pair[1] <= pareto_front[-1][1]:
                pareto_front.append(pair)
    
    '''Plotting process'''
    plt.scatter(Xs,Ys)
    pf_X = [pair[0] for pair in pareto_front]
    pf_Y = [pair[1] for pair in pareto_front]
    plt.plot(pf_X, pf_Y)
    plt.xlabel("Distance")
    plt.ylabel("Cost") 

    # higlight the minimum cost and minimum distance solutions

    plt.show()
    
    return pareto_front
    
