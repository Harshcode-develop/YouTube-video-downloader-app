import stat
from turtle import down
import customtkinter as ctk
import tkinter as ttk
from pydantic_core import Url
from pytube import YouTube
import os
from regex import E


def download_video():

    url=entry_url.get()
    res=res_var.get()
    progress_label.pack(pady=10)
    progress_bar.pack(pady=10)
    s_label.pack(pady=10)

    try:
        yt=YouTube(url, on_progress_callback=progress_function)
        stream=yt.streams.filter(res=res).first()
        stream.download()

    except Exception as e:
        s_label.config(text=f"Error{str(e)}", text_color="white", fg_color="red")


def progress_function(stream, chunk, bytes_remaining):
    size=stream.filesize
    progress=(1-bytes_remaining/size)*100
    progress_label.configure(text=str(int(progress))+"%")
    progress_label.update()
    progress_bar.set(float(progress/100))
         
    
#root window
root = ctk.CTk()
root.title('YouTube-Video-Downloader')

#window size
root.geometry("8000x500")
root.minsize(800, 500)
root.maxsize(1000, 780)


#frame content
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

#label
Url_label = ctk.CTkLabel(content_frame, text="Enter the YouTube URL of the video:", font=('Arial', 20))
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
Url_label.pack(pady=10)
entry_url.pack(pady=10)

#download button
d_button= ctk.CTkButton(content_frame, text="Download", command=download_video)
d_button.pack(pady=10)

#res combo box
res=["1080p","720p", "480p", "360p"]
res_var=ctk.StringVar()
res_combobox=ctk.CTkComboBox(content_frame, values=res)
res_combobox.pack(pady=10)
res_combobox.set("Select resolution")

#progress bar
progress_label=ctk.CTkLabel(content_frame, text="0%")
progress_bar=ctk.CTkProgressBar(content_frame, width=600)
progress_bar.set(0)

#status
s_label=ctk.CTkLabel(content_frame, text="")

#run app
root.mainloop()
