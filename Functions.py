class func:
    """
    Classe de funções da aplicação voltada a manipular os elementos do alfabeto
    """

    def fatorial(n):
        """
        Calcular fatorial

        n*n-1*n-2...
        """
        if n < 0: return
        def fat(_):
            if _ < 1: return 1
            return _ * fat(_ - 1)
        return fat(n)

    def QtdCombinacoes(n, k):
        """
        Calcula A quantidade de combinações possiveis

        se n<k: n^k

        se n>k: (n!/(n-k)!)+n

        n = quantidade de elementos

        k = Quantidade de posições
        """
        if n < k: return int(n ** k)
        return int((func.fatorial(n) / (func.fatorial(n - k))) + n)

    def ImprimirPalavras(list):
        """
        Imprime a lista de palavras recebida

        -
        """
        for _ in range(len(list)):
            palavra = ''
            for c in list[_]:
                palavra += c
            print('{0}º palavra: {1}'.format((_+1), palavra))

    def somar(indice, palavra, alf):
        if palavra[indice] < alf - 1:
            palavra[indice] += 1
        else:
            palavra[indice] = 0
            return func.somar(indice - 1, palavra, alf)
        return palavra

    def palavras(alf_, carac_, palav_):
        palavras = [[0] * carac_]
        OutPalavras = [[0] * carac_] * palav_
        for _ in range(1, palav_):
            palavras.append(palavras[_ - 1])
            r = func.somar(carac_ - 1, palavras[_], len(alf_))
            OutPalavras[_] = list(r)
        return OutPalavras

    def produto(alf, carac, palav):
        """
        Retorn uma lista de palavras de acordo com os parametros definidos

        :param alf: Caracteres do alfabeto
        :param carac: Quantidade de caractere por palavra
        :param palav: Quantidade de palavras
        """
        l = func.palavras(alf, carac, palav)
        Palavras = [[str()] * carac] * palav
        for _ in range(len(l)):
            lis = [''] * carac
            for e in range(len(l[_])):
                lis[e] = alf[l[_][e]]
            Palavras[_] = list(lis)
        return Palavras