import time
from abc import ABC, abstractmethod

class Lampu(ABC):
    def __init__(self, warna):
        self._CurrentLight = warna

    @abstractmethod
    def nyala(self):
        pass

class LampuMerah(Lampu):
    def nyala(self):
        print("Lampu Yang Sedang Menyala Adalah Warna Merah")

class LampuHijau(Lampu):
    def nyala(self):
        print("Lampu Yang Sedang Menyala Adalah Warna Hijau")

class LampuKuning(Lampu):
    def nyala(self):
        print("Lampu Yang Sedang Menyala Adalah Warna Kuning")


class TrafficLights:
    def __init__(self):
        self._CurrentLight = "HIJAU"
        self.Timer = 5

        self.merah = LampuMerah("MERAH")
        self.kuning = LampuKuning("KUNING")
        self.hijau = LampuHijau("HIJAU")

    @property
    def Current_Light(self):
        return self._CurrentLight

    @Current_Light.setter
    def Current_Light(self, value):
        if value not in ["MERAH", "HIJAU", "KUNING"]:
            raise ValueError("Warna tidak sesuai!")
        self._CurrentLight = value

    def PrintColor(self):
        time.sleep(self.Timer)
        MERAH = "| \033[41m      \033[0m |"
        MERAH_GELAP = "| \033[48;5;52m      \033[0m |"

        KUNING = "| \033[43m      \033[0m |"
        KUNING_GELAP = "| \033[48;5;58m      \033[0m |"

        HIJAU = "| \033[42m      \033[0m |"
        HIJAU_GELAP = "| \033[48;5;22m      \033[0m |"

        if self.Current_Light == "MERAH":
            self.Current_Light = "KUNING" # ubah parameter

            # Nyalakan Lampu Kuning
            print("\033[H\033[J", end="")
            print(" ________")
            print("|        |")
            print(MERAH_GELAP)
            print(MERAH_GELAP)
            print(KUNING)
            print(KUNING)
            print(HIJAU_GELAP)
            print(HIJAU_GELAP)
            print("|________|")
            print()
            self.kuning.nyala()

        elif self.Current_Light == "KUNING":
            self.Current_Light = "HIJAU"
            print("\033[H\033[J", end="") # ubah parameter

            # Nyalakan Lampu Hijau
            print(" ________")
            print("|        |")
            print(MERAH_GELAP)
            print(MERAH_GELAP)
            print(KUNING_GELAP)
            print(KUNING_GELAP)
            print(HIJAU)
            print(HIJAU)
            print("|________|")
            print()
            self.hijau.nyala()

        elif self.Current_Light == "HIJAU":
            self.Current_Light = "MERAH" # ubah parameter

            # Nyalakan Lampu Merah
            print("\033[H\033[J", end="")
            print(" ________")
            print("|        |")
            print(MERAH)
            print(MERAH)
            print(KUNING_GELAP)
            print(KUNING_GELAP)
            print(HIJAU_GELAP)
            print(HIJAU_GELAP)
            print("|________|")
            print()
            self.merah.nyala()

LampuLaluLintas = TrafficLights()
print("Menjalankan Program!")

while True:
    LampuLaluLintas.PrintColor()