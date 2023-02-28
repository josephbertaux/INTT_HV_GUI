import PySimpleGUI as sg

class MPOD_Channel():
    def __init__(self, _ip, _channel):
        self.ip = _ip
        self.channel = _channel

        self.args = {}
        self.args['ip'] = str(self.ip)
        self.args['channel'] = str(self.channel)

        self.dict = {
            'status': [
                0,
                'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputStatus.u{channel} i {status}'],


            'v_min': [
                0.0,
                'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMinSenseVoltage.u{channel} F {v_min}'],
            'v_max': [
                0.0,
                'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMaxSenseVoltage.u{channel} F {v_max}'],
            'v_set': [
                0.0,
                'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltage.u{channel} F {v_set}'],
            'v_get': [
                0.0,
                'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputMeasurementSenseVoltage.u{channel}'],


            'i_max': [
                0.0,
                'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMaxCurrent.u{channel} F {v_max}'],
            'i_set': [
                0.0,
                'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrent.u{channel} F {i_set}'],
            'i_get': [
                0.0,
                'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputMeasurementCurrent.u{channel}'],
    

            'v_rise': [
                0.0,
                'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltageRiseRate.u{channel} F {v_rise}'],
            'v_fall': [
                0.0,
                'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltageFallRate.u{channel} F {v_fall}'],
            'i_rise': [
                0.0,
                'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrentRiseRate.u{channel} F {i_rise}'],
            'i_fall': [
                0.0,
                'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrentFallRate.u{channel} F {i_fall}']}

        for k, v in self.dict.items():
            self.args[k] = ''

        self.text = {
                'channel': [
                    'Channel {channel}'],
                'voltage': [
                    '{v_get} ({v_set})'],
                'current': [
                    '{i_get} ({i_set})']}

        self.layout = [
                sg.Text(self.text['channel'][0].format(**self.args), key=str(self.channel) + ' ' + 'channel'),

                sg.Text(self.text['voltage'][0].format(**self.args), key=str(self.channel) + ' ' + 'voltage'),
                sg.Input(s=5, key=str(self.channel) + ' ' + 'v_set' + ' ' + 'value'),
                sg.Button('Set Voltage (V)', key=(self.channel) + ' ' + 'v_set' + ' ' + 'event'),

                sg.Text(self.text['current'][0].format(**self.args), key=str(self.channel) + ' ' + 'current'),
                sg.Input(s=5, key=str(self.channel) + ' ' + 'i_set' + ' ' + 'value'),
                sg.Button('Set Current (A)', key=(self.channel) + ' ' + 'i_set' + ' ' + 'event')]

    def UpdateArgs(self):
        for k, v in self.dict.items():
            print(v[1].format(**self.args))

    def UpdateArg(self, arg, val):
        if arg not in self.dict or arg not in self.args:
            print('No arg "' + str(arg) + '" currently used')
            return

        self.args[arg] = str(val)
        print(self.dict[arg][1].format(**self.args))

    def PrintArgs(self):
        for k, v in self.args.items():
            print(str(k) + ': ' + str(v))
