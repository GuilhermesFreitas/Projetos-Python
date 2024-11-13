import pyautogui as auto
import time
# vai esperar meio segundo para fazer as tarefas
auto.PAUSE=1
#para apertar alguma tecla
auto.press('win')
#para escrever
auto.write("Spotify")
#para apertar a tecla enter(caixa alta)
auto.press('ENTER')

# Aguarda o Spotify abrir 
time.sleep(5)
#dentro do spotify vamos usar a função escrever
auto.write("lofi para estudar ou dormir")
#agr usar enter
auto.press('ENTER')
# Aguarda o carregamento
time.sleep(3)
#apertar o play
auto.click(461,101)
#diminuir o volume
auto.click(1620,985)

#agora vamos fazer ele abrir o opera
time.sleep(2)
auto.press('win')
auto.write("Navegador Opera GX")
auto.press('ENTER')
#abrir o email
auto.write("https://mail.google.com/mail/u/0/#inbox")
auto.press('ENTER')
#vai esperar dois segundos
time.sleep(1)
#abrir o youtube
#"hotkey" para usar atalho
auto.hotkey('ctrl','t')
auto.write("Youtube.com")
auto.press('ENTER')

#e por fim abrir o VScode
auto.press('win')
auto.write("Visual Studio Code")
auto.press("ENTER")
