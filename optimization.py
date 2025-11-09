import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

#data is loaded
data = pd.read_csv("xy_data.csv")
x_obs = data["x"].values
y_obs = data["y"].values
N = len(x_obs)       # Number of data points


# equations
def model(t, theta, M, X):
    x = t * np.cos(theta) - np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.sin(theta) + X
    y = 42 + t * np.sin(theta) + np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.cos(theta)
    return x, y


def residuals(all_params, x_obs, y_obs):
    theta = all_params[0]
    M     = all_params[1]
    X     = all_params[2]
    t     = all_params[3:]       # One t per data point

    x_pred, y_pred = model(t, theta, M, X)

 #vector of errors
    return np.concatenate([x_pred - x_obs, y_pred - y_obs])



# Initial guesses
theta0 = np.deg2rad(25)               # 25° initial guess
M0     = 0.0                          # Good neutral start
X0     = 50.0                         # Center of allowed range
t0     = np.linspace(6, 60, N)        # Spread-out initial guess

initial_guess = np.concatenate([[theta0, M0, X0], t0])


# ================================================================
# 5. BOUNDS FOR ALL VARIABLES
# ================================================================
theta_min = np.deg2rad(0.1)
theta_max = np.deg2rad(50.0)

M_min = -0.05
M_max = +0.05

X_min = 0.0
X_max = 100.0

t_min = 6.0
t_max = 60.0

lower_bounds = np.concatenate([[theta_min, M_min, X_min], np.full(N, t_min)])
upper_bounds = np.concatenate([[theta_max, M_max, X_max], np.full(N, t_max)])


result = least_squares(
    residuals,
    initial_guess,
    bounds=(lower_bounds, upper_bounds),
    args=(x_obs, y_obs),
    verbose=2
)

# Extract estimated parameters
theta_est = result.x[0]
M_est     = result.x[1]
X_est     = result.x[2]
t_est     = result.x[3:]

print("\n================== ESTIMATED PARAMETERS ==================")
print("theta (deg) =", np.rad2deg(theta_est))
print("M           =", M_est)
print("X           =", X_est)
print("===========================================================\n")

# ================================================================
# 7. COMPUTE FITTED CURVE
# ================================================================
x_fit, y_fit = model(t_est, theta_est, M_est, X_est)


# ================================================================
# 8. COMPUTE L1 DISTANCE (Assessment Criterion)
# ================================================================
L1 = np.sum(np.abs(x_fit - x_obs)) + np.sum(np.abs(y_fit - y_obs))
print(f"L1 Distance = {L1:.6f}")

