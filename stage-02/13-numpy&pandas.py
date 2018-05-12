print("-----------------numpy的一些属性----------------")
import numpy as np

ar = np.array([[1,2,3],[2,3,4]])

print(ar)
print("number of dim",ar.ndim)
print("shape",ar.shape)
print("size",ar.size)

print("------------------numpy创建array------------")
import numpy as np

a = np.array([1,2,3],dtype = np.float)

print(a.dtype)

b = np.zeros((3,4))
print(b)

c = np.ones((3,4))
print(c)

d = np.arange(10,20,2)
print(d)


f = np.arange(12).reshape((3,4))
print(f)


g= np.linspace(1,10,5)
print(g)

print("-------------numpy的基础运算--------------")
aa = np.array([10,20,30,40])
bb = np.arange(4)
print(aa,bb)
cc = aa-bb

dd = bb**2 #bb的平方的写法
print(cc)
print(bb<3)

a1 = np.array([[1,1],
               [0,1]])

a2 = np.arange(4).reshape((2,2))

c1 = a1*a2 #简单的矩阵相乘
c_dot = np.dot(a1,a2)#以矩阵的方式进行相乘
print(c1)
print(c_dot)

a2 = np.random.random((2,4))
print(a2)
print(np.sum(a2))       #axis等于0 每一行中的求和,等于1 每一列中的求和
print(np.min(a2,axis=0)) #axis等于0 查找每一行中的最小值,等于1 查找每一列中的最小值
print(np.max(a2))


A= np.arange(14,2,-1).reshape((3,4))
print(A)
print(np.argmax(A))#返回的是最大值的位置索引
print(np.argmin(A))#返回的是最小值的位置索引
print(np.mean(A)) #平均值
print(np.average(A)) #平均值
print(np.median(A)) #中位数
print(np.cumsum(A)) #依次累加
print(np.diff(A)) #累差
print(np.nonzero(A)) #找出非0的数  返回的是两个数组 表示几行几列是非0的
print(np.sort(A))#排序会对逐行进行排序
print(np.transpose(A)) #矩阵的行列互转

print(np.clip(A,5,9)) #大于9的转化为9  小于5的转化为5

print("-------------------numpy的索引------------------")
B = np.arange(3,15).reshape((3,4))
print(B)
print(B[1][1])
print(B[1,1:3]) #索引出第1行第1列到第3列的数字

for row in B: #遍历出每一行
    print(row)

#python中没有提供遍历每一列 使用T对矩阵进行行列转换
for column in B.T: #遍历出每一列
    print(column)

print(B.flatten()) #转换成一个一维数组
#然后就可以遍历了 A.flat是转换成迭代器
for item in A.flat:
    print(item)

print("---------------numpy的array合并-----------------")
AA = np.array([1,1,1])
BB = np.array([2,2,2])
CC = np.vstack((AA,BB)) #上下合并
DD = np.hstack((AA,BB)) #左右合并
print(DD)  #[1 1 1 2 2 2]
print(DD.shape) #(6,) 合并后6个元素CC
print(CC)
'''
CC的print结果
[[1 1 1]
 [2 2 2]]
'''
print(AA.shape,CC.shape) # (3,)说明三个元素   (2, 3)说明cc在vstack后成了一个2行3列的矩阵

#多个数组的合并
print("-"*10)
DD = np.concatenate((A,B,B,A)) #可以加axis参数
print(DD)
print("-"*10)

#把横向数列变成纵向
print(AA[:,np.newaxis])

print("-----------------numpy的array分割------------------")
A1= np.arange(12).reshape((3,4))
print(A1)

print(np.split(A1,2,axis=1)) #对列进行纵向的分割

print(np.split(A1,3,axis=0)) #对行进行纵向的分割

print(np.array_split(A1,3,axis=1)) #对列进行纵向的不等分分割

print(np.vsplit(A1,3))
print(np.hsplit(A1,2))

print("----------------numpy的copy和deepcopy------------------")
A2 = np.arange(4)
print(A2)
B2 = A2
A2[0] = 11
print(A2)
print(B2)

C2 = A2.copy() #deep copy
A2[0] = 22
print(A2)
print(B2)
print(C2)

print("----------------pandas基本介绍------------------")
import pandas as pd
s = pd.Series([1,3,6,np.nan,44,1])
print(s)

dates = pd.date_range('20180101',periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)

df1 = pd.DataFrame(np.arange(12).reshape((3,4))) #不指定行列,默认就是0,1,2.....
print(df1)

#通过字典的方式定义
df2 = pd.DataFrame({'a':1,'b':'hello kitty','c':np.arange(2),'d':['o','k']})
print(df2)
print("类型===",df2.dtypes)  #查看对应的数据类型
print("下标===",df2.index)
print("标题===",df2.columns)
print("值====",df2.values)
print("描述===",df2.describe())
print("翻倒===",df2.T)

print(df2.sort_index(axis=1,ascending=False)) #按列排序
print(df2.sort_index(axis=0,ascending=False)) #按行排序
print(df2.sort_values(by='c')) #按值排序,需要确定是按哪个值

print("---------pandas选择数据-----------")
dates = pd.date_range('20180101',periods=6)
ff = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['a','b','c','d'])
print(ff)
# print(ff['a'],ff.a)

#这两种方式都可以
# print(ff[0:3])
# print(ff['20180102':'20180103'])

#查看指定的数据
# print(ff.loc['20180102'])
# print(ff.loc[:,['a','b']])

# print(ff.iloc[3])  #取数第三行
# print(ff.iloc[3,1]) #第三行的第一位
# print(ff.iloc[3:5,1:3]) #第三行到第五行 中第一位到第三位
# print(ff.iloc[[1, 3, 5], 1:3])

# print(ff.ix[:3,['a','c']])

# print(ff[ff.a > 8])#筛选出a列>8的数据 然后其他列也显示的数据

print("------------------pandas设置值--------------")
dates = pd.date_range('20180101',periods=6)
fff = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['a','b','c','d'])
print(fff)

# fff.iloc[2,2] = 111
# fff.loc['20180101','b'] = 222
# fff.a[fff.a > 0] = 0 只对a大于0的数赋值为0
# fff[fff.a > 0] = 0 #这个是先找出a列大于0的数据 然后再对整个列表大于4的全部赋值为0
# fff['f'] = np.nan
fff['e'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20180101',periods=6))
print(fff)

print("------------------pandas处理丢失数据--------------")
dates = pd.date_range('20180101',periods=6)
fdl = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['a','b','c','d'])
fdl.iloc[0,1] = np.nan
fdl.iloc[1,2] = np.nan
print(fdl)

print(fdl.dropna(axis=0,how='any'))# 按行丢掉  how = all 只有这一行'全部'是nan时才会丢掉

print(fdl.fillna(value=0)) #如果发现是nan 就填入0

print(fdl.isnull()) #判断是否缺失数据
print(np.any(fdl.isnull()) == True)

print("------------------pandas导入导出数据--------------")

# data = pd.read_csv('.csv')
# print(data)
#
# data.to_pickle("sss.pickle")

print("------------------pandas concat合并--------------")
ff1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
ff2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
ff3 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])

res = pd.concat([ff1,ff2,ff3],axis=0,ignore_index=True) #忽略之前的索引
print(res)

ff4 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
ff5 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])

#join
#inner会只保留相同的组 就是bcd join模式是outer 即abcde全有
# res1 = pd.concat([ff4,ff5],join='inner',ignore_index=True)

# 左右合并 并且按照ff4中index的形式去处理数据,即ff5中没有1这个index,就填nan 而多出来的index4会删除
res1 = pd.concat([ff4,ff5],axis=1,join_axes=[ff4.index])

ff6 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
ff7 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
ff8 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
#append
# res2 = ff6.append(ff7)

s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
res2 = ff6.append(s1,ignore_index=True)

print(res2)


print("------------------pandas merge--------------")
import pandas as pd
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                                  'A': ['A0', 'A1', 'A2', 'A3'],
                                  'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                                    'C': ['C0', 'C1', 'C2', 'C3'],
                                    'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
res = pd.merge(left, right, on='key')
print(res)
print('-------------------')

# consider two keys
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
res = pd.merge(left, right, on=['key1', 'key2'], how='inner')  #默认 how='inner'
print(res)
# how = ['left', 'right', 'outer', 'inner']的取值
res = pd.merge(left, right, on=['key1', 'key2'], how='left')
print(res)
print('-------------------')

# indicator  就是告诉你一个合并的方式
df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
print(df1)
print(df2)
res = pd.merge(df1, df2, on='col1', how='outer', indicator=True)
print(res)
# give the indicator a custom name
res = pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column')
print(res)

print('-------------------')

# merged by index
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])
print(left)
print(right)
# left_index and right_index
res = pd.merge(left, right, left_index=True, right_index=True, how='outer')
print(res)
res = pd.merge(left, right, left_index=True, right_index=True, how='inner')
print(res)
print('-------------------')

# handle overlapping
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
print(boys)
print(girls)
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
print(res)
print('-------------------')

print("---------------plot--------------")
import matplotlib.pyplot as plt

# plot data

# Series
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = data.cumsum() #累加
##data.plot()

# DataFrame
data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD"))
data = data.cumsum()
# plot methods:
# 'bar', 'hist', 'box', 'kde', 'area', scatter', hexbin', 'pie'
ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label="Class 1")
data.plot.scatter(x='A', y='C', color='DarkGreen', label='Class 2', ax=ax)

plt.show()







