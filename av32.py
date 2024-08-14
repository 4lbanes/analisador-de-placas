import sqlite3

def criar_banco_de_dados():
    conn = sqlite3.connect('placas.db')    
    dados_estados = [
        ('AAA', 'BEZ', 'Paraná'),
        ('BFA', 'GKI', 'São Paulo'),
        ('GKJ', 'HOK', 'Minas Gerais'),
        ('HOL', 'HQE', 'Maranhão'),
        ('HQF', 'HTW', 'Mato Grosso do Sul'),
        ('HTX', 'HZA', 'Ceará'),
        ('HZB', 'IAP', 'Sergipe'),
        ('IAQ', 'JDO', 'Rio Grande do Sul'),
        ('JDP', 'JKR', 'Distrito Federal'),
        ('JKS', 'JSZ', 'Bahia'),
        ('JTA', 'JWE', 'Pará'),
        ('JWF', 'JXY', 'Amazonas'),
        ('JXZ', 'KAU', 'Mato Grosso'),
        ('KAV', 'KFC', 'Goiás'),
        ('KFD', 'KME', 'Pernambuco'),
        ('KMF', 'LVE', 'Rio de Janeiro'),
        ('LVF', 'LWQ', 'Piauí'),
        ('LWR', 'MMM', 'Santa Catarina'),
        ('MMN', 'MOW', 'Paraíba'),
        ('MOX', 'MTZ', 'Espírito Santo'),
        ('MUA', 'MVK', 'Alagoas'),
        ('MVL', 'MXG', 'Tocantins'),
        ('MXH', 'MZM', 'Rio Grande do Norte'),
        ('MZN', 'NAG', 'Acre'),
        ('NAH', 'NBA', 'Roraima'),
        ('NBB', 'NEH', 'Rondônia'),
        ('NEI', 'NFB', 'Amapá'),
        ('NFC', 'NGZ', 'Goiás'),
        ('NHA', 'NHT', 'Maranhão'),
        ('NHU', 'NIX', 'Piauí'),
        ('NIY', 'NJW', 'Mato Grosso'),
        ('NJX', 'NLU', 'Goiás'),
        ('NLV', 'NMO', 'Alagoas'),
        ('NMP', 'NNI', 'Maranhão'),
        ('NNJ', 'NOH', 'Rio Grande do Norte'),
        ('NOI', 'NPB', 'Amazonas'),
        ('NPC', 'NPQ', 'Mato Grosso'),
        ('NPR', 'NQK', 'Paraíba'),
        ('NQL', 'NRE', 'Ceará'),
        ('NRF', 'NSD', 'Mato Grosso do Sul'),
        ('NSE', 'NTC', 'Pará'),
        ('NTD', 'NTW', 'Bahia'),
        ('NTX', 'NUG', 'Mato Grosso'),
        ('NUH', 'NUL', 'Roraima'),
        ('NUM', 'NVF', 'Ceará'),
        ('NVG', 'NVN', 'Sergipe'),
        ('NVO', 'NWR', 'Goiás'),
        ('NWS', 'NXQ', 'Maranhão'),
        ('NXR', 'NXT', 'Acre'),
        ('NXU', 'NXW', 'Pernambuco'),
        ('NXX', 'NYG', 'Minas Gerais'),
        ('NYH', 'NZZ', 'Bahia'),
        ('OAA', 'OAO', 'Amazonas'),
        ('OAP', 'OBS', 'Mato Grosso'),
        ('OBT', 'OCA', 'Pará'),
        ('OCB', 'OCU', 'Ceará'),
        ('OCV', 'ODT', 'Espírito Santo'),
        ('ODU', 'OEI', 'Piauí'),
        ('OEJ', 'OES', 'Sergipe'),
        ('OET', 'OFH', 'Paraíba'),
        ('OFI', 'OFW', 'Pará'),
        ('OFX', 'OGG', 'Paraíba'),
        ('OGH', 'OHA', 'Goiás'),
        ('OHB', 'OHK', 'Alagoas'),
        ('OHL', 'OHW', 'Rondônia'),
        ('OHX', 'OIQ', 'Ceará'),
        ('OIR', 'OJQ', 'Maranhão'),
        ('OJR', 'OKC', 'Rio Grande do Norte'),
        ('OKD', 'OKH', 'Santa Catarina'),
        ('OKI', 'OLG', 'Bahia'),
        ('OLH', 'OLN', 'Tocantins'),
        ('OLO', 'OMH', 'Minas Gerais'),
        ('OMI', 'OOF', 'Goiás'),
        ('OOG', 'OOU', 'Mato Grosso do Sul'),
        ('OOV', 'ORC', 'Minas Gerais'),
        ('ORD', 'ORM', 'Alagoas'),
        ('ORN', 'OSV', 'Ceará'),
        ('OSW', 'OTZ', 'Pará'),
        ('OUA', 'OUE', 'Piauí'),
        ('OUF', 'OVD', 'Bahia'),
        ('OVE', 'OVF', 'Espírito Santo'),
        ('OVG', 'OVG', 'Acre'),
        ('OVH', 'OVL', 'Espírito Santo'),
        ('OVM', 'OVV', 'Distrito Federal'),
        ('OVW', 'OVY', 'Piauí'),
        ('OVZ', 'OWG', 'Rio Grande do Norte'),
        ('OWH', 'OXK', 'Minas Gerais'),
        ('OXL', 'OXL', 'Rondônia'),
        ('OXM', 'OXM', 'Amazonas'),
        ('OXN', 'OXN', 'Alagoas'),
        ('OXO', 'OXO', 'Paraíba'),
        ('OXP', 'OXP', 'Acre'),
        ('OXQ', 'OXZ', 'Maranhão'),
        ('OYA', 'OYC', 'Tocantins'),
        ('OYD', 'OYK', 'Espírito Santo'),
        ('OYL', 'OYZ', 'Pernambuco'),
        ('OZA', 'OZA', 'Ceará'),
        ('OZB', 'OZB', 'Sergipe'),
        ('OZC', 'OZV', 'Bahia'),
        ('OZW', 'PBZ', 'Distrito Federal'),
        ('PCA', 'PED', 'Pernambuco'),
        ('PEE', 'PFQ', 'Pernambuco'),
        ('PFR', 'PGK', 'Pernambuco'),
        ('PGL', 'PGU', 'Pernambuco'),
        ('PGV', 'PGZ', 'Pernambuco'),
        ('PHA', 'PHZ', 'Amazonas'),
        ('PIA', 'PIZ', 'Piauí'),
        ('PJA', 'PLZ', 'Bahia'),
        ('PMA', 'POZ', 'Ceará'),
        ('PPA', 'PPZ', 'Espírito Santo'),
        ('PQA', 'PRZ', 'Goiás'),
        ('PSA', 'PTZ', 'Maranhão'),
        ('PUA', 'PZZ', 'Minas Gerais'),
        ('QAA', 'QAZ', 'Mato Grosso do Sul'),
        ('QBA', 'QCZ', 'Mato Grosso'),
        ('QDA', 'QEZ', 'Pará'),
        ('QFA', 'QFZ', 'Paraíba'),
        ('QGA', 'QGZ', 'Rio Grande do Norte'),
        ('QHA', 'QJZ', 'Santa Catarina'),
        ('QKA', 'QKM', 'Tocantins'),
        ('QKN', 'QKZ', 'Sergipe'),
        ('QLA', 'QLM', 'Alagoas'),
        ('QLN', 'QLT', 'Amapá'),
        ('QLU', 'QLZ', 'Acre'),
        ('QMA', 'QMP', 'Sergipe'),
        ('QMQ', 'QQZ', 'Minas Gerais'),
        ('QRA', 'QRA', 'Rondônia'),
        ('QRB', 'QRM', 'Espírito Santo'),
        ('QRN', 'QRZ', 'Piauí'),
        ('QSA', 'QSM', 'Paraíba'),
        ('QSN', 'QSZ', 'São Paulo'),
        ('QTA', 'QTJ', 'Rondônia'),
        ('QTK', 'QTL', 'Pará'),
        ('QTM', 'QTZ', 'Sergipe'),
        ('QUA', 'QUM', 'Goiás'),
        ('QUN', 'QUZ', 'Paraíba'),
        ('QVA', 'QVC', 'Maranhão'),
        ('QVD', 'QVL', 'Tocantins'),
        ('QVM', 'QVN', 'Sergipe'),
        ('QVO', 'QVP', 'Distrito Federal'),
        ('QVQ', 'QVZ', 'Goiás'),
        ('QWA', 'QWL', 'Alagoas'),
        ('QWM', 'QWQ', 'Acre'),
        ('QWR', 'QXZ', 'Minas Gerais'),
        ('QYA', 'QYZ', 'Pernambuco'),
        ('QZA', 'QZZ', 'Amazonas'),
        ('RAA', 'RAJ', 'Santa Catarina'),
        ('RAK', 'RAZ', 'Mato Grosso'),
        ('RBA', 'RBJ', 'Espírito Santo'),
        ('RBK', 'RCN', 'Goiás'),
        ('RCO', 'RDR', 'Bahia'),
        ('RDS', 'REB', 'Santa Catarina'),
        ('REC', 'REV', 'Distrito Federal'),
        ('REW', 'REZ', 'Mato Grosso do Sul'),
        ('RFA', 'RGD', 'Minas Gerais'),
        ('RGE', 'RGM', 'Rio Grande do Norte'),
        ('RGN', 'RGN', 'Rio Grande do Norte'),
        ('RGO', 'RGU', 'Alagoas'),
        ('RGV', 'RGZ', 'Sequências ainda não definidas'),
        ('RHA', 'RHZ', 'Paraná'),
        ('RIA', 'RIN', 'Ceará'),
        ('RIO', 'RIO', 'Rio de Janeiro'),
        ('RIP', 'RKV', 'Rio de Janeiro'),
        ('RKW', 'RLP', 'Santa Catarina'),
        ('RLQ', 'RMC', 'Paraíba'),
        ('RMD', 'RNZ', 'Minas Gerais'),
        ('ROA', 'ROZ', 'Maranhão'),
        ('RPA', 'RQL', 'Bahia'),
        ('RQM', 'RQV', 'Espírito Santo'),
        ('RQW', 'RRH', 'Sergipe'),
        ('RRI', 'RRZ', 'Mato Grosso'),
        ('RSA', 'RSF', 'Tocantins'),
        ('RSG', 'RST', 'Piauí'),
        ('RSU', 'RSZ', 'Rondônia'),
        ('RTA', 'RVZ', 'Minas Gerais'),
        ('RWA', 'RWJ', 'Mato Grosso do Sul'),
        ('RWK', 'RXD', 'Pará'),
        ('RXE', 'RXJ', 'Sequências ainda não definidas'),
        ('RXK', 'RYI', 'Santa Catarina'),
        ('RYJ', 'RYZ', 'Sequências ainda não definidas'),
        ('RZA', 'RZD', 'Roraima'),
        ('RZE', 'RZZ', 'Pernambuco'),
        ('SAA', 'SAJ', 'Alagoas'),
        ('SAK', 'SAM', 'Amapá'),
        ('SAN', 'SBV', 'Ceará'),
        ('SBW', 'SDS', 'Goiás'),
        ('SDT', 'ZZZ', 'Sequências ainda não definidas'),
    ]
    conn.commit()
    conn.close()

def buscar_estado(placa):
    letras_iniciais = placa[:3].upper()
    conn = sqlite3.connect('placas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT estado FROM placas WHERE letras_iniciais = ?', (letras_iniciais,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado else None

def contar_placas_por_estado(estado):
    conn = sqlite3.connect('placas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM placas WHERE estado = ?', (estado,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0]

def combinacoes_possiveis():
    mg = contar_placas_por_estado('Minas Gerais')
    mt = contar_placas_por_estado('Mato Grosso')
    df = contar_placas_por_estado('Distrito Federal')
    
    print(f"Minas Gerais (MG) tem {mg} placas registradas.")
    print(f"Mato Grosso (MT) tem {mt} placas registradas.")
    print(f"Distrito Federal (DF) tem {df} placas registradas.")
    
    total_placas = mg + mt + df
    print(f"Total de placas: {total_placas}")

while True:
    print("Osvaldo, escolha uma opção:")
    print("0. Finalizar programa")
    print("1. Reconhecer placa")
    print("2. Análise combinatória do número de placas entre DF, MT e MG")
    choice = input("Digite 0, 1 ou 2: ")

    if choice == '0':
        print("Programa finalizado...")
        break
    elif choice == '1':
        placa = input("Digite a placa do veículo: ")
        estado = buscar_estado(placa)
        if estado in ['Distrito Federal', 'Goiás', 'Minas Gerais']:
            print(f"A placa {placa} é de/do: {estado}")
        else:
            print(f"A placa {placa} não é de nossa responsabilidade, mas é do {estado}.")
    elif choice == '2':
        combinacoes_possiveis()
    else:
        print(f"Osvaldo, '{choice}' é uma opção inválida. Por favor, escolha 0, 1 ou 2.")
