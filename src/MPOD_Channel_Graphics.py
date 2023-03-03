from MPOD_Channel_Commands import *
import PySimpleGUI as sg
import time

class MPOD_Channel_Graphics():
    def Update():
        s = mpod.GetArg('status')
        if s == 1:
            self.dict['layman']['status']['text'].update(background_color='green')
        else:
            self.dict['layman']['status']['text'].update(background_color='red')
        self.dict['layman']['status']['text'].update('{:>02d}'.format(s))
        self.dict['layman']['v_get']['text'].update('{:>6.1f}  V'.format(mpod.GetArg('v_get')))
        self.dict['layman']['i_get']['text'].update('{:>6.1f} uA'.format(mpod.GetArg('i_get') * 10 ** 6))
        time.sleep(1)


    def TurnOn(self):
        return

    def TurnOff(self):
        return

    def Set_V(self):
        return

    def Clear(self):
        return

    def Expert(self):
        for k, v in self.dict['expert'].items():
            for kk, vv in v.items():
                vv.update(disable=self.expert)

        self.expert = not self.expert

    def __init__(self, _ip, _ch):
        self.refresh = 1
        self.expert = False
        self.mpod = MPOD_Channel_Commands(_ip, _ch) 
        self.dict = {
            'layman': {
                'switch': {
                    'on':       sg.Button('On',     key=lambda: self.TurnOn()),
                    'off':      sg.Button('Off',    key=lambda: self.TurnOff())},

                'status': {
                    'text':     sg.Text(s=2)},
                
                'v_get': {
                    'text':     sg.Text(s=9)},
                
                'i_get': {
                    'text':     sg.Text(s=9)} },

            'expert': {
                'v_set': {
                    'input':    sg.Input(s=6),
                    'button':   sg.Button('Set V',  key=lambda: self.Set_V())},

                'clear': {
                    'button':   sg.Button('Clear',  key=lambda: self.Clear())} } }

        self.gui_elements = []
        for k, v in self.dict.items():
            for kk, vv in v.items():
                for kkk, vvv in vv.items():
                    self.gui_elements += [vvv]
