import pywt
import scipy.io
from itertools import chain,islice
import numpy as np
import serial
import time

mat = scipy.io.loadmat('100m.mat')
mat_new = mat['val'][0]

(c1 , c2 , c3 , c4 , c5 , c6)= pywt.wavedec(mat_new,'db2' , level = 5)
new_coef  = list(chain(c1,c2,c3,c4,c5,c6))
new_coef_index = [len(c1),len(c2),len(c3),len(c4),len(c5),len(c6)]

max_coef = max(new_coef)
min_coef = min(new_coef)
th = 0.01*(max_coef - min_coef)

for i in range(len(new_coef)):
    if abs(new_coef[i])<th:
        new_coef[i] = 0
        
input_coef = iter(np.array(new_coef)) 
output_coef = [list(islice(input_coef, elem))for elem in new_coef_index] 
coef=([np.array(i) for i in output_coef])
denoised_signal = pywt.waverec(coef , 'db2')
print(denoised_signal)
