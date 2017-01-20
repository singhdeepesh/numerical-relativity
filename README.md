# numerical-relativity

This python code can be used to find the Christoffel Symbol, Riemann Tesnor, Ricci Tensor and Ricci Scalar for a given metric. 

HOW TO USE : -

1. Install gravipy and sympy modules in python using :- In terminal type, **sudo pip install gravipy** and **sudo pip install sympy**.

2. Define the variables of your metric space. In Sympy, you have to declare symbolic variables explicitly. 
    Example:- For cartesian space, I would define my symbols as _x, y, z = symbols("x, y, z")_. 
    Note that you may need to use back-slashes ('\') to escape any special characters you may be using as a symbol. 
    
3. Declare these symbols as your cooordinate-system variables. 
    Example:- For cartesian space, I would use _C = Coordinates('\chi', [x, y, z])_.

4. Define your metric matrix. 
    Example:- For cartesian space, I would use _Metric = diag(1,1,1)_

5. You are ready to go!! Just cd to the directory where the code is and run the code, the corresponding quantities will be dispayed. In terminal, type **cd /path_to_the_folder_where_code_is_placed** and **python gr.py**
   
6. Additional help can be found in the gravipy tutorial. 
