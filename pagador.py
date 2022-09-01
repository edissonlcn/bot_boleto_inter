import json


class Pagador:
    cnpjCpf = ""
    nome = ""
    email = ""
    telefone = ""
    cep = ""
    numero = ""
    complemento = ""
    bairro = ""
    cidade = ""
    uf = ""
    ddd = ""
    tipoPessoa = ""
    endereco = ""

    def __init__(self, cnpjCpf, nome, email, telefone, cep, numero, complemento, bairro, cidade, uf, ddd, tipoPessoa, endereco):
        self.cnpjCpf = cnpjCpf
        self.nome = nome
        self.email = '' if str(email) == 'nan' else email
        self.telefone = '' if str(telefone) == 'nan' else str(
            int(telefone)).replace("-", "")
        self.cep = cep
        self.numero = '' if str(numero) == 'nan' else str(int(numero))
        self.complemento = '' if str(complemento) == 'nan' else complemento
        self.bairro = '' if str(bairro) == 'nan' else bairro
        self.cidade = '' if str(cidade) == 'nan' else cidade
        self.uf = uf
        self.ddd = '' if str(ddd) == 'nan' else str(int(ddd))
        self.tipoPessoa = tipoPessoa
        self.endereco = endereco

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
