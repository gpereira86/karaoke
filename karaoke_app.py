import tkinter as tk
from tkinter import filedialog, ttk
import ttkbootstrap as ttkb
from video_player import VideoPlayer
from file_explorer import FileExplorer

class KaraokeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Karaoke em Glauco")
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="#212121")
        self.root.bind("<Escape>", self.sair_tela_cheia)

        self.video_player = VideoPlayer(self.root)
        self.configure_layout()

    def configure_layout(self):
        light_gray = "#424242"

        # Frame do título no topo
        self.title_frame = ttkb.Frame(self.root, bootstyle="primary")
        self.title_frame.pack(side="top", fill="x", pady=5)

        title_label = ttkb.Label(self.title_frame, text="Karaoke em Glauco", bootstyle="primary-inverse", font=("Arial", 24))
        title_label.pack(pady=0)

        # Frame de arquivos à esquerda
        self.file_explorer_frame = ttkb.Frame(self.root, bootstyle="secondary")
        self.file_explorer_frame.pack(side="left", fill="y", padx=5, pady=5)

        self.file_tree = ttk.Treeview(self.file_explorer_frame)
        self.file_tree.pack(fill="both", expand=True)

        self.folder_path = "C:/xampp/htdocs/portfolio2/views/assets/img"
        self.explorer = FileExplorer(self.file_tree, self.folder_path, self.video_player)

        # Frame principal para vídeos e controles
        self.main_frame = ttkb.Frame(self.root, bootstyle="secondary")
        self.main_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        # Frame de vídeos que ocupa 70% da altura do main_frame
        self.video_frame = ttkb.Frame(self.main_frame, bootstyle="secondary")
        self.video_frame.pack(side="top", fill="both", expand=True, padx=5, pady=5)

        # Frame de controle que ocupa o restante 30% da altura do main_frame
        self.control_frame = ttkb.Frame(self.main_frame, bootstyle="secondary")
        self.control_frame.pack(side="bottom", fill="x", pady=20)

        self.open_button = ttkb.Button(self.control_frame, text="Abrir Música", command=self.abrir_musica, bootstyle="secondary")
        self.open_button.pack(side="left", padx=10)

        self.pause_button = ttkb.Button(self.control_frame, text="Pausar", command=self.pausar_video, bootstyle="secondary")
        self.pause_button.pack(side="left", padx=10)

        self.resume_button = ttkb.Button(self.control_frame, text="Continuar", command=self.continuar_video, bootstyle="secondary")
        self.resume_button.pack(side="left", padx=10)

    def abrir_musica(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
        if file_path:
            self.video_player.load(file_path)
            self.video_player.play()

    def pausar_video(self):
        self.video_player.pause()

    def continuar_video(self):
        self.video_player.play()

    def sair_tela_cheia(self, event=None):
        self.root.attributes("-fullscreen", False)