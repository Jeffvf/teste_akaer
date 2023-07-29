def peca_faltante(pecas):
    pecas.sort()
    size = len(pecas)
    i = 1
    
    for peca in pecas:
        if peca != i:
            return i
        i += 1
    
    return i
    
def main():
    n = int(input(''))
    pecas = input('')
    
    arr_pecas = [int(peca) for peca in pecas.split(' ')]
    p = peca_faltante(arr_pecas)
    
    print(p)
    
if __name__ == '__main__':
    main()