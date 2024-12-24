# TrabalhoPadroesDeProjeto

Os códigos utilizados neste repositório foram feitos com base nos disponibilizados em: https://refactoring.guru/pt-br/design-patterns/catalog

Padrões Utilizados:

# Abscract Factory

Este foi o padrão  criacional escolhido. O padrão Abstract Factory busca lidar com o problema sobre a criação de obejtos relacionados sem êxpor suas classes concretas e, ao mesmo tempo, fazer o cliente ficar longe dos detalhes de implementação.
A forma com que o padrão realiza tais tarefas é a repartir os construtores em "fábricas" abstratas com fábricas concretas sendo apenas aquelas que o cliente especifica as quais deseja.
Por exemplo, no código deste repositório, são fábricas abstratas: CarFactory, Sedan e SUV. São fábricas concretas: EconomyCarFactory e LuxuryCarFactory. Os obejtos concretos serão criados com base na escolha do cliente entre "Luxury" ou "Economy", e, então, a fábrica concreta utiliza das fábricas abstratas para gerar tais objetos.

# Bridge
