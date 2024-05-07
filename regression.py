import matplotlib.pyplot as plt
from scipy import stats
import csv
import numpy as np
from scipy.optimize import curve_fit

# import sys
# import matplotlib
from scipy import odr
# matplotlib.use('Agg')
# from sklearn.metrics import r2_score

oils_year = {}
fileOil = 'Oil spillage dataset - Oil spillage dataset.csv'

BlueWhale_year = {}
fileBlueWhale = 'Blue Whale - Sheet1.csv'

FinWhale_year = {}
fileFinWhale = 'Finwhale - Sheet1.csv'

GrayWhale_year = {}
fileGrayWhale = 'Gray whale - Sheet1.csv'

HumpbackWhale_year = {}
fileHumpbackWhale = 'Humpback Whale - Sheet1.csv'

MinkeWhale_year = {}
fileMinkeWhale = 'Minke whale - Sheet1.csv'

RightWhale_year = {}
fileRightWhale = 'Right whale - Sheet1.csv'

for i in range(1903, 2024):
    oils_year[i] = 0
    # whale_year[i] = 0

# Get oil spill over years
with open(fileOil, newline='') as csvfile:
    reader = csv.reader(csvfile)
    c = 0
    for row in reader:
        if c != 0:
            year = int(row[2].split()[-1][0:4])

            amountSTR = row[4]
            if amountSTR != "unknown" and amountSTR != '':
                s = ""
                for a in amountSTR:
                    if a != ',':
                        s = s + a
                amount = float(s)
                oils_year[year] += amount
        c+=1
        

def whaleLinearRegress(file, whale, name):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        c = 0
        for row in reader:
            if c != 0:
                # print(row)
                year = int(row[0])

                amountSTR = row[1]
                s = ''
                for a in amountSTR:
                    if a != ',':
                        s = s + a
                amount = float(s)
                # print(amount)
                whale[year] = amount
            c+=1
    # print(whale)

    x = []
    y = []

    for i in list(whale.keys()):
        y.append(whale[i])
        x.append(oils_year[i])


    m, c, r, p, std_err = stats.linregress(x, y)

    def linearFunc(x):
      return m * x + c

    mymodel = list(map(linearFunc, x))
    print(name)
    print("r",r)
    print("p",p)
    print("std_err",std_err)
    print("slope", m)
    print("intercept", c)
    plt.scatter(x, y)
    l = 'sq_r = ' + str(r) + '\n p = ' + str(p) + '\n stdErr = ' + str(std_err) + '\n m = ' + str(m) + '\n c = ' + str(c)
    plt.plot(x, mymodel,label=l)
    plt.legend(loc='best')
    plt.title(name)
    plt.show()
    


def whalePolyRegress(file, whale, name):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        c = 0
        for row in reader:
            if c != 0:
                # print(row)
                year = int(row[0])

                amountSTR = row[1]
                s = ''
                for a in amountSTR:
                    if a != ',':
                        s = s + a
                amount = float(s)
                # print(amount)
                whale[year] = amount
            c+=1
    # print(whale)

    x = []
    y = []
    
    year = []

    for i in list(whale.keys()):
        y.append(whale[i])
        x.append(oils_year[i])
        year.append(i)
        
    poly_model = odr.polynomial(3)  # using third order polynomial model
    data = odr.Data(x, y)
    odr_obj = odr.ODR(data, poly_model)
    output = odr_obj.run()  # running ODR fitting
    poly = np.poly1d(output.beta[::-1])
    poly_y = poly(x)
    # plt.plot(x, y, label="input data")
    plt.scatter(x, y)
    plt.plot(x, poly_y, label="polynomial ODR")
    plt.legend()
    plt.show()
        
    # print(y)
    # print(x)
    # mymodel = np.poly1d(np.polyfit(x, y, 3))

    # myline = np.linspace(1903, 2024, 10)

    # plt.scatter(x, y)
    # plt.plot(myline, mymodel(myline))
    # plt.show()
    # plt.savefig(sys.stdout.buffer)
    # sys.stdout.flush()
    # mymodel = np.poly1d(np.polyfit(x, y, 3))

    # myline = np.linspace(min(year), max(year), 10)

    # plt.scatter(x, y)
    # plt.plot(myline, mymodel(myline))
    # plt.show()
        
    # def cubicFunc(x):
    #     return (cubic * x**3) + (quadratic * x**2) + (linear * x) + intercept

    # intercept, linear, quadratic, cubic = np.polyfit(x, y, 3)
    # l = []
    # # mymodel = np.poly1d(np.polyfit(x, y, 3))
    # # mymodel = np.poly1d(l)

    # mymodel = list(map(cubicFunc, x))
    # print(name)
    # # print("r",r)
    # # print("p",p)
    # # print("std_err",std_err)
    # # print("slope", m)
    # # print("intercept", c)
    # plt.scatter(x, y)
    # # l = 'sq_r = ' + str(r) + '\n p = ' + str(p) + '\n stdErr = ' + str(std_err) + '\n m = ' + str(m) + '\n c = ' + str(c)
    # l = 'test'

    # # m, c, r, p, std_err = stats.linregress(x, y)

    # # def quadFunc(x):
    # #   return m * x + c

    # # mymodel = list(map(quadFunc, x))
    # # print(name)
    # # print("r",r)
    # # print("p",p)
    # # print("std_err",std_err)
    # # print("slope", m)
    # # print("intercept", c)
    # # plt.scatter(x, y)
    # # l = 'sq_r = ' + str(r) + '\n p = ' + str(p) + '\n stdErr = ' + str(std_err) + '\n m = ' + str(m) + '\n c = ' + str(c)
    # plt.plot(x, mymodel,label=l)
    # # plt.legend(loc='best')
    # plt.title(name)
    # plt.show()
    # mymodel = np.poly1d(np.polyfit(x, y, 3))

    # myline = np.linspace(min(year), max(year), 10)

    # plt.scatter(x, y)
    # plt.plot(myline, mymodel(myline))
    # plt.legend(loc='best')
    # plt.show()

def whaleLinearRegresstTest(file, whale, name):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        c = 0
        for row in reader:
            if c != 0:
                # print(row)
                year = int(row[0])

                amountSTR = row[1]
                s = ''
                for a in amountSTR:
                    if a != ',':
                        s = s + a
                amount = float(s)
                # print(amount)
                whale[year] = amount
            c+=1
    # print(whale)

    x = []
    y = []

    for i in list(whale.keys()):
        if oils_year[i] > 0:
            y.append(whale[i])
            x.append(oils_year[i])
            # x.append(whale[i])
            # y.append(oils_year[i])
            # x.append(oils_year[i-15])
            # x.append(oils_year[i-10])
            # x.append(oils_year[i-20])
    # X = np.array(x)
    # Y = np.array(y)
    
    # def test(X, a, b, c):
    #     return (a*(X**2)) + (b*X) + c
    
    # param, param_cov = curve_fit(test, X, Y)
    
    
    # print("Quadratic function coefficients:")
    # print(param)
    # print("Covariance of coefficients:")
    # print(param_cov)
    
    # # ans stores the new y-data according to 
    # # the coefficients given by curve-fit() function
    # ans = ((param[0]*(X**2)) + (param[1]*X) + param[2])
    
    # # '''Below 4 lines can be un-commented for plotting results 
    # # using matplotlib as shown in the first example. '''
    
    # plt.plot(X, Y, 'o', color ='red', label ="data")
    # plt.plot(X, ans, '--', color ='blue', label ="optimized data")
    # plt.legend()
    # plt.show()


    m, c, r, p, std_err = stats.linregress(x, y)

    def linearFunc(x):
      return m * x + c

    mymodel = list(map(linearFunc, x))
    print(name)
    print("r",r)
    print("p",p)
    print("std_err",std_err)
    print("slope", m)
    print("intercept", c)
    plt.scatter(x, y)
    l = 'sq_r = ' + str(r) + '\n p = ' + str(p) + '\n stdErr = ' + str(std_err) + '\n m = ' + str(m) + '\n c = ' + str(c)
    plt.plot(x, mymodel,label=l)
    
    plt.ylabel(name[0]+name.lower()[1::]+" population in number of whales")
    plt.xlabel("Amount of oil spilled in tonnes")

    plt.legend(loc='best')
    plt.title(name)
    plt.show()

# whaleLinearRegress(fileBlueWhale, BlueWhale_year, "Blue Whale")
# whaleLinearRegress(fileFinWhale, FinWhale_year, "Fin Whale")
# whaleLinearRegress(fileGrayWhale, GrayWhale_year, "Gray Whale")
# whaleLinearRegress(fileHumpbackWhale, HumpbackWhale_year, "Humpback Whale")
# whaleLinearRegress(fileMinkeWhale, MinkeWhale_year, "Minke Whale")
# whaleLinearRegress(fileRightWhale, RightWhale_year, "Right Whale")

whaleLinearRegresstTest(fileBlueWhale, BlueWhale_year, "Blue Whale")
whaleLinearRegresstTest(fileFinWhale, FinWhale_year, "Fin Whale")
whaleLinearRegresstTest(fileGrayWhale, GrayWhale_year, "Gray Whale")
whaleLinearRegresstTest(fileHumpbackWhale, HumpbackWhale_year, "Humpback Whale")
whaleLinearRegresstTest(fileMinkeWhale, MinkeWhale_year, "Minke Whale")
whaleLinearRegresstTest(fileRightWhale, RightWhale_year, "Right Whale")



# whalePolyRegress(fileBlueWhale, BlueWhale_year, "Blue Whale")
# whalePolyRegress(fileFinWhale, FinWhale_year, "Fin Whale")
# whalePolyRegress(fileGrayWhale, GrayWhale_year, "Gray Whale")
# whalePolyRegress(fileHumpbackWhale, HumpbackWhale_year, "Humpback Whale")
# whalePolyRegress(fileMinkeWhale, MinkeWhale_year, "Minke Whale")
# whalePolyRegress(fileRightWhale, RightWhale_year, "Right Whale")
