import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

img1 = Image.open('points_price_plot.png')
img2 = Image.open('province_plot.png')
img3 = Image.open('province_price_plot.png')
img4 = Image.open('province_variety_plot.png')


img1_size = img1.size
img2_size = img2.size
img3_size = img3.size
img4_size = img4.size

new_im = Image.new('RGB', (2*img1_size[0],2*img1_size[1]), (250,250,250))

new_im.paste(img1, (0,0))
new_im.paste(img2, (img1_size[0],0))
new_im.paste(img3, (0,img1_size[1]))
new_im.paste(img4, (img1_size[0],img1_size[1]))

new_im.save("merged_images.png", "PNG")
new_im.show()