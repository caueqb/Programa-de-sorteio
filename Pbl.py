import random

participantes = []
quantidadeParticipantes = int(input('Digite a quantidade de participantes do sorteio: '))
for i in range(quantidadeParticipantes):
    participantes.append(input(f"Digite o nome da pessoa {i+1}: "))

print('')

premios = []
quantidadePremio = int(input('Digite a quantidade de prêmios a serem sorteados: '))
while (quantidadePremio > quantidadeParticipantes):
    print('A quantidade de prêmios não pode ser maior que a de participantes')
    quantidadePremio = int(input('Digite a quantidade de prêmios a serem sorteados: '))
for i in range(quantidadePremio):
    premios.append(input(f'Digite o prêmio {i+1}: '))

print('')

participantesSorteados = []
premiosSorteados = []
while (len(premios) != 0):
    participanteSorteado = random.choice(participantes)
    premioSorteado = random.choice(premios)
    participantesSorteados.append(participanteSorteado)
    premiosSorteados.append(premioSorteado)
    premios.remove(premioSorteado)
    participantes.remove(participanteSorteado)
    print(f'{participanteSorteado} ganhou o prêmio: {premioSorteado}')
    print('')
    input('Pressione Enter para continuar')
    print('')

print('Participantes sorteados:')
for i in participantesSorteados:
    print(f'- {i}' )

print('')

print('Prêmios sorteados:')
for i in premiosSorteados:
    print(f'- {i}')