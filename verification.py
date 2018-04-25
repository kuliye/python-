import random
from PIL import Image,ImageDraw,ImageFont#导入PIL相关类
def text():
    """生成随机验证文本"""
    text=[]
    for i in range(0,4):
        num=random.randint(65,90)
        text.append(chr(num))
    return text


def textRandColor():
    """生成随机文本颜色"""
    color1 = random.randrange(0 ,225)
    color2 = random.randrange(0, 225)
    color3 = random.randrange(0, 225)
    return (color1, color2, color3)

def draw():
    image=Image.new('RGB',(300,100),'white')#新建画板
    d=ImageDraw.Draw(image)#建立画笔
    ft=ImageFont.truetype('font111.ttc', 80)#字体以及以及颜色，字体根据位置进行变化
    for i in range(4):
        d.text((random.randint(70*i-5,70*i+25),random.randint(1,30)),str(text()[i]),font=ft,fill=textRandColor())#随机位置画上文字
        d.line([(0,random.randint(0,100)),(300,random.randint(0,100))],fill=textRandColor(),width=4)#添加干扰线
    image.save('code.png','png')


if __name__ == "__main__":
    draw()
