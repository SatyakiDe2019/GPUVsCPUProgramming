#################################################
#### Written By: SATYAKI DE                  ####
#### Written On: 18-Jan-2020                 ####
####                                         ####
#### Objective: Main calling scripts for     ####
#### use of GPU to speed-up the performance. ####
#################################################
 
import numpy as np
from timeit import default_timer as timer
 
# Adding GPU Instance
from os import environ
environ["KERAS_BACKEND"] = "plaidml.keras.backend"
 
def pow(a, b):
    return a ** b
 
def main():
    vec_size = 100000000
 
    a = b = np.array(np.random.sample(vec_size), dtype=np.float32)
    c = np.zeros(vec_size, dtype=np.float32)
 
    start = timer()
    c = pow(a, b)
    duration = timer() - start
 
    print(duration)
 
if __name__ == '__main__':
    main()
