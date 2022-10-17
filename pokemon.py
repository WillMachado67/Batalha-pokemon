import time


def fakeClear():
    return print('\n' * 50)


def dados_pokemon(pokemon_selected):
    return f"Nome: {pokemon_selected['name']}\nVida: {pokemon_selected['life']}\nAtaque: {pokemon_selected['atack']}\nCura: {pokemon_selected['cure']} "


def statusTreinador():
    if my_pokemon == charmeleon or my_pokemon == wartortle or my_pokemon == ivysaur:
        return f'{name_player} tem um {my_pokemon["name"]}'
    else:
        return f'{name_player} está {my_pokemon}'


def confirm():
    global confirm_select_pokemon
    erro_select = True
    while erro_select:
        print('confirmar sua escolha?')
        select = input('[S]im [N]ão\n').upper()
        if select == 'S':
            confirm_select_pokemon = False
            erro_select = False
            fakeClear()
        elif select == 'N':
            confirm_select_pokemon = confirm_select_pokemon
            erro_select = False
            fakeClear()
        else:
            print('Comando inválido!')
        fakeClear()


charmeleon = {'name': 'Charmeleon', 'life': 140, 'atack': 45, 'cure': 50}
wartortle = {'name': 'Wartortle', 'life': 170, 'atack': 35, 'cure': 55}
ivysaur = {'name': 'Ivysaur', 'life': 120, 'atack': 50, 'cure': 50}
mewtwo = {'name': 'Mewtwo', 'life': 250, 'atack': 40}
confirm_select_pokemon = True
confirm_name = True
my_pokemon = 'Sem Pokémon'
name_player = ''
erro_name_player = True

fakeClear()

print('Seja muito bem vindo a batalha pokemon.')
time.sleep(0.5)
print(f"Aqui você tera que derrotar o temivel {mewtwo['name']}")
time.sleep(0.8)
print()
print('Antes de começarmos, me diga seu nome.')
while confirm_name:
    while erro_name_player:
        name_player = input("Digite Seu nome: ")
        if len(name_player) < 4:
            fakeClear()
            print('Seu nome precisa de pelomenos 4 caracteres.')
        else:
            erro_name_player = False
    print('Tem certesa que esse é seu nome?')
    confirm1 = input('[S]im [N]ão\n').upper()
    if confirm1 == 'S':
        confirm_name = False
        time.sleep(0.5)
        fakeClear()
    elif confirm1 == 'N':
        erro_name_player = confirm_name
        time.sleep(0.5)
        fakeClear()
    else:
        fakeClear()
        print('comando invalido')
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
        print(dados_pokemon(my_pokemon))
        print()
        confirm()

    elif select_pokemon == 'B':
        my_pokemon = wartortle
        time.sleep(0.5)
        fakeClear()
        print(dados_pokemon(my_pokemon))
        print()
        confirm()
    elif select_pokemon == 'C':
        my_pokemon = ivysaur
        time.sleep(0.5)
        fakeClear()
        print(dados_pokemon(my_pokemon))
        print()
        confirm()
    else:
        time.sleep(0.5)
        print('Você não selecionou nenhum pokemon :(')
        fakeClear()

time.sleep(0.5)
print(statusTreinador())
print()
time.sleep(0.5)
print('Agora que você tem um pokémon, e hora de batalhar!')
time.sleep(0.5)
