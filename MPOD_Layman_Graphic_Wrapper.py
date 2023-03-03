from MPOD_Channel_Wrapper import *
import PySimpleGUI as sg
import time


class MPOD_Layman_Graphic_Wrapper():
    def Status(self, _k):
        s = self.dict[_k]['wrapper'].Get('status')

        self.dict[_k]['monitor']['status']['gui']['text'].update('{:>02d}'.format(s))

        # if s == 1:
        #   for k, v in self.dict[k]['monitor']:
        #       #set background green
        #       #v.update(color='green')
        # else:
        #   for k, v in self.dict[k]['monitor']:
        #       #set background red

    def V_Get(self, _k):
        self.dict[_k]['monitor']['v_get']['gui']['text'].update('{:>6.1f}  V'.format(self.dict[_k]['wrapper'].Get('v_get')))

    def I_Get(self, _k):
        self.dict[_k]['monitor']['i_get']['gui']['text'].update('{:>6.1f} uA'.format(self.dict[_k]['wrapper'].Get('i_get')))

    def Update(self, _k):
        for v in self.dict[_k]['monitor'].values:
            v['update']()

    def __init__(self, _map):
        # _ch should be a dictionary of sensor ids to channels and ips
        # e.g. {'NA':{'ip':0.0.0.0, 'ch':'000'}, ...}

        self.dict = {
                k: {
                'wrapper':  MPOD_Channel_Wrapper(v['ip'], v['ch']),
                'monitor': {
                    'status': {
                        'gui': {
                            'debug':    sg.Text(k + '_status'),
                            'text':     sg.Text(s=2)},
                        'update':   lambda: self.Status(k)},

                    'v_get': {
                        'gui': {
                            'debug':    sg.Text(k + '_v_get'),
                            'text':     sg.Text(s=9)},
                        'update':   lambda: self.V_Get(k)},

                    'i_get': {
                        'gui': {
                            'debug':    sg.Text(k + '_i_get'),
                            'text':     sg.Text(s=9)},
                        'update':   lambda: self.I_Get(k)}}}
                for k, v in _map.items()}
