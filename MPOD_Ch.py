import PySimpleGUI as sg

class MPOD_Ch():
    def __init__(self, _ip, _channel):

        self.args = {}
        self.args['ip'] = str(_ip)
        self.args['channel'] = str(_channel)

        self.dict = {
            'status': [
                'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputStatus.u{channel} i {status}',
                0.0,
                '{:1.0f}'],


            'v_min': [
                'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMinSenseVoltage.u{channel} F {v_min}',
                0.0,
                '{:>8.2f}'],
            'v_max': [
                'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMaxSenseVoltage.u{channel} F {v_max}',
                0.0,
                '{:>8.2f}'],
            'v_set': [
                'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltage.u{channel} F {v_set}',
                0.0,
                '{:>8.2f}'],
            'v_get': [
                'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputMeasurementSenseVoltage.u{channel}',
                0.0,
                '{:>8.2f}'],


            'i_max': [
                'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMaxCurrent.u{channel} F {v_max}',
                0.0,
                '{:>8.2f}'],
            'i_set': [
                'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrent.u{channel} F {i_set}',
                0.0,
                '{:>8.2f}'],
            'i_get': [
                'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputMeasurementCurrent.u{channel}',
                0.0,
                '{:>8.2f}'],
    

            'v_rise': [
                'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltageRiseRate.u{channel} F {v_rise}',
                0.0,
                '{:>8.2f}'],
            'v_fall': [
                'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltageFallRate.u{channel} F {v_fall}',
                0.0,
                '{:>8.2f}'],
            'i_rise': [
                'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrentRiseRate.u{channel} F {i_rise}',
                0.0,
                '{:>8.2f}'],
            'i_fall': [
                'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrentFallRate.u{channel} F {i_fall}',
                0.0,
                '{:>8.2f}']}

        for k, v in self.dict.items():
            self.args[k] = v[2].format(v[1])

        #self.text = {
        #        'channel': [
        #            'Channel {channel}'],
        #        'v_get': [
        #            '{v_get}'],
        #        'v_set': [
        #            '({v_set})'],
        #        'i_get': [
        #            '{i_get}'],
        #        'i_set': [
        #            '({i_set})']}

        #self.layout = [
        #        sg.Text(self.text['channel'][0].format(**self.args), key=str(self.channel) + ' ' + 'channel'),

        #        sg.Text(self.text['v_get'][0].format(**self.args), s=12, key=str(self.channel) + ' ' + 'v_get'),
        #        sg.Text(self.text['v_set'][0].format(**self.args), s=12, key=str(self.channel) + ' ' + 'v_set'),
        #        sg.Input(s=5, key=str(self.channel) + ' ' + 'v_set' + ' ' + 'value'),
        #        sg.Button('Set Voltage (V)', key=(self.channel) + ' ' + 'v_set' + ' ' + 'event'),

        #        sg.Text(self.text['i_get'][0].format(**self.args), s=12, key=str(self.channel) + ' ' + 'i_get'),
        #        sg.Text(self.text['i_set'][0].format(**self.args), s=12, key=str(self.channel) + ' ' + 'i_set'),
        #        sg.Input(s=5, key=str(self.channel) + ' ' + 'i_set' + ' ' + 'value'),
        #        sg.Button('Set Current (A)', key=(self.channel) + ' ' + 'i_set' + ' ' + 'event')]

    def UpdateArgs(self):
        for k, v in self.dict.items():
            print(v[0].format(**self.args))

    def UpdateArg(self, arg, val):
        if arg not in self.dict:
            print('No arg "' + str(arg) + '" in dict')
            return

        try:
            self.dict[arg][1] = float(val)
        except ValueError:
            print('Python3\'s float() fails to cast "' + str(val) + '" as float')
            print('Value not passed')
            return

        self.args[arg] = self.dict[arg][2].format(self.dict[arg][1])
        print(self.dict[arg][0].format(**self.args))

    def PrintArgs(self):
        for k, v in self.args.items():
            print(str(k) + ': ' + str(v))
