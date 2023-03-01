from MPOD_GUI import *

class HV_GUI():
    def __init__(self):
        sg.set_options(font=('Noto Mono', 14))

        self.ip = '0.0.0.0'
        self.dict = {str(ch):MPOD_GUI(self.ip, str(ch)) for ch in range(0, 4)}
        self.layout = [mpod.layout for mpod in self.dict.values()]
        self.window = sg.Window('HV GUI', self.layout)

    #def UpdateChannelText(self, ch):
    #    for k, t in self.dict[str(ch)].text.items():
    #        self.window[str(ch) + ' ' + k].update(t[0].format(**self.dict[str(ch)].args))

    def Loop(self):
        event, values = self.window.read()
        if event == sg.WIN_CLOSED:
            return False

        if callable(event):
            event()
        #event_txt = event.split()
        #ch = event_txt[0]
        #arg = event_txt[1]
        #val = values[ch + ' ' + arg + ' ' + 'value']
        #self.dict[ch].UpdateArg(arg, val)
        #self.UpdateChannelText(ch)

        return True
