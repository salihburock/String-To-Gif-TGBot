from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
letters = ["A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","N","O","Ö","P","Q","R","S","Ş","T","U","Ü","X","W","V","Y","Z"," "]

def makepng(letters=letters):
    global makepng
    for i in letters:
        img = Image.open("Letters\\blank.png").convert("RGBA")
        draw = ImageDraw.Draw(img)
        draw.rectangle(((0, 0), (500, 500)), fill="black")
        draw.text(xy=(0, 50), text=i, font=ImageFont.truetype("Letters\\font.TTF",size=500),stroke_width=0)
        img.save(f'Letters\{i}.png')