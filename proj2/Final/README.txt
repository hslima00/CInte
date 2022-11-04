The configuration file "configsP1.py" is used to set the parameters of the simulation. 

The parameters are described in the following table:

+-----------------------+---------------------------------------------------------------------------------+
|        Variable       |                                      Usage                                      |
+-----------------------+---------------------------------------------------------------------------------+
| Number_of_Evaluations |                                                                                 |
+-----------------------+                                                                                 |
|    Number_Customers   |          Sets the number of Evaluations, Customers and Population Size          |
+-----------------------+                                                                                 |
|    Population_Size    |                                                                                 |
+-----------------------+---------------------------------------------------------------------------------+
|   Warehouse_location  | Set this value to "Central" or "Corner" if you want the WH to be                |
|                       | on the center [50,50] or in the corner [0,0].                                   |
+-----------------------+---------------------------------------------------------------------------------+
|      deliver_type     | "variable"- variable uses the matrix with number of orders from each customer   |
|                       | "fixed" - the order has a fixed size of 50                                      |
+-----------------------+---------------------------------------------------------------------------------+
|      CXPB , MUTPB     | Probabilities of crossover and mutation                                         |
+-----------------------+---------------------------------------------------------------------------------+
|       heuristic       | Set this variable to:                                                           |
|                       | 0 - if you DON'T want the heuristic individual to be inserted in the initial    |
|                       |     population                                                                  |
|                       | 1 - if you want to insert the heuristic individual to be inserted in the        |
|                       |     initial population                                                          |
+-----------------------+---------------------------------------------------------------------------------+
|        verbose        | Set this variable to:                                                           |
|                       | True - if you want the program to create the Convergence Curve and other prints |
|                       | False - to a reduce version of prints                                           |
+-----------------------+---------------------------------------------------------------------------------+
|      n_iterations     | Number of iterations                                                            |
+-----------------------+---------------------------------------------------------------------------------+
