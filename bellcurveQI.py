"""
https://www.ime.unicamp.br/~cnaber/tabela_normal.pdf
https://www.iqcomparisonsite.com/iqtable.aspx
https://www.thoughtco.com/normal-distribution-bell-curve-formula-3126278
https://trumpexcel.com/bell-curve/
"""

from scipy.stats import norm


def calcular_cdf(z):
    return norm.cdf(z)


insira_a_media = int(input("Qual é a média de QI: "))
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
            print(f"Oque te torna mais inteligente do que {pop:.0f} pessoas, ou {nova_porcentagem:.2f}% da "
                  f"população descrita na curva.")
            print(f"1 a cada {casos:.2f} pessoas tem um QI igual ou maior que o seu.")
        elif 0.000009 < porcentagem <= 0.009:
            print(f"Você está entre os {porcentagem:.5f}% mais inteligentes da curva.")
            print(f"Oque te torna mais inteligente do que {pop:.0f} pessoas, ou {nova_porcentagem:.5f}% da "
                  f"população descrita na curva.")
            print(f"1 a cada {casos:.2f} pessoas tem um QI igual ou maior que o seu.")
        elif porcentagem <= 0.000009:
            print(f"Você está entre os {porcentagem:.10f}% mais inteligentes da curva.")
            print(f"Oque te torna mais inteligente do que {pop:.0f} pessoas, ou {nova_porcentagem:.10f}% da "
                  f"população descrita na curva.")
            print(f"1 a cada {casos:.2f} pessoas tem um QI igual ou maior que o seu.")
    elif insira_o_qi < insira_a_media or insira_o_qi == insira_a_media:
        porcentagem = 100 - porcentagem
        nova_porcentagem = 100 - porcentagem
        pop = populacao - (populacao / casos)
        print(f"Você está entre os {porcentagem:.2f}% mais inteligentes da curva.")
        print(f"Oque te torna mais inteligente do que {pop:.0f} pessoas, ou {nova_porcentagem:.2f}% da "
              f"população descrita na curva.")
        print(f"1 a cada {casos:.4f} pessoas tem um QI igual ou maior que o seu.")
elif cdf >= 1:
    print("IMPOSSIVEL DE CALCULAR")
