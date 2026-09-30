def velm(tamc, numv, temp):
    r = tp = 0.0
    tamc = tamc / 1000
    tp = numv * tamc
    temp = temp / 60
    r = tp/temp
    return r  

def main():
    vm = tc = nv = t = 0.0
    tc = int(input('insira o tamanho do circuito em metros: '))
    nv = int(input('insira o numero de voltas: '))
    t = int(input('insira o tempo em minutos: '))
    vm = velm(tc, nv, t)
    print('a volocidade media foi', vm, 'km/h.' )
if (__name__=='__main__'):
    main()
