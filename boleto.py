import json
import requests
from desconto import Desconto
import base64
from mensagem import Mensagem
from mora import Mora
from multa import Multa
from pagador import Pagador
import logging
import os


class Boleto:
    nossoNumero = ""
    dataEmissao = ""
    dataVencimento = ""
    seuNumero = ""
    cnpjCPFBeneficiario = ""
    numDiasAgenda = ""
    valorNominal = 0
    valorAbatimento = 0
    pagador = ""
    mensagem = ""
    desconto1 = ""
    desconto2 = ""
    desconto3 = ""
    multa = ""
    mora = ""

    def __init__(self, dataEmissao, seuNumero, cnpjCPFBeneficiario, numDiasAgenda, valorNominal, valorAbatimento, pagador, mensagem, desconto1, desconto2, desconto3, multa, mora, dataVencimento):
        self.dataEmissao = dataEmissao
        self.seuNumero = seuNumero
        self.cnpjCPFBeneficiario = cnpjCPFBeneficiario
        self.numDiasAgenda = numDiasAgenda
        self.valorNominal = valorNominal
        self.valorAbatimento = valorAbatimento
        self.pagador = pagador
        self.mensagem = mensagem
        self.desconto1 = desconto1
        self.desconto2 = desconto2
        self.desconto3 = desconto3
        self.multa = multa
        self.mora = mora
        self.dataVencimento = dataVencimento

    def toJSON(self):
        return {
            "pagador": {
                "cpfCnpj": self.pagador.cnpjCpf,
                "nome": self.pagador.nome,
                "email": self.pagador.email,
                "telefone": self.pagador.telefone,
                "cep": self.pagador.cep,
                "numero": str(self.pagador.numero),
                "complemento": self.pagador.complemento,
                "bairro": self.pagador.bairro,
                "cidade": self.pagador.cidade,
                "uf": self.pagador.uf,
                "endereco": self.pagador.endereco,
                "ddd": str(self.pagador.ddd),
                "tipoPessoa": "FISICA"
            },
            "dataEmissao": self.dataEmissao,
            "seuNumero": str(self.seuNumero),
            "dataVencimento": self.dataVencimento,
            "mensagem": {
                "linha1": self.mensagem.linha1,
                "linha2": self.mensagem.linha2,
                "linha3": self.mensagem.linha3,
                "linha4": self.mensagem.linha4,
                "linha5": self.mensagem.linha5
            },
            "desconto1": {
                "codigoDesconto": self.desconto1.codigoDesconto,
                "taxa": self.desconto1.taxa,
                "valor": "{:0.2f}".format(float(self.desconto1.valor)),
                "data": self.desconto1.data
            },
            "desconto2": {
                "codigoDesconto": self.desconto2.codigoDesconto,
                "taxa": self.desconto2.taxa,
                "valor": self.desconto2.valor,
                "data": self.desconto2.data
            },
            "desconto3": {
                "codigoDesconto": self.desconto3.codigoDesconto,
                "taxa": self.desconto3.taxa,
                "valor": self.desconto3.valor,
                "data": self.desconto3.data
            },
            "valorNominal": "{:0.2f}".format(float(self.valorNominal)),
            # "valorAbatimento": self.valorAbatimento,
            "multa": {
                "codigoMulta": self.multa.codigoMulta,
                "valor": self.multa.valor,
                "taxa": self.multa.taxa,
                "data": self.multa.data
            },
            "mora": {
                "codigoMora": self.mora.codigoMora,
                "valor": self.mora.valor,
                "taxa": self.mora.taxa,
                "data": self.mora.data
            },
            # "cnpjCPFBeneficiario": self.cnpjCPFBeneficiario,
            "numDiasAgenda": self.numDiasAgenda
        }
        # return json.dumps(self, default=lambda o: o.__dict__,
        #                  sort_keys=True, indent=4)

    def create(self, token):
        url = 'https://cdpj.partners.bancointer.com.br/cobranca/v2/boletos'
        hed = {'x-inter-conta-corrente': '30157021'}
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + token}
        cert_file_path = "Inter API_Certificado.crt"
        key_file_path = "Inter API_Chave.key"
        cert = (cert_file_path, key_file_path)
        payload = self.toJSON()
        check_create = requests.post(
            url, json=payload, headers=headers, cert=cert)
        if check_create.status_code == 200:
            result = json.loads(check_create.text)
            self.nossoNumero = result['nossoNumero']
        else:
            logging.info('boleto com problema: ' + self.pagador.nome +
                         '\n erro: ' + check_create.text)
            print('boleto com problema: ' + self.pagador.nome +
                  '\n erro: ' + check_create.text)

    def download(self, mes, nomeBoleto, token):
        url = 'https://cdpj.partners.bancointer.com.br/cobranca/v2/boletos/' + \
            self.nossoNumero+'/pdf'
        hed = {'x-inter-conta-corrente': '30157021'}
        headers = {'Authorization': 'Bearer ' + token}
        cert_file_path = "Inter API_Certificado.crt"
        key_file_path = "Inter API_Chave.key"
        cert = (cert_file_path, key_file_path)
        check_pdf = requests.get(
            url, headers=headers, cert=cert)
        if check_pdf.status_code == 200:
            if not os.path.exists(mes):
                os.mkdir(mes)
            with open(os.path.join(mes, nomeBoleto+"_"+mes+".pdf"), "wb") as fh:
                result = json.loads(check_pdf.text)
                fh.write(base64.b64decode(result["pdf"]))
        else:
            logging.info('download com problema: ' + self.pagador.nome +
                         '\n erro: ' + check_pdf.text)
            print('download com problema: ' + self.pagador.nome +
                  '\n erro: ' + check_pdf.text)
