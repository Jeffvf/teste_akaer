def n_pares(esq, dir):
    count = 0
    for bota in esq:
        if bota in dir:
            count+= 1
    
    return count

def main():
    while True:
        try:
            n = int(input(''))
                
            esq = []
            dir = []
            for i in range(n):
                m, l = input('').split(' ')
                m = int(m)
                if l == 'D':
                    dir.append(m)
                else:
                    esq.append(m)
            
            count = n_pares(esq, dir)
            print(count)
        except EOFError:
            break

if __name__ == '__main__':
    main()