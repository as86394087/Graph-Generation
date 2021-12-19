import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import jupyter

f = pd.read_excel('20210708163034-10A.xlsx',usecols=[0,1,2,3])
x1 = f['Time']
y = f['V1']



fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])

l1 = plt.plot(x1,y,'k-')
#l2 = plt.plot(x2,y,'rH--')

ax.legend(labels =('////////','////////'),loc = 'lower right')
ax.grid(True,color = 'g')
ax.set_title('//////////////////////')
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()