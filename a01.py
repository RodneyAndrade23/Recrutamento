n1 = int(input('Jovem por favor informe em que ano você nasceu: '))
i1 = 2022 - n1
i2 = 18 - i1
i3 = i1 - 18

if i1 < 18:
    print('Ainda não está na hora de você se alistar! Você está com {} anos, ainda faltam {} anos até o seu alistamento militar.'.format(i1, i2))

elif i1 == 18:
    print('Já está na hora de você se alistar!!! Procure uma junta militar para se apresentar.')

else:
    print('Seu tempo de se apresentar expirou! Sua idade atual é de {} anos, o tempo correto de se alistar era a {} anos atrás!'.format(i1, i3))

