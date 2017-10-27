import math
import numpy as np
x = 0
data_len = 1000
data_w = 32
data = np.zeros(data_w)

def list2str(input_list):
    out = ""
    for item in input_list:
        out += str(item) + "\t"
    return out
for i in range(data_len):
    y = math.sin(x)
    x += 0.1
    data[:-1] = data[1:]
    data[-1] = y
    data_str = list2str(data)
    with open("d_mask.txt", "a+") as f:  
        f.write(data_str+"\n")
        f.close()

print "done!"
