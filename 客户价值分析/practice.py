import pandas as pd
df = pd.DataFrame(pd.read_excel('./data/TB201812.xls'))
df1 = df[['订单付款时间','买家会员名','买家实际支付金额','数据采集时间']]
df1= df1.set_index('订单付款时间')
#日期显示
df2= df1.to_period('A') #以年为单位显示数据
print(df2)
#按日期统计数据
df3= df1.resample('Q').sum() #以季度为单位显示数据
df4= df1.resample('A').sum().to_period('A')
print(df3)
print(df4)
