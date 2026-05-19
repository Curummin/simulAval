with open ( "./lab01/dados.txt","r") as arq:
    dados = [ int ( linha . strip () ) for linha in arq if linha.strip () ]
    dados_ordenados = sorted (dados)
    media_simples = sum (dados) / len ( dados )
    valores_k = [2 , 4 , 6 , 8 , 10]
    medias_aparadas = []
    for k in valores_k :
        dados_aparados = dados_ordenados [ k : - k ]
        media_aparada = sum ( dados_aparados ) / len ( dados_aparados)
        medias_aparadas . append ( media_aparada )

    print (f" {'Media' : >10} " , end = " " )
    for k in valores_k :
        print (f" { f'k ={ k } ': >10} " , end = " " )
    print ()
    print (f"{media_simples :10.2f} " , end = " " )
    for media in medias_aparadas :
        print (f"{media :10.2f} " , end = " " )
    print ()


    
