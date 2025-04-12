import pyautogui
from time import sleep
# Script que vai abrir o spotify e tocar a musica pré-selecionada 

# Perguntando qual musica a pessoa quer antes de inical o programa

musica = str(input('Digite a musica que você quer escutar: ')).lower()

# Selecionando o time entre as ações 
pyautogui.PAUSE = 1



# Abrir o Spotify
pyautogui.press('win')
pyautogui.write('spotify')
pyautogui.press('enter')

# Digitando a musica no Spotify
pyautogui.click(x=776, y=130)
pyautogui.write(musica)

# Dando play no musicao
sleep(1)
pyautogui.click(x=808, y=363)


# Peguntando se gostaria de aumentar o som
while True:
    som = str(input('Gostaria de aumentar ou abaixar o som? [S/N] ')).lower()
    if som == 's':
        som1 = str(input('Digite (+) para aumentar ou (-) para diminuir: '))
        if som1 == '+':
            pyautogui.hotkey('alt', 'tab')
            pyautogui.hotkey('ctrl', 'up')
            while True:
                aum_mais = str(input('Gostaria de aumentar mais? [S/N] ')).lower()
                if aum_mais == 's':
                    pyautogui.hotkey('alt', 'tab')
                    pyautogui.hotkey('ctrl', 'up')
                elif aum_mais == 'n':
                    print('Ok! ')
                    break
        elif som1 == '-':
            pyautogui.hotkey('alt', 'tab')
            pyautogui.hotkey('ctrl', 'down')
            while True:
                dimi_mais = str(input('Gostaria de diminuir mais? [S/N] ')).lower()
                if dimi_mais == 's':
                    pyautogui.hotkey('alt', 'tab')
                    pyautogui.hotkey('ctrl', 'down')
                elif dimi_mais == 'n':
                    print('Ok! ')
                    break
    elif som == 'n':
        print('Ok! Aproveite a música 😁')
        break