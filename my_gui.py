from my_class import *

mc = my_class()
window = sg.Window('sample text', [mc.layout])

while(True):
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'button':
        mc.ChangeText()

window.close()
