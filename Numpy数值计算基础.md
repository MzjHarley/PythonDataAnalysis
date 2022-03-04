---
Author: MZJ
Date: 3/4,2022
---

>Numpy库是python数组运算，矩阵运算和科学计算的核心类库，以数组的形式对数据进行操作，并且由于使用c语言实现，故运算速度非常快。
>NumPy提供了两种基本的对象：ndarray（能存储单一数据类型的多维数组）和ufunc（能对数组进行处理的函数）

```python
import numpy as np
arr1 = np.array([1,2,3,4])# 采用numpy.array（object）创建一维数组
print("创建的数组为:",arr1)
```

    创建的数组为: [1 2 3 4]
    


```python
print("arr1数组元素类型:",arr1.dtype)
print("arr1数组维度:",arr1.shape)
print("arr1数组元素个数:",arr1.size)
print("arr1数组内每个元素大小:",arr1.itemsize)
```

    arr1数组元素类型: int32
    arr1数组维度: (4,)
    arr1数组元素个数: 4
    arr1数组内每个元素大小: 4
    


```python
arr2 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr2)
```

    [[ 1  2  3  4]
     [ 5  6  7  8]
     [ 9 10 11 12]]
    


```python
print("arr2数组维度:",arr2.shape)
arr2.shape = 4,3
print(arr2)
```

    arr2数组维度: (3, 4)
    [[ 1  2  3]
     [ 4  5  6]
     [ 7  8  9]
     [10 11 12]]
    


```python
arr3 = np.arange(0,1,0.1) # 采用numpy.arange（start,stop,step=1,dtype=None）,返回值为数组，不包含终止值
print(arr3)
```

    [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]
    


```python
arr4 = np.linspace(0,100,10,endpoint=False,retstep=True) #采用numpy.linspace（start,stop,num=50,endpoint=True,retstep=False,dtype=None）构造等差数列
print(arr4) #输出会显示间距
```

    (array([ 0., 10., 20., 30., 40., 50., 60., 70., 80., 90.]), 10.0)
    


```python
arr5 = np.logspace(0,2,20) #numpy.logspace（start,stop,num=50,endpoint=True,base=10.0,dtype=None）构造等比数列
print(arr5)
```

    [  1.           1.27427499   1.62377674   2.06913808   2.6366509
       3.35981829   4.2813324    5.45559478   6.95192796   8.8586679
      11.28837892  14.38449888  18.32980711  23.35721469  29.76351442
      37.92690191  48.32930239  61.58482111  78.47599704 100.        ]
    


```python
arr6=np.zeros((2,3)) #创建指定维度数组，并以0补充,参数为元组
print(arr6)
```

    [[0. 0. 0.]
     [0. 0. 0.]]
    


```python
arr7=np.eye(3) #创建主对角线为1，其他为0的数组
print(arr7)
```

    [[1. 0. 0.]
     [0. 1. 0.]
     [0. 0. 1.]]
    


```python
arr8=np.diag([1,2,3,4]) #创建除对角线其余为0的数组
print(arr8)
```

    [[1 0 0 0]
     [0 2 0 0]
     [0 0 3 0]
     [0 0 0 4]]
    


```python
arr9 = np.ones((5,3)) #创建元素全为1的数组
print(arr9)
```

    [[1. 1. 1.]
     [1. 1. 1.]
     [1. 1. 1.]
     [1. 1. 1.]
     [1. 1. 1.]]
    


```python
print(np.float64(42))
```

    42.0
    


```python
print(np.int8(42.0))
```

    42
    
