import tkinter as tk
from playsound import playsound
import threading
import time


def geri_sayim_baslat():
    saniye = int(entry_saniye.get())
    threading.Thread(target=geri_sayim, args=(saniye,)).start()

def geri_sayim(saniye):
    if saniye > 0:
        while saniye > 0:
            label_saniye["text"] = str(saniye)
            saniye -= 1
            time.sleep(1)
    else:
        label_saniye["text"] = "Süre Girin"
    # Geri sayım bittiğinde alarmı çal
    playsound("alarmm.mp3")

# Tkinter penceresini oluştur
pencere = tk.Tk()
pencere.title("Geri Sayım Uygulaması")

# Etiket ve giriş kutusu oluştur
label_saniye = tk.Label(pencere, text="Süre Girin",font=(32))
label_saniye.pack(pady=10)


entry_saniye = tk.Entry(pencere)
entry_saniye.pack(pady=5)

# Geri Sayım Başlat düğmesi
buton_baslat = tk.Button(pencere, text="Geri Sayım Başlat", command=geri_sayim_baslat)
buton_baslat.pack(pady=5)

# Pencereyi göster
pencere.mainloop()
