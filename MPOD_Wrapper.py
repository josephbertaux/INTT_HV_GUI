class MPOD_Wrapper():

    def Get(self, ladder, arg):
        ladder = str(ladder)
        arg = str(arg)

        if ladder not in self.ladder_dict:
            print('key "' + ladder + '" not in internal ladder dictionary')
            return -999

        if arg not in self.cmd_dict:
            print('key "' + arg + '" not in internal cmd dictionary')
            return -999

        if not self.cmd_dict[arg]['readable']:
            print('key "' + arg + '" not readable')
            return -999

        print('snmpget{x} -Oqv -v 2c -m +WIENER-CRATE-MIB -c public {ip} {name}.u{ch}'.format(
            x=self.cmd_dict[arg]['x'], ip=self.ip, name=self.cmd_dict[arg]['name'], ch=self.ch_dict[ladder])
        # self.cmd_dict[arg]['val'] = # Cast from piped output of the snmp command

    def Set(self, _ladder, _arg, _val):
        _ladder = str(ladder)
        _arg = str(arg)
        _val = str(val)

        if _ladder not in self.ladder_dict:
            print('key "' + _ladder + '" not in internal ladder dictionary')
            return -999

        if _arg not in self.cmd_dict:
            print('key "' + _arg + '" not in internal cmd dictionary')
            return -999

        if not self.cmd_dict[_arg]['writable']:
            print('key "' + _arg + '" not writable')
            return -999

        self.cmd_dict[_arg]['val'] = _val
        print('snmpset{x} -Oqv -v 2c -m +WIENER-CRATE-MIB -c public {ip} {name}.u{ch} {_type} {val}'.format(
            x=self.cmd_dict[arg]['x'], ip=self.ip, name=self.cmd_dict[arg]['name'], ch=self.ch_dict[ladder], _type=self.cmd_dict[arg]['type'], val=_val)

    def ChannelOn(self, _ch):
        # Turn on all high voltage channels with status 'disableKill'
        print('snmpset -Oqv -v 2c -m +WIENER-CRATE-MIB -c guru {ip} groupsSwitch.64 i 4'.format(ip=self.ip))

        # Set its supervision behavior to emergency off when trip current is exceeded (128, ramp down is 64, all off is 192)
        print('snmpset -Oqv -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSupervisionBehavior.u{ch} 128'.format(ip=self.ip, ch=_ch)

        # Set the trip time (time the current exceeds maximum to trip; default is 0 but this disables tripping--shortest trip time is 16ms)
        print('snmpset -Oqv -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputTripTimeMaxCurrent.u{ch} 16'.format(ip=self.ip, ch=_ch)

        # Set the current limit to something small (snmpsetx is not a typo; it enables e[x]tra precision in read/write)
        print('snmpsetx -Oqv -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputCurrent.u{ch} {arg}'.format(ip=self.ip, ch=_ch, arg=self.arg_dict['i_max'][0])

        # Turn channel on
        print('snmpset -Oqv -v 2c -m +WIENER-CRATE-MIB -c guru {ip} outputSwitch.u{ch} 1'.format(ip=self.ip, ch=_ch)




    def __init__(self, _ip):
        self.ip = _ip
        #will need to have an internal channel map

        # Map of channels to ladders
        # (should be loaded from file)
        self.ladder_dict = {
            'B0L00':    '000',
            'B0L01':    '001',
            'B0L02':    '010'}

        # Dictionary of SNMP commands
        # Shortened key with [value, command keyword]
        self.cmd_dict = {
            'status': {     # Read channel on/off or error status
                'readable': True,
                'writable': False,
                'val':      '0',
                'x':        '',
                'type':     'i',
                'name':     'outputSwitch'},

            'switch': {     # Toggle channel on/off
                'readable': True,
                'writable': True,
                'val':      '0',      # should call with 0, (off), 4 (for disableKill; allows supervision behavior), 10 (for clear events to reset flags)
                'x':        '',
                'type':     'i',
                'name':     'outputSwitch'},
            
            'su_be': {      # Supervision Behavior
                'readable': True,
                'writable': True,
                'val':      '128',    # should call with 64 for ramp down or 128 for emergency off when max current is exceeded
                'x':        '',
                'type':     'i',
                'name':     'outputSupervisionBehavior'},
            
            'tt_mc': {              # Duration for current to exceed maximum for supervision behavior to take effect
                'readable': True,
                'writable': True,
                'val':      '16',     # should be 16ms, the minimun value when this is enabled
                'x':        '',
                'type':     'i',
            
            'v_get': {      # Measured voltage (V)
                'readable': True,
                'writable': False,
                'val':      '0.0',
                'x':        '',
                'type':     'F',
                'name':     'outputMeasurementSenseVoltage'},

            'v_set': {      # User set voltage (V)
                'readable': True,
                'writable': True,
                'val':      '0.0',
                'x':        '',
                'type':     'F',
                'name':     'outputVoltage'},
            
            'i_get': {      # Measured current (A)
                'readable': True,
                'writable': False,
                'val':      '0.0',
                'x':        'x',    # read/write with extra precision when running snmp commands
                'type':     'F',
                'name':     'outputMeasurementCurrent'},
            
            'i_max': {      # Maximum current (A)
                'readable': True,
                'writable': True,
                'val':      '0.0',
                'x':        'x',    # read/write with extra precision when running snmp commands
                'type':     'F',
                'name':     'outputCurrent'}}
