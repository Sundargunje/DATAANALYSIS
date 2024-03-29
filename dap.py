# -*- coding: utf-8 -*-
"""DAP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cgq7OwMYlnkaUp2NE32Dhg2wr1fUvGRZ
"""

import numpy as np
#creating arrays
arr = np.array([1,2,3,4,5])
print(arr)

zeros_arr = np.zeros((3,3),dtype=int)
print(zeros_arr)
ones_arr = np.ones((2,2),dtype=int)
print(ones_arr)

import numpy as np
#creating arrays
arr = np.array([1,2,3,4,5])
print(arr)

zeros_arr = np.zeros((3,3),dtype=int)
print(zeros_arr)
ones_arr = np.ones((2,2),dtype=int)
print(ones_arr)
zeros_arr = np.zeros((3,3),dtype=int)
print(zeros_arr)
ones_arr = np.ones((2,2),dtype=int)
print(ones_arr)
arange_arr = np.arange(10)
#array manipulation
print(arange_arr)
reshape_arr = arr.reshape(5,1)
print(reshape_arr)

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
c=np.dot(a,b)
print(c)
d = np.linalg.eig(c)
print(d)



from google.colab import drive
drive.mount('/content/drive')



data = np.loadtxt("/content/drive/MyDrive/dataset (1)/data.txt", dtype=int, usecols=(0, 1))
d = np.savetxt("/content/date.txt", data)
print(d)
print(data)

import numpy as np
arange_arr = np.arange(0,100,5)
print(arange_arr)
d=np.savetxt("/content/dat.txt",arange_arr)
print(d)

a=np.random.rand()
print(a)
b=np.random.randint(0,3)
print(b)

a=np.array([[2,2],[3,3]])
print(type(a))
print(a.ndim)
print(a.shape)

a=np.linspace(0.8,2,5)
print(a)
b=np.arange(24).reshape(2,3,4)
print(b)

a=np.array([[2,2],[3,3]])
b=np.array([[2,2],[3,3]])
print(a*b)
print(a@b)
print(a-b)
print(np.dot(a,b))
print(a+b)

from numpy import random
a=np.ones((2,3),dtype=int)
print(a.max())
print(a.max(axis=1))
print(a.max(axis=0))
a=np.ceil(np.random.random([2,12]))
print(a)
c=np.random.random((2,2))
print(c)

from numpy import random
a=np.ones((2,3),dtype=int)
print(a.min())
print(a.min(axis=1))
print(a.min(axis=0))

from numpy import random
a=np.ones((2,3),dtype=int)
print(a.min())
print(a.cumsum(axis=1))
print(a.cumsum(axis=0))

a=np.array([2,3,5,6])
print(a.cumsum())
b=np.array([2,3,5,6,8,9])
print(b.resize(3,2))
print(b)
print(a)
print(a.shape)

a=np.array([2,3,5,6,8,9])
print(a.resize(2,3))
b=np.array([8,2,1,5,4,6])
print(b.resize(2,3))
print(np.vstack((a,b)))
print(np.hstack((a,b)))

"""no of rows become no of group
colum become rows
group become colum
"""

a=np.arange(30).reshape(2,3,5)
print(a)
print(np.dstack(a))

a1 = np.full((2,2),3)
print(a1)
print(a1.)

import numpy as np
a1 = np.full((2,2),3)
print(a1)
x =[1,2,3]
a = np.asarray(x)
print(a)
print(type(a))
x=np.array([1,4,0],float)
y=np.array([2,2,1],float)
print(np.inner(x,y))
print(np.outer(x,y))
print(np.cross(x,y))
a=np.array([1.1,2.2,3.9,4.1])
np.rint(a)
a1=np.array([1.1,2.2,3.9,4.1,2.5])
b1=np.array([1.6,2.7,3.8,1.2,3.5])
np.true_divide(a1,b1)
s=np.array([1,1,2,2,3,3,4,4])
np.unique(s)
s=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])
np.union1d(s,y)
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
np.setdiff1d(a,b)
a=8
b=6
c=np.hypot(a,b)
print(c)
x=np.sin(0)
print(x)

import numpy as np
a=8
b=6
c=np.hypot(a,b)
print(c)
x=np.sin(0)
print(x)

a=np.array([10,21,30,40,50,60])
b=np.array([20,21,2,20,25,25])
c=np.divmod(a,b)
s=np.mod(a,b)
d=np.divide(a,b)
x=np.multiply(a,b)
print(c)
print(s)
print(d)
print(x)

from numpy import random
x=random.normal(size=(2,3))
print(x)
x=random.normal(loc=1,scale=2,size=(2,3))
print(x)
x=random.binomial(n=12,p=0.5,size=10)
print(x)
y=random.poisson(lam=2,size=10)
print(y)
z=random.choice([1,2,3,4,5])
print(z)
x=random.choice([3,5],p=[0.2,0.8],size=(3,5))
print(x)



#circket
import numpy as np
import matplotlib.pyplot as plt
runs = np.array([100,50,91,78,89,25,34,19,9,10])
w=np.array([1,0,2,0,3,7,8,9,7,5])
plt.scatter(runs,w,color='red') #
plt.title



import numpy as np
import matplotlib.pyplot as plt
#generate array of 200 values b/w -pi &pi
tigar = np.linspace(-2*np.pi,2*np.pi,100)
print(tigar)
plt.plot(tigar,np.sin(tigar),color='yellow')
plt.title("sin(x)")
plt.show()

#plotting all in one graph
# use : plt.legend(loc='best')
#plt.plot(x,y,color,label)
import numpy as np
import matplotlib.pyplot as plt
#creating x
overs = np.arange(5,50,5)
overs_a = np.arange(5,30,5)
#creating y
runs_i = np.array([25,51,84,131,160,189,220,250,267])
runs_a = np.array([15,41,94,110,151])
wickets = np.array([12,32,96])
#plotting
plt.plot(overs,runs_i,color='blue',label='India')
plt.plot(overs_a,runs_a,color='yellow',label = 'Aus')
#combining two graphs
plt.legend(loc='best')
#displaying the final graph
plt.show()



sal = np.array([12000,60000,80000,76000])
wd = np.array([210,300,230,256])
years = [1,2]
bonus=[]
for i,j in zip(sal,wd):
 if j > 250:
 i = i+i*0.1
 bonus.append(i)
 else:
 i = i-i*0.1
 bonus.append(i)
print(bonus)

import matplotlib.pyplot as plt
a = [230,560,780,127,128]
b = [200,160,270,127,400]
years = [1,2,3,4]
profit_a = [(a[i]-a[i-1]) for i in range(1,len(a))]
profit_b = [(b[i]-b[i-1]) for i in range(1,len(b))]
plt.subplot(2,1,2)
plt.plot(years,profit_a,color='hotpink',linewidth = '3',label =
'CompanyA',marker='>',ms='20',mec='k')
plt.subplot(2,1,1)
plt.plot(years,profit_b,color='black',linestyle='dotted',label =
'CompanyB',marker = 'H')
plt.show()

a = np.array([25,60,5,10])
labe = ["AIML","Python","Pandas","Numpy"]
color =['green','pink','red','yellow']
explo = [0.2,0,0,0]
plt.pie(a,labels = labe,explode = explo,colors=color)
plt.show()

a = np.array([25,60,5,10])
labe = ["AIML","Python","Pandas","Numpy"]

explo = [0.3,0,0,0]
plt.pie(a,labels = labe,explode = explo,shadow=True)
plt.legend()
plt.show()

pip install seaborn