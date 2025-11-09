# parametric

I estimated the parameters theta, M and X of a nonlinear parametric curve using nonlinear least-squares optimization. 
The files included are the optimization python program and the L1 computation.

The optimization steps are:
1. load the data from the xy_data.csv
2. Define the model (using the equations)
3. Residual vectors initialized
4. use the scipy tool for the least squares funtion
5. theta, M and X are estimated

Value of unknown variables:
theta     = 29.99997300468593
M           = 0.029999997170792186
X           = 54.99999835240804

\[
\left(
t\cos(0.5235983044411857)
- e^{0.029999997170792186\lvert t\rvert}\,\sin(0.3t)\sin(0.5235983044411857)
+ 54.99999835240804,\;
42 + t\sin(0.5235983044411857)
+ e^{0.029999997170792186\lvert t\rvert}\,\sin(0.3t)\cos(0.5235983044411857)
\right)
\]


How to use:
  python optimization.py
  python L1.py


  
