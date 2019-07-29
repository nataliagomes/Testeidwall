texto = 'No começo, Deus criou os céus e a terra. Agora a terra estava sem forma e vazia, a escuridão acabou a superfície das profundezas e o Espírito de Deus pairava sobre as águas.E Deus disse: "Haja luz", e houve luz. Deus viu que a luz foi bom, e ele separou a luz da escuridão. Deus chamou a luz"dia" e a escuridão que ele chamou "noite." E houve noite e houve manhã - o primeiro dia.'
#i = contador do while para ir de 40 em 40
i = 40
#j = pegar onde começa o ultimo caracter da linha
j = 39
#k = pegar onde termina o ultimo caracter da linha
k = 40
#l = indice onde vai começar a linha
l = 0

#vai ficar no loop até o i ser maior que o número de caracter do texto
while i<len(texto)+40:
    #defini uma variavel linha para ficar mais facil o controle
    linha = texto
    #se o ultimo caracter for diferente que um espaço(não tiver uma letra)
    if(linha[j:k]!=' '):
        #ira repetir até encontrar um espaço
        while linha[j:k]!=' ':
            #subtrair os indices em -1 para voltar um caracter
            j-=1
            k-=1
    #irá printar a linha
    print(linha[l:k])
    # irá definir o l(onde ira começar a proxima linha) para igual ao k(onde parou a linha)
    l=k
    # irá adcionar um intervalo de 40
    k+=40
    j+=40
    i += 40
#irá printar o resto que sobrou
print(texto[k-40:])
