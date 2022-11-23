import time

class Pokemon:
    def __init__(self, name=None, life=None, attack=None, cure=None):
        self.name = name
        self.life = life
        self.attack = attack
        self.cure = cure

def fakeClear():
    return print('\n' * 50)


def dados_pokemon(pokemon_selected):
    return f"Nome: {pokemon_selected.name}\nVida: {pokemon_selected.life}\nAtaque: {pokemon_selected.attack}\nCura: {pokemon_selected.cure} "


def statusTreinador():
    if my_pokemon is not 'Sem Pokémon':
        return f'{name_player} tem um {my_pokemon.name}'
    else:
        return f'{name_player} está {my_pokemon}'


def confirm():
    true_false = ''
    erro_select = True

    while erro_select:
        print(dados_pokemon(my_pokemon))
        print('confirmar sua escolha?')
        select = input('[1]Sim [2]Não\n')
        if select == '1':
            erro_select = False
            true_false = False
        elif select == '2':
            erro_select = False
            true_false = True
        else:
            fakeClear()
            print('Comando inválido!')
    return true_false


charmeleon = Pokemon(name='Charmeleon', life=140, attack=45, cure=50)
wartortle = Pokemon(name='Wartortle', life=170, attack=35, cure=55)
ivysaur = Pokemon(name='Ivysaur', life=120, attack=50, cure=50)
boss = Pokemon(name= 'Mewtwo', life=250, attack=40)
my_pokemon = 'Sem Pokémon'
name_player = ''

confirm_select_pokemon = True
confirm_name = True
erro_name_player = True
reset = True

fakeClear()

print('Seja muito bem vindo a batalha pokemon.')
time.sleep(0.5)
print(f"Aqui você tera que derrotar o temivel {boss.name}")
time.sleep(0.8)
print()
print('Antes de começarmos, me diga seu nome.')

while confirm_name:

    while len(name_player) < 4:
        name_player = input("Digite Seu nome: ")

        if len(name_player) < 4:
            fakeClear()
            print('Seu nome precisa de pelomenos 4 caracteres.')

    print('Tem certesa que esse é seu nome?')
    confirm1 = input('[1]Sim [2]Não\n')

    if confirm1 == '1':
        confirm_name = False
        time.sleep(0.5)
        fakeClear()
    elif confirm1 == '2':
        name_player = ''
        time.sleep(0.5)
        fakeClear()
    else:
        fakeClear()
        print('comando inválido')
        print(name_player)


print(f'Seja muito bem vindo {name_player}!')
print()


while confirm_select_pokemon:
    print(statusTreinador())
    print('Selecione seu pokemon: ')
    select_pokemon = input('[1] Charmeleon\n[2] Wartortle\n[3] Ivysaur\n')
    if select_pokemon == '1':
        my_pokemon = charmeleon
        time.sleep(0.5)
        fakeClear()
        print()
        confirm_select_pokemon = confirm()
        if confirm_select_pokemon == True:
            my_pokemon = 'Sem Pokémon'
        fakeClear()

    elif select_pokemon == '2':
        my_pokemon = wartortle
        time.sleep(0.5)
        fakeClear()
        print()
        confirm_select_pokemon = confirm()
        if confirm_select_pokemon == True:
            my_pokemon = 'Sem Pokémon'
        fakeClear()

    elif select_pokemon == '3':
        my_pokemon = ivysaur
        time.sleep(0.5)
        fakeClear()
        print()
        confirm_select_pokemon = confirm()
        if confirm_select_pokemon == True:
            my_pokemon = 'Sem Pokémon'
        fakeClear()

    else:
        time.sleep(0.5)
        fakeClear()
        print('Você não selecionou nenhum pokemon :(')

while reset:
    time.sleep(0.5)
    print(statusTreinador())
    print()
    time.sleep(0.5)
    print('Agora que você tem um pokémon, é hora de batalhar!')
    time.sleep(0.8)
    print()
    print(f'pokemon {boss.name} apareceu')
    print(f'nome: {boss.name}\nvida:{boss.life}\nAtaque: {boss.attack}')
    print('\n' * 2)

    while my_pokemon.life > 0 and boss.life > 0:
        print(f'{my_pokemon.name} vida {my_pokemon.life}')
        print('O que você deseja fazer?')
        move = input('[1]Atacar [2]Curar\n')
        time.sleep(0.5)
        fakeClear()

        if move == '1':
            boss.life = boss.life - my_pokemon.attack
        elif move == '2':
            my_pokemon.life = my_pokemon.life + my_pokemon.cure
        else:
            print('Seu Pokemon não entendeu o comando!')
        print('\n')
        time.sleep(0.5)

        if boss.life > 0:
            print(f'{boss.name} vida {boss.life}')
            print(f'{boss.name} atacou')
            my_pokemon.life = my_pokemon.life - boss.attack

    if my_pokemon.life <= 0:
        print('Você perdeu! :(')
    elif boss.life <= 0:
        print(f'Parabens você derrotou o temivel {boss.name}')
    
    reset2 = True
    while reset2:
        print('Quer jogar novamente?')
        status_reset = input('[1]Sim [2]Não\n')
        if status_reset == '1':
            if my_pokemon.name == 'Charmeleon':
                my_pokemon = Pokemon(name='Charmeleaon',life=140, attack=45, cure=50)
            elif my_pokemon.name == 'Wartortle':
                my_pokemon = Pokemon(name='Wartortle',life=170, attack=35, cure=55)
            elif my_pokemon.name == 'Ivysaur':
                my_pokemon = Pokemon(name='Ivsaur' ,life=120, attack=50, cure=50)
            boss = Pokemon(name='Mewtwo', life=250, attack=40)
            reset = reset
            reset2 = False
        elif status_reset == '2':
            reset = False
            reset2 = False
        else:
            print('Comando inválido')

print('Obrigado por jogar Batalha pokemon.')