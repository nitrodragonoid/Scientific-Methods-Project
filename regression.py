import matplotlib.pyplot as plt
from scipy import stats
import csv

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
        

def whaleRegress(file, whale, name):
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

    def myfunc(x):
      return m * x + c

    mymodel = list(map(myfunc, x))
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


whaleRegress(fileBlueWhale, BlueWhale_year, "Blue Whale")
whaleRegress(fileFinWhale, FinWhale_year, "Fin Whale")
whaleRegress(fileGrayWhale, GrayWhale_year, "Gray Whale")
whaleRegress(fileHumpbackWhale, HumpbackWhale_year, "Humpback Whale")
whaleRegress(fileMinkeWhale, MinkeWhale_year, "Minke Whale")
whaleRegress(fileRightWhale, RightWhale_year, "Right Whale")
