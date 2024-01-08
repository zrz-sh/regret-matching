from regretmatching.rps import RPSPlayer
import numpy as np

a = RPSPlayer()
b = RPSPlayer()
t = 100
for i in range(0, t):
    a_move = a.move()
    b_move = b.move()
    a.learn_from(b_move)
    b.learn_from(a_move)

'''
Theorem: If two no-regret algorithms play a zero-sum game against one another 
for T iterations with average regret less than ϵ, then their average strategies 
approximate Nash Equilibrium (up to 2ϵ)
'''
_2e = np.round(2 * np.max([a.eps(), b.eps()]), 3) # 2 * epsilon

a_ne = a.current_best_response()
b_ne = b.current_best_response()
print("{0} - nash equilibrium for RPS: {1}, {2}".format(_2e, a_ne, b_ne))
