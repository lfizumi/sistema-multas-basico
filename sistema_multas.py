# Sistema básico de controle de multas de trânsito

placa = input("Digite sua placa: ")
nome = input("Digite seu nome: ")

velocidade = float(input("Digite a velocidade em km/h: "))
velocidade_max = float(input("Digite a velocidade máxima da via em km/h: "))

multado_anteriormente = input("Já foi autuado anteriormente? Digite '1' para sim e '2' para não: ")
paga_na_hora = input("Deseja pagar agora? Digite '3' para sim e '4' para não: ")

if velocidade <= velocidade_max:
    print("\n", placa)
    print(nome)
    print("Velocidade Registrada:", velocidade, "km/h")
    print("Velocidade máxima permitida:", velocidade_max, "km/h")
    print("Nenhuma infração.")

# Infração leve: até 20% acima
elif velocidade <= 1.2 * velocidade_max:
    multa = 130.16
    desconto = 0.2 if paga_na_hora == "3" else 0
    valor_final = multa * (1 - desconto)

    print("\n", placa)
    print(nome)
    print("Velocidade Registrada:", velocidade, "km/h")
    print("Velocidade máxima permitida:", velocidade_max, "km/h")
    print("Infração leve - Multa de R$130,16, Nenhum ponto na CNH.")
    if paga_na_hora == "3":
        print("Pagamento realizado! Você recebeu um desconto de 20%. Valor final: R$", round(valor_final, 2))

# Infração grave: entre 20% e 50% acima
elif velocidade <= 1.5 * velocidade_max:
    multa = 195.23
    if multado_anteriormente == "1":
        multa *= 2
        print("Atenção: Multa dobrada por reincidência!")

    desconto = 0.2 if paga_na_hora == "3" else 0
    valor_final = multa * (1 - desconto)

    print("\n", placa)
    print(nome)
    print("Velocidade Registrada:", velocidade, "km/h")
    print("Velocidade máxima permitida:", velocidade_max, "km/h")
    print("Infração grave - Multa de R$195,23, 5 pontos na CNH.")
    if paga_na_hora == "3":
        print("Pagamento realizado! Você recebeu um desconto de 20%. Valor final: R$", round(valor_final, 2))

# Infração gravíssima: acima de 50%
else:
    multa = 880.41
    if multado_anteriormente == "1":
        multa *= 2
        print("Atenção: Multa dobrada por reincidência!")

    desconto = 0.2 if paga_na_hora == "3" else 0
    valor_final = multa * (1 - desconto)

    print("\n", placa)
    print(nome)
    print("Velocidade Registrada:", velocidade, "km/h")
    print("Velocidade máxima permitida:", velocidade_max, "km/h")
    print("Infração gravíssima - Multa de R$880,41, 7 pontos na CNH e suspensão da carteira.")
    print("Atenção: CNH suspensa! Compareça ao Detran.")
    print("Atenção: Você precisa fazer um curso de reciclagem no Detran.")
    if paga_na_hora == "3":
        print("Pagamento realizado! Você recebeu um desconto de 20%. Valor final: R$", round(valor_final, 2))
