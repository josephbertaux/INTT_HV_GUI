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
        print(self.dict[arg][1][1].format(ip=self.ip, ch=self.ch, val=arg))
        return self.dict[arg][0]

    def SetArg(self, arg, val):
        if arg not in self.dict:
            print('No arg "' + str(arg) + '" in dict')
            return

        try:
            self.dict[arg][0] = float(val)
        except ValueError:
            print('Python3\'s float() fails to cast "' + str(val) + '" as float')
            print('Value not passed')
            return

        if not self.dict[arg][2][0]:
            print('Arg "' + str(arg) + '" not writeable via SNMP commands')
            print('Only dictionary value was set')
            return

        print(self.dict[arg][2][1].format(str(self.dict[arg][0])))


    def __init__(self, _ip, _ch):
        self.ip = _ip   # The IP of this MPOD formatted as a string
        self.ch = _ch
    
        self.dict = {
            'status': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c public {ip} outputStatus.u{ch}'],
                [True,  'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputStatus.u{ch} i {val}']],
    
    
    
            'v_get': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputMeasurementSenseVoltage.u{ch}'],
                [False, '']],
            'v_set': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltage.u{ch}'],
                [True,  'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltage.u{ch} F {val}']],
            'v_min': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMinSenseVoltage.u{ch}'],
                [True,  'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMinSenseVoltage.u{ch} F {val}']],
            'v_max': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMaxSenseVoltage.u{ch}'],
                [True,  'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMaxSenseVoltage.u{ch} F {val}']],
    
    
    
            'i_get': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputMeasurementCurrent.u{ch}'],
                [False, '']],
            'i_set': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrent.u{ch}'],
                [True,  'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrent.u{ch} F {val}']],
            'i_max': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMaxCurrent.u{ch}'],
                [True,  'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMaxCurrent.u{ch} F {val}']],
    
    
    
    
            'v_rise': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltageRiseRate.u{ch}'],
                [True,  'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltageRiseRate.u{ch} F {val}']],
            'v_fall': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltageFallRate.u{ch}'],
                [True,  'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltageFallRate.u{ch} F {val}']],
            'i_rise': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrentRiseRate.u{ch}'],
                [True,  'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrentRiseRate.u{ch} F {val}']],
            'i_fall': [
                0.0,
                [True,  'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrentFallRate.u{ch}'],
                [True,  'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrentFallRate.u{ch} F {val}']]}
    
