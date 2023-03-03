class MPOD_Channel_Commands():
    def Get(self, _arg):
        _arg = str(_arg)

        if _arg not in self.dict:
            print('key "' + _arg + '" not in internal cmd dictionary')
            return -999

        if not self.dict[_arg]['readable']:
            print('key "' + _arg + '" not readable')
            return -999

        print('snmpget{x} -Oqv -v 2c -m +WIENER-CRATE-MIB -c public {ip} {name}.u{ch}'.format(
            x=self.dict[_arg]['x'],
            ip=self.ip, name=self.dict[_arg]['name'],
            ch=self.ch))

        #_val = ''
        #try:
        #    _val = self.dict[_arg]['var_type'](#output of snmpget command)
        #except ValueError:
        #    print('Could not cast "' + str(_val) + '" as type "' + str(type(self.dict[_arg]['var_type'])))
        #    return -999
        #self.dict[_arg]['val'] = _val
        return self.dict[_arg]['val']

    def Set(self, _arg, _val):
        _arg = str(_arg)

        if _arg not in self.dict:
            print('key "' + _arg + '" not in internal cmd dictionary')
            return

        if not self.dict[_arg]['writable']:
            print('key "' + _arg + '" not writable')
            return

        try:
            _val = self.dict[_arg]['var_type'](_val)
        except ValueError:
            print('Could not cast "' + str(_val) + '" as type "' + str(type(self.dict[_arg]['var_type'])))
            print('No value was set')
            return

        self.dict[_arg]['val'] = _val
        print('snmpset{x} -Oqv -v 2c -m +WIENER-CRATE-MIB -c public {ip} {name}.u{ch} {str_type} {val}'.format(
            x=self.dict[_arg]['x'],
            ip=self.ip,
            name=self.dict[_arg]['name'],
            ch=self.ch,
            str_type=self.dict[_arg]['str_type'],
            val=_val))



    def TurnOn(self):
        # Check to see if this channel was previously set with flag for outputFailureMaxCurrent
        if self.Get('status') == 4:
            print('Previous run set error flag for outputFailureMaxCurrent')
            print('Channel "' + self.ladder_dict[_ladder] + '" was not switched on (corresponding to ladder "' + _ladder + '")')
            print('Clear Flags to switch back on, but make sure this was documented including previous voltage setting')
            return

        # Set all to diableKill (need to check if this can be done individually with outputSwitch 4)
        #print('snmpset -Oqv -v 2c -m +WIENER-CRATE-MIB -c guru {ip} groupsSwitch.64 i 4'.format(ip=self.ip))

        # Set its supervision behavior to emergency off when trip current is exceeded
        # (ramp down is 64, emergency off is 128, all off is 192)
        self.Set('su_be', 128)

        # Set the trip time (time the current exceeds maximum to trip
        # (default is 0 but this disables tripping--shortest trip time is 16ms)
        self.Set('tt_mc', 16)
        
        # Set the current limit to something small  # !!!   THIS VALUE IS IN AMPS   !!!
        self.Set('i_max', 0.0000001)                # !!!   THIS VALUE IS IN AMPS   !!!

        # Turn on this channel with status 'disableKill'
        self.Set('switch', 4)
        return

    def TurnOff(self):
        _ladder = str(_ladder)

        if _ladder not in self.ladder_dict:
            print('key "' + _ladder + '" not in internal ladder dictionary')
            return

        self.Set(_ladder, 'switch', 0)
        return

    def ClearEvents(self, _ladder):
        _ladder = str(_ladder)

        if _ladder not in self.ladder_dict:
            print('key "' + _ladder + '" not in internal ladder dictionary')
            return

        self.Set(_ladder, 'switch', 10)
        return



    def __init__(self, _ip, _ch):
        self.ip = _ip
        self.ch = _ch

        # Dictionary of SNMP commands
        # Shortened key with [value, command keyword]
        self.dict = {
            'status': {     # Read channel on/off or error status
                'readable': True,
                'writable': False,
                'val':      '0',
                'x':        '',
                'str_type': 'i',
                'var_type': int,
                'name':     'outputSwitch'},

            'switch': {     # Toggle channel on/off
                'readable': False,      # should read 'status' instead
                'writable': True,
                'val':      '0',        # should call with 0, (off), 4 (for disableKill; allows supervision behavior), 10 (for clear events to reset flags)
                'x':        '',
                'str_type': 'i',
                'var_type': int,
                'name':     'outputSwitch'},
            
            'su_be': {      # Supervision Behavior
                'readable': True,
                'writable': True,
                'val':      '128',      # should call with 64 for ramp down or 128 for emergency off when max current is exceeded
                'x':        '',
                'str_type': 'i',
                'var_type': int,
                'name':     'outputSupervisionBehavior'},
            
            'tt_mc': {      # Duration for current to exceed maximum for supervision behavior to take effect
                'readable': True,
                'writable': True,
                'val':      '16',       # should be 16ms, the minimun value when this is enabled
                'x':        '',
                'str_type': 'i',
                'var_type': int,
                'name':     'outputTripTimeMaxCurrent'},
            
            'v_get': {      # Measured voltage (V)
                'readable': True,
                'writable': False,
                'val':      '0.0',
                'x':        '',
                'str_type': 'F',
                'var_type': float,
                'name':     'outputMeasurementSenseVoltage'},

            'v_set': {      # User set voltage (V)
                'readable': True,
                'writable': True,
                'val':      '0.0',
                'x':        '',
                'str_type': 'F',
                'var_type': float,
                'name':     'outputVoltage'},
            
            'i_get': {      # Measured current (A)
                'readable': True,
                'writable': False,
                'val':      '0.0',
                'x':        'x',    # read/write with extra precision when running snmp commands
                'str_type': 'F',
                'var_type': float,
                'name':     'outputMeasurementCurrent'},
            
            'i_max': {      # Maximum current (A)
                'readable': True,
                'writable': True,
                'val':      '0.0',
                'x':        'x',    # read/write with extra precision when running snmp commands
                'str_type': 'F',
                'var_type': float,
                'name':     'outputCurrent'}}
