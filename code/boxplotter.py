# functions
def median_(numberset):
    numberset.sort()
    if len(numberset)%2 == 0:
        median = (numberset[int(len(numberset)/2-1)] + numberset[int(len(numberset)/2)])/2
    else:
        median = numberset[int(len(numberset)/2)]
    return median

# getting set
listdone = False
print('Keep typing the numbers in the set, when done type "exit". \nFinal image can be saved from preview.')
numset = []
while not listdone:
    ask = input('No: ')
    if ask == 'exit':
        listdone = True
    try:
        numset.append(int(ask))
    except:
        if not ask == 'exit':
            print('Not a number')
numset.sort()

# getting median
median = median_(numset)

# getting bottom set
bottomset = []
for i in range(int((len(numset)/2))):
    bottomset.append(numset[i])

# getting q1
q1 = median_(bottomset)

# getting top set
topset = []
for i in range(len(numset)):
    topset.append(numset[i])
for i in range(len(bottomset)):
    del topset[0]
if len(numset)%2 == 1:
    del topset[0]

# getting q3
q3 = median_(topset)

# top and bottom values
high = numset[-1]
low = numset[0]

# pixel array setup
from PIL import Image, ImageDraw, ImageFont
print('')
start_point = int(input('Lower Bound of Graph: '))
stop_point = int(input('Higher Bound of Graph: '))
s_step = int(input('Small step: '))
l_step = int(input('Large step: '))
length = ((stop_point-start_point)*20)+40
img = Image.new('RGB', (length, 300), color = (255,255,255))
standard_row = [(255,255,255)]*length
imglist = standard_row*300
def set_pixel(x,y,colour):
    global imglist
    co_ord = (length*(y-1))+x-1
    imglist[int(co_ord)] = colour
def line_horiz(y, x1, x2, colour):
    for i in range(int(x1), int(x2+1)):
        set_pixel(i, int(y), colour)
def line_vert(x, y1, y2, colour):
    for i in range(int(y1), int(y2+1)):
        set_pixel(int(x), i, colour)
# graph pixel creation
line_horiz(260, 21, (length-19), (0,0,0)) # axis
line_vert(21, 260, 280, (0,0,0))
line_vert((length-19), 260, 280, (0,0,0))

# large steps
if (stop_point-start_point)%l_step == 0: top = int(((stop_point-start_point)/l_step))
else: top = int(((stop_point-start_point)/l_step))+1
for i in range(1,top):
    line_vert((21+(i*(20*l_step))), 260, 275, (0,0,0))

# small steps
if (stop_point-start_point)%s_step == 0: top = int(((stop_point-start_point)/s_step))
else: top = int(((stop_point-start_point)/s_step))+1
for i in range(1,top):
    line_vert((21+(i*(20*s_step))), 260, 270, (0,0,0))

# calculated lines
line_vert(21+(20*(median-start_point)), 149, 249, (0,0,0))
line_vert(21+(20*(q1-start_point)), 149, 249, (0,0,0))
line_vert(21+(20*(q3-start_point)), 149, 249, (0,0,0))
line_vert(21+(20*(high-start_point)), 149, 249, (0,0,0))
line_vert(21+(20*(low-start_point)), 149, 249, (0,0,0))

# lines between
line_horiz(249, 21+(20*(q1-start_point)), 21+(20*(q3-start_point)), (0,0,0))
line_horiz(149, 21+(20*(q1-start_point)), 21+(20*(q3-start_point)), (0,0,0))
line_horiz(199, 21+(20*(low-start_point)), 21+(20*(q1-start_point)), (0,0,0))
line_horiz(199, 21+(20*(q3-start_point)), 21+(20*(high-start_point)), (0,0,0))
    
# loading on pixels
img.putdata(imglist) # image pixels

# numbering
fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 10)
fnt2 = ImageFont.truetype('/Library/Fonts/Arial.ttf', 30)
numbers = ImageDraw.Draw(img)
numbers.text((15,280), str(start_point), font=fnt, fill=(0,0,0))
numbers.text(((length-24),280), str(stop_point), font=fnt, fill=(0,0,0))

# text
title = input('\nTitle: ')
axtitle = input('Axis Title: ')
words = ImageDraw.Draw(img)
words.text((((length//2)-20),280), axtitle, font=fnt, fill=(0,0,0))
words.text((10,90), title, font=fnt2, fill=(0,0,0))

img = img.crop((0,84,length,300))

img.show() # show image





