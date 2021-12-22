import tkinter
import time
from math import *
 
Soap_width = 500
Soap_height = 200
Window_Width=1000
Window_Height=700
Refresh_Sec = 0.01
show = 0

def create_animation_window():
  Window = tkinter.Tk()
  Window.title("Soap")
  Window.geometry(f'{Window_Width}x{Window_Height}')
  return Window

def create_animation_canvas(Window):
  canvas = tkinter.Canvas(Window)
  canvas.configure(bg="White")
  canvas.pack(fill="both", expand=True)
  return canvas

def length(x1,y1,x2,y2):
  return sqrt(pow(x1-x2,2)+pow(y1-y2,2))

def get_ans(Window, canvas, final_angle, offset_x, offset_y, mini_offset):
  Window.update()
  canvas.delete("all")
  canvas.create_rectangle(250,250,250+Soap_width,250+Soap_height)
  x = -500-1000*sin(radians(90-final_angle))
  y = -500+1000*cos(radians(90-final_angle))
  l = 0.0
  for i in range(30):
    x_start = x+offset_x+mini_offset/10
    y_start = y+500+offset_y+mini_offset/10
    x_end = x+9000*tan(radians(final_angle))+offset_x+mini_offset/10
    y_end = y+6000*tan(radians(90-final_angle))+500+offset_y+mini_offset/10
    if x_end-x_start == 0: m = float('inf')
    else: m = (y_end-y_start)/(x_end-x_start)
    
    if m == 0:
      urh = float('inf')
      lrh = float('inf')
    else:
      urh = (250+Soap_height-y_start)/m+x_start
      lrh = (250-y_start)/m+x_start
    urv = m*(250+Soap_width-x_start)+y_start
    lrv = m*(250-x_start)+y_start
    
    if urh > 250 and urh < 250+Soap_width and lrh > 250 and lrh < 250+Soap_width:
      canvas.create_line(x_start,y_start,x_end,y_end, fill='green')
    elif urh > 250+Soap_width and lrh < 250:
      canvas.create_line(x_start,y_start,x_end,y_end, fill='blue')
    elif urh > 250 and lrh < 250 and urh < 250+Soap_width:
      canvas.create_line(x_start,y_start,x_end,y_end, fill='red')
    elif urh > 250+Soap_width and lrh > 250 and lrh < 250+Soap_width:
      canvas.create_line(x_start,y_start,x_end,y_end, fill='red')
    else: canvas.create_line(x_start,y_start,x_end,y_end)
    x+=100*sin(radians(90-final_angle))
    y-=100*cos(radians(90-final_angle))

def animate_ball(Window, canvas):
  ma = 0.0
  for mini_offset in range(1):
    for offset_x in range(1):
      for offset_y in range(10,100):
        for i in range(8774000,8775000):
          angle = i/100000
          if show:
            Window.update()
            canvas.delete("all")
            canvas.create_rectangle(250,250,250+Soap_width,250+Soap_height)
          x = -500-1000*sin(radians(90-angle))
          y = -500+1000*cos(radians(90-angle))
          l = 0.0
          for i in range(30):
            x_start = x+offset_x+mini_offset/10
            y_start = y+500+offset_y+mini_offset/10
            x_end = x+9000*tan(radians(angle))+offset_x+mini_offset/10
            y_end = y+6000*tan(radians(90-angle))+500+offset_y+mini_offset/10
            if x_end-x_start == 0: m = float('inf')
            else: m = (y_end-y_start)/(x_end-x_start)
            
            if m == 0:
              urh = float('inf')
              lrh = float('inf')
            else:
              urh = (250+Soap_height-y_start)/m+x_start
              lrh = (250-y_start)/m+x_start
            urv = m*(250+Soap_width-x_start)+y_start
            lrv = m*(250-x_start)+y_start
            
            if urh > 250 and urh < 250+Soap_width and lrh > 250 and lrh < 250+Soap_width:
              if show: canvas.create_line(x_start,y_start,x_end,y_end, fill='green')
              l+=length(urh,250+Soap_height,lrh,250)
            elif urh > 250+Soap_width and lrh < 250:
              if show: canvas.create_line(x_start,y_start,x_end,y_end, fill='blue')
              l+=length(250,lrv,250+Soap_width,urv)
            elif urh > 250 and lrh < 250 and urh < 250+Soap_width:
              if show: canvas.create_line(x_start,y_start,x_end,y_end, fill='red')
              l+=length(urh,250+Soap_height,250,lrv)
            elif urh > 250+Soap_width and lrh > 250 and lrh < 250+Soap_width:
              if show: canvas.create_line(x_start,y_start,x_end,y_end, fill='red')
              l+=length(250+Soap_width,urv,lrh,250)
            else: 
              if show: canvas.create_line(x_start,y_start,x_end,y_end)
            x+=100*sin(radians(90-angle))
            y-=100*cos(radians(90-angle))
          if ma < l:
            ma = l
            final_angle = angle
            final_offset_x = offset_x
            final_offset_y = offset_y
            final_mini_offset = mini_offset
          #print(l)
          #if l == 1095.9056552108316:
          #  time.sleep(1000)
          #time.sleep(Refresh_Sec)
        print(ma)
  print("%.2f cm  Angle: %.4f"%(ma/100, final_angle))
  get_ans(Window, canvas, final_angle, final_offset_x, final_offset_y, final_mini_offset)
  s = input()

Animation_Window = create_animation_window()
Animation_canvas = create_animation_canvas(Animation_Window)
animate_ball(Animation_Window,Animation_canvas)