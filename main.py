import pandas
import json
from boleto import Boleto
from desconto import Desconto
from mensagem import Mensagem
from mora import Mora
from multa import Multa
import logging

from pagador import Pagador
from auth import Auth
mes = "Setembro"
excel = pandas.read_excel("planilhaBoletos.xlsx", mes)

logging.basicConfig(level=logging.INFO, filename='boletosjunho.log')
auth = Auth("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", )
auth.generate_token_boleto_write("boleto-cobranca.write")
auth.generate_token_boleto_read("boleto-cobranca.read")

for i in excel.axes[0]:
    # for i in range(6):
    try:
        print(i)

        pagador = Pagador(str(excel.at[i, 'cnpjCpf']).replace(".", "").replace("-", ""), excel.at[i, 'nome'], excel.at[i, 'email'], excel.at[i, 'telefone'], str(int(excel.at[i, 'cep'])).replace("-", ""),
                          excel.at[i, 'numero'], excel.at[i, 'complemento'], excel.at[i, 'bairro'], excel.at[i, 'cidade'], excel.at[i, 'uf'], excel.at[i, 'ddd'], "FISICA", excel.at[i, 'endereco'])
        mensagem = Mensagem(excel.at[i, 'linha1'], excel.at[i, 'linha2'],
                            excel.at[i, 'linha3'], excel.at[i, 'linha4'], excel.at[i, 'linha5'])

        desconto1 = Desconto(excel.at[i, 'codigoDesconto'], excel.at[i,
                                                                     'taxa'], excel.at[i, 'valor'], excel.at[i, 'dataDesconto'])
        desconto2 = Desconto("NAOTEMDESCONTO", 0, 0, "nan")
        desconto3 = Desconto("NAOTEMDESCONTO", 0, 0, "nan")

        multa = Multa("PERCENTUAL", 2, 0, excel.at[i, 'dataMulta'])
        mora = Mora("TAXAMENSAL", 1, 0, excel.at[i, 'dataMora'])

        dataEmissao = excel.at[i, 'dataEmissao']
        seuNumero = str(int(excel.at[i, 'seuNumero']))
        dataVencimento = excel.at[i, 'dataVencimento']
        valorNominal = float(excel.at[i, 'valorNominal'])
        valorAbatimento = float(excel.at[i, 'valorAbatimento'])
        cnpjCPFBeneficiario = "31315546000165"
        numDiasAgenda = 60

        boleto = Boleto(dataEmissao._date_repr, seuNumero, cnpjCPFBeneficiario, numDiasAgenda, valorNominal,
                        valorAbatimento, pagador, mensagem, desconto1, desconto2, desconto3, multa, mora, dataVencimento._date_repr)

        boleto.create(auth.token_boleto_write)

        if not boleto.nossoNumero == '':
            boleto.download(
                mes, excel.at[i, 'nomeBoleto'], auth.token_boleto_read)

            excel.at[i, 'nossoNumero'] = boleto.nossoNumero
    except Exception as e:
        logging.error(e)
        print(e)


excel.to_excel("output.xlsx")
teste = "a"
