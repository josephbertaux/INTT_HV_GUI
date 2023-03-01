from MPOD_SNMP import *
import PySimpleGUI as sg

class MPOD_GUI():
    def Disable(self):
        status = bool(self.mpod_snmp.GetArg('status'))

        self.dict['v_set_event'].update(disabled=not status)

        self.dict['v_min_event'].update(disabled=((not status) or (not self.is_expert)))
        self.dict['v_max_event'].update(disabled=((not status) or (not self.is_expert)))

    def Toggle_Expert(self, i=-1):
        if i == -1:
            self.is_expert = not self.is_expert
        else:
            self.is_expert = bool(i)
        self.Disable()



    def Channel_Text(self):
        self.dict['channel_text'].update('Channel: {:>}'.format(self.mpod_snmp.channel))



    def Status_Text(self):
        self.dict['status_text'].update(' On' if bool(self.mpod_snmp.GetArg('status')) else 'Off')

    def Status_Event(self, status=-1):
        if status == -1:
            status = self.mpod_snmp.GetArg('status')
            status = not bool(status)
        else:
            status = bool(status)
        self.mpod_snmp.SetArg('status', float(status))
        self.Disable()
        self.Status_Text()



    def V_Text(self):
        self.dict['v_get_text'].update('{:>6.1f}'.format(self.mpod_snmp.GetArg('v_get')))
        self.dict['v_set_text'].update('({:>6.1f})'.format(self.mpod_snmp.GetArg('v_set')))
        self.dict['v_min_text'].update('({:>6.1f})'.format(self.mpod_snmp.GetArg('v_min')))
        self.dict['v_max_text'].update('({:>6.1f})'.format(self.mpod_snmp.GetArg('v_max')))

    def V_Set_Event(self, set_v=''):
        if set_v == '':
            set_v = self.dict['v_set_value'].get()

        arg = 0.0
        try:
            arg = float(set_v)
        except ValueError:
            print('Could not cast "' + set_v + '" as float')
            print('No value was set')
            return

        v = self.mpod_snmp.GetArg('v_min')
        if arg < v:
            print('Voltage ' + str(arg) + ' is less than minimum voltage ' + str(v) + ' V')
            print('Lower the minimum voltage or set a different voltage')
            print('No value was set')
            return

        v = self.mpod_snmp.GetArg('v_max')
        if arg > v:
            print('Voltage ' + str(arg) + ' is more than maximum voltage ' + str(v) + ' V')
            print('Raise the maximum voltage or set a different voltage')
            print('No value was set')
            return

        self.mpod_snmp.SetArg('v_set', arg)
        self.V_Text()

    def V_Min_Event(self, v_min=''):
        if v_min == '':
            v_min = self.dict['v_min_value'].get()

        self.mpod_snmp.SetArg('v_min', v_min)
        self.V_Text()

    def V_Max_Event(self, max_v=''):
        if max_v == '':
            max_v = self.dict['v_max_value'].get()

        self.mpod_snmp.SetArg('v_max', max_v)
        self.V_Text()



    def Text(self):
        Channel_Text()
        Status_Text()
        V_Text()



    def __init__(self, _ip, _channel):
        self.is_expert = False
        self.mpod_snmp = MPOD_SNMP(_ip, _channel)

        self.dict = {
                'channel_text':     sg.Text('Channel {:>}'.format(_channel)),

                'status_text':      sg.Text('Off',      s=3),
                'status_event':     sg.Button('Toggle', key=lambda: self.Status_Event()),

                'v_get_text':       sg.Text('',         s=10),
                'v_set_text':       sg.Text('',         s=10),
                'v_set_value':      sg.InputText('',    s=8),
                'v_set_event':      sg.Button('V Set',  key=lambda: self.V_Set_Event()),

                # Current

                # Rise/Fall Rates

                'v_min_text':       sg.Text('',         s=10),
                'v_min_value':      sg.InputText('',    s=8),
                'v_min_event':      sg.Button('V Min',  key=lambda: self.V_Min_Event()),

                'v_max_text':       sg.Text('',         s=10),
                'v_max_value':      sg.InputText('',    s=8),
                'v_max_event':      sg.Button('V Max',  key=lambda: self.V_Max_Event())}

                # Current Max

        self.layout = [v for k, v in self.dict.items()]
