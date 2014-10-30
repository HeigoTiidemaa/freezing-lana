__author__ = 'heigo'

isikukood= str(input('Sisesta isikukood: '))

if not len(isikukood)==11:
    raise ValueError("Peaks olema 11 märki pikk")

kontrollnumbri_summa= (1*int(isikukood[0])+2*int(isikukood[1])+3*int(isikukood[2])+4*int(isikukood[3])+5*int(isikukood[4])
                +6*int(isikukood[5])+7*int(isikukood[6])+8*int(isikukood[7])+9*int(isikukood[8])+1*int(isikukood[9]))

kontrollnumbri_j22k= int(kontrollnumbri_summa) % 11

print(kontrollnumbri_j22k)
