## QUESTÃO 1 ##
#
# Um site exige que os usuários insiram nome de usuário e senha para se registrarem. 
# Escreva um programa para verificar se a senha digitada pelos usuários é forte o suficiente.
# A seguir estão os critérios para verificar a senha:
#
# 1. Pelo menos uma letra entre [a-z]
# 2. Pelo menos 1 número entre [0-9]
# 3. Pelo menos uma letra entre [A-Z]
# 4. Pelo menos 1 caractere de [$ # @]
# 5. Comprimento mínimo da senha: 6
# 6. Comprimento máximo da senha: 12
#
# Seu programa deve aceitar uma sequência de senhas separadas por vírgula e as verificará 
# de acordo com os critérios acima. As senhas que correspondem aos critérios devem ser 
# impressas, separadas por uma vírgula.
# Exemplo
# Se as seguintes senhas forem fornecidas como entrada para o programa:
# ABd1234 @ 1, um F1 #, 2w3E *, 2We3345
# Então, a saída do programa deve ser:
# ABd1234 @ 1
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    print("questao 1")
    
    senha = input('Digite as senhas separadas por virgula: ')
    senha = senha.split(',')
    senhas = []


    def alpha(senha):
        for x in senha:
            if x.isalpha() == True:
                return True


    def especial(senha):
        c1 = '@'
        c2 = '#'
        c3 = '$'
        for x in senha:
            if x == c1 or x == c2 or x == c3:
                return True


    def maiusculo(senha):
        for x in senha:
            if x.isupper() == True:
                return True


    def minusculo(senha):
        for x in senha:
            if x.islower() == True:
                return True


    def numero(senha):
        for x in senha:
            if x.isnumeric() == True:
                return True


    def tamanho(senha):
        lenx = len(senha)
        if lenx >= 6 and lenx <= 12:
            return True


    def all(senha):
        if alpha(senha) and numero(senha) and especial(senha) and maiusculo(senha) and minusculo(senha) and tamanho(senha):
            return True

    for palavra in senha :
            if all(palavra) == True:
                senhas.append(palavra)
            else:
                continue
    print(','.join(senhas))  


if __name__ == '__main__':
    main()
