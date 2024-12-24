from abc import ABC, abstractmethod

class RemoteControl: #controle remoto
    def __init__(self, device):
        self.device = device

    def toggle_power(self):
        self.device.toggle_power()

class Device(ABC): #dispositivo
    @abstractmethod
    def toggle_power(self):
        pass

class Lamp(Device): #lampada
    def __init__(self):
        self.is_on = False

    def toggle_power(self):
        self.is_on = not self.is_on
        state = "ligada" if self.is_on else "desligada"
        print(f"Lâmpada {state}.")

if __name__ == "__main__":
    lamp = Lamp()
    remote = RemoteControl(lamp)
    remote.toggle_power()
    remote.toggle_power()
