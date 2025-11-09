# parametric

I estimated the parameters theta, M and X of a nonlinear parametric curve using nonlinear least-squares optimization. 
The files included are the optimization python program and the L1 computation.

The optimization steps are:
1. load the data from the xy_data.csv
2. Define the model (using the equations)
3. Residual vectors initialized
4. use the scipy tool for the least squares funtion
5. theta, M and X are estimated

How to use:
  python optimization.py
  python L1.py


  
