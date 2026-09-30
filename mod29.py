def calcin(tip, vali):
    r =0.0
    if tip == 1:
        r = vali * 1.03
    elif tip == 2:
        r = vali * 1.05
        return r
def main():
    ti = 0
    vi = vc = 0.0
    ti = int(input('insira o tipo do investimento(1 = poupança 2= renda fixa) '))
    vi = int(input('insira o valor que deseja investir '))
    vc = calcin(ti, vi)
    print ('o valor após 30 dias será ', vc)
if (__name__ == '__main__'):
    main()