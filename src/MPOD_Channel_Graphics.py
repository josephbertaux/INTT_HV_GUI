from MPOD_Channel_Commands import *
import PySimpleGUI as sg
import time

class MPOD_Channel_Graphics():
    def Update(self):
        val = self.mpod.Get('status')
        s = ''
        b = False
        if val is not None and val == 1:
            self.dict['layman']['status_text'].update(background_color='green')
            s = '{:>02d}'.format(val)
        else:
            self.dict['layman']['status_text'].update(background_color='red')
            b = True
            if val is not None:
                s = '{:>02d}'.format(val)
        self.dict['layman']['status_text'].update(s)
        
        val = self.mpod.Get('v_get')
        self.dict['layman']['v_get_text'].update('{:>6.1f}  V'.format(val) if val is not None else '')

        val = self.mpod.Get('i_get')
        self.dict['layman']['i_get_text'].update('{:>6.1f} uA'.format(val * 10 ** 6) if val is not None else '')

        time.sleep(self.refresh)


    def TurnOn(self):
        self.mpod.TurnOn()

    def TurnOff(self):
        self.mpod.TurnOff()

    def Set_V(self):
        return

    def Clear(self):
        return

    def Expert(self):
        for k, v in self.dict['expert'].items():
                v.update(disable=self.expert)

        self.expert = not self.expert

    def __init__(self, _ip, _ch):
        self.refresh = 1
        self.expert = False
        self.mpod = MPOD_Channel_Commands(_ip, _ch) 
        self.dict = {
            'layman': {
                'on_button':    sg.Button('On',     key=lambda: self.TurnOn()),
                'off_button':   sg.Button('Off',    key=lambda: self.TurnOff()),
                'status_text':  sg.Text(s=2),
                'v_get_text':   sg.Text(s=9),
                'i_get_text':   sg.Text(s=9),
                'update_button':sg.Button('Update', key=lambda: self.Update())},

            'expert': {
                'v_set_text':   sg.Input(s=6),
                'v_set_button': sg.Button('Set V',  key=lambda: self.Set_V()),
                'clear':        sg.Button('Clear',  key=lambda: self.Clear())}}

        self.layman_elements = [v for k, v in self.dict['layman'].items()]
        self.expert_elements = [v for k, v in self.dict['expert'].items()]
