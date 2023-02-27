class MPOD_Channel():
    def __init__(self, _ip, _channel):

        self.args = {}
        self.args['ip'] = str(_ip)
        self.args['channel'] = str(_channel)

        self.dict = {
            'status':   'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputStatus.u{channel} i {status}',
            'v_min':    'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMinSenseVoltage.u{channel} F {v_min}',
            'v_max':    'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMaxSenseVoltage.u{channel} F {v_max}',
            'v_set':    'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltage.u{channel} F {v_set}',
            'v_get':    'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputMeasurementSenseVoltage.u{channel}',

            'i_max':    'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMaxCurrent.u{channel} F {v_max}',
            'i_set':    'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrent.u{channel} F {i_set}',
            'i_get':    'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputMeasurementCurrent.u{channel}',

            'v_rise':   'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltageRiseRate.u{channel} F {v_rise}',
            'v_fall':   'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltageFallRate.u{channel} F {v_fall}',
            'i_rise':   'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrentRiseRate.u{channel} F {i_rise}',
            'i_fall':   'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrentFallRate.u{channel} F {i_fall}'}

        for k, v in self.dict.items():
            self.args[k] = ''

        # Should initialize from a database

    def UpdateArgs(self):
        for k, v in self.dict.items():
            print(v.format(**self.args))

    def UpdateArg(self, arg, val):
        if arg not in self.args:
            print('No arg "' + str(arg) + '" in args')
            return

        self.args[arg] = str(val)

        if arg not in self.dict:
            print('No arg "' + str(arg) + '" in dict')

        print(self.dict[arg].format(**self.args))

    def PrintArgs(self):
        for k, v in self.args.items():
            print(str(k) + ': ' + str(v))
