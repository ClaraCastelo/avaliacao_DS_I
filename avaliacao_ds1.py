ruim = 1
bom = 2
execelente = 3

av_execelente = 0
av_ruim = 0
for i in range (50):
    input("nome: ")
    input("idade: ")
    print("1 = ruim, 2 = bom, 3 = excelente")
    opiniao = float(input("avalie: "))
    if opiniao == execelente: 
        av_execelente += 1
    elif opiniao == ruim:
        av_ruim +=  1
    
print("avaliações de execelente:", av_execelente)
print("avaliações de ruim:", av_ruim)



