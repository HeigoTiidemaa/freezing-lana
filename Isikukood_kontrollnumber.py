# -*- coding: utf-8 -*-
__author__ = 'heigo'
import random


def sajand():
    return str(random.randint(1, 6))


def sünniaeg():
    aasta = str(random.randint(0, 99)).zfill(2)
    kuu = str(random.randint(0, 12)).zfill(2)
    päev = str(random.randint(0, 28)).zfill(2)
    return aasta + kuu + päev


def järjekorra_number():
    return str(random.randint(0, 999)).zfill(3)


def genereeri_isikukood():
    isikukood = sajand() + sünniaeg() + järjekorra_number()
    isikukood = isikukood + str(kontrollnumber(isikukood))
    return isikukood


def kontrollnumber(isikukood):
    esimese_astme_kaalud = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    teise_astme_kaalud = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    esimene_jaak = moodul11(isikukood, esimese_astme_kaalud)
    if esimene_jaak != 10:
        return esimene_jaak
    teine_jaak = moodul11(isikukood, teise_astme_kaalud)

    if teine_jaak != 10:
        return teine_jaak
    else:
        return 0


def moodul11(isikukood, kaalud):
    summa = 0
    for i in range(10):
        summa += int(isikukood[i]) * kaalud[i]
    return summa % 11


if __name__ == '__main__':
    print(genereeri_isikukood())