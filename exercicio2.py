import json
lista: list = ["Sapato", 39, 18.38, True]

produto1: dict = {
    "nome":"Sapato",
    "quantidade":39,
    "preço": 10.38,
    "disponivel": True
}


produto2: dict = {
    "nome":"Televisao",
    "quantidade":10,
    "preço": 749.99,
    "disponivel": False
}

carrinho: list = []

carrinho.append(produto1)
carrinho.append(produto2)

carrinho_json = json.dumps(carrinho)

print(carrinho_json)
