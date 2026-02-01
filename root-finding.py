# To comment in nvim - press esc to go in normal mode, then 
# type gcc, then either press v or shift v, and select by using arrows, then press gc. go comment

# To do it for entire file press ggVG and then gc 

# Credit to https://lemesurierb.people.charleston.edu/introduction-to-numerical-methods-and-analysis-python.pdf
# #
# # We want to solve for x in x = cos x;
# # So we solve for x in f(x) = 0 by letting f(x):= x - cos x
# # Recall that |cos x| <= 1, the only way x - cos x can be 0 is when x is also less or equal 1, outside that they are dominated by x.
#
# import numpy as np 
# import matplotlib.pyplot as plt 
#
# def f(x):
#     return x - np.cos(x) 
#
# a = -1; b = 1
#
# x = np.linspace(a, b)
# plt.figure(figsize=(12, 6))
# plt.plot(x, f(x))
# plt.plot([a,b], [0,0], 'g')
# plt.grid(True)
# plt.show() # this command is necessary if you run it on terminal to retrive the rendered image in memory to be shown on the screen. This also triggers the display backend like Qt, X11 etc. while also starting an infinite loop
#
# Analysis this shows that you can find the solution in some interval between 0.5 and 0.75, so we now let a = 0.5 and b = 0.75 and repeat the same thing as above, and then we repeat again until we are satisfied with the value of x. But this is extremely slow, waste of useful time, monetary and computer resources (such as evaluating f(x) for all points created by linspace) except when one is actually learning. Thus, a better way is to use bisection method and identifying three points of interest repeatedly, a, b and their midpoints
#
#
#
# # a = -1; b = 1; c = (a + b) / 2 
# #
# # acb = [a, c, b]
# plt.figure(figsize=(12, 6))
# plt.plot(acb, f(acb), 'b*')
# # x = np.linspace(a, b)
# plt.plot(x, f(x), 'b-.')
# # plt.plot([a, b], [0,0], 'g')
# # plt.grid(True)
# plt.show()
#
# # a = c 
# # b = b 
# c = (a + b) / 2 
# # print(f"{a=}, {b=}, {c=}")
# # acb = [a, c, b]
# # x = np.linspace(a, b)
# # plt.figure(figsize=(12,6))
# plt.plot(acb, f(acb), 'b*', x, f(x), 'b-.')
# # plt.plot([a,b], [0,0], 'g')
# plt.grid(True);
# # plt.show()
# #
# # a = c 
# # b = b 
# # c = (a + b ) / 2
# # print(f"{a=}, {b=}, {c=}")
# # acb = [a, c, b]
# # x = np.linspace(a, b)
# # plt.figure(figsize=(12, 6))
# # # plt.plot(acb, f(acb), 'b*', x, f(x), 'b-.')
# plt.plot([a,b], [0,0], 'g')
# plt.grid(True);
# # plt.show()
# #
# a = a 
# # b = c 
# # # c = (a + b) / 2
# # print(f"{a=},{b=},{c=}")
# # acb = [a, c, b]
# # # x = np.linspace(a, b)
# # plt.figure(figsize=(12,6))
# plt.plot(acb, f(acb), 'b*', x, f(x), 'b-.')
# # plt.plot([a, b], [0,0], 'g')
# # # plt.grid(True)
# # plt.show()
