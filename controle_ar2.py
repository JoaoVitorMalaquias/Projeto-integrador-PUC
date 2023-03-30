import sys

def particulas_inalaveis():
   
    try:
        MCP10 = float(input("Digite o valor da concentração do MCP10 obtido em campo : "))
        if MCP10 < 1:
            print("Digite numeros positivos!")
            sys.exit()
        else:
            if MCP10 >= 0 and MCP10 <= 50:
                calculo = 40 / 50
                calculo_final = calculo * MCP10
                print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar BOA""")
                print()
                print("Praticamente não há riscos à saúde")               
            elif MCP10 > 50 and MCP10 <= 100:
                calculo_indice = 80 - 41
                calculo_concentracao =  100 - 50   
                calculo_2 = calculo_indice / calculo_concentracao
                calculo_3 = MCP10 - 50
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + 41
                print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar MODERADA""")
                print()
                print("""Pessoas de grupos sensíveis (crianças, idosos e 
pessoas com doenças respiratórias e cardíacas),
podem apresentar sintomas como tosse seca e
cansaço. A população, em geral, não é afetada.""")
                
            elif MCP10 > 150 and MCP10 <=250:
                calculo_indice = 120 - 81
                calculo_concentracao =  150 - 100   
                calculo_2 = calculo_indice / calculo_concentracao
                calculo_3 = MCP10 - 100
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + 81
                print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar RUIM""")
                print()
                print("""Toda a população pode apresentar sintomas 
como tosse seca, cansaço, ardor nos olhos, nariz 
e garganta. Pessoas de grupos sensíveis 
(crianças, idosos e pessoas com doenças 
respiratórias e cardíacas), podem apresentar 
efeitos mais sérios na saúde.""")
            
            elif MCP10 > 150 and MCP10 < 250:
                calculo_indice = 200 - 121
                calculo_concentracao =  250 - 150
                calculo_2 = calculo_indice / calculo_concentracao
                calculo_3 = MCP10 - 150
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + 121
                print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar MUITO RUIM""")
                print()
                print("""Toda a população pode apresentar 
agravamento dos sintomas como tosse seca, 
cansaço, ardor nos olhos, nariz e garganta e 
ainda apresentar falta de ar e respiração 
ofegante. Efeitos ainda mais graves à saúde de 
grupos sensíveis (crianças, idosos e pessoas 
com problemas cardiovasculares).""")
            elif MCP10 > 250:
                print(f"É uma qualidade de ar PESSIMA")
                print()
                print("""Toda a população pode apresentar sérios riscos 
de manifestações de doenças respiratórias e 
cardiovasculares. Aumento de mortes prematuras 
em pessoas de grupos sensíveis.""")
            
            print()
    except:
        print("ERRO! TOME CUIDADO DIGITE APENAS NUMEROS")
        sys.exit()
print("=" * 100)
print()
def  particulas_inalaveis_fina():
    try:
        MP2_5 = float(input("Digite o valor das partículas inaláveis finas (MP2,5): "))
        if MP2_5 < 1:
                print("Digite numeros positivos!")
                sys.exit()
        else:
            if MP2_5 >= 0 and MP2_5 <= 25:
               calculo = 40 / 25
               calculo_final = calculo * MP2_5
               print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar BOA""")
               print("Praticamente não há riscos à saúde")
               print()            
            elif MP2_5 > 25 and MP2_5 <= 50:
                calculo_indice = 80 - 41
                calculo_concentracao =  50 - 25   
                calculo_2 = calculo_indice / calculo_concentracao
                calculo_3 = MP2_5 - 25
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + 41
                print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar MODERADA""")
                print()
                print("""Pessoas de grupos sensíveis (crianças, idosos e 
pessoas com doenças respiratórias e cardíacas),
podem apresentar sintomas como tosse seca e
cansaço. A população, em geral, não é afetada.""")
            elif MP2_5 > 50 and MP2_5 <= 75:
                calculo_indice = 120 - 81
                calculo_concentracao =  75 - 50   
                calculo_2 = calculo_indice / calculo_concentracao
                calculo_3 = MP2_5 - 50
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + 81
                print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar RUIM""")
                print()
                print("""Toda a população pode apresentar sintomas
como tosse seca, cansaço, ardor nos olhos, nariz
e garganta. Pessoas de grupos sensíveis
(crianças, idosos e pessoas com doenças
respiratórias e cardíacas), podem apresentar
efeitos mais sérios na saúde.""")
            elif MP2_5 > 75 and MP2_5 <=125:
                calculo_indice = 200 - 121
                calculo_concentracao =  125 - 75
                calculo_2 = calculo_indice / calculo_concentracao
                calculo_3 = MP2_5 - 75
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + 121
                print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar MUITO RUIM""")
                print()
                print("""Toda a população pode apresentar
agravamento dos sintomas como tosse seca,
cansaço, ardor nos olhos, nariz e garganta e
ainda apresentar falta de ar e respiração
ofegante. Efeitos ainda mais graves à saúde de
grupos sensíveis (crianças, idosos e pessoas
com problemas cardiovasculares).""")
            
            else:
                print(f"É uma qualidade de ar PESSIMA")
                print()
                print("""Toda a população pode apresentar sérios riscos
de manifestações de doenças respiratórias e
cardiovasculares. Aumento de mortes prematuras
em pessoas de grupos sensíveis.""")
            print()   
    except:
        print("ERRO! TOME CUIDADO DIGITE APENAS NUMEROS")
        sys.exit()
print("=" * 100)               
print()
def ozonio():
    try:
        O3 = float(input("Digite o valor do ozônio(O3): "))
        if O3 < 1:
                print("Digite numeros positivos!")
                sys.exit()
        else:
            if O3 >= 0 and O3 <= 100:
                calculo = 40 / 100
                calculo_final = calculo * O3
                print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar BOA""")
                print()
                print("Praticamente não há riscos à saúde")
            elif O3 > 100 and O3 <= 130:
                calculo_indice = 80 - 41
                calculo_concentracao =  130 - 100   
                calculo_2 = calculo_indice / calculo_concentracao
                calculo_3 = O3 - 100
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + 41
                print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar MODERADA""")
                print()
                print("""Pessoas de grupos sensíveis (crianças, idosos e 
pessoas com doenças respiratórias e cardíacas),
podem apresentar sintomas como tosse seca e
cansaço. A população, em geral, não é afetada.""")
            elif O3 > 130 and O3 <= 160:
                calculo_indice = 120 - 81
                calculo_concentracao =  160 - 130   
                calculo_2 = calculo_indice / calculo_concentracao
                calculo_3 = O3 - 130
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + 81
                print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar RUIM""")
                print()
                print("""Toda a população pode apresentar sintomas 
como tosse seca, cansaço, ardor nos olhos, nariz 
e garganta. Pessoas de grupos sensíveis 
(crianças, idosos e pessoas com doenças 
respiratórias e cardíacas), podem apresentar 
efeitos mais sérios na saúde.""")
            elif O3 > 160 and O3 <=200:
                calculo_indice = 200 - 121
                calculo_concentracao =  200 - 160
                calculo_2 = calculo_indice / calculo_concentracao
                calculo_3 = O3 - 160
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + 121
                print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar MUITO RUIM""")
                print()
                print("""Toda a população pode apresentar 
agravamento dos sintomas como tosse seca, 
cansaço, ardor nos olhos, nariz e garganta e
ainda apresentar falta de ar e respiração 
ofegante. Efeitos ainda mais graves à saúde de 
grupos sensíveis (crianças, idosos e pessoas 
com problemas cardiovasculares).""")
            
            else:
                print(f"É uma qualidade de ar PESSIMA")
                print()
                print("""Toda a população pode apresentar sérios riscos 
de manifestações de doenças respiratórias e 
cardiovasculares. Aumento de mortes prematuras 
em pessoas de grupos sensíveis.""")
            print()   
    except:
        print("ERRO! TOME CUIDADO DIGITE APENAS NUMEROS")
        sys.exit()
print("=" * 100)   
print()
def monoxido_carbono():
    try:
        MCO=float(input("Digite o valor do monóxido de carbono (CO): "))
        if MCO < 1:
                print("Digite numeros positivos!")
                sys.exit()
        else:
            if MCO >= 0 and MCO <= 9 :
                 calculo = 40 / 9
                 calculo_final = calculo * MCO
                 print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar BOA""")
                 print("Praticamente não há riscos à saúde")
            elif MCO > 9  and MCO <= 11:
                calculo_indice = 80 - 41
                calculo_concentracao =  11 - 9   
                calculo_2 = calculo_indice / calculo_concentracao
                calculo_3 = MCO - 9
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + 41
                print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar MODERADA""")
                print()
                print("""Pessoas de grupos sensíveis (crianças, idosos e "
pessoas com doenças respiratórias e cardíacas),
podem apresentar sintomas como tosse seca e
cansaço. A população, em geral, não é afetada.""")
            elif MCO > 11 and MCO <= 13:
                calculo_indice = 120 - 81
                calculo_concentracao =  13 - 11   
                calculo_2 = calculo_indice / calculo_concentracao
                calculo_3 = MCO - 11
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + 81
                print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar RUIM""")
                print()
                print("""Toda a população pode apresentar sintomas 
como tosse seca, cansaço, ardor nos olhos, nariz 
e garganta. Pessoas de grupos sensíveis 
(crianças, idosos e pessoas com doenças 
respiratórias e cardíacas), podem apresentar 
efeitos mais sérios na saúde.""")
            elif MCO > 13 and MCO <=15:
                calculo_indice = 200 - 121
                calculo_concentracao =  15 - 13
                calculo_2 = calculo_indice / calculo_concentracao
                calculo_3 = MCO - 13
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + 121
                print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar MUITO RUIM""")
                print()
                print("""Toda a população pode apresentar 
agravamento dos sintomas como tosse seca, 
cansaço, ardor nos olhos, nariz e garganta e 
ainda apresentar falta de ar e respiração 
ofegante. Efeitos ainda mais graves à saúde de 
grupos sensíveis (crianças, idosos e pessoas 
com problemas cardiovasculares).""")
                
            else:
                print(f"É uma qualidade de ar PESSIMA")
                print()
                print("""Toda a população pode apresentar sérios riscos 
de manifestações de doenças respiratórias e 
cardiovasculares. Aumento de mortes prematuras 
em pessoas de grupos sensíveis.""")
            print()   
    except:
        print("ERRO! TOME CUIDADO DIGITE APENAS NUMEROS")        
        sys.exit()
print("=" * 100)
print()
def dioxido_nitrogenio():
    try:
        NO2 = float(input("Digite o valor do dióxido de nitrogênio (NO2): "))
        if NO2 < 1:
                print("Digite numeros positivos!")
                sys.exit()
        else:
            if NO2 >= 0 and NO2 <= 200 :
                 calculo = 40 / 200
                 calculo_final = calculo * NO2
                 print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar BOA""")
                 print()
                 print("Praticamente não há riscos à saúde")
            elif NO2 > 200  and NO2 <= 240:
                calculo_indice = 80 - 41
                calculo_concentracao =  240 - 200  
                calculo_2 = calculo_indice / calculo_concentracao
                calculo_3 = NO2 - 200
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + 41
                print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar MODERADA""")
                print()
                print("""Pessoas de grupos sensíveis (crianças, idosos e 
pessoas com doenças respiratórias e cardíacas),
podem apresentar sintomas como tosse seca e
cansaço. A população, em geral, não é afetada.""")
            elif NO2 > 240 and NO2 <= 320:
                calculo_indice = 120 - 81
                calculo_concentracao =  320 - 240   
                calculo_2 = calculo_indice / calculo_concentracao
                calculo_3 = NO2 - 240
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + 81
                print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar RUIM""")
                print()
                print("""Toda a população pode apresentar sintomas 
como tosse seca, cansaço, ardor nos olhos, nariz 
e garganta. Pessoas de grupos sensíveis 
(crianças, idosos e pessoas com doenças 
respiratórias e cardíacas), podem apresentar 
efeitos mais sérios na saúde.""")
            elif NO2 > 320 and NO2 <=1130:
                calculo_indice = 200 - 121
                calculo_concentracao =  1130 - 320
                calculo_2 = calculo_indice / calculo_concentracao
                calculo_3 = NO2 - 320
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + 121
                print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar MUITO RUIM""")
                print()
                print("""Toda a população pode apresentar 
agravamento dos sintomas como tosse seca, 
cansaço, ardor nos olhos, nariz e garganta e
ainda apresentar falta de ar e respiração 
ofegante. Efeitos ainda mais graves à saúde de 
grupos sensíveis (crianças, idosos e pessoas 
com problemas cardiovasculares).""")
            
            else:
                print(f"É uma qualidade de ar PESSIMA")
                print()
                print("""Toda a população pode apresentar sérios riscos 
de manifestações de doenças respiratórias e 
cardiovasculares. Aumento de mortes prematuras 
em pessoas de grupos sensíveis.""")
            print() 
    except:
        print("ERRO! TOME CUIDADO DIGITE APENAS NUMEROS")   
        sys.exit()       
print("=" * 100)
print()
def dioxido_enxofre():
    try:
     SO2 = float(input("Digite o valor do dióxido de enxofre (SO2): "))
     if SO2 < 1:
        print("Digite numeros positivos!")
        sys.exit()
     else:
            if SO2 >= 0 and SO2 <= 20 :
                 calculo = 40 / 20
                 calculo_final = calculo * SO2
                 print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar BOA""")
                 print("Praticamente não há riscos à saúde")
            elif SO2 > 20 and SO2 <= 40:
                calculo_indice = 80 - 41
                calculo_concentracao =  40 - 20  
                calculo_2 = calculo_indice / calculo_concentracao
                calculo_3 = SO2 - 20
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + 41
                print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar MODERADA""")
                print("""Pessoas de grupos sensíveis (crianças, idosos e 
pessoas com doenças respiratórias e cardíacas),
podem apresentar sintomas como tosse seca e
cansaço. A população, em geral, não é afetada.""")
            elif SO2 > 40 and SO2 <= 365:
                calculo_indice = 120 - 81
                calculo_concentracao =  365 - 40   
                calculo_2 = calculo_indice / calculo_concentracao
                calculo_3 = SO2 - 40
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + 81
                print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar RUIM""")
                print()
                print("""Toda a população pode apresentar sintomas 
como tosse seca, cansaço, ardor nos olhos, nariz 
e garganta. Pessoas de grupos sensíveis 
(crianças, idosos e pessoas com doenças 
respiratórias e cardíacas), podem apresentar 
efeitos mais sérios na saúde.""")
            elif SO2 > 365 and SO2 <=800:
                calculo_indice = 200 - 121
                calculo_concentracao =  800 - 365
                calculo_2 = calculo_indice / calculo_concentracao
                calculo_3 = SO2 - 365
                calculo_4 = calculo_2 * calculo_3
                calculo_final = calculo_4 + 121
                print(f"""o resultado obtido é de {calculo_final}. 
É uma qualidade de ar MUITO RUIM""")
                print()
                print("""Toda a população pode apresentar 
agravamento dos sintomas como tosse seca, 
cansaço, ardor nos olhos, nariz e garganta e 
ainda apresentar falta de ar e respiração
ofegante. Efeitos ainda mais graves à saúde de 
grupos sensíveis (crianças, idosos e pessoas 
com problemas cardiovasculares).""")
            else:
                print(f"É uma qualidade de ar PESSIMA")
                print()
                print("""Toda a população pode apresentar sérios riscos 
de manifestações de doenças respiratórias e 
cardiovasculares. Aumento de mortes prematuras 
em pessoas de grupos sensíveis.""")
            print() 
    except:
        print("ERRO! TOME CUIDADO DIGITE APENAS NUMEROS")
        sys.exit()
print("=" * 100)
print()
def sair():
    print("saindo do algoritimo")
    sys.exit()

# def listar():
#     lista = [particulas_inalaveis(), particulas_inalaveis_fina(), ozonio(), monoxido_carbono(), dioxido_nitrogenio(), dioxido_enxofre()]
#     print(lista)

while True:
    particulas_inalaveis()
    particulas_inalaveis_fina()
    ozonio()
    monoxido_carbono()
    dioxido_nitrogenio()
    dioxido_enxofre()

    print()
    print("=" * 100)
    print("PARA SABER SE A QUALIDADE DO AR ESTÁ BOA OU NÃO, SEMPRE CONSIDERAR A PIOR QUALIDADE DE AR OBTIDA")
    print("=" * 100)
    print()
    print("selecione uma opcao!")
   
    pergunta = str(input("Quer continuar? s para sim - n para nao: "))
    
    if pergunta == "n" and "N":
         sair()
    
         
         
    elif pergunta == "s" and "S":
        print("Continuando para outro calculo")
        continue
