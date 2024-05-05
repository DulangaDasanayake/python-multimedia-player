import tkinter as tk
from tkinter import filedialog
import pygame

class MP3Player:
    def __init__(self, master):
        self.master = master
        self.master.title("D - Player")
        self.master.geometry("300x100")
        
        self.song_label = tk.Label(self.master, text="No song selected")
        self.song_label.pack()
        
        self.select_button = tk.Button(self.master, text="Select Song", command=self.select_song)
        self.select_button.pack()
        
        self.play_button = tk.Button(self.master, text="Play", command=self.play_song)
        self.play_button.pack()
        
        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_song)
        self.stop_button.pack()
        
        self.song = None
        
    def select_song(self):
        self.song = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if self.song:
            self.song_label.config(text=self.song)
        
    def play_song(self):
        if self.song:
            pygame.mixer.init()
            pygame.mixer.music.load(self.song)
            pygame.mixer.music.play()
        
    def stop_song(self):
        pygame.mixer.music.stop()

def main():
    root = tk.Tk()
    mp3_player = MP3Player(root)
    root.mainloop()

if __name__ == "__main__":
    main()
