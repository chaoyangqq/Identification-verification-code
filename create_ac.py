##http://www.pythontab.com/html/2013/pythonhexinbiancheng_0201/197.html
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

_letter_cases = "abcdefghjkmnpqrsuvwxy" 
_upper_cases = _letter_cases.upper()
_numbers = ''.join(map(str, range(3, 10)))
init_chars = ''.join((_letter_cases, _upper_cases, _numbers))
fontType="/usr/share/fonts/truetype/freefont/FreeSans.ttf"

def create_validate_code(size=(120, 30),chars=init_chars,img_type="GIF",mode="RGB",bg_color=(255, 255, 255),fg_color=(0,0,255),font_size=18,font_type=fontType,length=4,draw_lines=True,n_line=(1, 2),draw_points=True,point_chance = 2):
    width, height = size 
    img = Image.new(mode, size, bg_color) 
    draw = ImageDraw.Draw(img) 
    if draw_lines:
        create_lines(draw,n_line,width/3,height/3)
    if draw_points:
        create_points(draw,point_chance,width,height)
    strs = create_strs(draw,chars,length,font_type, font_size,width,height,fg_color)
    params = [1 - float(random.randint(1, 2)) / 100,0,0,0,1 - float(random.randint(1, 10)) / 100,float(random.randint(1, 2)) / 500,0.001,float(random.randint(1, 2)) / 500]
    img = img.transform(size, Image.PERSPECTIVE, params) 
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return img, strs

def create_lines(draw,n_line,width,height):
    line_num = random.randint(n_line[0],n_line[1])
    for i in range(line_num):
        begin = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([begin, end], fill=(0, 0, 0))


def create_points(draw,point_chance,width,height):
    chance = min(100, max(0, int(point_chance)))
    for w in xrange(width):
        for h in xrange(height):
            tmp = random.randint(0, 100)
            if tmp > 100 - chance:
                draw.point((w, h), fill=(0, 0, 0))

def create_strs(draw,chars,length,font_type, font_size,width,height,fg_color):
    c_chars = random.sample(chars, length)
    strs = ' %s ' % ' '.join(c_chars)
    font = ImageFont.truetype(font_type, font_size)
    font_width, font_height = font.getsize(strs)
    draw.text(((width - font_width) / 3, (height - font_height) / 3),strs, font=font, fill=fg_color)
    return ''.join(c_chars)


for ii in xrange(10000):
    code_img = create_validate_code(fg_color=(random.randint(0,255),random.randint(0,255), random.randint(0,255)))
    code_img[0].save("/mnt/hgfs/data/yixin/testset/"+code_img[1]+".png", "PNG")




