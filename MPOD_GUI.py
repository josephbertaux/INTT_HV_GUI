from MPOD_SNMP import *
import PySimpleGUI as sg

class MPOD_GUI():
    def Disable(self):
        status = bool(self.mpod_snmp.GetArg('status'))

        self.dict['v_set_event'].update(disabled=not status)
        self.dict['i_set_event'].update(disabled=not status)

        self.dict['v_min_event'].update(disabled=((not status) or (not self.is_expert)))
        self.dict['v_max_event'].update(disabled=((not status) or (not self.is_expert)))
        self.dict['i_max_event'].update(disabled=((not status) or (not self.is_expert)))

    def Toggle_Expert(self, i=-1, b=False):
        if b and not self.receive_all:
            return
        if i == -1:
            # Potentially make a pop-up to confirm
            self.is_expert = not self.is_expert
        else:
            self.is_expert = bool(i)
        self.Disable()



    def Channel_Text(self):
        self.dict['channel_text'].update('Channel: {:>}'.format(self.mpod_snmp.channel))



    def Status_Text(self):
        self.dict['status_text'].update(' On' if bool(self.mpod_snmp.GetArg('status')) else 'Off')

    def Status_Event(self, status=-1, b=False):
        if b and not self.receive_all:
            return
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

    def V_Set_Event(self, v_set='', b=False):
        if b and not self.receive_all:
            return
        if v_set == '':
            v_set = self.dict['v_set_value'].get()

        arg = 0.0
        try:
            arg = float(v_set)
        except ValueError:
            print('Could not cast "' + v_set + '" as float')
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

    def V_Min_Event(self, v_min='', b=False):
        if b and not self.receive_all:
            return
        if v_min == '':
            v_min = self.dict['v_min_value'].get()

        self.mpod_snmp.SetArg('v_min', v_min)
        self.V_Text()

    def V_Max_Event(self, v_max='', b=False):
        if b and not self.receive_all:
            return
        if v_max == '':
            v_max = self.dict['v_max_value'].get()

        self.mpod_snmp.SetArg('v_max', v_max)
        self.V_Text()



    def I_Text(self):
        self.dict['i_get_text'].update('{:>6.1f}'.format(self.mpod_snmp.GetArg('i_get')))
        self.dict['i_set_text'].update('({:>6.1f})'.format(self.mpod_snmp.GetArg('i_set')))
        self.dict['i_max_text'].update('({:>6.1f})'.format(self.mpod_snmp.GetArg('i_max')))

    def I_Set_Event(self, i_set='', b=False):
        if b and not self.receive_all:
            return
        if i_set == '':
            i_set = self.dict['i_set_value'].get()

        arg = 0.0
        try:
            arg = float(i_set)
        except ValueError:
            print('Could not cast "' + i_set + '" as float')
            print('No value was set')
            return

        i = self.mpod_snmp.GetArg('i_max')
        if arg > i:
            print('Current ' + str(arg) + ' is more than maximum current ' + str(i) + ' A')
            print('Raise the maximum current or set a different current')
            print('No value was set')
            return

        self.mpod_snmp.SetArg('i_set', arg)
        self.I_Text()

    def I_Max_Event(self, i_max='', b=False):
        if b and not self.receive_all:
            return
        if i_max == '':
            i_max = self.dict['i_max_value'].get()

        self.mpod_snmp.SetArg('i_max', i_max)
        self.I_Text()



    def Receive_All_Text(self):
        self.dict['receive_all_text'].update('Receive "All": {}'.format('Yes' if self.receive_all else ' No'))

    def Receive_All_Event(self, r_a=-1):
        if r_a == -1:
            self.receive_all = not self.receive_all
        else:
            status = bool(status)
        self.Receive_All_Text()



    def Text(self):
        Channel_Text()
        Status_Text()
        V_Text()
        I_Text()

    def Init(self):
        self.Disable()
        self.Text()



    def __init__(self, _ip, _channel):
        self.is_expert = False
        self.receive_all = True

        self.mpod_snmp = MPOD_SNMP(_ip, _channel)

        self.dict = {
                'channel_text':         sg.Text('Channel {:>}'.format(_channel)),

                # Status (On/Off)
                'status_text':          sg.Text('Off',      s=3),
                'status_event':         sg.Button('Toggle', key=lambda: self.Status_Event()),

                # Voltage
                'v_get_text':           sg.Text('',         s=10),
                'v_set_text':           sg.Text('',         s=10),
                'v_set_value':          sg.InputText('',    s=8),
                'v_set_event':          sg.Button('V Set',  key=lambda: self.V_Set_Event()),

                # Current
                'i_get_text':           sg.Text('',         s=10),
                'i_set_text':           sg.Text('',         s=10),
                'i_set_value':          sg.InputText('',    s=8),
                'i_set_event':          sg.Button('I Set',  key=lambda: self.I_Set_Event()),

                # Rise/Fall Rates

                # Expert
                'v_min_text':           sg.Text('',         s=10),
                'v_min_value':          sg.InputText('',    s=8),
                'v_min_event':          sg.Button('V Min',  key=lambda: self.V_Min_Event()),

                'v_max_text':           sg.Text('',         s=10),
                'v_max_value':          sg.InputText('',    s=8),
                'v_max_event':          sg.Button('V Max',  key=lambda: self.V_Max_Event()),

                'i_max_text':           sg.Text('',         s=10),
                'i_max_value':          sg.InputText('',    s=8),
                'i_max_event':          sg.Button('I Max',  key=lambda: self.I_Max_Event()),

                # Receive All
                'receive_all_text':     sg.Text('Receive "All": Yes'),
                'receive_all_event':    sg.Button('Toggle', key=lambda: self.Receive_All_Event())}

        self.layout = [v for k, v in self.dict.items()]
