# A wrapper for the SNMP commands to be used to get or set MPod values
# Be sure to listen to its new album on Soundcloud

from MPOD import MPOD

class HV_Wrapper():
    def __init__(self):
        self.commands = [
            # Status/Meta commands
            # ..

            # Voltage SNMP commands
            {'cmd': 'get_v',            'args':'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputMeasurementSenseVoltage.u{channel}'},
            {'cmd': 'set_v',            'args':'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltage.u{channel} F {v}'},
            {'cmd': 'get_set_v',        'args':'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltage.u{channel}'},

            {'cmd': 'get_min_v',        'args':'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMinSenseVoltage.u{channel}'},
            {'cmd': 'set_min_v',        'args':'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMinSenseVoltage.u{channel} F {v_min}'},
            {'cmd': 'get_max_v',        'args':'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMaxSenseVoltage.u{channel}'},
            {'cmd': 'set_max_v',        'args':'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMaxSenseVoltage.u{channel} F {v_max}'},
            
            # Current SNMP commands
            {'cmd': 'get_i',            'args':'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputMeasurementCurrent.u{channel}'},
            {'cmd': 'set_i',            'args':'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrent.u{channel} F {i}'},
            {'cmd': 'get_set_i',        'args':'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrent.u{channel}'},

            {'cmd': 'get_max_i',        'args':'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMaxCurrent.u{channel}'},
            {'cmd': 'set_max_i',        'args':'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionMaxCurrent.u{channel} F {i_max}'},

            # (Voltage) Rise/Fall Rate SNMP commands
            ### Not sure how useful these will be
            ### Fuck it, I'm thorough on principle
            {'cmd': 'set_v_rise',       'args':'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltageRiseRate.u{channel} F {v_rise}'},
            {'cmd': 'get_set_v_rise',   'args':'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltageRiseRate.u{channel}'},
            
            {'cmd': 'set_v_fall',       'args':'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltageFallRate.u{channel} F {v_fall}'},
            {'cmd': 'get_set_v_fall',   'args':'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltageFallRate.u{channel}'},

            # (Current) Rise/Fall Rate SNMP commands
            ### Not sure how useful these will be
            ### Fuck it, I'm thorough on principle
            {'cmd': 'set_i_rise',       'args':'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrentRiseRate.u{channel} F {i_rise}'},
            {'cmd': 'get_set_i_rise',   'args':'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrentRiseRate.u{channel}'},
            
            {'cmd': 'set_i_fall',       'args':'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrentFallRate.u{channel} F {i_fall}'},
            {'cmd': 'get_set_i_fall',   'args':'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrentFallRate.u{channel}'}]

        self.mpod[MPOD(3), MPOD(4)]


    def TryCommand(self, cmd, arg_map):
        # Could be log * log but I'm not making a dictionary of dictionaries
        # Enjoy your for loop, not that many elements in the first place
        # Also python isn't worth optimizing lmao
        for i in self.commands:
            if i['cmd'] == cmd:
                # reference for how I'm using the format command:
                # https://docs.python.org/3/library/string.html#format-examples
                print(i['args'].format(**arg_map))
                return
        print('cmd "' + cmd + '" not found in dictionary')

    def TryMPOD
