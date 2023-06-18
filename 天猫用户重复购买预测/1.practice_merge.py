import pandas as pd
ls = [(1,2,3,4),(4,5,6,7),(8,9,10,11)]
ls1 = [(1,2,3,4),(3,5,6,7),(8,9,10,11)]
df = pd.DataFrame(ls)
df1 = pd.DataFrame(ls1)
print(df)
print("-"*20)
print(df1)
print("-"*20)
df.columns=['a','b','c','d']
print(df)
print("-"*20)
df1.columns=['a','b','c','d']
print(df1)
print("-"*20)
t= df.merge(df1,on='a')
#内连接：用于连接的列名值交集，存在即合并。默认为此连接
#外连接：用于连接列名值并集 ，存在即合并，否则也合并，无公共部分则NAN
#左连接：按照做左边dataframe进行外连接
#右连接：按照右边的dataframe进行外连接。
print(t)
print("-"*20)
df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'value': [1, 2, 3, 4],'value1':[8,11,8,11]})
print("df1:\n",df1)
df3=df1.groupby(by='value1')
print("d3:\n",list(df3))
print("-"*20)
df4 = df3.size().reset_index()
print("df4:\n",df4)
print("-"*20)
df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'], 'value': [5, 6, 7, 8]})
print("df2:\n",df2)
print("-"*20)
result = pd.merge(df1, df2, on='key',how='left')
print("left:\n",result)
print("-"*20)
result = pd.merge(df1, df2, on='key',how='right')
print('right:\n',result)
print("-"*20)
matrix = pd.concat([df1, df2], axis=0)
print("concat:\n",matrix)
print("-"*20)
print(type(matrix))
print("-"*20)
pt = matrix[['key','value']]
print(pt)
print("-"*20)