
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
    # import pg
    import PyGMO as pg 
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

    # calculate hypervolume
    hv = pg.hypervolume(pareto_front)
    print("Hypervolume: ", hv.compute([max(pf_X), max(pf_Y)]))

    
    
    return pareto_front
    
def plot_hyper_volume(x, y, reference_point):
    x = np.array(x)
    y = np.array(y)

    # Zip x and y into a numpy ndarray
    coordinates = np.array(sorted(zip(x, y)))

    # Empty pareto set
    pareto_set = np.full(coordinates.shape, np.inf)

    i = 0
    for point in coordinates:
        if i == 0:
            pareto_set[i] = point
            i += 1
        elif point[1] < pareto_set[:, 1].min():
            pareto_set[i] = point
            i += 1

    # Get rid of unused spaces
    pareto_set = pareto_set[:i + 1, :]

    # Add reference point to the pareto set
    pareto_set[i] = reference_point

    # These points will define the path to be plotted and filled
    x_path_of_points = []
    y_path_of_points = []

    for index, point in enumerate(pareto_set):

        if index < i - 1:
            plt.plot([point[0], point[0]], [point[1], pareto_set[index + 1][1]], marker='o', markersize=4, c='#4270b6',
                     mfc='black', mec='black')
            plt.plot([point[0], pareto_set[index + 1][0]], [pareto_set[index + 1][1], pareto_set[index + 1][1]],
                     marker='o', markersize=4, c='#4270b6', mfc='black', mec='black')

            x_path_of_points += [point[0], point[0], pareto_set[index + 1][0]]
            y_path_of_points += [point[1], pareto_set[index + 1][1], pareto_set[index + 1][1]]

    # Link 1 to Reference Point
    plt.plot([pareto_set[0][0], reference_point[0]], [pareto_set[0][1], reference_point[1]], marker='o', markersize=4,
             c='#4270b6', mfc='black', mec='black')
    # Link 2 to Reference Point
    plt.plot([pareto_set[-1][0], reference_point[0]], [pareto_set[-2][1], reference_point[1]], marker='o', markersize=4,
             c='#4270b6', mfc='black', mec='black')
    # Highlight the Reference Point
    plt.plot(reference_point[0], reference_point[1], 'o', color='red', markersize=8)

    # Fill the area between the Pareto set and Ref y
    plt.fill_betweenx(y_path_of_points, x_path_of_points, max(x_path_of_points) * np.ones(len(x_path_of_points)),
                      color='#dfeaff', alpha=1)

    plt.xlabel(r"$f_{\mathrm{1}}(x)$", fontsize=18)
    plt.ylabel(r"$f_{\mathrm{2}}(x)$", fontsize=18)
    plt.tight_layout()

    plt.show()