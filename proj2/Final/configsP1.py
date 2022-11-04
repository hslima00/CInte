# configuration file for the single objective problem
Number_of_Evaluations = 10000
#options -> 50, 30, 10
Number_Customers = 50
#size of the population
Population_Size = 100

#comment the unwanted option to select the warehouse location
Warehouse_location = "Central"
#Warehouse_location = "Corner"

#comment the unwanted option to select the type of costs in deliveries
deliver_type = 	"variable"
#deliver_type = "fixed"

# CXPB  is the probability with which two individuals are crossed
CXPB = 0.5
# MUTPB is the probability for mutating an individual
MUTPB = 0.5

#insert heuristic - on(1)/off(0) 
heuristic = 0

#change to True if print you want prints 
verbose = True

#define the number of iterations 
n_iterations = 30

