# Importa o módulo random
import random

# Cria as variáveis para as estatísticas de saúde do tamagotchi
felicidade = 100
energia = 100
limpeza = 100

# Cria uma variável aleatória para a característica principal do tamagotchi
caracteristica = random.choice(["bravo", "fofo", "bobo", "patético", "gentil", "enjoado", "esperto", "leal", "estranho", "hiperativo", "safado"])

# Cria a variável de imagem do tamagotchi gato
gato = '''
 /\_/\ 
( o.o )
 > ^ <
'''

# Cria a variável de imagem do tamagotchi coelho
coelho = '''
 (\\(\\ 
 ( -.-) 
 o_(")(")
'''

# Cria a variável de imagem do tamagotchi cachorro
cachorro = '''
 / \\__
(    @\\____
 /         O
/   (_____/
/_____/   U
'''

# Pergunta ao usuário o nome que deseja dar ao tamagotchi
nome = input("Qual nome você quer dar ao seu tamagotchi? ")

# Mensagem para o usuário com o nome que ele escolheu para o tamagotchi
print("Você escolheu nomear seu tamagotchi de " + nome + "!")

# Pergunta ao usuário qual animal ele quer que o tamagotchi seja
print("Qual animal você gostaria que seu tamagotchi fosse?")

# Lista as opções de animais para o usuário escolher
print("1. Coelho")
print("2. Gato")
print("3. Cachorro")

# Pergunta qual dos animais ele gostaria de escolher
resposta = int(input("Qual você gostaria de escolher? "))

# Se a resposta for igual a 1, seleciona o coelho como o animal de estimação do usuário
if resposta == 1:
    print("Você selecionou Coelho!")
    animal = coelho
    print(animal)
    tipo = "Coelho"

# Se a resposta for igual a 2, seleciona o gato como o animal de estimação do usuário
elif resposta == 2:
    print("Você selecionou Gato!")
    animal = gato
    print(animal)
    tipo = "Gato"

# Se a resposta for igual a 3, seleciona o cachorro como o animal de estimação do usuário
elif resposta == 3:
    print("Você selecionou Cachorro!")
    animal = cachorro
    print(animal)
    tipo = "Cachorro"

# Exibe uma mensagem do tamagotchi mostrando o nome, característica e tipo.
print("Olá, meu nome é " + nome + ". Eu sou um " + caracteristica + " " + tipo + "!")

# Exibe mais algumas mensagens para o usuário
print("Seu trabalho é cuidar de mim!")
print("Você terá um painel de como estou me sentindo!")

# Cria o loop do painel de controle
for numero in range(300000000):
    
    if felicidade < 1:
        print("Seu " + tipo + " morreu porque ficou muito triste")
        break
    
    if energia < 1:
        print("Seu " + tipo + " morreu porque ficou muito cansado!")
        break
    
    if limpeza < 1:
        print("Seu " + tipo + " morreu porque ficou muito sujo!")
        break
    
    # Imprime a imagem do animal
    print(animal)
    
    # Imprime as diferentes estatísticas de saúde do animal
    print("1. Minha felicidade está em " + str(felicidade) + "% ")
    print("2. Minha energia está em " + str(energia) + "% ")
    print("3. Minha limpeza está em " + str(limpeza) + "% ")
    
    # Pergunta ao usuário uma configuração do painel. 1,2,3
    painel = int(input("Qual você gostaria de escolher? "))
    
    # Menu de felicidade
    if painel == 1:
        print(" ")
        print("Você selecionou o menu de felicidade!")
        print("1. Levar para passear.")
        print("2. Acariciar.")
        print("3. Alimentar.")
        menu_felicidade = int(input("Selecione uma opção. "))
        
        if menu_felicidade == 1:
            print("Você levou seu " + tipo + " para passear")
            evento = random.randint(1, 3)
            if evento == 1 or evento == 2:
                felicidade += 10
                print("Seu passeio foi um sucesso e agora seu " + tipo + " ganhou 10% de felicidade!")
            if evento == 3:
                felicidade -= 40
                print("No passeio, seu " + tipo + " comeu um graveto, o veterinário conseguiu resolver, mas ainda dói! -40 felicidade!")
            
        elif menu_felicidade == 2:
            print("Você escolheu acariciar seu " + tipo + ". ")
            evento = random.randint(1, 3)
            if evento == 1 or evento == 2:
                felicidade += 10
                print("Você acariciou seu " + tipo + " com sucesso! +10% felicidade!")
            if evento == 3:
                felicidade -= 40
                print("Durante o carinho, você recebeu uma ligação urgente e teve que sair. Agora seu " + tipo + " acha que você não o ama! -40 felicidade!")
                
        elif menu_felicidade == 3:
            print("Você escolheu alimentar seu " + tipo + ". ")
            evento = random.randint(1, 3)
            if evento == 1 or evento == 2:
                felicidade += 10
                print("Você alimentou seu " + tipo + " com sucesso! +10% felicidade!")
            if evento == 3:
                felicidade -= 40
                print("Enquanto alimentava seu " + tipo + ", ele começou a engasgar. Você conseguiu ajudar, mas ele ficou traumatizado. -40 felicidade!")
    
    elif painel == 2:
        print(" ")
        print("Você selecionou o menu de energia!")
        print("1. Dar doces!")
        print("2. Levar à academia animal.")
        print("3. Alimentar.")
        menu_energia = int(input("Selecione uma opção. "))
        
        if menu_energia == 1:
            print("Você decidiu dar doces para seu " + tipo + ". ")
            print("Seu " + tipo + " passou mal com os doces. -50 em todas as estatísticas!")
            felicidade -= 50
            energia -= 50
            limpeza -= 50
            
        elif menu_energia == 2:
            print("Você escolheu levar seu " + tipo + " à academia. ")
            evento = random.randint(1, 3)
            if evento == 1 or evento == 2:
                energia += 10
                print("Na academia, seu " + tipo + " ganhou músculos e está cheio de energia! +10 energia!")
            if evento == 3:
                energia -= 40
                print("Na academia, um peso caiu em seu " + tipo + ". -40 energia!")
        
        elif menu_energia == 3:
            print("Você escolheu alimentar seu " + tipo + ". ")
            evento = random.randint(1, 3)
            if evento == 1 or evento == 2:
                energia += 10
                print("Você alimentou seu " + tipo + " com sucesso! +10% energia!")
            if evento == 3:
                energia -= 40
                print("Seu " + tipo + " começou a engasgar ao comer. Você conseguiu ajudar, mas ele ficou assustado. -40 energia!")
    
    elif painel == 3:
        print(" ")
        print("Você selecionou o menu de limpeza!")
        print("1. Dar banho!")
        print("2. Pentear")
        print("3. Cortar o pelo.")
        menu_limpeza = int(input("Selecione uma opção. "))
        
        if menu_limpeza == 1:
            if tipo == "Gato":
                print("Gatos não gostam de água! -30 felicidade, mas +10 limpeza!")
                limpeza += 10
                felicidade -= 30
            else:
                limpeza += 10
                print("Você limpou seu " + tipo + " com sucesso! +10 limpeza!")
                
        elif menu_limpeza == 2:
            print("Você escolheu pentear seu " + tipo + ". ")
            evento = random.randint(1, 3)
            if evento == 1 or evento == 2:
                limpeza += 10
                print("Você penteou seu " + tipo + " com sucesso! +10% limpeza!")
            if evento == 3:
                felicidade -= 40
                limpeza -= 40
                print("O pelo do seu " + tipo + " ficou embaraçado! -40 felicidade e limpeza!")
        
        elif menu_limpeza == 3:
            print("Você escolheu cortar o pelo do seu " + tipo + ". ")
            evento = random.randint(1, 3)
            if evento == 1 or evento == 2:
                limpeza += 10
                print("Você cortou o pelo do seu " + tipo + " com sucesso! +10% limpeza!")
            if evento == 3:
                limpeza -= 40
                felicidade -= 40
                print("Você se empolgou e deixou seu " + tipo + " careca! Agora ele está sempre com frio! -40 felicidade e limpeza!")
    
    else:
        print("Entrada inválida, selecione outra opção.")