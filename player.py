import tkinter as tk
from tkinter import filedialog
import pygame
from pygame.locals import *

class MediaPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("D - Player")
        self.master.geometry("600x400")
        self.master.config(bg="lightblue")

        self.song_label = tk.Label(self.master, text="No media selected", bg="lightblue")
        self.song_label.pack(pady=10)

        self.select_button = tk.Button(self.master, text="Select Media", command=self.select_media, bg="white")
        self.select_button.pack(pady=5)

        self.play_button = tk.Button(self.master, text="Play", command=self.play_media, bg="green")
        self.play_button.pack(pady=5)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_media, bg="red")
        self.stop_button.pack(pady=5)

        self.media = None
        self.is_video = False

        pygame.init()

    def select_media(self):
        self.media = filedialog.askopenfilename(filetypes=[("Media files", "*.mp3 *.mp4")])
        if self.media:
            self.song_label.config(text=self.media)
            self.is_video = self.media.lower().endswith(('.mp4', '.mov', '.avi'))

    def play_media(self):
        if self.media:
            pygame.mixer.quit()
            if self.is_video:
                pygame.display.set_mode((600, 400))
                pygame.display.set_caption("D - Player")
                self.movie = pygame.movie.Movie(self.media)
                self.movie_screen = pygame.display.set_mode(self.movie.get_size())
                self.movie.set_display(self.movie_screen)
                self.movie.play()
            else:
                pygame.mixer.init()
                pygame.mixer.music.load(self.media)
                pygame.mixer.music.play()

    def stop_media(self):
        if self.is_video:
            self.movie.stop()
            pygame.display.quit()
        else:
            pygame.mixer.music.stop()

def main():
    root = tk.Tk()
    media_player = MediaPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
