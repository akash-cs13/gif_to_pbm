import os
import cv2
import numpy
from PIL import Image
import PIL.ImageOps

#path = os.getcwd()

class Converter:
    def __init__(self):
        #self.path = path
        #self.image1 = Image.open(self.path)
        self.threshold = 128
        a,b = 128,64
        
        self.left = 0
        self.top = 0
        self.right = a
        self.bottom = b 
    def path(self, path):
        self.path = path
        self.image1 = Image.open(self.path)
        a,b = self.image1.size
        self.size = (a,b)
        self.set_frame_rate()

    def set_frame_rate(self, frame_rate=25):
        frames = self.image1.n_frames
        start_frame = 0
        x = frames/frame_rate
        self.frames_array = []
        for _ in range(0,frame_rate):
            self.frames_array.append(int(start_frame))
            start_frame = start_frame + x
        
        

    def save_images(self, save_path, save_name, invert=False):
        #print(self.frames_array)
        z = 1
        os.makedirs(f"{save_path}/{save_name}",mode=0o777,exist_ok=True)
        for f in self.frames_array:
            self.image1.seek(f)
            self.image1.convert("1")
            #x,y = self.size
            #self.myresize(x,y)
            image2 = self.black_and_white(self.threshold, self.image1.resize(self.size).crop((self.left, self.top, self.right, self.bottom)).resize(self.size))
            if invert:
                image2 = self.invert_image(image2)
            #print("save: "+os.path.join(save_path, "/"+save_name, f"/frame({str(z)}).pbm"))
            image2.save( f"{save_path}/{save_name}/frame({str(z)}).pbm" ) 
            z = z + 1
        
        
        print(f"Saved {save_name} successfully!")

    def set_threshold(self, x):
        self.threshold = x
        

    def get_image(self,frame=0, type="original"):
        
        self.image1.seek(self.frames_array[frame])
        self.image1.convert("1")
        itemp = self.image1.resize(self.size).crop((self.left, self.top, self.right, self.bottom)).resize(self.size)
        image2 = self.black_and_white(self.threshold, itemp)
        if type == "bw":
            return image2
        elif type == "inv":
            return PIL.ImageOps.invert(image2)    
        else: 
            return itemp
            
    def invert_image(self, image):
        return PIL.ImageOps.invert(image)
        

    
    def myresize(self, width=128, height=64):
        self.size = (width, height)
        self.right = width
        self.bottom = height

    def black_and_white(self, threshold, image1):
        self.threshold = threshold
        ocv_img = cv2.cvtColor(numpy.array(image1), cv2.COLOR_RGB2BGR)
        ret, image2 = cv2.threshold(ocv_img, threshold, 255, cv2.THRESH_BINARY)
        
        converted_img = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        image2=Image.fromarray(converted_img)
        return image2

    def send_dimensions(self):
        return (self.left, self.top, self.right, self.bottom, self.size, self.threshold, self.frames_array)          
    
    def setDimensions(self,send_dimen):
        left,top,right,bottom,size,threshold,frames = send_dimen
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.size = size
        self.threshold = threshold
        self.frames_array = frames

    def manipulate(self,left,top,right,bottom):
        #print(self.left, self.top, self.right, self.bottom)

        self.left = self.left + left
        self.top = self.top + top
        self.right = self.right + right
        self.bottom = self.bottom + bottom
        #print("setting ",self.left, self.top, self.right, self.bottom)

    
if __name__ == "__main__" :
    print("yo man!  ")
    
    

    