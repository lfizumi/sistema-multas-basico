# Sistema básico de controle de multas de trânsito

def calcular_multa(valor_base, pontos, descricao, multado_anteriormente, paga_na_hora):
    # Aplica multa dobrada se for reincidente
    if multado_anteriormente == "1":
        valor_base *= 2
        print("Atenção: Multa dobrada por reincidência!")

    valor_final = valor_base
    if paga_na_hora == "3":
        valor_final *= 0.8
        desconto_texto = f"Pagamento realizado! Você recebeu um desconto de 20%. Valor final: R$ {round(valor_final, 2)}"
    else:
        desconto_texto = ""

    print("\nInfração " + descricao)
    print(f"Multa de R$ {round(valor_base, 2)}, {pontos} pontos na CNH.")
    if desconto_texto:
        print(desconto_texto)

    return valor_final

# Entrada de dados
placa = input("Digite sua placa: ")
nome = input("Digite seu nome: ")

velocidade = float(input("Digite a velocidade em km/h: "))
velocidade_max = float(input("Digite a velocidade máxima da via em km/h: "))

multado_anteriormente = input("Já foi autuado anteriormente? Digite '1' para sim e '2' para não: ")
paga_na_hora = input("Deseja pagar agora? Digite '3' para sim e '4' para não: ")

# Impressão comum
print("\n", placa)
print(nome)
print("Velocidade Registrada:", velocidade, "km/h")
print("Velocidade máxima permitida:", velocidade_max, "km/h")

# Avaliação da infração
if velocidade <= velocidade_max:
    print("Nenhuma infração.")

elif velocidade <= 1.2 * velocidade_max:
    calcular_multa(130.16, 0, "leve", multado_anteriormente, paga_na_hora)

elif velocidade <= 1.5 * velocidade_max:
    calcular_multa(195.23, 5, "grave", multado_anteriormente, paga_na_hora)

else:
    calcular_multa(880.41, 7, "gravíssima", multado_anteriormente, paga_na_hora)
    print("Atenção: CNH suspensa! Compareça ao Detran.")
    print("Atenção: Você precisa fazer um curso de reciclagem no Detran.")

    print("Atenção: Você precisa fazer um curso de reciclagem no Detran.")
    if paga_na_hora == "3":
        print("Pagamento realizado! Você recebeu um desconto de 20%. Valor final: R$", round(valor_final, 2))
