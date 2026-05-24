##############################################################################################################################
#                                                                                                                            #
#   Youtube Video Downloader                                                                                                 #
#   This project is a translation of https://github.com/Tomshiii/ahk/blob/main/Streamdeck%20AHK/download/mult-dl.ahk         #
#   to work more broadly across different operating systems (namely Linux as I transitioned to it)                           #
#                                                                                                                            #
##############################################################################################################################

import tkinter as tk
from tkinter import ttk
from tkinter import ttk, filedialog
import subprocess

#Creating the window for the application
root = tk.Tk()
root.geometry("400x400")
icon = tk.PhotoImage(file="/home/sam/Projects/ytdownloader/ytdownloader.png")
root.iconphoto(True, icon)
root.title("Youtube Downloader")
root.resizable(False, False)

#Changes destination directory to download, called by a button
def change_directory():
    global download_folder
    filepath = filedialog.askdirectory(initialdir=download_folder)
    if filepath:
        download_folder = filepath
        folder_label.config(text=f"Download Folder: {filepath}")

download_folder = "~/Downloads"
folder_label = ttk.Label(root, text=f"Download Folder: {download_folder}")
folder_label.grid(row=0, column=0, padx=5, pady=20)

folder_select = ttk.Button(root, text="Select Folder", command=change_directory)
folder_select.grid(row=0, column=1, padx=5, pady=5)

#Creating a list of tabs
tabs = ttk.Notebook(root)
tabs.grid(row=1, column=0, columnspan=2, sticky="nsew")
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

#Creates frames inside the window that can be tabs to choose from
single_tab = ttk.Frame(tabs, width=400, height=300)
playlist_tab = ttk.Frame(tabs, width=400, height=300)

#Single tab
single_tab.pack(fill='both', expand=1)

url = ttk.Label(single_tab, text="URL:")
url.grid(row=0, column=0, padx=5, pady=5, sticky="e")
url_entry = ttk.Entry(single_tab, width=25)
url_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

file_name = ttk.Label(single_tab, text="Filename:")
file_name.grid(row=1, column=0, padx=5, pady=5, sticky="e")
file_name_entry = ttk.Entry(single_tab, width=25)
file_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

format_var = tk.StringVar(value="mp3")
format_dropdown = ttk.Combobox(single_tab, textvariable=format_var, values=["mp3", "wav", "flac", "aac"], state="readonly", width=5)
format_dropdown.grid(row=4, column=2, padx=5, pady=5)

playlist_var = tk.BooleanVar()
playlist_toggle = ttk.Checkbutton(single_tab, text="Playlist", variable=playlist_var)
playlist_toggle.grid(row=2, column=1, padx=5, pady=5)

cookies_var = tk.BooleanVar()
cookies_toggle = ttk.Checkbutton(single_tab, text="Cookies", variable=cookies_var)
cookies_toggle.grid(row=3, column=1, padx=5, pady=5)

#Downloads audio based on the toggles and the type of audio file selected
def download_audio():
    input_url = url_entry.get()
    if input_url == "":
        return
    audio_format = format_var.get()
    command = ["yt-dlp", "-x", "--audio-format", audio_format, input_url]
    subprocess.run(command)

audiodl_button = ttk.Button(single_tab, text="Download Audio", command=download_audio)
audiodl_button.grid(row=4, column=1, padx=5, pady=5)

videodl_button = ttk.Button(single_tab, text="Download Video")
videodl_button.grid(row=5, column=1, padx=5, pady=5)

#Playlist tab
playlist_tab.pack(fill='both', expand=1)


#Adding the frames the tabs to the window
tabs.add(single_tab, text='Single')
tabs.add(playlist_tab, text='Playlist')


root.mainloop()