import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk, ImageSequence
import time
import math 

root = tk.Tk()
bg = tk.PhotoImage(file = "background.png")
global brower_home_bg
brower_home_bg = tk.PhotoImage(file = "brower_home.png")


monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

canvas1 = tk.Canvas( root, width = monitor_width, height = monitor_height)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg, anchor = "nw")      #nw代表前面的座標是左上角的點
canvas1.pack()
windows_num = 0
global mem_coe
mem_coe = 0.002
mem_spec = {0: 0.002,1: 0.003, 2: 0.004, 3: 0.005}
1

root.title('Computer spec test')
root.resizable(width=True, height=True)
root.state('zoomed')        #啟動時最大化
root.minsize(480, 270)      #最小是470X270


def explorer_click(event):
    global windows_num
    
    which_mem = mem_select.current()        #抓現在選到哪個RAM
    mem_coe = mem_spec.get(which_mem,0)     #用字典根據選到哪一個RAM 指派對應的coe給它

    #用來顯示loading的GIF##############
    loading_gif = Image.open('loading.gif')
    # GIF图片流的迭代器
    iter = ImageSequence.Iterator(loading_gif)
    #frame就是gif的每一帧，转换一下格式就能显示了
    for frame in iter:
        frame = frame.resize((50,50))       #resize會回傳一個新的圖片而非直接更改
        pic = ImageTk.PhotoImage(frame)
        gif = canvas1.create_image(monitor_width/2,monitor_height/2, image=pic)
        canvas1.tag_bind(gif,"<Button-2>", explorer_click)
        time.sleep(0.01)        #the loading gif have 29 frames
        root.update_idletasks()  #刷新
        root.update()
    #用來顯示loading的GIF################
      
    time.sleep(20*(1-math.exp(-(windows_num*mem_coe))))     #時間計算公式
    windows_num = windows_num + 1
    second = tk.Toplevel()
    second.title("Internet brower")
    second.geometry("640x360")
    canvas_brower = tk.Canvas( second, width = monitor_width, height = monitor_height)
    canvas_brower.pack(fill = "both", expand = True)
    canvas_brower.create_image( 0, 0, image = brower_home_bg, anchor = "nw")      #nw代表前面的座標是左上角的點
    canvas_brower.pack()
    
    
    
photo = Image.open('edge.png')
photo.thumbnail((50,50))
explorer_image = ImageTk.PhotoImage(photo)
explorer = canvas1.create_image(50, 50, image = explorer_image)
canvas1.tag_bind(explorer, "<Button-1>", explorer_click)

mem_select = ttk.Combobox(root,value=["DDR4 16G","DDR4 8G","DDR3 16G","DDR3 8G"])
mem_select.current(0)
combo_canvas = canvas1.create_window(1700, 780,anchor = "nw",window = mem_select)

memory_label_canvas = canvas1.create_text(1750, 730,anchor = "nw",text = "RAM", font=('Arial', 18), fill = 'white')


root.mainloop()
