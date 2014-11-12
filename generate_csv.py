import random
import Isikukood_kontrollnumber
import csv

header = ['social_security_number', 'forename', 'surname', 'gender', 'date_of_birth']
forenames = []
surnames = []

with open('names.txt', mode='r', encoding='UTF-8') as nimede_file:
    for line in nimede_file:
        forenames.append(line.split(',')[0].strip())
        try:
            surnames.append(line.split(',')[1].strip())
        except IndexError:
            continue


def forename():
    return random.choice(forenames)


def surname():
    return random.choice(surnames)


def gender(isikukood):
    if isikukood[0] in ('1', '3', '5'):
        return 'M'
    else:
        return 'F'


def date_of_birth(isikukood):
    date = isikukood[5:7] + '.'
    date += isikukood[3:5] + '.'
    if isikukood[0] in ('1', '2'):
        date += '18'
    elif isikukood[0] in ('3', '4'):
        date += '19'
    else:
        date += '20'
    date += isikukood[1:3]
    return date


with open('isikukoodide_csv.csv', mode='w', encoding='UTF-8', newline='') as isikukoodide_file:
    isikukoodide_csv = csv.writer(isikukoodide_file, delimiter=',')
    isikukoodide_csv.writerow(header)

    for i in range(1000000):
        isikukood = Isikukood_kontrollnumber.genereeri_isikukood()
        data = [isikukood, forename(), surname(), gender(isikukood), date_of_birth(isikukood)]
        isikukoodide_csv.writerow(data)

