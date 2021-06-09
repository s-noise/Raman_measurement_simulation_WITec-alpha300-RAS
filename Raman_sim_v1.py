#!/usr/bin/env python


#########################################################
##### univie , PNM , practical class MMM            #####
#####                                               #####
##### WITec alpha300 RAS, Raman settings simulation #####
#####                                               #####
##### Version 1.0                                   #####
#####                                               #####
##### Stefan Noisternig                             #####
#####                                               #####
##### comments will be added in future version      #####
#####                                               #####
##### see also: operation guides in WITec Suite     #####
#####           Help (since WITec Suite 5.3)        #####
#########################################################


import tkinter as tk

from PIL import ImageTk, Image

from inspect import currentframe, getframeinfo
from pathlib import Path

import time

import numpy as np


#filename = getframeinfo(currentframe()).filename
#print(filename)
#parent = Path(filename).resolve().parent
#path= parent / "images" / "2-Raman-CCD-cooldown-wait.png"


class WITec_Raman(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(self, width=800, height=600, background="bisque")
        self.xsb = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.ysb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)
        self.canvas.configure(scrollregion=(0,0,1514,1295))#(self.canvas.bbox("all"))#(scrollregion=(0,0,1000,1000))

        self.xsb.grid(row=1, column=0, sticky="ew")
        self.ysb.grid(row=0, column=1, sticky="ns")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


        #self.original = Image.open(path)
        #self.image = ImageTk.PhotoImage(self.original)
        #self.display = tk.Canvas(self, bd=0, highlightthickness=0)
        #self.display.create_image(0, 0, image=self.image, anchor='nw', tags="IMG")
        #self.display.grid(row=0, sticky='w'+'e'+'n'+'s')


        # button widget 
        #self.b1 = tk.Button(self, text = "Click me !") 
  
        # This is where b1 is placed inside b2 with in_ option 
        #self.b1.place(x = 500, y = 500, anchor = "nw") 
        #self.canvas.create_window(10, 10, anchor='nw', window=self.b1)


        # This is what enables using the mouse:
        self.canvas.bind("<ButtonPress-1>", self.move_start)
        self.canvas.bind("<B1-Motion>", self.move_move)



        root.title("WiTec simulation for AFM measurement")
        self.image=None

        filename = getframeinfo(currentframe()).filename
        self.parent = Path(filename).resolve().parent / "images"

        self.buttonimage1=None
        self.buttonimage2=None
        self.buttonimage3=None
        self.buttonimage4=None
        self.buttonimage5=None
        self.buttonimage6=None

        self.labelimage1=None
        self.labelimage2=None




        self.variableS1=tk.StringVar(root)
        self.variable1=tk.IntVar()
        self.variable2=tk.IntVar()
        self.variableD1=tk.DoubleVar()
        self.variableD2=tk.DoubleVar()
        self.variableS1=tk.StringVar(value='512')
        self.variableS2=tk.StringVar(value='512')
        self.variableS3=tk.StringVar(value='50')
        self.variableS4=tk.StringVar(value='24')
        self.variableS5=tk.StringVar(value='1')
        self.variableS6=tk.StringVar(value='0')
        self.variableS7=tk.StringVar(value='0')



        self.z_state=1
        self.klicked=False
        self.x_state=0
        self.y_state=0

        self.window=None

        self.rect = None

        self.start_x = None
        self.start_y = None
        self.x = self.y = 0


    #move
    def move_start(self, event):
        self.canvas.scan_mark(event.x, event.y)
    def move_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)


    def frameimage(self,imagename):
        path = self.parent / imagename
        print(path)
        self.image= ImageTk.PhotoImage(Image.open(path))
        self.canvas.create_image(0,0,image=self.image, anchor="nw")


    def button1(self,imagename,fname,positionX,positionY):
        # button widget
        path = self.parent / imagename
        self.buttonimage1 = ImageTk.PhotoImage(Image.open(path))

        button = tk.Button(root, image=self.buttonimage1,highlightthickness=0,borderwidth=0,relief=tk.FLAT)


        button.bind('<Button-1>', lambda event: fname())
        #button.bind('<Double-1>', lambda event: self.quiting())

        self.canvas.create_window(positionX, positionY, anchor='center', window=button)



    def button2(self,imagename,fname,positionX,positionY):
        # button widget
        path = self.parent / imagename
        self.buttonimage2 = ImageTk.PhotoImage(Image.open(path))

        button = tk.Button(root, image=self.buttonimage2,highlightthickness=0,borderwidth=0,relief=tk.FLAT)


        button.bind('<Button-1>', lambda event: fname())
        #button.bind('<Double-1>', lambda event: self.quiting())

        self.canvas.create_window(positionX, positionY, anchor='nw', window=button)


    def button3(self,imagename,fname,positionX,positionY):
        # button widget
        path = self.parent / imagename
        self.buttonimage3 = ImageTk.PhotoImage(Image.open(path))

        button = tk.Button(root, image=self.buttonimage3,highlightthickness=0,borderwidth=0,relief=tk.FLAT)


        button.bind('<Button-1>', lambda event: fname())
        #button.bind('<Double-1>', lambda event: self.quiting())

        self.canvas.create_window(positionX, positionY, anchor='nw', window=button)

    def button4(self,imagename,fname,positionX,positionY):
        # button widget
        path = self.parent / imagename
        self.buttonimage4 = ImageTk.PhotoImage(Image.open(path))

        button = tk.Button(root, image=self.buttonimage4,highlightthickness=0,borderwidth=0,relief=tk.FLAT)


        button.bind('<Button-1>', lambda event: fname())
        #button.bind('<Double-1>', lambda event: self.quiting())

        self.canvas.create_window(positionX, positionY, anchor='nw', window=button)

    def button5(self,imagename,fname,positionX,positionY):
        # button widget
        path = self.parent / imagename
        self.buttonimage5 = ImageTk.PhotoImage(Image.open(path))

        button = tk.Button(root, image=self.buttonimage5,highlightthickness=0,borderwidth=0,relief=tk.FLAT)


        button.bind('<Button-1>', lambda event: fname())
        #button.bind('<Double-1>', lambda event: self.quiting())

        self.canvas.create_window(positionX, positionY, anchor='nw', window=button)

    def button6(self,imagename,fname,positionX,positionY,bindbutton='<Button-1>'):
        # button widget
        path = self.parent / imagename
        self.buttonimage6 = ImageTk.PhotoImage(Image.open(path))

        button = tk.Button(root, image=self.buttonimage6,highlightthickness=0,borderwidth=0,relief=tk.FLAT)


        button.bind(bindbutton, lambda event: fname())
        #button.bind('<Double-1>', lambda event: self.quiting())

        self.canvas.create_window(positionX, positionY, anchor='nw', window=button)


    def label_image1(self,imagename,posX,posY):
        path = self.parent / imagename
        self.labelimage1 = ImageTk.PhotoImage(Image.open(path))

        label_frame=tk.LabelFrame(root,width=self.labelimage1.width(),height=self.labelimage1.height())
        label=tk.Label(label_frame,image=self.labelimage1)
        label.place(x=0,y=0)
        self.canvas.create_window(posX, posY, anchor='nw', window=label_frame)


    def label_image2(self,imagename,posX,posY):
        path = self.parent / imagename
        self.labelimage2 = ImageTk.PhotoImage(Image.open(path))

        label_frame=tk.LabelFrame(root,width=self.labelimage2.width(),height=self.labelimage2.height())
        label=tk.Label(label_frame,image=self.labelimage2)
        label.place(x=0,y=0)
        self.canvas.create_window(posX, posY, anchor='nw', window=label_frame)




    def numberfield(self,letterwidth,positionX,positionY):
        field=tk.Entry(root,width=letterwidth)
        field.bind('<Return>', lambda event: self.numbers(field))
        self.canvas.create_window(positionX, positionY, anchor='nw', window=field)


    def dropdown1(self,positionX,positionY,*Optionlist):

        def callback():
            print(self.variableS1.get())

        self.variableS1.set(Optionlist[0])
        dropdown=tk.OptionMenu(root,self.variableS1,*Optionlist)
        self.canvas.create_window(positionX, positionY, anchor='center', window=dropdown)
        self.variableS1.trace('w',callback)


    def lasermenu(self,imagename,positionX,positionY):

        path = self.parent / imagename
        self.buttonimage1 = ImageTk.PhotoImage(Image.open(path))

        mb=tk.Menubutton(root,image=self.buttonimage1)
        #mb.grid()
        mb.menu=tk.Menu(mb,tearoff=0)
        mb["menu"]=mb.menu

        mb.menu.add_checkbutton(label="Laser 532", command=self.next)
        mb.menu.add_checkbutton(label="Laser 488", command=lambda : self.failmessage(540,650,"!! Wrong Laser Entered !!"))
        mb.menu.add_checkbutton(label="Laser 633", command=lambda : self.failmessage(540,650,"!! Wrong Laser Entered !!"))
        mb.menu.add_checkbutton(label="Laser 785", command=lambda : self.failmessage(540,650,"!! Wrong Laser Entered !!"))

        self.canvas.create_window(positionX, positionY, anchor='nw', window=mb)


    def scantablemenu(self,imagename,positionX,positionY):

        path = self.parent / imagename
        self.buttonimage1 = ImageTk.PhotoImage(Image.open(path))

        mb=tk.Menubutton(root,image=self.buttonimage1)
        #mb.grid()
        mb.menu=tk.Menu(mb,tearoff=0)
        mb["menu"]=mb.menu

        mb.menu.add_checkbutton(label="Never", command=lambda : self.failmessage(360,220,"!! Choose Once option !!"))
        mb.menu.add_checkbutton(label="Once", command=self.next)
        mb.menu.add_checkbutton(label="Multiple", command=lambda : self.failmessage(360,220,"!! Choose Once option !!"))

        self.canvas.create_window(positionX, positionY, anchor='nw', window=mb)




    def checkbutton1(self,text,positionX,positionY,state=0,):
        check=tk.Checkbutton(root,text=text,variable=self.variable1)
        self.canvas.create_window(positionX, positionY, anchor='nw', window=check)
        if state==1:
            check.select()
        self.variable1.trace('w',self.hello)

    def checkbutton2(self,text,positionX,positionY,state=0,):
        check=tk.Checkbutton(root,text=text,variable=self.variable2)
        self.canvas.create_window(positionX, positionY, anchor='nw', window=check)
        if state==1:
            check.select()
        self.variable2.trace('w',self.hello)

    def scale1(self,positionX,positionY,text=None,length=100):
        scale=tk.Scale(root,variable=self.variableD1,orient='horizontal',from_=0,to_=0.25,resolution=0.025,length=length,label=text)
        self.canvas.create_window(positionX, positionY, anchor='nw', window=scale)
        self.variableD1.trace('w',self.hello)

    def scale2(self,positionX,positionY,text=None,length=100):
        scale=tk.Scale(root,variable=self.variableD2,orient='horizontal',from_=0,to_=48,resolution=4.8,length=length,label=text)
        self.canvas.create_window(positionX, positionY, anchor='nw', window=scale)
        self.variableD2.trace('w',self.hello)



    def brightness_scales(self,value1=0,value2=0):
        frame2=tk.LabelFrame(root,height=70,width=340)
        scale1=tk.Scale(frame2,variable=self.variableD1,orient='horizontal',from_=0,to_=0.25,resolution=0.025,length=175,width=5)
        scale1.set(value1)
        scale1.place(x=150,y=0)
        scalelabel1=tk.Label(frame2,text="Exposure [s]")
        scalelabel1.place(x=10,y=8)
        scale2=tk.Scale(frame2,variable=self.variableD2,orient='horizontal',from_=0,to_=48,resolution=4.8,length=175,width=5)
        scale2.set(value2)
        scale2.place(x=150,y=27)
        scalelabel2=tk.Label(frame2,text="Gain [dB]")
        scalelabel2.place(x=10,y=35)
        return frame2


    def brightness_checkbuttons(self,select=True):
        frame1=tk.LabelFrame(root,height=60,width=340)
        check1=tk.Checkbutton(frame1,text="Smart Exposure",variable=self.variable1)
        if select==True:
            check1.select()
        check1.place(x=10,y=3)
        check2=tk.Checkbutton(frame1,text="Smart Gain",variable=self.variable2)
        if select==True:
            check2.select()
        check2.place(x=10,y=27)
        return frame1



    def brightness_unset(self,posX1,posY1,posX2,posY2):
        self.klicked=False

        def checksetting(*args):
            if self.variable1.get()+self.variable2.get()==0:
                if self.variableD1.get()<0.05 and self.variableD2.get()<5.0 and self.klicked==False:
                    self.next()
                    self.klicked=True
                    self.variable1.trace_vdelete('w',trace1_id)
                    self.variable2.trace_vdelete('w',trace2_id)
                    self.variableD1.trace_vdelete('w',traceD1_id)
                    self.variableD2.trace_vdelete('w',traceD2_id)
        
        frame1=self.brightness_checkbuttons()
        self.canvas.create_window(posX1, posY1, anchor='nw', window=frame1)

        frame2=self.brightness_scales(value1=0.1,value2=10)
        self.canvas.create_window(posX2, posY2, anchor='nw', window=frame2)

        trace1_id=self.variable1.trace('w',checksetting)
        trace2_id=self.variable2.trace('w',checksetting)
        traceD1_id=self.variableD1.trace('w',checksetting)
        traceD2_id=self.variableD2.trace('w',checksetting)


    def brightness_change(self,darkimagename,brightimagename,posX,posY,posX2,posY2):
        self.klicked=False

        path = self.parent / darkimagename
        darkscreen = ImageTk.PhotoImage(Image.open(path))
        path = self.parent / brightimagename
        brightscreen=ImageTk.PhotoImage(Image.open(path))
        label=tk.Label(root,image=brightscreen)
        labelwindow=self.canvas.create_window(posX, posY, anchor='nw', window=label)

        def replacelabel(labelwindow,tkimage):
            self.canvas.delete(labelwindow)
            label=tk.Label(root,image=tkimage)
            labelwindow=self.canvas.create_window(posX, posY, anchor='nw', window=label)
            
        def checksetting(*args):
            if self.variableD1.get()<=0.08 or self.variableD2.get()<=37.0:
                replacelabel(labelwindow,darkscreen)
            elif  self.variableD1.get()>0.08 and self.variableD1.get()<0.17 and self.variableD2.get()>37.0 and self.variableD2.get()<47.0 and self.klicked==False:
                self.next()
                self.klicked=True
                self.variableD1.trace_vdelete('w',traceD1_id)
                self.variableD2.trace_vdelete('w',traceD2_id)
            else:
                replacelabel(labelwindow,brightscreen)

        frame2=self.brightness_scales(value1=0.25,value2=48)
        self.canvas.create_window(posX2, posY2, anchor='nw', window=frame2)

        traceD1_id=self.variableD1.trace('w',checksetting)
        traceD2_id=self.variableD2.trace('w',checksetting)



    def brightness_set(self,darkimagename,brightimagename,posX,posY,posX1,posY1,posX2,posY2):
        self.klicked=False

        path = self.parent / darkimagename
        darkscreen = ImageTk.PhotoImage(Image.open(path))
        path = self.parent / brightimagename
        brightscreen=ImageTk.PhotoImage(Image.open(path))
        label=tk.Label(root,image=brightscreen)
        labelwindow=self.canvas.create_window(posX, posY, anchor='nw', window=label)

        def replacelabel(labelwindow,tkimage):
            self.canvas.delete(labelwindow)
            label=tk.Label(root,image=tkimage)
            labelwindow=self.canvas.create_window(posX, posY, anchor='nw', window=label)
            
        def checksetting(*args):
            if self.variableD1.get()<=0.08 or self.variableD2.get()<=37.0:
                replacelabel(labelwindow,darkscreen)
                if self.variableD1.get()<0.08 and self.variableD2.get()<14.0 and (self.variable1.get()+self.variable2.get())==int(2):
                    self.variable1.trace_vdelete('w',trace1_id)
                    self.variable2.trace_vdelete('w',trace2_id)
                    self.variableD1.trace_vdelete('w',traceD1_id)
                    self.variableD2.trace_vdelete('w',traceD2_id)
                    self.next()

            else:
                replacelabel(labelwindow,brightscreen)

        frame1=self.brightness_checkbuttons(select=False)
        self.canvas.create_window(posX1, posY1, anchor='nw', window=frame1)

        frame2=self.brightness_scales(value1=0.25,value2=48)
        self.canvas.create_window(posX2, posY2, anchor='nw', window=frame2)

        trace1_id=self.variable1.trace('w',checksetting)
        trace2_id=self.variable2.trace('w',checksetting)
        traceD1_id=self.variableD1.trace('w',checksetting)
        traceD2_id=self.variableD2.trace('w',checksetting)


    def setprobescreen(self,imagename,buttonimagename,labw,labh,butX,butY,posX,posY):
        path = self.parent / imagename
        self.buttonimage1 = ImageTk.PhotoImage(Image.open(path))
        path = self.parent / buttonimagename
        self.buttonimage2 = ImageTk.PhotoImage(Image.open(path))

        label_frame=tk.LabelFrame(root,width=labw,height=labh)
        label=tk.Label(label_frame,image=self.buttonimage1,cursor='crosshair')
        label.place(x=0,y=0)
        button = tk.Button(label_frame, image=self.buttonimage2,highlightthickness=0,borderwidth=0,relief=tk.FLAT,cursor='crosshair')
        button.place(x=butX,y=butY)
        button.bind('<Button-1>', lambda event: self.next())
        self.canvas.create_window(posX, posY, anchor='nw', window=label_frame)



    
    def laserpower_field(self,max_value,min_value,letterwidth,positionX,positionY,mx,my):
        self.klicked=False

        def numbers(entry,self):
            try:
                number=float(entry.get())
                if number > float(max_value) or number < float(min_value) :
                    self.canvas.delete(self.window)
                    fail = tk.Label(root, text = "!!! Wrong value entered !!!", background='red', height=3, width=30) 
                    self.window=self.canvas.create_window(mx, my, anchor='nw', window=fail)
                    self.klicked=False


                else:
                    self.canvas.delete(self.window)
                    self.klicked=True

            except:
                self.canvas.delete(self.window)
                fail = tk.Label(root, text = "!!! Wrong value entered !!!", background='red', height=3, width=30)
                self.window=self.canvas.create_window(mx, my, anchor='nw', window=fail)

                self.klicked=False


        field=tk.Entry(root,width=letterwidth)
        field.bind('<Return>', lambda event: numbers(field,self))
        self.canvas.create_window(positionX, positionY, anchor='nw', window=field)

    


    def driving_amplitude(self,letterwidth,imagen0,imagen1,imagen2,positionX,positionY,posX,posY,posX1,posY1,posX2,posY2):
        self.klicked=False

        number=0.1
        returnnumber=0.061

        path = self.parent / imagen0
        screen0 = ImageTk.PhotoImage(Image.open(path))
        path = self.parent / imagen1
        screen1=ImageTk.PhotoImage(Image.open(path))
        path = self.parent / imagen2
        screen2=ImageTk.PhotoImage(Image.open(path))

        label=tk.Label(root,image=screen0,highlightthickness=0,borderwidth=0 )
        labelwindow=self.canvas.create_window(posX, posY, anchor='nw', window=label)

        driving_amp= tk.Label(root, text = number, background='lightgray',highlightthickness=0,borderwidth=0, height=1, width=3)
        driving_amp_w=self.canvas.create_window(posX1, posY1, anchor='nw', window=driving_amp)
  
        free_amp = tk.Label(root, text = returnnumber, background='white',highlightthickness=0,borderwidth=0, height=1, width=5) 
        free_amp_w=self.canvas.create_window(posX2, posY2, anchor='nw', window=free_amp)



        def replacelabel(labelwindow,driving_amp_w,free_amp_w,tkimage,number,returnnumber):
            self.canvas.delete(labelwindow)
            label=tk.Label(root,image=tkimage,highlightthickness=0,borderwidth=0)
            labelwindow=self.canvas.create_window(posX, posY, anchor='nw',window=label)
 
            self.canvas.delete(driving_amp_w)
            driving_amp= tk.Label(root, text = number, background='lightgray',highlightthickness=0,borderwidth=0, height=1, width=3)
            driving_amp_w=self.canvas.create_window(posX1, posY1, anchor='nw', window=driving_amp)
 
            self.canvas.delete(free_amp_w)
            free_amp = tk.Label(root, text = returnnumber, background='white',highlightthickness=0,borderwidth=0, height=1, width=5) 
            free_amp_w=self.canvas.create_window(posX2, posY2, anchor='nw', window=free_amp)


        def checksetting(entry):
            try:
                number=float(entry.get())
                returnnumber=number*0.425
                if returnnumber<0 or returnnumber>3:
                    self.klicked=False
                    self.failmessage()
                elif returnnumber<0.57:
                    self.klicked=False
                    replacelabel(labelwindow,driving_amp_w,free_amp_w,screen0,number,returnnumber)
                elif returnnumber>=0.57 and returnnumber <1.4:
                    self.klicked=False
                    replacelabel(labelwindow,driving_amp_w,free_amp_w,screen1,number,returnnumber)
                else:
                    self.klicked=True
                    replacelabel(labelwindow,driving_amp_w,free_amp_w,screen2,number,returnnumber)
            except:
                self.klicked=False
                self.failmessage()



        field=tk.Entry(root,width=letterwidth)
        field.bind('<Return>', lambda event: checksetting(field))
        self.canvas.create_window(positionX, positionY, anchor='nw', window=field)

        
    def setpoint(self,letterwidth,positionX,positionY):
        self.klicked=False
        def numbers(entry):
            try:
                number=float(entry.get())
                if number > 1.5 or number <1.1 :
                    self.klicked=False
                    self.failmessage()
                else:
                    self.klicked=True
            except:
                self.klicked=False
                self.failmessage()

       
        field=tk.Entry(root,width=letterwidth)
        field.bind('<Return>', lambda event: numbers(field))
        self.canvas.create_window(positionX, positionY, anchor='nw', window=field)




    def scan_settings(self,letterwidth,posX,posY,originX,originY,scale=2):

        self.klicked=False


        label1= tk.Label(root, textvariable = self.variableS1, background='lightgray',highlightthickness=0,borderwidth=0, height=1, width=7)
        label1=self.canvas.create_window(posX, posY-19, anchor='nw', window=label1)

        label2= tk.Label(root, textvariable = self.variableS2, background='lightgray',highlightthickness=0,borderwidth=0, height=1, width=7)
        label2=self.canvas.create_window(posX+35, posY-19, anchor='nw', window=label2)

        label3= tk.Label(root, textvariable = self.variableS3, background='lightgray',highlightthickness=0,borderwidth=0, height=1, width=7)
        label3=self.canvas.create_window(posX+70, posY-19, anchor='nw', window=label3)

        label4= tk.Label(root, textvariable = self.variableS4, background='lightgray',highlightthickness=0,borderwidth=0, height=1, width=7)
        label4=self.canvas.create_window(posX+105, posY-19, anchor='nw', window=label4)

                
        rectangle_w=self.canvas.create_line(originX-round(scale*float(self.variableS3.get())*0.5),originY-round(scale*float(self.variableS4.get())*0.5),originX+round(scale*float(self.variableS3.get())*0.5),originY-round(scale*float(self.variableS4.get())*0.5),originX+round(scale*float(self.variableS3.get())*0.5),originY+round(scale*float(self.variableS4.get())*0.5),originX-round(scale*float(self.variableS3.get())*0.5),originY+round(scale*float(self.variableS4.get())*0.5),originX-round(scale*float(self.variableS3.get())*0.5),originY-round(scale*float(self.variableS4.get())*0.5),width=2,fill='yellow',tags='rectangle')
        

        def make_rectangle(rectangle_w,scale,originX,originY):
            try:
                self.canvas.delete('rectangle')
                originX_shifted=originX+round(scale*float(self.variableS6.get()))
                originY_shifted=originY-round(scale*float(self.variableS7.get()))


                rectangle_w=self.canvas.create_line(originX_shifted-round(scale*float(self.variableS3.get())*0.5),originY_shifted-round(scale*float(self.variableS4.get())*0.5),originX_shifted+round(scale*float(self.variableS3.get())*0.5),originY_shifted-round(scale*float(self.variableS4.get())*0.5),originX_shifted+round(scale*float(self.variableS3.get())*0.5),originY_shifted+round(scale*float(self.variableS4.get())*0.5),originX_shifted-round(scale*float(self.variableS3.get())*0.5),originY_shifted+round(scale*float(self.variableS4.get())*0.5),originX_shifted-round(scale*float(self.variableS3.get())*0.5),originY_shifted-round(scale*float(self.variableS4.get())*0.5),width=2,fill='yellow',tags='rectangle')
            except:
                None
 

        def checksetting(*args):
            try:
                if float(self.variableS1.get())<4 or float(self.variableS2.get())<4 or float(self.variableS3.get())<=0 or float(self.variableS4.get())<=0 or float(self.variableS1.get())>512 or float(self.variableS2.get())>512 or float(self.variableS5.get())<0 or float(self.variableS5.get())>10 :
             
                    self.klicked=False
                    self.failmessage()

                elif  float(self.variableS3.get())*0.5+abs(float(self.variableS6.get()))>50:
                    if abs(float(self.variableS6.get()))<49:
                        self.variableS3.set(str(100-2*round(abs(float(self.variableS6.get())))))
                    else:
                        self.variableS6.set('49')
                        self.variableS3.set('1')

                    make_rectangle(rectangle_w,scale,originX,originY)
                    self.klicked=False
                    self.failmessage()


                elif  float(self.variableS4.get())*0.5+abs(float(self.variableS7.get()))>50:
                    if abs(float(self.variableS7.get()))<49:
                        self.variableS4.set(str(100-2*round(abs(float(self.variableS7.get())))))
                    else:
                        self.variableS7.set('49')
                        self.variableS4.set('1')

                    make_rectangle(rectangle_w,scale,originX,originY)
                    self.klicked=False
                    self.failmessage()


                else:
                    make_rectangle(rectangle_w,scale,originX,originY)
                    self.klicked=True
            except:
                self.klicked=False
                self.failmessage()


        field1=tk.Entry(root,width=letterwidth,textvariable=self.variableS1)
        field1.bind('<Return>', lambda event: checksetting(field1))
        self.canvas.create_window(posX, posY, anchor='nw', window=field1)

        field2=tk.Entry(root,width=letterwidth,textvariable=self.variableS2)
        field2.bind('<Return>', lambda event: checksetting(field2))
        self.canvas.create_window(posX, posY+20, anchor='nw', window=field2)

        field3=tk.Entry(root,width=letterwidth,textvariable=self.variableS3)
        field3.bind('<Return>', lambda event: checksetting(field3))
        self.canvas.create_window(posX, posY+80, anchor='nw', window=field3)

        field4=tk.Entry(root,width=letterwidth,textvariable=self.variableS4)
        field4.bind('<Return>', lambda event: checksetting(field4))
        self.canvas.create_window(posX, posY+100, anchor='nw', window=field4)


        field5=tk.Entry(root,width=letterwidth,textvariable=self.variableS5)
        field5.bind('<Return>', lambda event: checksetting(field5))
        self.canvas.create_window(posX, posY+280, anchor='nw', window=field5)


        field6=tk.Entry(root,width=letterwidth,textvariable=self.variableS6)
        field6.bind('<Return>', lambda event: checksetting(field6))
        self.canvas.create_window(posX, posY+140, anchor='nw', window=field6)

        field7=tk.Entry(root,width=letterwidth,textvariable=self.variableS7)
        field7.bind('<Return>', lambda event: checksetting(field7))
        self.canvas.create_window(posX, posY+160, anchor='nw', window=field7)


        #trace1_id=self.variableS1.trace('w',checksetting)
        #trace2_id=self.variableS2.trace('w',checksetting)
        #trace3_id=self.variableS3.trace('w',checksetting)
        #trace4_id=self.variableS4.trace('w',checksetting)
        #trace5_id=self.variableS5.trace('w',checksetting)










    def numbers(self,entry):
        number=float(entry.get())+1
        print(number)
        if number > 5 :
            self.quiting()
        else:
            self.failmessage()
           
    def failmessage(self,w,h,text,dh=3,dw=30):
        fail = tk.Label(root, text = text, background='red', height=dh, width=dw) 
        failwindow=self.canvas.create_window(w, h, anchor='nw', window=fail)

    def failmessage_brightness(self):
        fail = tk.Label(root, text = "Adjust Brightness first !!!", background='red', height=3, width=30) 
        self.canvas.create_window(360, 630, anchor='nw', window=fail)

    def failmessage1(self):
        fail = tk.Label(root, text = "Adjust Brightness first !!!", background='red', height=3, width=30) 
        self.canvas.create_window(360, 630, anchor='nw', window=fail)



    def next(self):
        self.canvas.delete("all")
        root.quit()


    def hello(self,*args):
        print("Single Click, Button-l")
        print(self.variable1.get()+self.variable2.get())
        print(self.variableD1.get())
        print(self.variableD2.get())

    def quiting(self):                           
        print("Double Click, so let's stop")
        self.canvas.delete("all")
        root.quit()

    def show(self):
        self.pack(fill="both", expand=True)
        root.mainloop()


    def z_raise(self,min=1):
        if self.z_state>min:
            self.z_state=self.z_state-1
        self.next()

    def z_lower(self,max=10):
        if self.z_state<max:
            self.z_state=self.z_state+1
        self.next()

    def z_zero_focus(self):
        self.klicked=True
        self.next()


    def x_right(self):
        if self.x_state<1:
            self.x_state=self.x_state+1
        self.next()

    def x_left(self):
        if self.x_state>0:
            self.x_state=self.x_state-1
        self.next()

    def y_up(self):
        if self.y_state<1:
            self.y_state=self.y_state+1
        self.next()

    def y_down(self):
        if self.y_state>0:
            self.y_state=self.y_state-1
        self.next()

    def cant_raise(self):
        if self.z_state<2:
            self.z_state=self.z_state+1
        self.klicked=False
        self.next()

    def cant_lower(self):
        if self.z_state>0:
            self.z_state=self.z_state-1
        self.klicked=False
        self.next()

    def cant_focusrequest(self):
        self.klicked=True
        fail = tk.Label(root, text = "CHOOSE A DIFFERENT DEFOCUS !!", background='red', height=3, width=30)
        self.canvas.create_window(570, 600, anchor='nw', window=fail)
        if self.z_state==1:
            self.next()

    def next_if_klicked(self):
        if self.klicked==True:
            self.next()
            self.klicked=False

    def oscillate_img(self,image1,image2,image3,posx,posy):
        self.klicked=False

        #self.variable1.set(0)

        def change_image1(*args):
            self.canvas.delete(self.window)
            label=tk.Label(root,image=image1,highlightthickness=0,borderwidth=0)
            self.window=self.canvas.create_window(posx, posy, anchor='nw',window=label)
            if self.klicked==False:
                self.after(500,lambda: change_image2())


        def change_image2(*args):
            self.canvas.delete(self.window)
            label=tk.Label(root,image=image2,highlightthickness=0,borderwidth=0)
            self.window=self.canvas.create_window(posx, posy, anchor='nw',window=label)
            if self.klicked==False:
                self.after(500,lambda: change_image3())


        def change_image3(*args):
            self.canvas.delete(self.window)
            label=tk.Label(root,image=image3,highlightthickness=0,borderwidth=0)
            self.window=self.canvas.create_window(posx, posy, anchor='nw',window=label)
            if self.klicked==False:
                self.after(500,lambda: change_image1())



            #self.window=self.canvas.create_image(posx,posy, anchor='nw', image=image2)
            #self.pack()

            
        label=tk.Label(root,image=image1,highlightthickness=0,borderwidth=0)
        self.window=self.canvas.create_window(posx, posy, anchor='nw',window=label)

        #trace1_id=self.variable1.trace('w',change)

        self.after(500,lambda: change_image2())



    def mouse_select_region(self,x1a,x1b,y1a,y1b,x2a,x2b,y2a,y2b,rectangle=True):




        def on_button_press(event):
            self.klicked=False

            # save mouse drag start position
            self.start_x = self.canvas.canvasx(event.x)
            self.start_y = self.canvas.canvasy(event.y)

            if self.start_x >x1a and self.start_x <x1b and self.start_y>y1a and self.start_y<y1b:
                self.klicked=True
            print("clicked at", self.start_x , self.start_y)

            # create rectangle if not yet exist
            if rectangle:
                if not self.rect:
                    self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline='red')
        def on_move_press(event):
            curX = self.canvas.canvasx(event.x)
            curY = self.canvas.canvasy(event.y)

            w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
            if event.x > 0.9*w:
                self.canvas.xview_scroll(1, 'units') 
            elif event.x < 0.1*w:
                self.canvas.xview_scroll(-1, 'units')
            if event.y > 0.9*h:
                self.canvas.yview_scroll(1, 'units') 
            elif event.y < 0.1*h:
                self.canvas.yview_scroll(-1, 'units')

            # expand rectangle as you drag the mouse
            if rectangle:
                self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)  


        def on_button_release(event):

            curX = self.canvas.canvasx(event.x)
            curY = self.canvas.canvasy(event.y)

            print("released at", curX, curY)
            if self.klicked==True and curX>x2a and curX<x2b and curY>y2a and curY<y2b:
                self.canvas.unbind("<ButtonPress-1>")
                self.canvas.unbind("<B1-Motion>")
                self.canvas.unbind("<ButtonRelease-1>")
                self.rect = None
                self.start_x = None
                self.start_y = None
                self.x = self.y = 0

                self.next()

  

        self.canvas.bind("<ButtonPress-1>", on_button_press)
        self.canvas.bind("<B1-Motion>", on_move_press)
        self.canvas.bind("<ButtonRelease-1>", on_button_release)
        




if __name__ == "__main__":
    root = tk.Tk()
    p=WITec_Raman(root)


#    start here
    p.frameimage("0-start-program.png")
    p.button1("b_ControlFive.png",p.next,37,432)
    p.show()
    
    p.frameimage("0-1_start-program.png")
    p.button2("b_ok1.png",p.next,403,531)
    p.show()

    p.frameimage("0-2_AFM-menues.png")
    p.button1("b_configurations.png",p.next,235,30)
    p.show()

    p.frameimage("1-0_config.png")
    p.button2("b_Raman.png",p.next,189,100)
    p.show()

    p.frameimage("1-1_config.png")
    p.button2("b_Raman-ccd1.png",p.next,399,97)
    p.show()

    p.frameimage("1-2_Raman-setting.png")
    p.lasermenu("b_select-laser.png",629,739)
    p.show()


    p.frameimage("2_before-z-up.png")
    p.button2("b_z-up.png",p.next,397,745)
    p.show()

    p.frameimage("2-1_z-up-sample-mount.png")
    p.button2("b_ok2.png",p.next,653,617)
    p.show()


    p.frameimage("2-2_z-down1.png")
    p.button2("b_z-down.png",p.next,397,795)
    p.show()

    p.frameimage("2-3_brightness-adjust.png")
    p.button3("b_y-button.png",p.next,549,154)
    p.button2("b_z-down.png",p.failmessage_brightness,397,795)
    p.show()
#
# find z focus

    imagelist=["3-1_def.png","3-2_def.png","3-3_def.png","3-4_def.png","3-5_def.png","3-6_def.png","3-7_def.png","3-8_def.png","3-9_def.png","3-10_def.png"]

    p.z_state=1
    p.klicked=False
    while (p.z_state is not 7 or p.klicked is False):
        p.klicked=False
        p.frameimage(imagelist[p.z_state-1])
        p.button3("b_z-up.png",p.z_raise,397,745)
        p.button2("b_z-down.png",p.z_lower,397,795)
        p.button4("b_autofocus.png",p.z_zero_focus,471,740)
        p.show()


    p.frameimage("4_after-auto-focus.png")
    p.button2("b_zero-focus.png",p.next,482,826)
    p.show()




# find sample region
#
    imagelist = ["4_pos4.png","4_pos1.png","4_pos3.png","4_pos2.png"]
    
    p.x_state=0
    p.y_state=1
    p.klicked=False
    while ((p.x_state is not 1 or p.y_state is not 0) or p.klicked is False):
        p.klicked=False
        p.frameimage(imagelist[2*p.x_state+p.y_state])
        p.button3("b_x-right.png",p.x_right,562,769)
        p.button2("b_x-left.png",p.x_left,511,769)
        p.button4("b_y-up.png",p.y_up,537,745)
        p.button5("b_y-down.png",p.y_down,537,795)
        p.button6("b_zero-focus.png",p.z_zero_focus,604,834)
        p.show()


    p.frameimage("5-1_objective-change.png")
    p.button2("b_A-button.png",p.next,438,243)
    p.show()

    p.frameimage("5-2_objective-change.png")
    p.button2("b_left-right-obj-change.png",p.next,258,290)
    p.show()

    p.frameimage("5-3_objective-change.png")
    p.button2("b_A-button.png",p.next,438,243)
    p.show()

    p.frameimage("5-4_objective-change.png")
    p.button2("b_A-button.png",p.next,438,243)
    p.show()

    p.frameimage("5-5_after-objective-change.png")
    p.button3("b_z-up.png",p.next,397,745)
    p.button2("b_z-down.png",lambda: p.failmessage(440,690,"!!! Always UP FIRST (narrow surface - objective distance) !!!",dh=3,dw=50),397,795)
    p.show()

    p.frameimage("6_100-obj-in-focus.png")
    p.button2("b_zero-focus.png",p.next,482,826)
    p.show()

    p.frameimage("6-1_100-obj-in-focus_zeroed.png")
    p.button2("b_I-stiching.png",p.next,806,681)
    p.show()

    p.frameimage("7-1_I-stitching.png")
    p.button2("b_I-stiching_start.png",p.next,932,1017)
    p.show()

    p.frameimage("7-2_I-stitching.png")
    p.button2("b_I-stiching_ok.png",p.next,1174,734)
    p.show()

    p.frameimage("7-3_I-stitching.png")
    p.button2("b_I-stiching_start.png",p.next,932,1017)
    p.show()

    p.frameimage("7-4_I-stitching_finished.png")
    p.button2("b_ok2.png",p.next,1035,605)
    p.show()

    p.frameimage("8-1_focus-laser_off.png")
    p.laserpower_field(0.101,0.09,6,661,788,600,700)
    p.button2("b_laser-is-off.png",p.next_if_klicked,649,810)
    p.show()

    p.frameimage("8-2_focus-laser_on.png")
    p.button2("b_illum-top.png",p.next,893,354)
    p.show()

    p.frameimage("8-3-0_focus-laser_ill-off.png")
    p.button2("b_illum-setting.png",p.next,893,324)
    p.show()

    p.frameimage("8-3-1_focus-laser_ill-menu.png")
    p.brightness_unset(1170,563,1170,743)
    p.show()

 #find z focus on laser

    imagelist=["8-4_focus-laser_1.png","8-4_focus-laser_2.png","8-4_focus-laser_3.png"]

    p.klicked=False
    p.z_state=1
    while (p.z_state is not 2 or p.klicked is False):
        p.klicked=False
        p.frameimage(imagelist[p.z_state-1])
        p.button3("b_z-up.png",lambda: p.z_raise(min=1),397,1085)
        p.button2("b_z-down.png",lambda: p.z_lower(max=3),397,1135)
        p.button4("b_zero-focus.png",p.z_zero_focus,482,1166 )
        p.show()

    p.frameimage("8-4_focus-laser_focus-zeroed.png")
    p.button2("b_laser-is-on.png",p.next,648,1150)
    p.show()

    p.frameimage("8-5_focus-laser_off2.png")
    p.button2("b_ok2.png",p.next,677,937)
    p.show()

    p.frameimage("9_before-spectograph-1.png")
    p.button2("b_spectrograph.png",p.next,6,273)
    p.show()

    p.frameimage("10_spectograph-1.png")
    p.button2("b_oscill-menu.png",p.next,6,511)
    p.show()

    p.frameimage("11_oszi-menu.png")
    p.laserpower_field(2.001,1.701,6,654,956,590,875)
    p.button2("b_osci-start.png",p.next_if_klicked,212,512)
    p.show()


# oszillating spectrum

    path = p.parent / "b_osci-spec1.png"
    screen1 = ImageTk.PhotoImage(Image.open(path))
    path = p.parent / "b_osci-spec2.png"
    screen2=ImageTk.PhotoImage(Image.open(path))
    path = p.parent / "b_osci-spec3.png"
    screen3=ImageTk.PhotoImage(Image.open(path))

    p.frameimage("12_oszi-start.png")
    p.button2("b_osci-stop.png",p.z_zero_focus,212,532)
    p.oscillate_img(screen1,screen2,screen3,407, 473)
    p.show()

    p.frameimage("13_oszi-stop2.png")
    p.button2("b_osci-int-time.png",p.next,211,551)
    p.show()

    p.frameimage("13_oszi-stop2.png")
    p.laserpower_field(1.001,0.499,10,211,551,100,575)
    p.button2("b_osci-start.png",p.next_if_klicked,212,512)
    p.show()

    p.frameimage("14_osci_0-5s.png")
    p.button6("b_spec-osci-0-5s.png",p.next,407,473,bindbutton='<Button-3>')
    p.show()

    p.frameimage("14-1_osci_zoom1.png")
    p.button2("b_spec-zoom1.png",p.next,657,665)
    p.show()

    p.frameimage("14-2_osci_zoom2.png")
    p.button2("b_spec-zoom2.png",p.next,838,833)
    p.show()

    p.frameimage("14-2_osci_zoom2.png")
    p.mouse_select_region(504,504+33,575,575+193,540,540+65,491,491+49)
    p.show()


    imagelist=["14-3_osci_focus1.png","14-3_osci_focus2.png","14-3_osci_focus3.png"]

    p.klicked=False
    p.z_state=1
    while (p.z_state is not 2 or p.klicked is False):
        p.klicked=False
        p.frameimage(imagelist[p.z_state-1])
        p.button3("b_z-up.png",lambda: p.z_raise(min=1),397,912)
        p.button2("b_z-down.png",lambda: p.z_lower(max=3),397,962)
        p.button4("b_spec-rescale.png",p.z_zero_focus,875,797 )
        p.show()

    p.frameimage("15_spec-max-Si.png")
    p.button2("b_osci-stop.png",p.next,212,532)
    p.show()

    p.frameimage("15-1_spec-max-Si_stoped.png")
    p.button2("b_scan-table.png",p.next,6,191)
    p.show()

    p.frameimage("16_scan-table.png")
    p.button2("b_scan-table_never.png",p.next,211,211)
    p.show()

    p.frameimage("16-1_scan-table_select.png")
    p.button2("b_scan-table_once.png",p.next,211,244)
    p.show()

    p.frameimage("16-2_scan-table_once.png")
    p.setprobescreen("label_video-stitch-small.png","b_area1_1layer-small.png",320,350,1142-930,282-105,930,105)
    p.show()

    p.frameimage("16-3_scan-table_new-pos-never.png")
    p.button2("b_osci-start.png",p.next,212,612)
    p.show()

    p.frameimage("17_osci-spec-graphene1.png")
    p.button2("b_osci-stop.png",p.next,212,632)
    p.show()

    p.frameimage("17-1_osci-spec-graphene1-stop.png")
    p.button2("b_grating-1.png",p.next,211,391)
    p.show()

    p.frameimage("18-1_osci-grating1.png")
    p.button2("b_grating-2.png",p.next,211,437)
    p.show()

    p.frameimage("18-2_osci-grating2.png")
    p.button2("b_osci-start.png",p.next,212,612)
    p.show()

    p.frameimage("18-3_osci-graphene2.png")
    p.button2("b_osci-stop.png",p.next,212,632)
    p.show()


    p.frameimage("18-4_osci-graphene2-stoped.png")
    p.laserpower_field(5.001,4.701,6,654,956,590,875)
    p.button2("b_osci-start.png",p.next_if_klicked,212,612)
    p.show()

    p.frameimage("19-1_osci-graphene5watt.png")
    p.button2("b_ok2.png",p.next,453,930)
    p.show()

    p.frameimage("19-2_osci-graphene5watt_stopped.png")
    p.button2("b_single_spec.png",p.next,5,750)
    p.show()

    p.frameimage("19-3_single-aquis.png")
    p.laserpower_field(10.001,8.001,6,213,833,150,760)
    p.button2("b_aqu-spectra.png",p.next_if_klicked,211,771)
    p.show()

    p.frameimage("21_cosmic-ray.png")
    p.button2("b_aqu-spectra.png",p.next,211,771)
    p.show()

    p.frameimage("20_accum-aquis.png")
    p.button2("b_ok2.png",p.next,705,405)
    p.show()

    # Measure on graphene flake , the 4 different layers

    p.frameimage("22_graphene-flake-position.png")
    p.scantablemenu("b_scan-table_never.png",211,211)
    p.show()

    p.frameimage("22_graphene-flake-position.png")
    p.setprobescreen("label_video-stitch-big.png","b_flake_1layer.png",518,547,607-403,606-354,403,354)
    p.show()
    
    # loop through positions
    
    numbers=[0,1,2,3]
    positions=np.array([[595-403,479-354],[620-403,497-354],[636-403,548-354]])
    for i in numbers:
        
        p.frameimage("".join((str(23+i),"_graphene-flake-position",str(1+i),"-spectrum.png")))
        p.label_image1("".join(("label_graphene-flake-position",str(1+i-1),"-spectrum.png")),704,464)
        p.button2("b_aqu-spectra.png",p.next,211,771)
        p.show()

        p.frameimage("".join((str(23+i),"-1_graphene-flake-position",str(1+i),"-spectrum.png")))
        p.label_image1("".join(("label_graphene-flake-position",str(1+i),"-spectrum.png")),704,464)
        p.button2("".join(("b_graphene-flake-position",str(1+i),"-manager.png")),p.next,927,161+i*39)
        p.show()

        p.frameimage("".join((str(23+i),"-2_graphene-flake-position",str(1+i),"-spectrum.png")))
        p.label_image1("".join(("label_graphene-flake-position",str(1+i),"-spectrum.png")),704,464)
        p.mouse_select_region(927,927+316,160+i*39,160+24+i*39,407,407+545,358,358+542, rectangle=False)
        p.show()

        p.frameimage("".join((str(23+i),"-2_graphene-flake-position",str(1+i),"-spectrum.png")))
        p.label_image1("".join(("label_graphene-flake-position",str(1+i),"-spectrum.png")),704,464)
        p.button2("b_show-position.png",p.next,450,477)
        p.show()

        if i < 3:

            p.frameimage("".join((str(23+i),"-3_graphene-flake-position",str(1+i),"-spectrum.png")))
            p.label_image1("".join(("label_graphene-flake-position",str(1+i),"-spectrum.png")),704,464)
            p.scantablemenu("b_scan-table_never.png",211,211)
            p.show()

            p.frameimage("".join((str(23+i),"-3_graphene-flake-position",str(1+i),"-spectrum.png")))
            p.setprobescreen("label_video-stitch-big.png","".join(("b_flake_",str(2+i),"layer.png")),518,547,positions[i,0],positions[i,1],403,354)
            p.label_image1("".join(("label_graphene-flake-position",str(1+i),"-spectrum.png")),704,464)
            p.show()
    
  
    p.frameimage("27_manager-all-spectra.png")
    p.label_image1("label_graphene-flake-position4-spectrum.png",704,464)
    p.button2("b_file.png",p.next,3,22)
    p.show()

    p.frameimage("28_save-project_1.png")
    p.label_image1("label_graphene-flake-position4-spectrum.png",704,464)
    p.button2("b_save-as.png",p.next,5,134)
    p.show()

    p.frameimage("29_save-project_2.png")
    p.label_image1("label_graphene-flake-position4-spectrum.png",704,464)
    p.button2("b_save.png",p.next,332,573)
    p.show()

    p.frameimage("30_export_1.png")
    p.button2("b_name-index.png",p.next,927,26)
    p.show()

    p.frameimage("31_export_2.png")
    p.button2("b_ok2.png",p.next,707,186)
    p.show()

    p.frameimage("32_export_3.png")
    p.button6("b_spectra-right-click.png",p.next,927,66,bindbutton='<Button-3>')
    p.show()

    p.frameimage("33_export_4.png")
    p.button2("b_Export.png",p.next,759,143)
    p.show()

    p.frameimage("34_export_5.png")
    p.button2("b_Table.png",p.next,997,202)
    p.show()

    p.frameimage("35_export_6.png")
    p.button2("b_ok1.png",p.next,910,488)
    p.show()

    p.frameimage("36_close-message.png")
    p.button2("b_ok2.png",p.next,688,653)
    p.show()


