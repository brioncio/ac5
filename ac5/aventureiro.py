"""
Programação Estruturada
2024.1
18/03/2024

Estruturas de repetição
AC5
"""
import random

def main():
    aventureiro_vida = 100
    aventureiro_ataque = random.randint(10, 20)
    aventureiro_defesa = random.randint(1, 5)

    monstro_vida = random.randint(60, 80)
    monstro_ataque = random.randint(20, 30)
    
    cont = 0

    while aventureiro_vida > 0 and monstro_vida > 0:
        cont += 1

        print(f"Aventureiro: vida {aventureiro_vida} - att {aventureiro_ataque} - def {aventureiro_defesa}")
        print(f"Monstro: vida {monstro_vida} - att {monstro_ataque}")
        print(f"Rodada: {cont}")

        monstro_vida -= (random.randint(1, aventureiro_ataque))

        if monstro_vida <= 0:
            print("O monstro morreu!")
            break

        dano = random.randint(1, monstro_ataque) - aventureiro_defesa
        if dano > 0:
            aventureiro_vida -= dano

        if aventureiro_vida <= 0:
            print("O aventureiro morreu!")
            break


main()