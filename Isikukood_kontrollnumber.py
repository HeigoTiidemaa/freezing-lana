__author__ = 'heigo'

esimese_astme_kaalud=[1,2,3,4,5,6,7,8,9,1]
teise_astme_kaalud=[]
def kontrollnumber(isikukood):
    esimene_jaak = moodul11(isikukood, esimese_astme_kaalud)#'esimene')
    if esimene_jaak != 10:
        return esimene_jaak
    teine_jaak = moodul11(isikukood, 'teine')

    if teine_jaak !=10:
        return teine_jaak
    else:
        return 0

def moodul11(isikukood, aste):
    if aste == 'esimene':
        kontrollnumbri_summa= (1*int(isikukood[0])+2*int(isikukood[1])+3*int(isikukood[2])+4*int(isikukood[3])+5*int(isikukood[4])
                +6*int(isikukood[5])+7*int(isikukood[6])+8*int(isikukood[7])+9*int(isikukood[8])+1*int(isikukood[9]))
        return int(kontrollnumbri_summa) % 11
    else:
        kontrollnumbri_summa= (3*int(isikukood[0])+4*int(isikukood[1])+5*int(isikukood[2])+6*int(isikukood[3])+7*int(isikukood[4])
                +8*int(isikukood[5])+9*int(isikukood[6])+1*int(isikukood[7])+2*int(isikukood[8])+3*int(isikukood[9]))
        return int(kontrollnumbri_summa) % 11   