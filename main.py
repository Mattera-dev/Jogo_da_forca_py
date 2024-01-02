import re
import random




def main():
    lista_palavras = [
    {'palavra': 'python', 'letras': 6, 'dica': 'Linguagem de programação'},
    {'palavra': 'alegria', 'letras': 7, 'dica': 'Sentimento positivo'},
    {'palavra': 'felicidade', 'letras': 10, 'dica': 'Estado de contentamento'},
    {'palavra': 'sol', 'letras': 3, 'dica': 'Fonte de luz'},
    {'palavra': 'abraco', 'letras': 6, 'dica': 'Expressão de afeto'},
    {'palavra': 'amizade', 'letras': 8, 'dica': 'Relação de carinho'},
    {'palavra': 'harmonia', 'letras': 8, 'dica': 'Equilíbrio e paz'},
    {'palavra': 'sucesso', 'letras': 7, 'dica': 'Realização positiva'},
    {'palavra': 'sorriso', 'letras': 7, 'dica': 'Expressão facial alegre'},
    {'palavra': 'serenidade', 'letras': 10, 'dica': 'Tranquilidade e paz interior'},
    {'palavra': 'gentileza', 'letras': 8, 'dica': 'Atitude amável'},
    {'palavra': 'tranquilidade', 'letras': 13, 'dica': 'Estado de calma'},
    {'palavra': 'paz', 'letras': 3, 'dica': 'Ausência de conflitos'},
    {'palavra': 'esperanca', 'letras': 9, 'dica': 'Sentimento de otimismo'},
    {'palavra': 'respeito', 'letras': 8, 'dica': 'Consideração pelo próximo'},
    {'palavra': 'gratidao', 'letras': 8, 'dica': 'Sentimento de reconhecimento'},
    {'palavra': 'amor', 'letras': 4, 'dica': 'Sentimento afetuoso'},
    {'palavra': 'criatividade', 'letras': 12, 'dica': 'Faculdade de criar'},
    {'palavra': 'alegre', 'letras': 6, 'dica': 'De bom humor'},
    {'palavra': 'compaixao', 'letras': 9, 'dica': 'Sentimento de compreensão'},
    {'palavra': 'otimismo', 'letras': 8, 'dica': 'Crença no melhor'},
    {'palavra': 'sabedoria', 'letras': 8, 'dica': 'Conhecimento e discernimento'},
    {'palavra': 'humildade', 'letras': 8, 'dica': 'Modéstia e simplicidade'},
    {'palavra': 'solidariedade', 'letras': 13, 'dica': 'Apoio mútuo'},
    {'palavra': 'energia', 'letras': 6, 'dica': 'Força vital'},
    {'palavra': 'vitalidade', 'letras': 10, 'dica': 'Energia e vitalidade'},
    {'palavra': 'equilibrio', 'letras': 9, 'dica': 'Estado de estabilidade'},
    {'palavra': 'uniao', 'letras': 4, 'dica': 'Ato de estar junto'},
    {'palavra': 'saudavel', 'letras': 8, 'dica': 'Bom para a saúde'},
]
    rand = random.randint(0, (len(lista_palavras) - 1))
    chances = (lista_palavras[rand]['letras'] + 1) 
    dica = lista_palavras[rand]['dica']
    aviso = ''
    palavra = lista_palavras[rand]['palavra']
    letras_usadas = []
    ganhou = 0
    
    while ganhou == 0 and chances > 0:
        if letras_usadas != []:
            letras_usadas_str = re.sub("[\[\],\s\']", '', str(letras_usadas))
            letras_usadas_aux = f'[^{re.escape(letras_usadas_str)}]'
        else:
            letras_usadas_aux = '[a-zA-Z]'
        print("\033c", end="")     
        palavra_escondida = re.sub(letras_usadas_aux ,'_ ', palavra)
        if palavra == palavra_escondida:
                    ganhou = 1
                    continue
        print(f'Chances restantes [{chances}]')
        print(f'Dica da palavra: {dica}')
        print(f'Letras usadas: ', end='')
        if letras_usadas != []:
            for i in letras_usadas: 
                print(i.upper(), end=' ')
        else:
            print('\n')
            
        print('\n\n', palavra_escondida)
        if aviso != '':
            print(aviso)
        opt = input('\nDigite uma letra: ').lower()
        if len(opt) == 1:    
            if numero(opt):
                aviso = "Selecione apenas letras!"
                continue
            elif verificarepetido(opt, letras_usadas):
                aviso = 'Letra repetida, por favor selecione outra!'
            elif (re.findall(opt, palavra)) == []:
                chances -= 1
                aviso = 'A letra selecionada nao existe dentro da palavra misteriosa!'
                letras_usadas += opt
            else:
                letras_usadas += opt
                
        elif len(opt) == 0:
            aviso = ("Voce precisa selecionar uma letra para jogar")
        else:
            aviso = "Selecione apenas uma letra por vez!"
    if ganhou == 1:
        print(f'\033cVoce Ganhou! a palavra era "{palavra}"')
    else:
        print(f'\033cVoce perdeu! a palavra era "{palavra}"')
    repetir = input('\nDeseja jogar novamente? (y/n)').lower()
    if repetir == 'y':
        main()
    elif repetir == 'n':
        print('Jogo finalizado!')
    else:
        print('Opcao invalida, Abortando jogo!')

def numero(opt):
    try:
        if int(opt) > -1:
            return True
    except ValueError:
        return False
    
def verificarepetido(opt: str, usadas: list):
    try:
        if usadas.index(opt) != '':
            return True
    except ValueError:
        return False

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\033c \n abortado pelo usuario!')
    