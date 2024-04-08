import numpy as np

from scipy.optimize import curve_fit

import matplotlib.pyplot as plt

import math

import numpy as np

from scipy.optimize import curve_fit

# from matplotlib import pyplot as plt


def linear(x, m, c):
    return (m * x) + c


def quadratic(x, a, b, c):
    return (a * (x**2)) + (b * x) + c


start = 1987
end = 2015
years = []
y = {}

# loc = [{2009: 15300, 2019: 4600},
#        {1990:1230, 2000:2330, 2009:4400, 2010:4400, 2012:5000, 2020:6470},
#        {2009: 5160, 2020: 4480},
#        {1990: 263, 2000:308, 2010: 476, 2019:370}]

for i in range(start, end + 1):
    y[i] = 0


def extrapolate_linear(years, whales):

    y = np.array(whales)
    x = np.array(years)

    curve, = plt.plot(x, y, color='r', label='whales')
    plt.xlabel('years')
    plt.ylabel('whales')
    plt.legend(loc='best')
    plt.show()

    xdata = curve.get_xdata()
    ydata = curve.get_ydata()
    print("X data points for the plot is: ", xdata)
    print("Y data points for the plot is: ", ydata)


#     param, param_cov = curve_fit(linear, x, y)

#     print("Linear function coefficients:")
#     print(param)
#     print("Covariance of coefficients:")
#     print(param_cov)

# # # ans stores the new y-data according to
# # # the coefficients given by curve-fit() function
#     ans = ((param[0]*x)+param[1])

# # # '''Below 4 lines can be un-commented for plotting results
# # # using matplotlib as shown in the first example. '''

#     plt.plot(x, y, 'o', color ='red', label ="data")
#     plt.plot(x, ans, '--', color ='blue', label ="optimized data")
#     plt.legend()
#     plt.show()

# years = [1997,1998,2000,2001,2002,2007,2008,2010,2011,2015,2016,2020,2022]

# whales = [21100,21100,16400,16400,16000,20660,19040,20720,20790,23260,26640,20720,16650]

# 1978/79-1983/84	450	
# 1985/86-1990/91	560	
# 1991/92-2003/04	2300	

# 2008	2500	



def getlinear(p1, p2, x):
    return ((p2[1] - p1[1]) /(p2[0] - p1[0])) * x + (p2[1] - (((p2[1] - p1[1])/(p2[0] - p1[0])) * p2[0]))


for i in range(1987, 1990):
    f = 14800	
    y[i] += f
    
for i in range(1990, 1995):
    f = getlinear([1989, 14800], [1995, 21900], i)
    y[i] += f
    
for i in range(1995, 2002):
    f = getlinear([1995, 21900], [2001, 25800], i)
    y[i] += f
    
for i in range(2002, 2008):
    f = getlinear([2001, 25800], [2007, 21900], i)
    y[i] += f
    
for i in range(2008, 2016):
    f = getlinear([2007, 21900], [2015, 40800], i)
    y[i] += f


for i in range(2005, 2008):
    f = getlinear([2005, 9800], [2007,16000], i)
    y[i] += f
    
for i in range(2008, 2016):
    f = getlinear([2007, 16000], [2015, 2200], i)
    y[i] += f



for i in range(start, end + 1):
    print(i, int(y[i]))
    
    
1987 14800
1988 14800
1989 14800
1990 15983
1991 17166
1992 18350
1993 19533
1994 20716
1995 21900
1996 22550
1997 23200
1998 23850
1999 24500
2000 25150
2001 25800
2002 25150
2003 24500
2004 23850
2005 33000
2006 35450
2007 37900
2008 38537
2009 39175
2010 39812
2011 40450
2012 41087
2013 41725
2014 42362
2015 43000
   
# years = [2009, 2019]

# whales = [15300, 4600]

# extrapolate_linear(years,whales)

# y = np.array(rad)

# # x = np.array(t)
# x = np.array(t2)

# plt.plot(x, y, color='r', label='rotation of disc')
# # plt.plot(x, y, color='b', label='x2')
# plt.xlabel('time')
# plt.ylabel('theta')
# plt.legend(loc='best')
# plt.show()

# param, param_cov = curve_fit(test, x, y)

# print("Linear function coefficients:")
# print(param)
# print("Covariance of coefficients:")
# print(param_cov)

# # ans stores the new y-data according to
# # the coefficients given by curve-fit() function
# ans = ((param[0]*x)+param[1])

# # '''Below 4 lines can be un-commented for plotting results
# # using matplotlib as shown in the first example. '''

# plt.plot(x, y, 'o', color ='red', label ="data")
# plt.plot(x, ans, '--', color ='blue', label ="optimized data")
# plt.legend()
# plt.show()

# param, param_cov = curve_fit(test, x, y)

# print("Quadratic function coefficients:")
# print(param)
# print("Covariance of coefficients:")
# print(param_cov)

# # ans stores the new y-data according to
# # the coefficients given by curve-fit() function
# ans = ((param[0]*(x**2)) + (param[1]*x) + param[2])

# # '''Below 4 lines can be un-commented for plotting results
# # using matplotlib as shown in the first example. '''

# plt.plot(x, y, 'o', color ='red', label ="data")
# plt.plot(x, ans, '--', color ='blue', label ="optimized data")
# plt.legend()
# plt.show()
