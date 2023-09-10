from somma_di_punti import *
from point import point 
from prime_elliptic_curve import prime_elliptic_curve

# calcola Q = kP ove P appartiene alla curva ellittica prima Ep(a,b)
def raddoppi_ripetuti(P: point, k: int, curva_ellittica:prime_elliptic_curve):
    if k <= 0:
        print(f'ERRORE: non posso fare i raddoppi se k <= 0')
        return -1

    if curva_ellittica.p <= 0:
        print(f'ERRORE: non posso fare i raddoppi se p <= 0')
        return -1
    
    if appartiene_alla_curva(P, curva_ellittica.a, curva_ellittica.b, curva_ellittica.p) == False:
        print(f'ERRORE: il punto P = {P} non appartiene alla curva ellittica specificata!')
        return -1 

    bink = bin(k)[::-1][:-2]
    maxk = len(bink) # ceil(log(k, 2)) ma meno pesante 
    points = [P]

    for i in range(1, maxk):
        new = somma_di_punti(points[-1], points[-1], curva_ellittica.a, curva_ellittica.b, curva_ellittica.p)
        #print(f'{2**i}P = {new}')
        points.append(new)        

    #str = f'{k}P = '
    result = -1
    for i, digit in enumerate(bink):
        if(digit == '1'): 
            if result == -1: result = points[i]
            else: result = somma_di_punti(result, points[i], curva_ellittica.a, curva_ellittica.b, curva_ellittica.p)

            #str += f'{2**i}P + '

    #str = str[:-2] + f'= {result}'
    #print(str)
    return result

P = point(1, 2)
curva_scelta = prime_elliptic_curve(
    23, 
    14,
    12,
    point(),
    "my_curve"
)
k = 11

def main():
    raddoppi_ripetuti(P, k, curva_scelta)


if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()