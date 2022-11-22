import time


def fakeClear():
    return print('\n' * 50)


def dados_pokemon(pokemon_selected):
    return f"Nome: {pokemon_selected['name']}\nVida: {pokemon_selected['life']}\nAtaque: {pokemon_selected['atack']}\nCura: {pokemon_selected['cure']} "


def statusTreinador():
    if my_pokemon is not 'Sem Pokémon':
        return f'{name_player} tem um {my_pokemon["name"]}'
    else:
        return f'{name_player} está {my_pokemon}'


def confirm():
    true_false = ''
    erro_select = True

    while erro_select:
        print(dados_pokemon(my_pokemon))
        print('confirmar sua escolha?')
        select = input('[S]im [N]ão\n').upper()
        if select == 'S':
            erro_select = False
            true_false = False
        elif select == 'N':
            erro_select = False
            true_false = True
        else:
            fakeClear()
            print('Comando inválido!')
        return true_false


charmeleon = {'name': 'Charmeleon', 'life': 140, 'atack': 45, 'cure': 50}
wartortle = {'name': 'Wartortle', 'life': 170, 'atack': 35, 'cure': 55}
ivysaur = {'name': 'Ivysaur', 'life': 120, 'atack': 50, 'cure': 50}
mewtwo = {'name': 'Mewtwo', 'life': 250, 'atack': 40}
my_pokemon = 'Sem Pokémon'
name_player = ''

confirm_select_pokemon = True
confirm_name = True
erro_name_player = True
reset = True

fakeClear()

print('Seja muito bem vindo a batalha pokemon.')
time.sleep(0.5)
print(f"Aqui você tera que derrotar o temivel {mewtwo['name']}")
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
    confirm1 = input('[S]im [N]ão\n').upper()

    if confirm1 == 'S':
        confirm_name = False
        time.sleep(0.5)
        fakeClear()
    elif confirm1 == 'N':
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
    select_pokemon = input('[A] Charmeleon\n[B] Wartortle\n[C] Ivysaur\n').upper()
    if select_pokemon == 'A':
        my_pokemon = charmeleon
        time.sleep(0.5)
        fakeClear()
        print()
        confirm_select_pokemon = confirm()
        if confirm_select_pokemon == True:
            my_pokemon = 'Sem Pokémon'
        fakeClear()

    elif select_pokemon == 'B':
        my_pokemon = wartortle
        time.sleep(0.5)
        fakeClear()
        print()
        confirm_select_pokemon = confirm()
        if confirm_select_pokemon == True:
            my_pokemon = 'Sem Pokémon'
        fakeClear()

    elif select_pokemon == 'C':
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
    print(f'pokemon {mewtwo["name"]} apareceu')
    print(f'nome: {mewtwo["name"]}\nvida:{mewtwo["life"]}\nAtaque: {mewtwo["atack"]}')
    print('\n' * 2)

    while my_pokemon['life'] > 0 and mewtwo['life'] > 0:
        print(f'{my_pokemon["name"]} vida {my_pokemon["life"]}')
        print('O que você deseja fazer?')
        move = input('[1]Atacar [2]Curar\n')
        time.sleep(0.5)

        if move == '1':
            mewtwo['life'] = mewtwo['life'] - my_pokemon['atack']
        elif move == '2':
            my_pokemon['life'] = my_pokemon['life'] + my_pokemon['cure']
        else:
            print('Seu Pokemon não entendeu o comando!')
        print('\n' * 2)
        time.sleep(0.5)
        fakeClear()

        if mewtwo['life'] > 0:
            print(f'{mewtwo["name"]} vida {mewtwo["life"]}')
            print(f'{mewtwo["name"]} atacou')
            my_pokemon['life'] = my_pokemon['life'] - mewtwo['atack']

    if my_pokemon['life'] <= 0:
        print('Você perdeu! :(')
    elif mewtwo['life'] <= 0:
        print(f'Parabens você derrotou o temivel {mewtwo["name"]}')

    print('Quer jogar novamente?')
    status_reset = input('[S]im [N]ão\n').upper()
    if status_reset == 'S':
        if my_pokemon['name'] == 'Charmeleon':
            my_pokemon = {'name': 'Charmeleon', 'life': 140, 'atack': 45, 'cure': 50}
        elif my_pokemon["name"] == 'Wartortle':
            my_pokemon = {'name': 'Wartortle', 'life': 170, 'atack': 35, 'cure': 55}
        elif my_pokemon["name"] == 'Ivysaur':
            my_pokemon = {'name': 'Ivysaur', 'life': 120, 'atack': 50, 'cure': 50}
        mewtwo = {'name': 'Mewtwo', 'life': 250, 'atack': 40}
        reset = reset
    elif status_reset == 'N':
        reset = False
    else:
        print('Comando inválido')

print('Obrigado por jogar Batalha pokemon.')