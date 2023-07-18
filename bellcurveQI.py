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
#populacao = int(input("Insira a população: "))

Z = (insira_o_qi - insira_a_media) / 15
print("Z:", Z)
cdf = calcular_cdf(Z)
print("CDF:", cdf)
porcentagem = cdf * 100

if cdf < 1:
    novo_cdf = 1 - cdf
    if insira_o_qi > insira_a_media:

        porcentagem = 100 - porcentagem
        nova_porcentagem = 100 - porcentagem
        if porcentagem > 0.009:
            print(f"Você está entre os {porcentagem:.2f}% mais inteligentes da curva.")
        elif 0.000009 < porcentagem <= 0.009:
            print(f"Você está entre os {porcentagem:.5f}% mais inteligentes da curva.")
        elif porcentagem <= 0.000009:
            print(f"Você está entre os {porcentagem:.10f}% mais inteligentes da curva.")
    elif insira_o_qi < insira_a_media or insira_o_qi == insira_a_media:
        porcentagem = 100 - porcentagem
        nova_porcentagem = 100 - porcentagem
        print(f"Você está entre os {porcentagem:.2f}% mais inteligentes da curva.")
elif cdf >= 1:
    print("IMPOSSIVEL DE CALCULAR")
