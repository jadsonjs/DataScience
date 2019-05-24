#
# This program is distributed without any warranty and it
# can be freely redistributed for research, classes or private studies,
# since the copyright notices are not removed.
#
# This file performs convolution between two arrays using scipy
#
# Jadson Santos - jadsonjs@gmail.com
#
#
# to run this exemple install pyhton modules:
#
# python3 -m pip install SciPy
#

from scipy import signal
con = signal.convolve([1, 2, 3], [1, 2, 3, 4, 5], mode='full')
print(con)
