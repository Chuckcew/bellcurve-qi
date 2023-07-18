"""
https://www.ime.unicamp.br/~cnaber/tabela_normal.pdf
https://www.iqcomparisonsite.com/iqtable.aspx
https://www.thoughtco.com/normal-distribution-bell-curve-formula-3126278
https://trumpexcel.com/bell-curve/
"""


from scipy.stats import norm


def calcular_cdf(z):
    return norm.cdf(z)


variavel = input("Select 'e' for english. \n"
                 "Selecione 'p' para português \n"
                 "> ")
x = True

while x is True:
    if variavel == 'p':
        insira_a_media = int(input("Qual é a média de QI para o estudo: "))
        insira_o_qi = int(input("Qual o seu QI: "))
        populacao = int(input("Insira a população: "))

        Z = (insira_o_qi - insira_a_media) / 15
        print("Z:", Z)
        cdf = calcular_cdf(Z)
        print("CDF:", cdf)
        porcentagem = cdf * 100

        if cdf < 1:
            novo_cdf = 1 - cdf
            casos = (populacao / (populacao * novo_cdf))
            if insira_o_qi > insira_a_media:

                porcentagem = 100 - porcentagem
                nova_porcentagem = 100 - porcentagem
                pop = populacao - (populacao / casos)
                if porcentagem > 0.009:
                    print(f"Você está entre os {porcentagem:.2f}% mais inteligentes da curva.")
                    print(f"Oque te torna mais inteligente do que ≅{pop:.0f} pessoas, ou {nova_porcentagem:.2f}% da "
                          f"população descrita na curva.")
                    print(f"1 a cada {casos:.2f} pessoas tem um QI igual ou maior que o seu.")
                elif 0.000009 < porcentagem <= 0.009:
                    print(f"Você está entre os {porcentagem:.5f}% mais inteligentes da curva.")
                    print(f"Oque te torna mais inteligente do que ≅{pop:.0f} pessoas, ou {nova_porcentagem:.5f}% da "
                          f"população descrita na curva.")
                    print(f"1 a cada {casos:.2f} pessoas tem um QI igual ou maior que o seu.")
                elif porcentagem <= 0.000009:
                    print(f"Você está entre os {porcentagem:.10f}% mais inteligentes da curva.")
                    print(f"Oque te torna mais inteligente do que ≅{pop:.0f} pessoas, ou {nova_porcentagem:.10f}% da "
                          f"população descrita na curva.")
                    print(f"1 a cada {casos:.2f} pessoas tem um QI igual ou maior que o seu.")
            elif insira_o_qi < insira_a_media or insira_o_qi == insira_a_media:
                porcentagem = 100 - porcentagem
                nova_porcentagem = 100 - porcentagem
                pop = populacao - (populacao / casos)
                print(f"Você está entre os {porcentagem:.2f}% mais inteligentes da curva.")
                print(f"Oque te torna mais inteligente do que ≅{pop:.0f} pessoas, ou {nova_porcentagem:.2f}% da "
                      f"população descrita na curva.")
                print(f"1 a cada {casos:.4f} pessoas tem um QI igual ou maior que o seu.")
        elif cdf >= 1:
            print("IMPOSSIVEL DE CALCULAR. ERRO = CDF > 1")
        y = input("\nPressione 's' para sair ou qualquer outro caractere para continuar: ")
        if y == 's':
            x = False
        print('---------------------------------------------------------------\n')
    elif variavel == "e":
        insira_a_media = int(input("What is the average IQ for the study: "))
        insira_o_qi = int(input("What is your IQ: "))
        populacao = int(input("Insert the population: "))

        Z = (insira_o_qi - insira_a_media) / 15
        print("Z:", Z)
        cdf = calcular_cdf(Z)
        print("CDF:", cdf)
        porcentagem = cdf * 100

        if cdf < 1:
            novo_cdf = 1 - cdf
            casos = (populacao / (populacao * novo_cdf))
            if insira_o_qi > insira_a_media:

                porcentagem = 100 - porcentagem
                nova_porcentagem = 100 - porcentagem
                pop = populacao - (populacao / casos)
                if porcentagem > 0.009:
                    print(f"You are among the top {porcentagem:.2f}% most intelligent on the curve.")
                    print(f"Which makes you more intelligent than ≅{pop:.0f} individuals, or {nova_porcentagem:.2f}% of "
                          f"the population described in the curve.")
                    print(f"1 in every {casos:.2f} people have an IQ equal to or greater than yours.")
                elif 0.000009 < porcentagem <= 0.009:
                    print(f"You are among the top {porcentagem:.5f}% most intelligent on the curve.")
                    print(f"Which makes you more intelligent than ≅{pop:.0f} people, or {nova_porcentagem:.5f}% of the "
                          f"population described in the curve.")
                    print(f"1 in every {casos:.2f} people has an IQ equal to or greater than yours.")
                elif porcentagem <= 0.000009:
                    print(f"You are among the top {porcentagem:.10f}% most intelligent on the curve.")
                    print(f"Which makes you more intelligent than ≅{pop:.0f} people, or {nova_porcentagem:.10f}% of the "
                          f"population described in the curve.")
                    print(f"1 in every {casos:.2f} people has an IQ equal to or greater than yours.")
            elif insira_o_qi < insira_a_media or insira_o_qi == insira_a_media:
                porcentagem = 100 - porcentagem
                nova_porcentagem = 100 - porcentagem
                pop = populacao - (populacao / casos)
                print(f"You are among the top {porcentagem:.2f}% most intelligent on the curve.")
                print(f"Which makes you more intelligent than ≅{pop:.0f} people, or {nova_porcentagem:.2f}% of the "
                        f"population described in the curve.")
                print(f"1 in every {casos:.4f} people has an IQ equal to or greater than yours.")
        elif cdf >= 1:
            print("IMPOSSIBLE TO CALCULATE. ERROR = 'CDF > 1'")
        y = input("\nPress 's' to exit or any other character to continue: ")
        if y == 's':
            x = False
        print('---------------------------------------------------------------\n')
    else:
        print("An error occurred, please select only 'e' or 'p'. \n"
              "Um erro ocorreu, por favor selecione apenas 'e' ou 'p'.")
        x = False
