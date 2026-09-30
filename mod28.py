def calcn(vala, mem):
    novo = 0.0
    if mem < 500.0 and vala < 30.0:
        novo = vala * 1.10
    elif mem < 1000 and vala < 80:
        novo = vala * 1.15
    elif mem > 999 and vala > 79:
        novo = vala * 0.95
    return novo

def main():
    va = mm = nv = 0.0
    va = int(input('insira o valor atual '))
    mm = int(input('insira a media mensal '))
    nv = calcn(va, mm)
    print('o novo valor do produto é ', nv, '.')
if (__name__=='__main__'):
    main()