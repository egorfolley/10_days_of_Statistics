from math import erf, sqrt

if __name__ == '__main__':
    weight = int(input())
    load = int(input())
    mean = int(input())
    stdt_dev = int(input())

    CDF = lambda x, mean, stdt_dev : 1/2 * (1 + erf((x - mean)/(stdt_dev * sqrt(2))))

    print(round(CDF(weight, load * mean, sqrt(load) * stdt_dev), 4))

