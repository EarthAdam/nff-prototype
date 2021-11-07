#Filename:- gif_QRCode.py
#Required
#pip install MyQR

from MyQR import myqr
import os
  
version, level, qr_name = myqr.run(
  # Add string or a URL (add http(s):// before it)
  words="https://bit.ly/3ERzHnr",     

  # Set the highest fault tolerance rate
  version=1,               

  # Control the error correction level,
  # the range is L, M, Q, H, increasing from left to right
  level='H',               

  # Combining QR code + Image
  #Add file name eg. your_image.gif
  picture="nff_c1_1_actual.gif", 

  # Color QR code            
  colorized=True,    

  # Set contrast of the image,
  # 1.0 - original picture / default,
  # small value - low contrast,
  # large value - high contrast.        
  contrast=1.0,      

  # Set brightness of the image,
  # adjustment values ​​same as above        
  brightness=1.0,       

  # Save the file name, the format can be jpg, png, bmp, gif      
  save_name="collection1_nff1.gif",

  #Control location      
  save_dir=os.getcwd()          
)