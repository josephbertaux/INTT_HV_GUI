from MPOD_GUI import *

class HV_GUI():
    #...


    def Loop(self):
        event, values = self.window.read()
        if event == sg.WIN_CLOSED:
            return False

        if callable(event):
            event()

        return True

    def Init(self):
        self.window.read()
        for mpod in self.mpods.values():
            mpod.Init()



    def __init__(self):
        sg.set_options(font=('Noto Mono', 8))

        self.ip = '0.0.0.0'
        self.mpods = {str(ch):MPOD_GUI(self.ip, str(ch)) for ch in range(0, 4)}

        self.dict = {
                'all':  sg.Text('all')}
        self.layout = [[v for v in self.dict.values()]]
        for mpod in self.mpods.values():
            self.layout += [mpod.layout]

        self.window = sg.Window('HV GUI', self.layout)
