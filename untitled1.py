# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Akx4qDIDmIpx8qQaSNGv-3dsb1mIbsNn
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,6])
y=np.array([0,250])
plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,0.20,0.40,0.60,0.80,1,1.19,1.39,1.59,1.78,2])
y=np.array([0,0.82,-1.14,0.94,-0.38,-0.23,0.66,-0.74,0.48,-0.03,-1])
plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,0,0,2,2,2,1,1,1])
y=np.array([0,30,15,30,15,0,30,0,15])
plt.scatter(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,1,2,3])
y=np.array([0,2,5,1])
mycolor=['red','green','purple','blue']
size=[400,700,500,300]
plt.scatter(x,y,color=mycolor)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array(['680','681','611','510','612','540'])
y=np.array([25,23,18,27,16,30])
plt.bar(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([70,82,69,87,76])
mylabels=["SI asoslari", "Kompyuterni tashkil etilishi", "Elektronika va sxemalar", "Kiberxavfsizlik asoslari", "Malumotlar tuzilmasi va algoritm"]
mycolor=['silver','blue','yellow','violet','cyan']
plt.pie(x, labels=mylabels, colors=mycolor)
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([70,82,69,87,76])
mylabels=["SI asoslari", "Kompyuterni tashkil etilishi", "Elektronika va sxemalar", "Kiberxavfsizlik asoslari", "Malumotlar tuzilmasi va algoritm"]
myexplode=[0.1,0,0,0,0]
plt.pie(x, labels=mylabels, startangle=87, explode=myexplode)
plt.show()