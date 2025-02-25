
#A lambda function is a small function containing a single expression 
# written in a single line. Lambda functions can also act as anonymous functions
# where they don’t require function name or identifier. 
# These are very helpful when we have to perform small tasks with less code.

import pandas as pd
df=pd.DataFrame({
    'id':[1,2,3,4,5],
    'name':['Jeremy','Frank','Janet','Ryan','Mary'],
    'age':[20,25,15,10,30],
    'income':[4000,7000,200,0,10000]
})
print(df)

df['age']=df.apply(lambda x: x['age']+3,axis=1)
print(df)

a= list(filter(lambda x: x>18,df['age']))
print(a)

df['income']=list(map(lambda x: int(x+x*0.2),df['income']))
print(df)

import functools
functools.reduce(lambda a,b: a+b,df['income'])


a = (lambda x: x*x*x)(10)
print(a)