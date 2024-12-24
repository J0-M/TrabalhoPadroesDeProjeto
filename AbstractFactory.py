from abc import ABC, abstractmethod

class CarFactory(ABC): #fábrica abstrata de carros
    @abstractmethod
    def create_sedan(self):
        pass

    @abstractmethod
    def create_suv(self):
        pass

class EconomyCarFactory(CarFactory): #Fabrica Concreta economica
    def create_sedan(self):
        return EconomySedan()

    def create_suv(self):
        return EconomySUV()

class LuxuryCarFactory(CarFactory): #Fabrica Concreta luxo
    def create_sedan(self):
        return LuxurySedan()

    def create_suv(self):
        return LuxurySUV()

class Sedan(ABC): #Sedan
    @abstractmethod
    def show_details(self):
        pass

class EconomySedan(Sedan): #Sedan Economico
    def show_details(self):
        print("Sedan econômico: prático e eficiente.")

class LuxurySedan(Sedan): #Sedan de luxo
    def show_details(self):
        print("Sedan de luxo: confortável e sofisticado.")

class SUV(ABC): #SUVs
    @abstractmethod
    def show_details(self):
        pass

class EconomySUV(SUV): #SUV economico
    def show_details(self):
        print("SUV econômico: espaçoso e acessível.")

class LuxurySUV(SUV): #SUV de luxo
    def show_details(self):
        print("SUV de luxo: potente e elegante.")

class Application:
    def __init__(self, factory: CarFactory):
        self.factory = factory
        self.sedan = None
        self.suv = None

    def create_cars(self):
        self.sedan = self.factory.create_sedan()
        self.suv = self.factory.create_suv()

    def show_cars(self):
        self.sedan.show_details()
        self.suv.show_details()

class ApplicationConfigurator:
    @staticmethod
    def main(car_type: str):
        if car_type == "Economy":
            factory = EconomyCarFactory()
        elif car_type == "Luxury":
            factory = LuxuryCarFactory()
        else:
            raise Exception("Erro! Tipo de carro desconhecido.")

        app = Application(factory)
        app.create_cars()
        app.show_cars()

if __name__ == "__main__":
    # Mude o valor para "Luxury" para testar carros de luxo
    selected_type = "Economy"
    ApplicationConfigurator.main(selected_type)