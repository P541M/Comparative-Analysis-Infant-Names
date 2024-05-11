#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

def printGraph():
    plt.ioff()
    #print(matplotlib.is_interactive())
    # Define X and Y variable data
    x = np.array([1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927,
    1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941,
    1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955,
    1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969,
    1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983,
    1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997,
    1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011,
    2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019])
    
    y = np.array([5, 5, 8, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
    3, 3, 2, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 5, 5, 7, 9, 11, 16, 17, 22, 25, 28, 31, 32,
    31, 35, 34, 34, 38, 40, 55, 59, 64, 60, 60, 70, 66, 58, 66, 75, 73, 81, 72, 84, 85, 82, 83,
    67, 79, 91, 99, 101, 104, 118, 116, 135, 146, 164, 173, 172, 180, 158, 149, 160, 162,196])
    plt.plot(x, y)
    plt.xlabel("X-axis") # add X-axis label
    plt.ylabel("Y-axis") # add Y-axis label
    plt.title("Popularity of Mary from 1917 to 2019") # title
    #Plot a line graph
    #plt.plot([1.5, 3.0])

    # Plot the title, X and Y axis labels
    plt.title("Non Interactive Mode")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.savefig("test2.png")

    # Data for plotting
    #t = np.arange(0.0, 2.0, 0.01)
    #s = 1 + np.sin(2 * np.pi * t)

    #fig, ax = plt.subplots()
    #ax.plot(t, s)

    #ax.set(xlabel='time (s)', ylabel='voltage (mV)',
    # #   title='About as simple as it gets, folks')
    #ax.grid()

    #fig.savefig("test.png")
    #plt.show()
