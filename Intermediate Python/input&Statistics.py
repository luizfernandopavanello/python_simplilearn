'''
Averages and measures of central location

These functions calculate an average or typical value from a population or sample.

mean() → Arithmetic mean (“average”) of data.
fmean() → Fast, floating point arithmetic mean.
geometric_mean() → Geometric mean of data.
harmonic_mean() → Harmonic mean of data.
median() → Median (middle value) of data.
median_low() → Low median of data.
median_high() → High median of data.
median_grouped() → Median, or 50th percentile, of grouped data.
mode() → Single mode (most common value) of discrete or nominal data.
multimode() → List of modes (most common values) of discrete or nomimal data.
quantiles() → Divide data into intervals with equal probability.
'''

# Input from user:
'''
name = input('What is your name?: ')
print('Hello', name)
'''

import statistics

exList = [5, 3, 2, 9, 7, 4, 1, 8, 9]

x = statistics.mean(exList) #Arithmetic mean (“average”) of data.
print(x)

x = statistics.median(exList) #Median (middle value) of data.
print(x)

x = statistics.mode(exList) #Single mode (most common value) of discrete or nominal data.
print(x)

x = statistics.stdev(exList) #Sample standard deviation of data.
print(x)

x = statistics.variance(exList) #Sample variance of data.
print(x)