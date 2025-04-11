import requests

def buscar_endereco_por_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        logradouro = dados.get("logradouro", "")
        bairro = dados.get("bairro", "")
        localidade = dados.get("localidade", "")
        uf = dados.get("uf", "")
        return f"{logradouro}, {bairro}, {localidade} - {uf}"
    else:
        return "Erro ao buscar o endereço. Verifique o CEP."

print(buscar_endereco_por_cep("13186210"))
