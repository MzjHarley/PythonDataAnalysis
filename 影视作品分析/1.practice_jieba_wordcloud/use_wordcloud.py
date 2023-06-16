import wordcloud   # 导入词云模块
import imageio
import matplotlib.pyplot as plt
import jieba
back_color = imageio.imread('background.png')  # 解析该图片
w = wordcloud.WordCloud(
    font_path="./SIMYOU.TTF",  # 字体,防止中文乱码
    background_color="WHITE",  # 白色背景
    mask = back_color,  # 设置背景的形状
                        ) # 创建词云对象

with open("写不完的温柔.txt","r",encoding='utf-8') as fp:
    content = fp.read()
content = jieba.lcut(content)
print(content)
content=[x for x in content if x.strip()!=''] #去除换行符
print(content)
content = str(content).replace(",","") #去掉逗号
print(content)
sentence = ''
for x in content[1:-1]:
    sentence = sentence+" "+ x #去掉引号
print(sentence)
w.generate(sentence)
plt.imshow(w, interpolation="bilinear") #使用双线性插值，设置边界的模糊度，或者是图片的模糊度，
plt.axis("off")
plt.show()
w.to_file('picture.png')  # 保存图片
