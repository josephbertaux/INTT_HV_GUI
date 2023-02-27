class MPOD_Channel():
    def __init__(self, _ip, _channel):

        self.dict = {
            'status':   ['snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputStatus.u{channel} i {status}',                        '0'],
            'v_min':    ['snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMinSenseVoltage.u{channel} F {v_min}',     '0.0'],
            'v_max':    ['snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMaxSenseVoltage.u{channel} F {v_max}',     '100.0'],
            'v_set':    ['snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltage.u{channel} F {v_set}',                        '0.0'],
            'v_get':    ['snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputMeasurementSenseVoltage.u{channel}',                  ''],

            'i_max':    ['snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMaxCurrent.u{channel} F {v_max}',          '10.0'],
            'i_set':    ['snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrent.u{channel} F {i_set}',                        '0.0'],
            'i_get':    ['snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputMeasurementCurrent.u{channel}',                       ''],

            'v_rise':   ['snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltageRiseRate.u{channel} F {v_rise}',               '0.0'],
            'v_fall':   ['snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltageFallRate.u{channel} F {v_fall}',               '0.0'],
            'i_rise':   ['snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrentRiseRate.u{channel} F {i_rise}',               '0.0'],
            'i_fall':   ['snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrentFallRate.u{channel} F {i_fall}',               '0.0']}

        self.args = {}
        self.args['ip'] = str(_ip)
        self.args['channel'] = str(_channel)
        for k, v in self.dict.items():
            self.args[k] = v[1]

        # Should initialize from a database

    def UpdateArgs(self):
        for k, v in self.dict.items():
            print(v[0].format(**self.args))

    def UpdateArg(self, arg, val):
        if arg not in self.args:
            print('No arg "' + str(arg) + '" in args')
            return

        self.args[arg] = str(val)

        if arg not in self.dict:
            print('No arg "' + str(arg) + '" in dict')

        print(self.dict[arg][0].format(**self.args))

    def PrintArgs(self):
        for k, v in self.args.items():
            print(str(k) + ': ' + str(v))
