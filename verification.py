import random
from PIL import Image,ImageDraw,ImageFont
def text():
    text=[]
    for i in range(0,4):
        num=random.randint(65,90)
        text.append(chr(num))
    return text


def textRandColor():
    color1 = random.randrange(0 ,225)
    color2 = random.randrange(0, 225)
    color3 = random.randrange(0, 225)
    return (color1, color2, color3)

def draw():
    image=Image.new('RGB',(300,100),'white')
    d=ImageDraw.Draw(image)
    ft=ImageFont.truetype('font111.ttc', 80)
    for i in range(4):
        d.text((random.randint(70*i-5,70*i+25),random.randint(1,30)),str(text()[i]),font=ft,fill=textRandColor())
        d.line([(0,random.randint(0,100)),(300,random.randint(0,100))],fill=textRandColor(),width=4)
    image.save('code.png','png')


if __name__ == "__main__":
    draw()
