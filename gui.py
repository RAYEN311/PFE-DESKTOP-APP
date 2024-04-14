import time
import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from PIL import Image, ImageTk
import cv2

#followed by __INIT__.PY CODE

def exit_fullscreen(root):
    root.attributes('-fullscreen', False)
    root.geometry("800x700")  # Adjust as needed
    center_window(root)

def center_window(window):
  """Centers the window on the screen."""
  window.update_idletasks()
  width = window.winfo_width()
  height = window.winfo_height()
  x = (window.winfo_screenwidth() // 2) - (width // 2)
  y = (window.winfo_screenheight() // 2) - (height // 2)
  window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


it = 0  

def change_width():
    global it  
    it += 1
    label_progress.place(relx=0.5, rely= 0.84 , anchor=tk.CENTER , height=5 , width= int(620 / 100 * it))
    progresstxt.config(text=str(int(it / 1.02)) + ' %')
    print(it)
    print(int(620 / 10000 * it))
    if(int(620 / 100 * it) < 630):
       main_frame.after(400, change_width)
    else:
       print('MID PCB READY')


root = tk.Tk()
s = ttk.Style()
# Custom theme with flat design elements and accessibility considerations
s.configure('custom.TFrame', background='#f5f5f5')  # Light gray background
s.configure('custom.TButton',
                        font=('Arial', 12, 'bold'),
              foreground='#3498db',  # Primary blue color
              borderwidth=1,
              bordercolor='#cccccc',  # Light gray border
              relief='flat',
              cursor='hand2'
              )
s.configure('custom.TLabel',
              font=('Arial', 12),
              foreground='#333333',  # Darker gray text for good contrast
              background='#f5f5f5'  # Inherit background color
              )
s.configure('TRounded.TLabel'
              )

root.title("Home Page")
root.attributes('-fullscreen', True)  # Fullscreen

  # Main frame
main_frame = ttk.Frame(root, style='custom.TFrame')
main_frame.pack(fill=tk.BOTH, expand=True)



bg_image = ttk.Label(main_frame)
bg_image = Image.open("background_image.jpg")
bg_image_resized = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image_resized)
bg_label = ttk.Label(main_frame, image=bg_photo)
bg_label.place(x=-1, y=-1, relwidth=1, relheight=1)


  # Exit fullscreen button with hover effect
exit_button_img = PhotoImage(file="exit_button.png", height=20, width=20)
exit_button = ttk.Button(
    main_frame,
      image=exit_button_img,
      command=lambda: exit_fullscreen(root),
      style='custom.TButton',
      cursor="hand2"
  )
exit_button.place(x=root.winfo_screenwidth() - 60, y=20)


logo_image = Image.open("logo.png")
logo_image_resized = logo_image.resize((800, 635), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image_resized)

logo_label = ttk.Label(main_frame, image=logo_photo, style='custom.TLabel')
logo_label.place(relx=0.5, rely=0.47, anchor=tk.CENTER )

logo_label.lift()

label_wait = ttk.Label(main_frame,background="#ffffff")
label_wait.place(relx=0.5, rely= 0.84 , anchor=tk.CENTER , height=7 , width= 640)


progresstxt = ttk.Label(main_frame, text= '0 %' ,foreground= "#5fffff" , background= "#21212e" , font=('Arial', 14))

progresstxt.place(relx=0.5, rely= 0.81 , anchor=tk.CENTER , height=28 , width= 60 )


label_progress = ttk.Label(main_frame,background="#0000ff")

label_progress.place(relx=0.5005, rely= 0.84 , anchor=tk.CENTER , height=5 , width= 0 )

change_width()

root.mainloop()
    


   

 



 
























# def run_soft():
    

# # Change directory to 'main_object'
#    os.chdir('main_object')

# # Run the __init__.py script
#    runpy.run_path("__init__.py") 





    # # Video player
    # video_path = "slide.mp4"  # Replace with your video file path
    # cap = cv2.VideoCapture(video_path)

    # def play_video():
    #     ret, frame = cap.read()
    #     if ret:
    #         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #         frame = Image.fromarray(frame)
    #         frame = ImageTk.PhotoImage(frame , height= 40 , width= 100 )
    #         video_label.config(image=frame)
    #         video_label.image = frame
    #         video_label.after(10, play_video)  # Update every 10 milliseconds for smooth playback
    #     else:
    #         cap.release()

    # video_label = tk.Label(root)
    # video_label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    # play_video()
  

# #   root.wm_attributes('-transparentcolor','#add123')
#   b = RoundedLabel(root, 700, 550 , cornerradius = 20 , padding= 1 , color="#000000" , bg="#4444aa")
#   b.place(relx=0.5, rely=0.5, anchor=tk.CENTER )
# class RoundedLabel(tk.Canvas):
#     def __init__(self, parent, width, height, cornerradius, padding, bg , color, command=None):
#         tk.Canvas.__init__(self, parent, borderwidth=0, bg=bg ,
#             relief="flat", highlightthickness=0)
#         self.command = command

#         if cornerradius > 0.5*width:
#             print("Error: cornerradius is greater than width.")
#             return None

#         if cornerradius > 0.5*height:
#             print("Error: cornerradius is greater than height.")
#             return None

#         rad = 2*cornerradius
#         def shape():
#             self.create_polygon((padding,height-cornerradius-padding,padding,cornerradius+padding,padding+cornerradius,padding,width-padding-cornerradius,padding,width-padding,cornerradius+padding,width-padding,height-cornerradius-padding,width-padding-cornerradius,height-padding,padding+cornerradius,height-padding), fill=color, outline=color)
#             self.create_arc((padding,padding+rad,padding+rad,padding), start=90, extent=90, fill=color, outline=color)
#             self.create_arc((width-padding-rad,padding,width-padding,padding+rad), start=0, extent=90, fill=color, outline=color)
#             self.create_arc((width-padding,height-rad-padding,width-padding-rad,height-padding), start=270, extent=90, fill=color, outline=color)
#             self.create_arc((padding,height-padding-rad,padding+rad,height-padding), start=180, extent=90, fill=color, outline=color)


#         id = shape()
#         (x0,y0,x1,y1)  = self.bbox("all")
#         width = (x1-x0)
#         height = (y1-y0)
#         self.configure(width=width, height=height)
#         self.bind("<ButtonPress-1>", self._on_press)
#         self.bind("<ButtonRelease-1>", self._on_release)

#     def _on_press(self, event):
#         self.configure(relief="sunken")

#     def _on_release(self, event):
#         self.configure(relief="raised")
#         if self.command is not None:
#             self.command()

# # button = RoundedButton(root, 200, 100, 50, 2, 'red', 'white', command=test)
# # button.place(relx=.1, rely=.1)