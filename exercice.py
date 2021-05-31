#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number > 0:
        return number
    else: return -number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'

    return [""]


def prime_integer_summation(num=100) -> int:
    i = 2
    primes = [2]
    while len(primes)<num:
        for prime in primes:
            if i%prime == 0:
                #n'est pas premier
                break
            elif prime >= i//2:
                #est premier
                primes.append(i)
                break
        i+=1
    return sum(primes)


def factorial(number: int) -> int:
    temp = 1
    for i in range(1,number):
        temp*=i
    return temp


def use_continue() -> None:
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    evaluation = []
    for groupe in groups:
        groupe.sort()
        print(groupe)
        if len(groupe) not in range(4,9):
            evaluation.append(False)
        else:
            if 25 in groupe:
                evaluation.append(True)
                continue
            for membre in groupe:
                if membre < 18:
                    evaluation.append(False)
                    break
                elif membre > 70 and 50 in groupe:
                    evaluation.append(False)
                    break
            else:
                evaluation.append(True)
    return evaluation


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
