import sys
import json
bom = 5
moderado = 4
ruim = 3
muito_ruim = 2
pessimo = 1

listar_qualidade = []
def particulas_inalaveis(calculo_final, resultado):
    
        try:
            
                MCP10 = float(input("Digite o valor da concentração do MCP10 obtido em campo : "))
                if MCP10 < 1:
                    print("Digite numeros positivos!")
                    sys.exit()
                else:
                    if MCP10 >= 0 and MCP10 <= 50:
                        calculo = 40 / 50
                        calculo_final = calculo * MCP10
                        result = round(calculo_final, 2)
                        resultado.append(result)
                        qualidade = bom
                        listar_qualidade.append(qualidade)
                
                    elif MCP10 > 50 and MCP10 <= 100:
                        calculo_indice = 80 - 41
                        calculo_concentracao =  100 - 50   
                        calculo_2 = calculo_indice / calculo_concentracao
                        calculo_3 = MCP10 - 50
                        calculo_4 = calculo_2 * calculo_3
                        calculo_final = calculo_4 + 41
                        resultado.append(calculo_final)
                        qualidade = moderado
                        listar_qualidade.append(qualidade)
                        
                    elif MCP10 > 150 and MCP10 <=250:
                        calculo_indice = 120 - 81
                        calculo_concentracao =  150 - 100   
                        calculo_2 = calculo_indice / calculo_concentracao
                        calculo_3 = MCP10 - 100
                        calculo_4 = calculo_2 * calculo_3
                        calculo_final = calculo_4 + 81
                        result = round(calculo_final, 2)
                        resultado.append(result)
                        
                        qualidade = ruim
                        listar_qualidade.append(qualidade)
                    
                    elif MCP10 > 150 and MCP10 < 250:
                        calculo_indice = 200 - 121
                        calculo_concentracao =  250 - 150
                        calculo_2 = calculo_indice / calculo_concentracao
                        calculo_3 = MCP10 - 150
                        calculo_4 = calculo_2 * calculo_3
                        calculo_final = calculo_4 + 121
                        result = round(calculo_final, 2)
                        resultado.append(result)
                        qualidade = muito_ruim
                        listar_qualidade.append(qualidade)
                    elif MCP10 < 250 and MCP10 <= 3000:
                        calculo_indice = 200 - 121
                        calculo_concentracao =  3000 - 250
                        calculo_2 = calculo_indice / calculo_concentracao
                        calculo_3 = MCP10 - 250
                        calculo_4 = calculo_2 * calculo_3
                        calculo_final = calculo_4 + 121
                        result = round(calculo_final, 2)
                        resultado.append(result)
                        qualidade = pessimo
                        listar_qualidade.append(qualidade)
                        
        
        except:
            print("ERRO! TOME CUIDADO DIGITE APENAS NUMEROS")
            sys.exit()
        print("=" * 100)
        print()
def  particulas_inalaveis_fina(calculo_final, resultado):
        try:
            MP2_5 = float(input("Digite o valor das partículas inaláveis finas (MP2,5): "))
            if MP2_5 < 1:
                    print("Digite numeros positivos!")
                    sys.exit()
            else:
                if MP2_5 >= 0 and MP2_5 <= 25:
                    calculo = 40 / 25
                    calculo_final = calculo * MP2_5
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = bom
                    listar_qualidade.append(qualidade)
                    
                
                elif MP2_5 > 25 and MP2_5 <= 50:
                    calculo_indice = 80 - 41
                    calculo_concentracao =  50 - 25   
                    calculo_2 = calculo_indice / calculo_concentracao
                    calculo_3 = MP2_5 - 25
                    calculo_4 = calculo_2 * calculo_3
                    calculo_final = calculo_4 + 41
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = moderado
                    listar_qualidade.append(qualidade)
        
                elif MP2_5 > 50 and MP2_5 <= 75:
                    calculo_indice = 120 - 81
                    calculo_concentracao =  75 - 50   
                    calculo_2 = calculo_indice / calculo_concentracao
                    calculo_3 = MP2_5 - 50
                    calculo_4 = calculo_2 * calculo_3
                    calculo_final = calculo_4 + 81
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = ruim
                    listar_qualidade.append(qualidade)
        
                elif MP2_5 > 75 and MP2_5 <=125:
                    calculo_indice = 200 - 121
                    calculo_concentracao =  125 - 75
                    calculo_2 = calculo_indice / calculo_concentracao
                    calculo_3 = MP2_5 - 75
                    calculo_4 = calculo_2 * calculo_3
                    calculo_final = calculo_4 + 121
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = muito_ruim
                    listar_qualidade.append(qualidade)
                elif MP2_5 > 125 and MP2_5 <= 3000:
                    calculo_indice = 200 - 121
                    calculo_concentracao =  3000- - 125
                    calculo_2 = calculo_indice / calculo_concentracao
                    calculo_3 = MP2_5 - 125
                    calculo_4 = calculo_2 * calculo_3
                    calculo_final = calculo_4 + 121
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = pessimo
                    listar_qualidade.append(qualidade)
    
        except:
            print("ERRO! TOME CUIDADO DIGITE APENAS NUMEROS")
            sys.exit()
        print("=" * 100)               
        print()
def ozonio(calculo_final, resultado):
        try:
            O3 = float(input("Digite o valor do ozônio(O3): "))
            if O3 < 1:
                    print("Digite numeros positivos!")
                    sys.exit()
            else:
                if O3 >= 0 and O3 <= 100:
                    calculo = 40 / 100
                    calculo_final = calculo * O3
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = bom
                    listar_qualidade.append(qualidade)
                elif O3 > 100 and O3 <= 130:
                    calculo_indice = 80 - 41
                    calculo_concentracao =  130 - 100   
                    calculo_2 = calculo_indice / calculo_concentracao
                    calculo_3 = O3 - 100
                    calculo_4 = calculo_2 * calculo_3
                    calculo_final = calculo_4 + 41
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = moderado
                    listar_qualidade.append(qualidade)
                elif O3 > 130 and O3 <= 160:
                    calculo_indice = 120 - 81
                    calculo_concentracao =  160 - 130   
                    calculo_2 = calculo_indice / calculo_concentracao
                    calculo_3 = O3 - 130
                    calculo_4 = calculo_2 * calculo_3
                    calculo_final = calculo_4 + 81
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = ruim
                    listar_qualidade.append(qualidade)
                elif O3 > 160 and O3 <=200:
                    calculo_indice = 200 - 121
                    calculo_concentracao =  200 - 160
                    calculo_2 = calculo_indice / calculo_concentracao
                    calculo_3 = O3 - 160
                    calculo_4 = calculo_2 * calculo_3
                    calculo_final = calculo_4 + 121
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = muito_ruim
                    listar_qualidade.append(qualidade)
                elif O3 > 200 and O3 <= 3000:
                    calculo_indice = 200 - 121
                    calculo_concentracao =  3000 - 200
                    calculo_2 = calculo_indice / calculo_concentracao
                    calculo_3 = O3 - 200
                    calculo_4 = calculo_2 * calculo_3
                    calculo_final = calculo_4 + 121
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = pessimo
                    listar_qualidade.append(qualidade)
                
        except:
            print("ERRO! TOME CUIDADO DIGITE APENAS NUMEROS")
            sys.exit()
        print("=" * 100)   
        print()
def monoxido_carbono(calculo_final, resultado):
        try:
            MCO=float(input("Digite o valor do monóxido de carbono (CO): "))
            if MCO < 1:
                    print("Digite numeros positivos!")
                    sys.exit()
            else:
                if MCO >= 0 and MCO <= 9 :
                    calculo = 40 / 9
                    calculo_final = calculo * MCO
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = bom
                    listar_qualidade.append(qualidade)
                elif MCO > 9  and MCO <= 11:
                    calculo_indice = 80 - 41
                    calculo_concentracao =  11 - 9   
                    calculo_2 = calculo_indice / calculo_concentracao
                    calculo_3 = MCO - 9
                    calculo_4 = calculo_2 * calculo_3
                    calculo_final = calculo_4 + 41
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = moderado
                    listar_qualidade.append(qualidade)
                elif MCO > 11 and MCO <= 13:
                    calculo_indice = 120 - 81
                    calculo_concentracao =  13 - 11   
                    calculo_2 = calculo_indice / calculo_concentracao
                    calculo_3 = MCO - 11
                    calculo_4 = calculo_2 * calculo_3
                    calculo_final = calculo_4 + 81
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = ruim
                    listar_qualidade.append(qualidade)
                elif MCO > 13 and MCO <=15:
                    calculo_indice = 200 - 121
                    calculo_concentracao =  15 - 13
                    calculo_2 = calculo_indice / calculo_concentracao
                    calculo_3 = MCO - 13
                    calculo_4 = calculo_2 * calculo_3
                    calculo_final = calculo_4 + 121
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = muito_ruim
                    listar_qualidade.append(qualidade)
                elif MCO > 15 and MCO <= 3000:
                    calculo_indice = 200 - 121
                    calculo_concentracao = 3000 - 15
                    calculo_2 = calculo_indice / calculo_concentracao
                    calculo_3 = MCO - 15
                    calculo_4 = calculo_2 * calculo_3
                    calculo_final = calculo_4 + 121
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = pessimo
                    listar_qualidade.append(qualidade)
                

                
        except:
            print("ERRO! TOME CUIDADO DIGITE APENAS NUMEROS")        
            sys.exit()
        print("=" * 100)
        print()
def dioxido_nitrogenio(calculo_final, resultado):
        try:
            NO2 = float(input("Digite o valor do dióxido de nitrogênio (NO2): "))
            if NO2 < 1:
                    print("Digite numeros positivos!")
                    sys.exit()
            else:
                if NO2 >= 0 and NO2 <= 200 :
                    calculo = 40 / 200
                    calculo_final = calculo * NO2
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = bom
                    listar_qualidade.append(qualidade)
                elif NO2 > 200  and NO2 <= 240:
                    calculo_indice = 80 - 41
                    calculo_concentracao =  240 - 200  
                    calculo_2 = calculo_indice / calculo_concentracao
                    calculo_3 = NO2 - 200
                    calculo_4 = calculo_2 * calculo_3
                    calculo_final = calculo_4 + 41
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = moderado
                    listar_qualidade.append(qualidade)
                elif NO2 > 240 and NO2 <= 320:
                    calculo_indice = 120 - 81
                    calculo_concentracao =  320 - 240   
                    calculo_2 = calculo_indice / calculo_concentracao
                    calculo_3 = NO2 - 240
                    calculo_4 = calculo_2 * calculo_3
                    calculo_final = calculo_4 + 81
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = ruim
                    listar_qualidade.append(qualidade)
                elif NO2 > 320 and NO2 <=1130:
                    calculo_indice = 200 - 121
                    calculo_concentracao =  1130 - 320
                    calculo_2 = calculo_indice / calculo_concentracao
                    calculo_3 = NO2 - 320
                    calculo_4 = calculo_2 * calculo_3
                    calculo_final = calculo_4 + 121
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = muito_ruim
                    listar_qualidade.append(qualidade)
                elif NO2 > 1130 and NO2 <= 3000:
                    calculo_indice = 200 - 121
                    calculo_concentracao =  3000 - 1130
                    calculo_2 = calculo_indice / calculo_concentracao
                    calculo_3 = NO2 - 1130
                    calculo_4 = calculo_2 * calculo_3
                    calculo_final = calculo_4 + 121
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = pessimo
                    listar_qualidade.append(qualidade)
        except:
            print("ERRO! TOME CUIDADO DIGITE APENAS NUMEROS")   
            sys.exit()       
        print("=" * 100)
        print()
def dioxido_enxofre(calculo_final, resultado):
        try:
            SO2 = float(input("Digite o valor do dióxido de enxofre (SO2): "))
            if SO2 < 1:
                print("Digite numeros positivos!")
                sys.exit()
            else:
                if SO2 >= 0 and SO2 <= 20 :
                    calculo = 40 / 20
                    calculo_final = calculo * SO2
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = bom
                    listar_qualidade.append(qualidade)
    
                elif SO2 > 20 and SO2 <= 40:
                    calculo_indice = 80 - 41
                    calculo_concentracao =  40 - 20  
                    calculo_2 = calculo_indice / calculo_concentracao
                    calculo_3 = SO2 - 20
                    calculo_4 = calculo_2 * calculo_3
                    calculo_final = calculo_4 + 41
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = moderado
                    listar_qualidade.append(qualidade)
                    
                elif SO2 > 40 and SO2 <= 365:
                    calculo_indice = 120 - 81
                    calculo_concentracao =  365 - 40   
                    calculo_2 = calculo_indice / calculo_concentracao
                    calculo_3 = SO2 - 40
                    calculo_4 = calculo_2 * calculo_3
                    calculo_final = calculo_4 + 81
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = ruim
                    listar_qualidade.append(qualidade)
                elif SO2 > 365 and SO2 <=800:
                    calculo_indice = 200 - 121
                    calculo_concentracao =  800 - 365
                    calculo_2 = calculo_indice / calculo_concentracao
                    calculo_3 = SO2 - 365
                    calculo_4 = calculo_2 * calculo_3
                    calculo_final = calculo_4 + 121
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = muito_ruim
                    listar_qualidade.append(qualidade)
                elif SO2 > 800 and SO2 <=3000:
                    calculo_indice = 200 - 121
                    calculo_concentracao =  3000 - 800
                    calculo_2 = calculo_indice / calculo_concentracao
                    calculo_3 = SO2 - 800
                    calculo_4 = calculo_2 * calculo_3
                    calculo_final = calculo_4 + 121
                    result = round(calculo_final, 2)
                    resultado.append(result)
                    qualidade = pessimo
                    listar_qualidade.append(qualidade)
                    

        except:
                print("ERRO! TOME CUIDADO DIGITE APENAS NUMEROS")
                sys.exit()
        print("=" * 100)
        print()
def sair():
        print("saindo do algoritimo")
        sys.exit()

    
def listar(resultado):
        print()
        if not resultado:
            print('Nenhuma tarefa para listar')
            return

        print('resultado:')
        
        for resultados in resultado:
            print(f'\t Resultado: {resultados}')
        print()
        
def ler(resultado,caminho_arquivo):
        dados = []
        try:
            with open(caminho_arquivo, "r", encoding="utf8") as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            print("Arquivo nao existe")
            salvar(resultado,caminho_arquivo)
        return dados

def salvar(resultado, caminho_arquivo):
        dados = resultado
        with open(caminho_arquivo, "w", encoding="utf8") as arquivo:
                dados = json.dump(resultado, arquivo, indent=2, ensure_ascii=False)
        return dados


CAMINHO_ARQUIVO = "C:\\Users\\Cryy   Joao\\OneDrive - Sociedade Campineira de Educação e Instrução\\Estudos\\Curso de python\\curso de python udemy\\"
CAMINHO_ARQUIVO += "controle_ar.json"
resultado = ler([],CAMINHO_ARQUIVO)
calculo_final = []

while True:
        particulas_inalaveis(calculo_final, resultado)
        particulas_inalaveis_fina(calculo_final, resultado)
        ozonio(calculo_final, resultado)
        monoxido_carbono(calculo_final, resultado)
        dioxido_nitrogenio(calculo_final, resultado)
        dioxido_enxofre(calculo_final, resultado)

        
        print()
        print("=" * 100)
        salvar(resultado, CAMINHO_ARQUIVO)
        listar(resultado)
        print("=" * 100)
        if min(listar_qualidade) == 1:
            print("QUALIDADE DE AR PESSIMA")
            print()
            print("""Toda a população pode apresentar sérios riscos 
de manifestações de doenças respiratórias e 
cardiovasculares. Aumento de mortes prematuras 
em pessoas de grupos sensíveis.""")
        elif min(listar_qualidade) == 2:
            print("QUALIDADE DE AR MUITO RUIM")
            print()
            print("""Toda a população pode apresentar 
agravamento dos sintomas como tosse seca, 
cansaço, ardor nos olhos, nariz e garganta e
ainda apresentar falta de ar e respiração 
ofegante. Efeitos ainda mais graves à saúde de 
grupos sensíveis (crianças, idosos e pessoas 
com problemas cardiovasculares).""")
        elif min(listar_qualidade) == 3:
            print("QUALIDADE DE AR RUIM")
            print()
            print(print("""Toda a população pode apresentar sintomas 
como tosse seca, cansaço, ardor nos olhos, nariz 
e garganta. Pessoas de grupos sensíveis 
(crianças, idosos e pessoas com doenças 
respiratórias e cardíacas), podem apresentar 
efeitos mais sérios na saúde."""))
        elif min(listar_qualidade) == 4:
            print("QUALIDADE DE AR MODERADA")
            print()
            print("""Pessoas de grupos sensíveis (crianças, idosos e 
pessoas com doenças respiratórias e cardíacas),
podem apresentar sintomas como tosse seca e
cansaço. A população, em geral, não é afetada.""")
        elif min(listar_qualidade) == 5:
            print("QUALIDADE DE AR BOA")
            print()
            print("Praticamente não há riscos à saúde")
        print("=" * 100)
        print()
        print("selecione uma opcao!")
    
        pergunta = str(input("Quer continuar? s para sim - n para nao: "))
        
        if pergunta == "n" and "N":
            sair()
        
            
            
        elif pergunta == "s" and "S":
            print("Continuando para outro calculo")
            continue
