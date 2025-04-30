import pyttsx3
import math

voz = pyttsx3.init()

def falar(texto):
    print(f"Resultado: {texto}")
    voz.say(texto)
    voz.runAndWait()

def menu():
    print("\n=== CALCULADORA AVANÇADA ===")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz quadrada")
    print("7. Porcentagem")
    print("0. Sair")

def calcular():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            falar("Encerrando a calculadora. Até mais!")
            break

        if opcao in ["1", "2", "3", "4", "5", "7"]:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = a + b
            falar(f"A soma é {resultado}")
        elif opcao == "2":
            resultado = a - b
            falar(f"A subtração é {resultado}")
        elif opcao == "3":
            resultado = a * b
            falar(f"A multiplicação é {resultado}")
        elif opcao == "4":
            if b == 0:
                falar("Erro! Divisão por zero.")
            else:
                resultado = a / b
                falar(f"A divisão é {resultado}")
        elif opcao == "5":
            resultado = a ** b
            falar(f"{a} elevado a {b} é {resultado}")
        elif opcao == "6":
            n = float(input("Digite o número: "))
            if n < 0:
                falar("Erro! Não existe raiz quadrada real de número negativo.")
            else:
                resultado = math.sqrt(n)
                falar(f"A raiz quadrada de {n} é {resultado}")
        elif opcao == "7":
            resultado = (a * b) / 100
            falar(f"{b}% de {a} é {resultado}")
        else:
            falar("Opção inválida.")

calcular()
