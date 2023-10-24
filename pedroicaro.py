# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
print('Alistamento militar')
nascano =int(input("Digite seu ano de nascimento:"))
anoatual= int(input("Digite o ano atual: "))
if anoatual-nascano >18:
   print(f'Voçê passou da idade de se alistar, por favor procure um quartel para se alistar. Voçê está atrasado há {(anoatual-nascano)-18} ano(s):')
elif anoatual-nascano < 18:
     print(f'Voçê está não está idade exata de se alistar. Quanto tempo falta {18-(anoatual-nascano)} ano(s):')
else:
   print("Voçê está na idade exata de se alistar, por favor ALISTE-SE!: ")
