# A wrapper for the SNMP commands to be used to get or set MPod values
# Be sure to listen to its new album on Soundcloud

class HV_Wrapper():
    def __init__(self):
        self.commands = [
                {'cmd': 'set_v',        'args':'snmpset -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltage.{channel} F {voltage}'},
                {'cmd': 'get_v',        'args':'snmpget -OqvU -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputVoltage.{channel}'}]

    def TryCommand(self, cmd, arg_map):
        # cpp has a library standard std::map which can lookup an item in log time and return an iterator to it
        # linear time goes brrrrr
        # fucking normoid language for baby programmers
        for i in self.commands:
            if i['cmd'] == cmd:
                print(i['args'].format(**arg_map))
                return
        print('cmd "' + cmd + '" not found in dictionary')
