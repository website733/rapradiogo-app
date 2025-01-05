pip install pyinstaller
pyinstaller --onefile --noconsole RadioRapGo.py

import tkinter as tk
from tkinter import messagebox
import vlc

# Liste des radios avec leurs URL de streaming
RADIOS = {
    "Skyrock": "http://icecast.skyrock.net/s/natio_mp3_128k",
    "Fun Radio": "http://streaming.radio.funradio.fr/fun-1-44-128",
    "NRJ": "http://cdn.nrjaudio.fm/audio1/fr/30001/mp3_128.mp3",
    "RTL 2": "http://streaming.radio.rtl2.fr/rtl2-1-44-128",
    "RMC": "http://chai5she.cdn.dvmr.fr/rmcinfo",
}

class RadioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RadioRap Go")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#333")

        # Titre
        tk.Label(
            root,
            text="🎧 RadioRap Go 🎧",
            font=("Arial", 20, "bold"),
            fg="white",
            bg="#333"
        ).pack(pady=10)

        # Liste des radios
        self.radio_var = tk.StringVar(value=list(RADIOS.keys())[0])
        for radio in RADIOS.keys():
            tk.Radiobutton(
                root,
                text=radio,
                variable=self.radio_var,
                value=radio,
                font=("Arial", 12),
                fg="white",
                bg="#333",
                activebackground="#555",
                activeforeground="white",
                selectcolor="#444"
            ).pack(anchor="w", padx=20)

        # Boutons
        tk.Button(
            root,
            text="▶️ Lancer",
            command=self.play_radio,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=20
        ).pack(pady=10)

        tk.Button(
            root,
            text="⏹️ Arrêter",
            command=self.stop_radio,
            font=("Arial", 12, "bold"),
            bg="#f44336",
            fg="white",
            padx=20
        ).pack()

        # Gestion du player VLC
        self.player = None

    def play_radio(self):
        selected_radio = self.radio_var.get()
        url = RADIOS[selected_radio]

        # Arrêter la radio en cours (s'il y en a une)
        if self.player:
            self.player.stop()

        # Démarrer la nouvelle radio
        self.player = vlc.MediaPlayer(url)
        self.player.play()

        messagebox.showinfo("Radio en cours", f"Vous écoutez {selected_radio} !")

    def stop_radio(self):
        if self.player:
            self.player.stop()
            self.player = None
            messagebox.showinfo("Arrêté", "La radio a été arrêtée.")

# Création de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = RadioApp(root)
    root.mainloop()
