import tkinter as tk
from tkinter import filedialog
import pygame
import threading

class MP3Player:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple MP3 Player")
        self.master.geometry("400x150")
        
        self.song_label = tk.Label(self.master, text="No song selected")
        self.song_label.pack()
        
        self.select_button = tk.Button(self.master, text="Select Song", command=self.select_song)
        self.select_button.pack()
        
        self.play_button = tk.Button(self.master, text="Play", command=self.play_song)
        self.play_button.pack()
        
        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_song)
        self.stop_button.pack()
        
        self.slider = tk.Scale(self.master, from_=0, to=100, orient="horizontal", command=self.set_volume)
        self.slider.pack()
        
        self.song = None
        self.playing = False
        self.volume = 0.5
        self.slider.set(50)
        
        self.update_slider_thread = None

    def select_song(self):
        self.song = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if self.song:
            self.song_label.config(text=self.song)
        
    def play_song(self):
        if self.song:
            pygame.mixer.init()
            pygame.mixer.music.load(self.song)
            pygame.mixer.music.set_volume(self.volume)
            pygame.mixer.music.play()
            self.playing = True
            self.update_slider_thread = threading.Thread(target=self.update_slider)
            self.update_slider_thread.start()
        
    def stop_song(self):
        pygame.mixer.music.stop()
        self.playing = False
        if self.update_slider_thread:
            self.update_slider_thread.join()
        
    def set_volume(self, value):
        self.volume = float(value) / 100
        if self.playing:
            pygame.mixer.music.set_volume(self.volume)
        
    def update_slider(self):
        while pygame.mixer.music.get_busy() and self.playing:
            position = pygame.mixer.music.get_pos() / 1000  # Convert milliseconds to seconds
            duration = pygame.mixer.Sound(self.song).get_length()
            percentage = (position / duration) * 100
            self.slider.set(percentage)
            self.master.update()
            pygame.time.wait(1000)  # Update every second

def main():
    root = tk.Tk()
    mp3_player = MP3Player(root)
    root.mainloop()

if __name__ == "__main__":
    main()
