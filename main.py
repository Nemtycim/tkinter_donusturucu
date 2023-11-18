import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip
from PIL import Image,ImageSequence

class FileConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("File Converter")

        # Dosya adı için etiket
        self.file_label = tk.Label(master, text="Dosya Seçilmedi!")
        self.file_label.pack()

        # Dosya seç butonu
        self.select_button = tk.Button(master, text="Dosya Seç!", command=self.select_file)
        self.select_button.pack(pady=10)

        # Radio düğmelerini oluştur
        self.operation_var = tk.StringVar()
        self.mp4_to_mp3_radio = tk.Radiobutton(master, text="MP4 --> MP3", variable=self.operation_var, value="mp4_to_mp3")
        self.mp4_to_mp3_radio.pack()

        self.png_to_jpeg_radio = tk.Radiobutton(master, text="PNG --> JPEG", variable=self.operation_var, value="png_to_jpeg")
        self.png_to_jpeg_radio.pack()

        self.gif_to_png_radio = tk.Radiobutton(master, text="GIF --> PNG", variable=self.operation_var, value="gif_to_png")
        self.gif_to_png_radio.pack()

        # Convert düğmesini oluştur
        self.convert_button = tk.Button(master, text="Dönüştür!", command=self.convert)
        self.convert_button.pack(pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename(title="Dosya Seç!")
        self.file_label.config(text=f"Seçilen Dosya: {file_path}")
        self.selected_file = file_path

    def convert(self):
        selected_operation = self.operation_var.get()

        if not hasattr(self, 'selected_file') or not self.selected_file:
            tk.messagebox.showwarning("Uyarı!", "Dönüştürülecek dosya seç!")
            return

        if selected_operation == "mp4_to_mp3":
            self.mp4_to_mp3()
        elif selected_operation == "png_to_jpeg":
            self.png_to_jpeg()
        elif selected_operation == "gif_to_png":
            self.gif_to_png()

    def mp4_to_mp3(self):
        video = VideoFileClip(self.selected_file)
        audio = video.audio
        audio.write_audiofile("dönüştürülen.mp3")
        audio.close()

    def png_to_jpeg(self):
        image = Image.open(self.selected_file)
        image.convert("RGB").save("dönüştürülen.jpg", "JPEG")

    def gif_to_png(self):
     output_file = "gif.png"
     image = Image.open(self.selected_file)
     image.save(output_file, save_all=True, append_images=list(ImageSequence.Iterator(image)))


# Tkinter uygulamasını başlat
root = tk.Tk()
app = FileConverterApp(root)
root.mainloop()
