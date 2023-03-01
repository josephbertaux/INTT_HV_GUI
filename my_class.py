import PySimpleGUI as sg

class my_class():
    def __init__(self):
        self.counter = 0
        self.layout = [
                sg.Text('{:d}'.format(self.counter)),
                sg.Button('button'), key='button']

    def ChangeText(self):
        self.counter += 1
        self.layout[0].update('{:d}'.format(self.counter))
