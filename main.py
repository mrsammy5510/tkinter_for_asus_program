import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk, ImageSequence
import time
import math 
global mem_coe
global brower_home_bg
global video_home_bg

root = tk.Tk()
monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

img = Image.open("./image\\background.png")
img = img.resize((monitor_width,monitor_height), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(img)
brower_home_bg = tk.PhotoImage(file = "./image\\brower_home.png")
video_home_bg = tk.PhotoImage(file = "./image\\video_home.png")






'''height_scale = monitor_height/1080


bg = bg.zoom(int(height_scale))
bg = bg.subsample(int(height_scale))'''

canvas1 = tk.Canvas( root, width = monitor_width, height = monitor_height)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg, anchor = "nw")      #nw代表前面的座標是左上角的點
canvas1.pack()
windows_num = 0


mem_spec = {0: 0.3,1: 0.15, 2: 0.08, 3: 0.02}      #From worst to best
cpu_spec = {0: 0.16487,1: 0.10758, 2: 0.0534, 3: 0.002}


root.title('Computer spec test')
root.resizable(width=True, height=True)
root.state('zoomed')        #啟動時最大化
root.minsize(480, 270)      #最小是470X270


#Displaying the memory selecting combo box
mem_select = ttk.Combobox(root,value=["DDR3 8G","DDR4 8G","DDR3 16G","DDR4 16G"])
mem_select.current(0)
#mem_select_canvas = canvas1.create_window(1700, 780,anchor = "nw",window = mem_select)
mem_select_canvas = canvas1.create_window(monitor_width-220, monitor_height-300,anchor = "nw",window = mem_select)

#Displaying the CPU selecting combo box
cpu_select = ttk.Combobox(root,value=["i3-12100","i5-12500","i7-12700","i9-12900"])
cpu_select.current(0)
#cpu_select_canvas = canvas1.create_window(1700, 880,anchor = "nw",window = cpu_select)
cpu_select_canvas = canvas1.create_window(monitor_width-220, monitor_height-200,anchor = "nw",window = cpu_select)

#Label to point out the RAM menu position
#memory_label_canvas = canvas1.create_text(1750, 730,anchor = "nw",text = "RAM", font=('Arial', 18), fill = 'white')
memory_label_canvas = canvas1.create_text(monitor_width-170, monitor_height-350,anchor = "nw",text = "RAM", font=('Arial', 18), fill = 'white')

#Label to point out the CPU menu position
#cpuLabelCanvas = canvas1.create_text(1750, 830,anchor = "nw",text = "CPU", font=('Arial', 18), fill = 'white')
cpuLabelCanvas = canvas1.create_text(monitor_width-170, monitor_height-250,anchor = "nw",text = "CPU", font=('Arial', 18), fill = 'white')





def explorer_click(event):
    global windows_num
    
    which_mem = mem_select.current()        #抓現在選到哪個RAM
    mem_coe = mem_spec.get(which_mem,0)     #用字典根據選到哪一個RAM 指派對應的coe給它
    which_cpu = cpu_select.current()
    cpu_coe = cpu_spec.get(which_cpu,0)

    #用來顯示loading的GIF##############
    loading_gif = Image.open('./image\\loading.gif')
    # GIF图片流的迭代器
    iter = ImageSequence.Iterator(loading_gif)
    #frame就是gif的每一帧，转换一下格式就能显示了
    for frame in iter:
        frame = frame.resize((50,50))       #resize會回傳一個新的圖片而非直接更改
        pic = ImageTk.PhotoImage(frame)
        canvas1.create_image(monitor_width/2,monitor_height/2, image=pic)
        time.sleep(0.005)        #the loading gif have 29 frames
        root.update_idletasks()  #刷新
        root.update()
    #用來顯示loading的GIF################
      
    time.sleep((1-math.exp(-(windows_num*mem_coe))) + (1-math.exp(-(cpu_coe))))     #時間計算公式
    print("first coe: ",(1-math.exp(-(windows_num*mem_coe))),"\n")
    print("second coe: ",(1-math.exp(-(cpu_coe))),"\n")
    windows_num = windows_num + 1
    second = tk.Toplevel()
    second.title("Internet brower")
    second.geometry("640x360")
    canvas_brower = tk.Canvas(second, width = monitor_width, height = monitor_height)
    canvas_brower.pack(fill = "both", expand = True)
    canvas_brower.create_image( 0, 0, image = brower_home_bg, anchor = "nw")      #nw代表前面的座標是左上角的點
    canvas_brower.pack()
    
def mp4_click(event):

    which_mem = mem_select.current()        #抓現在選到哪個RAM
    mem_coe = mem_spec.get(which_mem,0)     #用字典根據選到哪一個RAM 指派對應的coe給它
    which_cpu = cpu_select.current()
    cpu_coe = cpu_spec.get(which_cpu,0)

    #create window
    third = tk.Toplevel()
    third.title("Exporting video")
    third.geometry("640x360+%d+%d" %(monitor_width/2-320,monitor_height/2-180))   #640X360 is the size, 640+360 is the position
    #The progress bar
    canvas_video = tk.Canvas(third, width = 640, height = 360)
    video_trans = ttk.Progressbar(third,length=320)
    video_trans.pack(pady=20)
    canvas_video.create_window(160, 302, anchor='nw', window = video_trans)

    #Set the background for the video window
    canvas_video.pack(fill = "both", expand = True)
    canvas_video.create_image( 0, 0, image = video_home_bg, anchor = "nw")      #nw代表前面的座標是左上角的點'''
    canvas_video.pack()

    val = 0
    
    #Updating the progress bar
    for i in range(101):
        video_trans['value'] = i
        third.update()
        timer = 0.01*(math.log(cpu_coe*500+mem_coe*100)+1)
        time.sleep(timer)
        
        
    #Show the total time consuming
    val = timer*101
    val = round(val,2)
    canvas_video.create_text(226, 250,anchor = "nw",text = "共花了", font=('Arial', 18), fill = 'black')
    canvas_video.create_text(300, 250,anchor = "nw",text = val, font=('Arial', 18), fill = 'black')
    canvas_video.create_text(350, 250,anchor = "nw",text = "秒", font=('Arial', 18), fill = 'black')
    
    
    
    


    
    
    
    
    

#Displaying the explorer icon
explorerIcon = Image.open('./image\\edge.png')
explorerIcon.thumbnail((50,50))
explorer_image = ImageTk.PhotoImage(explorerIcon)
explorer = canvas1.create_image(50, 50, image = explorer_image)
canvas1.tag_bind(explorer, "<Button-1>", explorer_click)

#Displaying mp4 transistor icon
mp4Icon = Image.open('./image\\mp4.png')
mp4Icon.thumbnail((50,50))
mp4_image = ImageTk.PhotoImage(mp4Icon)
mp4 = canvas1.create_image(50, 130, image = mp4_image)
canvas1.tag_bind(mp4, "<Button-1>", mp4_click)






root.mainloop()
