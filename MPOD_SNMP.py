import PySimpleGUI as sg

class MPOD_SNMP():

    def GetArg(self, arg):
        if arg not in self.dict:
            print('No arg "' + str(arg) + '" in dict')
            return 0.0

        if not self.dict[arg][1][0]:
            print('Arg "' + str(arg) + '" not readable via SNMP commands')
            print('Returning value from dictionary')
            return self.dict[arg][0]

        #self.dict[arg][0] = print(self.dict[arg][1][1])
        print(self.dict[arg][1][1])
        return self.dict[arg][0]

    def SetArg(self, arg, val):
        if arg not in self.dict:
            print('No arg "' + str(arg) + '" in dict')
            return

        try:
            self.dict[arg][0] = float(val)
        except ValueError:
            print('Python3\'s float() fails to cast "' + str(arg) + '" as float')
            print('Value not passed')
            return

        if not self.dict[arg][2][0]:
            print('Arg "' + str(arg) + '" not writeable via SNMP commands')
            print('Only dictionary value was set')
            return

        print(self.dict[arg][2][1].format(str(self.dict[arg][0])))


    def __init__(self, _ip, _channel):
        self.ip = _ip
        self.channel = _channel

        self.dict = {
            'status': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru ' + _ip + ' outputStatus.u' + _channel],
                [True,  'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru ' + _ip + ' outputStatus.u' + _channel+' i {}']],



            'v_get': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru ' + _ip + ' outputMeasurementSenseVoltage.u' + _channel],
                [False, '']],
            'v_set': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru ' + _ip + ' outputVoltage.u' + _channel],
                [True,  'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru ' + _ip + ' outputVoltage.u' + _channel+' F {}']],
            'v_min': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru ' + _ip + ' outputSupervisionMinSenseVoltage.u' + _channel],
                [True,  'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru ' + _ip + ' outputSupervisionMinSenseVoltage.u' + _channel+' F {}']],
            'v_max': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru ' + _ip + ' outputSupervisionMaxSenseVoltage.u' + _channel],
                [True,  'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru ' + _ip + ' outputSupervisionMaxSenseVoltage.u' + _channel+' F {}']],



            'i_get': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru ' + _ip + ' outputMeasurementCurrent.u' + _channel],
                [False, '']],
            'i_set': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru ' + _ip + ' outputCurrent.u' + _channel],
                [True,  'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru ' + _ip + ' outputCurrent.u' + _channel+' F {}']],
            'i_max': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru ' + _ip + ' outputSupervisionMaxCurrent.u' + _channel],
                [True,  'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru ' + _ip + ' outputSupervisionMaxCurrent.u' + _channel+' F {}']],


    

            'v_rise': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru ' + _ip + ' outputVoltageRiseRate.u' + _channel],
                [True,  'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru ' + _ip + ' outputVoltageRiseRate.u' + _channel+' F {}']],
            'v_fall': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru ' + _ip + ' outputVoltageFallRate.u' + _channel],
                [True,  'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru ' + _ip + ' outputVoltageFallRate.u' + _channel+' F {}']],
            'i_rise': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru ' + _ip + ' outputCurrentRiseRate.u' + _channel],
                [True,  'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru ' + _ip + ' outputCurrentRiseRate.u' + _channel+' F {}']],
            'i_fall': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru ' + _ip + ' outputCurrentFallRate.u' + _channel],
                [True,  'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru ' + _ip + ' outputCurrentFallRate.u' + _channel+' F {}']]}

