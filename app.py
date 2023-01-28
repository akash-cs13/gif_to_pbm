import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Scale, ttk, filedialog, Frame, StringVar, messagebox
from PIL import Image, ImageTk
from converter import Converter
from PIL import Image
import os
import webbrowser

CanvasConfig = dict( bg="#FFFFFF", height=500, width=650, bd=0, highlightthickness=0, relief="ridge")
path = os.getcwd()
gif_path = "D:/Projects/Python/gif_to_pbm/4.gif"
resize_height = 64
resize_width = 128
total_frames = 25
i = False


def setter(info):
    myconverter.setDimensions(info)

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._Canvas = None
        self.switch_Canvas(StartPage)

    def switch_Canvas(self, Canvas_class):
        new_Canvas = Canvas_class(self)
        if self._Canvas is not None:
            self._Canvas.destroy()
        self._Canvas = new_Canvas
        self._Canvas.pack()



class StartPage(tk.Canvas):
    def __init__(self, master):
        tk.Canvas.__init__(self, master, **CanvasConfig)
        self.place(x=0, y=0)
        self.button_image_1 = PhotoImage(file = path+"\\assets\\frame0\\button_1.png")
        button_1 = tk.Button(image = self.button_image_1, borderwidth=0, highlightthickness=0,
                  command=self.open_path, relief="flat")
        button_1.place(x=176.0, y=425.0, width=288.0, height=48.0)
        
        self.create_rectangle( 190.0, 242.0, 278.0, 293.0, fill="#000000", outline="")
 
        self.create_text( 198.0, 247.0, anchor="nw", text=".pbm", fill="#FFFFFF", font=("Arial Bold", 30 * -1))

        self.create_text( 287.0,  248.0, anchor="nw", text="Converter", fill="#000000", font=("Arial Bold", 36 * -1))

        self.create_text( 290.0, 212.0, anchor="nw", text=".gif to", fill="#000000", font=("Arial Bold", 24 * -1))

        
        self.button_image_2 = tk.PhotoImage( file = path+"\\assets\\frame0\\button_2.png")
        self.button_2 = Button( image=self.button_image_2, borderwidth=0, highlightthickness=0, command=lambda: master.switch_Canvas(RoutePage), relief="flat")
        
        
        self.button_image_3 = PhotoImage( file = path+"\\assets\\frame0\\button_3.png")
        button_3 = Button( image=self.button_image_3, borderwidth=0,  highlightthickness=0, command=self.github,  relief="flat")
        button_3.place( x=581.0,  y=81.0,  width=25.0,  height=25.0)

        self.button_image_4 = PhotoImage( file = path+"\\assets\\frame0\\button_4.png")
        button_4 = Button( image=self.button_image_4,  borderwidth=0,  highlightthickness=0,  command=self.info, relief="flat")
        button_4.place( x=580.0, y=45.0, width=27.0,  height=27.0)
    def info(self):
        messagebox.showinfo("Tip","Only file with .gif extenstions are supported for conversions, use \"Open Gif\" button to select your gif.")

    def github(self):
        webbrowser.open_new("https://github.com/akash-cs13/gif_to_pbm")

    def open_path(self):
        global gif_path
        global myconverter
        open_path = filedialog.askopenfilename()
        gif_path = open_path
        if gif_path.endswith(".gif"):
            myconverter = Converter()
            myconverter.path(gif_path)
            self.button_2.place( x=560.0, y=425.0,   width=48.0,  height=48.0)

        else:
            #print("error")
            messagebox.showerror("Error", "Select files with .gif extension")
    
class RoutePage(tk.Canvas):
    def __init__(self, master):
        tk.Canvas.__init__(self, master, **CanvasConfig)
        self.place(x = 0, y = 0)

        self.create_rectangle( 22.0, 21.0, 61.0, 45.0, fill="#000000", outline="")

        self.create_text( 27.0, 26.0, anchor="nw", text=".pbm", fill="#FFFFFF", font=("Arial Bold", 12 * -1))

        self.create_text( 66.0, 27.0, anchor="nw", text="Converter", fill="#000000", font=("Arial Bold", 12 * -1))

        self.button_image_1 = PhotoImage( file=path+"\\assets\\frame1\\button_1.png")
        button_1 = Button( image=self.button_image_1, borderwidth=0, highlightthickness=0, command=lambda: master.switch_Canvas(StartPage), relief="flat" )
        button_1.place( x=42.0, y=425.0, width=48.0, height=48.0 )

        self.button_image_2 = PhotoImage( file=path+"\\assets\\frame1\\button_2.png")
        button_2 = Button( image=self.button_image_2, borderwidth=0, highlightthickness=0, command=self.info, relief="flat" )
        button_2.place( x=580.0, y=20.0, width=27.0, height=27.0 )

        self.button_image_3 = PhotoImage( file=path+"\\assets\\frame1\\button_3.png")
        button_3 = Button( image=self.button_image_3, borderwidth=0, highlightthickness=0, command=lambda: master.switch_Canvas(Tools_SetFrames), relief="flat" )
        button_3.place( x=182.0, y=142.0, width=288.0, height=48.0 )

        self.button_image_4 = PhotoImage( file=path+"\\assets\\frame1\\button_4.png")
        button_4 = Button( image=self.button_image_4, borderwidth=0, highlightthickness=0, command=lambda: master.switch_Canvas(Adjust), relief="flat" )
        button_4.place( x=182.0, y=226.0, width=288.0, height=48.0 )

        self.button_image_5 = PhotoImage( file=path+"\\assets\\frame1\\button_5.png")
        button_5 = Button( image=self.button_image_5, borderwidth=0, highlightthickness=0, command=lambda: master.switch_Canvas(ExportPage), relief="flat" )
        button_5.place( x=182.0, y=310.0, width=288.0, height=48.0 )
    
    def info(self):
        messagebox.showinfo("Tip","Recommended to edit your gif first using \"Tools\" , then adjust for black and white correction in \"Adjust\" before exporting.")

class Tools_SetFrames(tk.Canvas):
    def __init__(self, master):
        tk.Canvas.__init__(self, master, **CanvasConfig)
        self.total_frames = total_frames
        self.gif_path = gif_path
        global myconverter
        self.image2 = myconverter
        self.image2.set_frame_rate(total_frames)
        self.place(x = 0, y = 0)
        self.create_rectangle( 22.0, 21.0, 61.0, 45.0, fill="#000000", outline="")

        self.create_text( 27.0, 26.0, anchor="nw", text=".pbm", fill="#FFFFFF", font=("Arial Bold", 12 * -1) )

        self.create_text( 66.0, 27.0, anchor="nw", text="Converter", fill="#000000", font=("Arial Bold", 12 * -1) )

        #self.create_rectangle( 197.0, 113.0, 453.0, 304.47967529296875, fill="#E9E9E9", outline="")
        self.image_area_1 = Canvas( bg='#E9E9E9', width=256, height=191.48, highlightthickness=0, borderwidth=0, relief="flat")
        self.image_area_1.place(x=197.0, y=113.0)
        self.resize_image()
        
        self.frames = StringVar(value=str(self.total_frames))
        self.frames.trace("w", lambda name, index, mode, sv=self.frames: self.callback(sv))
        self.entry_image_1 = PhotoImage( file=path+"\\assets\\frame2\\entry_1.png")
        self.create_image( 375.0, 365.0, image=self.entry_image_1 )
        entry_1 = Entry( bd=0, textvariable=self.frames, bg="#FFFFFF", fg="#000716", font=("Arial Bold", 16 * -1), highlightthickness=0 )
        entry_1.place( x=358.0, y=352.0, width=36.0, height=26.0 )

        self.create_text( 250.0, 356.0, anchor="nw", text="Total frames:", fill="#000000", font=("Arial Bold", 16 * -1) )

        self.button_image_1 = PhotoImage( file=path+"\\assets\\frame2\\button_1.png")
        button_1 = Button( image=self.button_image_1, borderwidth=0, highlightthickness=0, command=lambda: master.switch_Canvas(RoutePage), relief="flat" )
        button_1.place( x=42.0, y=425.0, width=48.0, height=48.0 )

        self.button_image_2 = PhotoImage( file=path+"\\assets\\frame2\\button_2.png")
        button_2 = Button( image=self.button_image_2, borderwidth=0, highlightthickness=0, command=self.info, relief="flat" )
        button_2.place( x=580.0, y=20.0, width=27.0, height=27.0 )
        

        self.button_image_3 = PhotoImage( file=path+"\\assets\\frame2\\button_3.png")
        button_3 = Button( image=self.button_image_3, borderwidth=0, highlightthickness=0, command=lambda: master.switch_Canvas(Tools_Resize), relief="flat" )
        button_3.place( x=301.0, y=425.0, width=48.0, height=48.0 )

        self.button_image_4 = PhotoImage( file=path+"\\assets\\frame2\\button_4.png")
        button_4 = Button( image=self.button_image_4, borderwidth=0, highlightthickness=0, command=lambda: master.switch_Canvas(Tools_Crop), relief="flat" )
        button_4.place( x=373.0, y=425.0, width=48.0, height=48.0 )

        self.button_image_5 = PhotoImage( file=path+"\\assets\\frame2\\button_5.png")
        self.create_image( 229.0+24.0, 425.0+24.0, image=self.button_image_5 )

        self.button_image_6 = PhotoImage( file=path+"\\assets\\frame2\\button_6.png")
        button_6 = Button( image=self.button_image_6, borderwidth=0, highlightthickness=0, command=self.setFrames, relief="flat" )
        button_6.place( x=522.0, y=432.0, width=85.0, height=33.0 ) 
    
    def resize_image(self):
        input_image = Image.open(self.gif_path)
        w,h = input_image.size
        wsize = 256
        hsize = 191.48
        if w>h:
            a = (256/float(input_image.size[0]))
            b = int((float(input_image.size[1])*float(a)))
            padd_x = 0
            padd_y = (191.48-b)/2
            hsize = b
            
        else:
            b = (191.48/float(input_image.size[1]))
            a = int((float(input_image.size[0])*float(b)))
            padd_x = (256-a)/2
            padd_y = 0
            wsize = a

        disp_original_image =input_image.resize((int(wsize),int(hsize)), Image.Resampling.LANCZOS)
        self.image = ImageTk.PhotoImage(disp_original_image)
        self.image_area_1.create_image(0+padd_x,0+padd_y,image=self.image, anchor="nw" )

    def callback(self, sv):
        self.total_frames = int(sv.get())

    def setFrames(self):
        global total_frames
        global myconverter
        total_frames = self.total_frames
        setter(self.image2.send_dimensions())
    
    def info(self):
        messagebox.showinfo("Tip","Each frame takes 0.1s to play, increasing the number of frames will increase the duration of the animation. \n\nBy default, the animation is set to play for 2.5s.")
        
class Tools_Crop(tk.Canvas):
    def __init__(self, master):
        tk.Canvas.__init__(self, master, **CanvasConfig)
        self.gif_path = gif_path
        self.resize_height = resize_height
        self.resize_width = resize_width
        global myconverter
        self.image2 = myconverter
        self.image2.set_frame_rate(total_frames)
        #self.image2.myresize(self.resize_width,self.resize_height)


        self.place(x = 0, y = 0)
        self.create_rectangle( 22.0, 21.0, 61.0, 45.0, fill="#000000", outline="")

        self.create_text( 27.0, 26.0, anchor="nw", text=".pbm", fill="#FFFFFF", font=("Arial Bold", 12 * -1) )

        self.create_text( 66.0, 27.0, anchor="nw", text="Converter", fill="#000000", font=("Arial Bold", 12 * -1) )

        #self.create_rectangle( 207.0, 186.0, 463.0, 314.0, fill="#E9E9E9", outline="")
        self.resize_image()

        self.button_image_1 = PhotoImage( file=path+"\\assets\\frame3\\button_1.png")
        button_1 = Button( image=self.button_image_1, borderwidth=0, highlightthickness=0, command=self.up_arrow, relief="flat" )
        button_1.place( x=298.0, y=327.0, width=74.0, height=36.0 )

        self.button_image_2 = PhotoImage( file=path+"\\assets\\frame3\\button_2.png")
        button_2 = Button( image=self.button_image_2, borderwidth=0, highlightthickness=0, command=self.down_arrow, relief="flat" )
        button_2.place( x=298.0, y=137.0, width=74.0, height=36.0 )

        self.button_image_3 = PhotoImage( file=path+"\\assets\\frame3\\button_3.png")
        button_3 = Button( image=self.button_image_3, borderwidth=0, highlightthickness=0, command=self.right_arrow, relief="flat" )
        button_3.place( x=475.0, y=213.00001525878906, width=36.0, height=73.99998474121094 )

        self.button_image_4 = PhotoImage( file=path+"\\assets\\frame3\\button_4.png")
        button_4 = Button( image=self.button_image_4, borderwidth=0, highlightthickness=0, command=self.left_arrow, relief="flat" )
        button_4.place( x=159.0, y=213.0, width=36.0, height=74.0 )

        self.button_image_5 = PhotoImage( file=path+"\\assets\\frame3\\button_5.png")
        button_5 = Button( image=self.button_image_5, borderwidth=0, highlightthickness=0, command=self.zoom_plus, relief="flat" )
        button_5.place( x=560.0, y=186.0, width=34.0, height=33.0 )

        self.button_image_6 = PhotoImage( file=path+"\\assets\\frame3\\button_6.png")
        button_6 = Button( image=self.button_image_6, borderwidth=0, highlightthickness=0, command=lambda: master.switch_Canvas(RoutePage), relief="flat" )
        button_6.place( x=42.0, y=425.0, width=48.0, height=48.0 )

        self.button_image_7 = PhotoImage( file=path+"\\assets\\frame3\\button_7.png")
        button_7 = Button( image=self.button_image_7, borderwidth=0, highlightthickness=0, command=self.zoom_minus, relief="flat" )
        button_7.place( x=560.0, y=281.0, width=34.0, height=33.0 )

        self.image_image_1 = PhotoImage( file=path+"\\assets\\frame3\\image_1.png")
        self.create_image( 577.0, 249.0, image=self.image_image_1 )

        self.button_image_8 = PhotoImage( file=path+"\\assets\\frame3\\button_8.png")
        button_8 = Button( image=self.button_image_8, borderwidth=0, highlightthickness=0, command=self.mycrop, relief="flat" )
        button_8.place( x=522.0, y=432.0, width=85.0, height=33.0 )

        self.button_image_9 = PhotoImage( file=path+"\\assets\\frame3\\button_9.png")
        button_9 = Button( image=self.button_image_9, borderwidth=0, highlightthickness=0, command=self.info, relief="flat" )
        button_9.place( x=580.0, y=20.0, width=27.0, height=27.0 )

        self.button_image_10 = PhotoImage( file=path+"\\assets\\frame3\\button_10.png")
        button_10 = Button( image=self.button_image_10, borderwidth=0, highlightthickness=0, command=lambda: master.switch_Canvas(Tools_Resize), relief="flat" )
        button_10.place( x=301.0, y=425.0, width=48.0, height=48.0 )

        self.button_image_11 = PhotoImage( file=path+"\\assets\\frame3\\button_11.png")
        self.create_image( 373.0+24.0, 425.0+24.0, image=self.button_image_11 )

        self.button_image_12 = PhotoImage( file=path+"\\assets\\frame3\\button_12.png")
        button_12 = Button( image=self.button_image_12, borderwidth=0, highlightthickness=0, command=lambda: master.switch_Canvas(Tools_SetFrames), relief="flat" )
        button_12.place( x=229.0, y=425.0, width=48.0, height=48.0 )

    def info(self):
        messagebox.showinfo("Tip","Use the arrows and zoom to crop the gif. \n\nSome Oled displays have dual tone, adjust padding accordingly.")

    def resize_image(self):
        #self.image_area_1 = Canvas( bg='#E9E9E9', width=256, height=128, borderwidth=0, highlightthickness=0, relief="flat")
        self.image_area_1 = Canvas( bg='#E9E9E9', width=min(256,self.resize_width), height=min(128,self.resize_height), borderwidth=0, highlightthickness=0, relief="flat")
        self.image_area_1.place(x=335, y=250, anchor="center")
        self.image = ImageTk.PhotoImage(self.image2.get_image())
        self.image_area_1.create_image(0,0,image=self.image, anchor="nw" )

    def up_arrow(self):
        b = 0.05*resize_height
        self.image2.manipulate(0,-b,0,-b)
        self.resize_image()
    
    def down_arrow(self):
        b = 0.05*resize_height
        self.image2.manipulate(0,b,0,b)
        self.resize_image()

    def right_arrow(self):
        a = 0.05*resize_width
        self.image2.manipulate(-a,0,-a,0)
        self.resize_image()
    
    def left_arrow(self):
        a = 0.05*resize_width
        self.image2.manipulate(a,0,a,0)
        self.resize_image()

    def zoom_plus(self):
        a = 0.05*resize_width
        b = 0.05*resize_height
        self.image2.manipulate(a,b,-a,-b)
        self.resize_image()
    
    def zoom_minus(self):
        a = 0.05*resize_width
        b = 0.05*resize_height
        self.image2.manipulate(-a,-b,a,b)
        self.resize_image()

    def mycrop(self):
        global myconverter
        #print("crp temp: ",self.image2.send_dimensions())
        #myconverter = self.image2
        setter(self.image2.send_dimensions())
        #myconverter.setDimensions(self.image2.send_dimensions())
        #print(myconverter.send_dimensions())
        #print("done!")

class Tools_Resize(tk.Canvas):
    def __init__(self, master):
        tk.Canvas.__init__(self, master, **CanvasConfig)
        self.gif_path = gif_path
        self.resize_height = resize_height
        self.resize_width = resize_width
        global myconverter
        self.image2 = myconverter
        self.image2.set_frame_rate(total_frames)
       #self.image2.myresize(self.resize_width,self.resize_height)

        self.place(x = 0, y = 0)
        self.create_rectangle( 22.0, 21.0, 61.0, 45.0, fill="#000000", outline="")

        self.create_text( 27.0, 26.0, anchor="nw", text=".pbm", fill="#FFFFFF", font=("Arial Bold", 12 * -1) )

        self.create_text( 66.0, 27.0, anchor="nw", text="Converter", fill="#000000", font=("Arial Bold", 12 * -1) )

        #self.create_rectangle( 197.0, 113.0, 453.0, 304.48, fill="#E9E9E9", outline="")

        self.resize_image()
        

        self.height = StringVar(value=str(self.resize_height))
        self.height.trace("w", lambda name, index, mode, sv=self.height: self.hcallback(sv))
        self.entry_image_1 = PhotoImage( file=path+"\\assets\\frame4\\entry_1.png")
        self.create_image( 358.0, 365.0, image=self.entry_image_1 )
        entry_1 = Entry( bd=0, textvariable=self.height, bg="#FFFFFF", fg="#000716", font=("Arial Bold", 16 * -1), highlightthickness=0 )
        entry_1.place( x=341.0, y=352.0, width=36.0, height=26.0 )

        self.create_text( 320.0, 355.0, anchor="nw", text="x", fill="#000000", font=("Arial Bold", 16 * -1),  )

        self.width = StringVar(value=str(self.resize_width))
        self.width.trace("w", lambda name, index, mode, sv=self.width: self.wcallback(sv))
        self.entry_image_2 = PhotoImage( file=path+"\\assets\\frame4\\entry_2.png")
        self.create_image( 291.0, 365.0, image=self.entry_image_2 )
        entry_2 = Entry( bd=0, textvariable=self.width, bg="#FFFFFF", fg="#000716", font=("Arial Bold", 16 * -1), highlightthickness=0 )
        entry_2.place( x=274.0, y=352.0, width=36.0, height=26.0 )

        self.button_image_1 = PhotoImage( file=path+"\\assets\\frame4\\button_1.png")
        button_1 = Button( image=self.button_image_1, borderwidth=0, highlightthickness=0, command=lambda: master.switch_Canvas(RoutePage), relief="flat" )
        button_1.place( x=42.0, y=425.0, width=48.0, height=48.0 )

        self.button_image_2 = PhotoImage( file=path+"\\assets\\frame4\\button_2.png")
        button_2 = Button( image=self.button_image_2, borderwidth=0, highlightthickness=0, command=self.info, relief="flat" )
        button_2.place( x=580.0, y=20.0, width=27.0, height=27.0 )

        self.button_image_3 = PhotoImage( file=path+"\\assets\\frame4\\button_3.png")
        self.create_image( 301.0+24.0, 425.0+24.0, image=self.button_image_3 )

        self.button_image_4 = PhotoImage( file=path+"\\assets\\frame4\\button_4.png")
        button_4 = Button( image=self.button_image_4, borderwidth=0, highlightthickness=0, command=lambda: master.switch_Canvas(Tools_Crop), relief="flat" )
        button_4.place( x=373.0, y=425.0, width=48.0, height=48.0 )

        self.button_image_5 = PhotoImage( file=path+"\\assets\\frame4\\button_5.png")
        button_5 = Button( image=self.button_image_5, borderwidth=0, highlightthickness=0, command=lambda: master.switch_Canvas(Tools_SetFrames), relief="flat" )
        button_5.place( x=229.0, y=425.0, width=48.0, height=48.0 )

        self.button_image_6 = PhotoImage( file=path+"\\assets\\frame4\\button_6.png")
        button_6 = Button( image=self.button_image_6, borderwidth=0, highlightthickness=0, command=self.setSize, relief="flat" )
        button_6.place( x=522.0, y=432.0, width=85.0, height=33.0 )
    def info(self):
        messagebox.showinfo("Tip","Recomended maximum width and height is 500 x 250")
        
    def hcallback(self, sv):
        try: 
            self.resize_height = int(sv.get())
            #self.resize_image()
        except: pass#print("error")
    
    def wcallback(self, sv):
        try: 
            self.resize_width = int(sv.get())
            #self.resize_image()
        except: pass #print("error")

    def setSize(self):
        global resize_width
        global resize_height
        
        resize_height = self.resize_height
        resize_width = self.resize_width
        self.image2.myresize(self.resize_width, self.resize_height)
        self.resize_image()
        setter(self.image2.send_dimensions())
        
    def resize_image(self):
        self.image_area_1 = Canvas( bg='#FFFFFF', width=min(500,self.resize_width), height=min(250,self.resize_height), borderwidth=0, highlightthickness=0, relief="flat")
        self.image_area_1.place(x=325, y=201, anchor="center")

        self.image = ImageTk.PhotoImage(self.image2.get_image())
        self.image_area_1.create_image(0,0,image=self.image, anchor="nw" )

class Adjust(tk.Canvas):
    def __init__(self, master):
        tk.Canvas.__init__(self, master, **CanvasConfig)
        global i
        self.invert = i
        self.gif_path = gif_path
        self.resize_height = resize_height
        self.resize_width = resize_width
        global myconverter
        self.image2 = myconverter
        
        self.image2.set_frame_rate(total_frames)
        self.f = 0
        #self.image2.myresize(resize_width,resize_height)
        self.place(x = 0, y = 0)
        self.create_rectangle( 22.0, 21.0, 61.0, 45.0, fill="#000000", outline="")

        self.create_text( 27.0, 26.0, anchor="nw", text=".pbm", fill="#FFFFFF", font=("Arial Bold", 12 * -1) )

        self.create_text( 66.0, 27.0, anchor="nw", text="Converter", fill="#000000", font=("Arial Bold", 12 * -1) )

        #self.create_rectangle( 147.0, 120.0, 507.0, 300.0, fill="#E9E9E9", outline="")
        self.resize_image()

        self.button_image_1 = PhotoImage( file=path+"\\assets\\frame5\\button_1.png")
        button_1 = Button( image=self.button_image_1, borderwidth=0, highlightthickness=0, command=self.next, relief="flat" )
        button_1.place( x=526.0, y=166.99998474121094, width=36.0, height=73.99998474121094 )

        self.button_image_2 = PhotoImage( file=path+"\\assets\\frame5\\button_2.png")
        button_2 = Button( image=self.button_image_2, borderwidth=0, highlightthickness=0, command=self.back, relief="flat" )
        button_2.place( x=92.0, y=167.0, width=36.0, height=74.0 )

        self.create_text( 221.0, 439.0, anchor="nw", text="Invert:", fill="#000000", font=("Arial Bold", 16 * -1) )

        style = ttk.Style(self)
        style.configure("my.Horizontal.TScale", background="#FFFFFF", foreground="#000000", resolution=1,)
        self.slider = ttk.Scale(from_=0, to=255, length=360, value=128.0 , orient="horizontal",style="my.Horizontal.TScale",command=self.slider_fn)
        self.slider.place(x=147.0 ,y=350.0)

        self.button_image_3 = PhotoImage( file=path+"\\assets\\frame5\\button_3.png")
        button_3 = Button( image=self.button_image_3, borderwidth=0, highlightthickness=0, command=lambda: master.switch_Canvas(RoutePage), relief="flat" )
        button_3.place( x=42.0, y=425.0, width=48.0, height=48.0 )

        self.button_image_4 = PhotoImage( file=path+"\\assets\\frame5\\button_4.png")
        button_4 = Button( image=self.button_image_4, borderwidth=0, highlightthickness=0, command=self.invert_change, relief="flat" )
        button_4.place( x=274.0, y=425.0, width=48.0, height=48.0 )

        self.button_image_5 = PhotoImage( file=path+"\\assets\\frame5\\button_5.png")
        button_5 = Button( image=self.button_image_5, borderwidth=0, highlightthickness=0, command=self.myadjust, relief="flat" )
        button_5.place( x=346.0, y=425.0, width=48.0, height=48.0 )

        self.button_image_6 = PhotoImage( file=path+"\\assets\\frame5\\button_6.png")
        button_6 = Button( image=self.button_image_6, borderwidth=0, highlightthickness=0, command=self.info, relief="flat" )
        button_6.place( x=580.0, y=20.0, width=27.0, height=27.0 )
    
    def info(self):
        messagebox.showinfo("Tip","Use arrows to move through all the frames before saving. \n\nOled only displays the white region use the Invert option if necessary. \n\nLight greys are also considered to be a white region.")
    
    def slider_fn(self, var):
        #print(int(self.slider.get()))
        self.image2.set_threshold(int(self.slider.get()))
        self.resize_image()

    def resize_image(self):
        self.image_area_1 = Canvas( bg='#E9E9E9', width=min(500,self.resize_width), height=min(250,self.resize_height), borderwidth=0, highlightthickness=0, relief="flat")
        self.image_area_1.place(x=327, y=210, anchor="center")
        if self.invert:
            self.image = ImageTk.PhotoImage(self.image2.get_image(frame=self.f, type="inv"))
        else:
            self.image = ImageTk.PhotoImage(self.image2.get_image(frame=self.f, type="bw"))
        self.image_area_1.create_image(0,0,image=self.image, anchor="nw" )
    
    def next(self):
        if self.f >= total_frames-1:
            self.f = 0
        elif self.f < 0:
            self.f = total_frames-1
        else:
            self.f = self.f + 1
        self.resize_image()

    def back(self):
        if self.f >= total_frames-1:
            self.f = 0
        elif self.f < 0:
            self.f = total_frames-1
        else:
            self.f = self.f - 1  
        self.resize_image()
 
    def invert_change(self):
        self.invert = not self.invert
        self.resize_image()

    def myadjust(self):
        global i
        i = self.invert
        setter(self.image2.send_dimensions())

class ExportPage(tk.Canvas):
    def __init__(self, master):
        tk.Canvas.__init__(self, master, **CanvasConfig)
        self.save_name = "Animation"
        self.save_path = path
        self.place(x = 0, y = 0)
        self.button_image_1 = PhotoImage( file=path+"\\assets\\frame6\\button_1.png")
        self.button_1 = Button( image=self.button_image_1, borderwidth=0, highlightthickness=0, command=self.export, relief="flat" )
        

        self.create_rectangle( 326.0, 186.0, 414.0, 237.0, fill="#000000", outline="")

        self.create_text( 333.0, 192.0, anchor="nw", text=".pbm", fill="#FFFFFF", font=("Arial Bold", 30 * -1) )

        self.create_text( 236.0, 188.0, anchor="nw", text="Save", fill="#000000", font=("Arial Bold", 36 * -1) )

        self.name = StringVar(value=str(self.save_name))
        self.name.trace("w", lambda name, index, mode, sv=self.name: self.savecallback(sv))
        self.entry_image_1 = PhotoImage( file=path+"\\assets\\frame6\\entry_1.png")
        entry_bg_1 = self.create_image( 235.5, 299.0, image=self.entry_image_1 )
        entry_1 = Entry( bd=0,textvariable=self.name, bg="#FFFFFF", fg="#000716", font=("Arial Bold", 16 * -1), highlightthickness=0 )
        entry_1.place( x=172.0, y=278.0, width=128.0, height=40.0 )

        self.create_text( 139.0, 290.0, anchor="nw", text="as", fill="#000000", font=("Arial Bold", 16 * -1) )

        self.create_text( 316.0, 293.0, anchor="nw", text="in the  ", fill="#000000", font=("Arial Bold", 16 * -1) )

        self.button_image_2 = PhotoImage( file=path+"\\assets\\frame6\\button_2.png")
        button_2 = Button( image=self.button_image_2, borderwidth=0, highlightthickness=0, command=self.open_path, relief="flat" )
        button_2.place( x=369.0, y=278.0, width=139.0, height=48.0 )

        self.button_image_3 = PhotoImage( file=path+"\\assets\\frame6\\button_3.png")
        button_3 = Button( image=self.button_image_3, borderwidth=0, highlightthickness=0, command=lambda: master.switch_Canvas(StartPage), relief="flat" )
        button_3.place( x=560.0, y=425.0, width=48.0, height=48.0 )

        self.button_image_4 = PhotoImage( file=path+"\\assets\\frame6\\button_4.png")
        button_4 = Button( image=self.button_image_4, borderwidth=0, highlightthickness=0, command=lambda: master.switch_Canvas(RoutePage), relief="flat" )
        button_4.place( x=42.0, y=425.0, width=48.0, height=48.0 )

        self.button_image_5 = PhotoImage( file=path+"\\assets\\frame6\\button_5.png")
        button_5 = Button( image=self.button_image_5, borderwidth=0, highlightthickness=0, command=self.github, relief="flat" )
        button_5.place( x=581.0, y=81.0, width=25.0, height=25.0 )

        self.button_image_6 = PhotoImage( file=path+"\\assets\\frame6\\button_6.png")
        button_6 = Button( image=self.button_image_6, borderwidth=0, highlightthickness=0, command=self.info, relief="flat" )
        button_6.place( x=580.0, y=45.0, width=27.0, height=27.0 )

    def export(self):
        myconverter.save_images(self.save_path, self.save_name,i)
    
    def savecallback(self, sv):
        try: 
            self.save_name = str(sv.get())
            #print(self.save_name)
            #self.resize_image()
        except: pass#print("error")

    def open_path(self):
        global myconverter
        open_path = filedialog.askdirectory()
        self.save_path = open_path
        self.button_1.place( x=241.0, y=423.0, width=178.0, height=48.0 )
    
    def info(self):
        messagebox.showinfo("Tip","Folder with same name will be overwritten")

    def github(self):
        webbrowser.open_new("https://github.com/akash-cs13/gif_to_pbm")
    

if __name__ == "__main__":
    app = SampleApp()
    app.geometry("650x500")
    app.configure(bg = "#FFFFFF")
    app.resizable(False, False)
    app.title("Converter")
    app.iconbitmap(path+"\\assets\\myLogo.ico")
    app.mainloop()