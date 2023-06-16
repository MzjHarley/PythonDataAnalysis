

from pyecharts import Geo
data = [ ("海门", 9),("鄂尔多斯", 12),("招远", 12),("舟山", 12),("齐齐哈尔", 14),("盐城", 15), ("赤峰", 16),("青岛", 18),("乳山", 18),("金昌", 19),("泉州", 21),("莱西", 21), ("日照", 21),("胶南", 22),("南通", 23),("拉萨", 24),("云浮", 24),("梅州", 25)]
geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff",title_pos="center", width=1200, height=600, background_color='#404a59')#画出地图的背景
attr, value = geo.cast(data)#换数据序列，将带字典和元组类型的序列转换为 k_lst,v_lst 两个列表
print(attr,value)
geo.add('practice', attr, value, visual_range=[0, 200],visual_text_color="#fff", symbol_size=15, is_visualmap=True)#将点展示到上面加载的地图上
geo.show_config()
geo.render()#将地图保存为文件,默认path="render.html"