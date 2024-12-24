# TrabalhoPadroesDeProjeto

Os códigos utilizados neste repositório foram feitos com base nos disponibilizados em: https://refactoring.guru/pt-br/design-patterns/catalog

Padrões Utilizados:

# Abstract Factory

Este foi o padrão criacional escolhido. O padrão Abstract Factory busca lidar com o problema sobre a criação de obejtos relacionados sem êxpor suas classes concretas e, ao mesmo tempo, fazer o cliente ficar longe dos detalhes de implementação.
A forma com que o padrão realiza tais tarefas é a repartir os construtores em "fábricas" abstratas com fábricas concretas sendo apenas aquelas que o cliente especifica as quais deseja.
Por exemplo, no código deste repositório, são fábricas abstratas: CarFactory, Sedan e SUV. São fábricas concretas: EconomyCarFactory e LuxuryCarFactory. Os obejtos concretos serão criados com base na escolha do cliente entre "Luxury" ou "Economy", e, então, a fábrica concreta utiliza das fábricas abstratas para gerar tais objetos.
``` python
class ApplicationConfigurator:
    @staticmethod
    def main(car_type: str):
        if car_type == "Economy":
            factory = EconomyCarFactory()
        elif car_type == "Luxury":
            factory = LuxuryCarFactory()
        else:
            raise Exception("Erro! Tipo de carro desconhecido.")
```

# Bridge

Este foi o padrão estrutural escolhido. O padrão Bridge lida com o problema de relacionar classes de modo que elas não se tornem dependentes, ou seja, criar uma forma de relacionar duas classes diferentes de modo que, as alterações feitas em uma classe não afetará as demais classes que estão relacionadas a ela. No código neste repositório, isso foi feito relacionando a classe RemoteControl a uma classe Lamp atrave´s de uma classe intermediária, responsável pela ligação entre as duas. Desse modo, RemoteControl não está diretamente ligado a Lamp, pois as duas estão ligadas por uma terceira classe, assim, se quisermos substituir Lamp por algum outro dispositivo, não é necessário alterar nada em RemoteControl, apenas cirar outra conexão.

# Memento

Este foi o padrão comportamental esolhido. Ele busca tratar do problema de restauração dos atributos de um objeto sem expor os detalhes de implementação. Isso é feito a partir de uma classe responsável por armazenar os valores de um objeto, como uma espécie de Backup. No código deste repositório isso é feito a partir de uma classe Editor, responsável por "criar" textos e uma classe Snapshot (Versão) realcionada há uma dada instância de Editor, ou seja, quando salvamos um Snapshot, estamos aramazenando uma versão de Editor de forma que, ao usarmos a classe Restore(Snapshot) em Editor, restaruamos informações antigas de um texto.
