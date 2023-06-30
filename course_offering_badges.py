from PIL import Image, ImageDraw, ImageFont

width = 1000
height = 100
text = "Offered Fall '23 & Winter '24"

width = 1100
text = "Offered Winter '24 & Spring '24"


img = Image.new('RGBA', (width, height))
imgDraw = ImageDraw.Draw(img)

imgDraw.rounded_rectangle((5, 5, width-5, height-5), outline="black", fill="white", width=8, radius=100)
imgDraw.multiline_text((width/2, height/2), text=text, font=ImageFont.truetype("FreeSansBold.ttf",
              size=70, layout_engine=ImageFont.Layout.BASIC), fill=(0,0,0), align="center", anchor="mm")
img.save("out.png")