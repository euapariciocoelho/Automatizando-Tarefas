# reproduzindo musica no Spotify
import pyautogui
from turtle import position
import time
#pyautogui.alert("O codigo esta rodando, não mexa em nada!")
pyautogui.PAUSE = 3.0
pyautogui.press('winleft')
pyautogui.write('edge')
pyautogui.press('enter')
# time.sleep(1) dorme por 1 seg
pyautogui.write('https://open.spotify.com/')
pyautogui.press('enter')

# pyautogui.hotkey('winleft', 'd') usa atalhos do mouse 
# pyautogui.hotkey(primeira tecla, segunda tecla)
'''pyautogui.write('spotify web')
pyautogui.press('enter')'''


''' como usar o mouse? 
deixa o mouse (seta) no local onde vai ser clicado
executa pyautogui.position (e vai mostrar a posição onde a seta está)

https://open.spotify.com/

'''
time.sleep(10)
pyautogui.moveTo(89, 249) # os valores são os que foram pegos no arquivo position

pyautogui.leftClick()
pyautogui.write('blackpink')
pyautogui.press('enter')

time.sleep(3)
pyautogui.moveTo(470, 375)
pyautogui.leftClick()

time.sleep(3)
pyautogui.moveTo(297, 496)
pyautogui.leftClick()


