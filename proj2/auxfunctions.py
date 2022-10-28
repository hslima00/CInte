"""
Created on Fri Oct 28 11:25:48 2022

@author: Resende
"""

def evaluatecostvariable(individual, CustDist, CustOrd_list):
    total_distance = 0 
    load = 1000 
    
    #falta ele ir ter de descarregar na última cena (corrigir)
    for i in range(len(individual)):
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
            
    return total_distance,


def evaluatecostfixed(individual, CustDist, CustOrd_list):
    total_distance = 0 
    load = 1000 
    
    #falta ele ir ter de descarregar na última cena (corrigir)
    for i in range(len(individual)):
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
            
    return total_distance,

