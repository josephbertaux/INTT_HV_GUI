from INTT_Barrel_Graphics import *

class Layman_GUI():
    def Update(self, _k):
        self.window.perform_long_operation(self.flat[_k].Update, _k)

    def BeginMonitoring(self):
        self.monitoring = True
        for key in self.flat.keys():
            self.Update(key)

    def StopMonitoring(self):
        self.monitoring = False

    def AllOn(self):
        return

    def AllOff(self):
        return

    def ToggleExpert(self):
        return


    def Loop(self):
        event, values = self.window.read()

        if event == sg.WIN_CLOSED:
            try:
                self.window.close()
                return False
            except ValueError:
                return False

        if callable(event):
            self.window.perform_long_operation(event, '___USER___')
            return True

        elif event == '___USER___':
            # Do nothing
            # A thread started by user input has finished
            return True

        else:
            # Restart the thread if we're still monitoring
            if self.monitoring:
                self.Update(event)
            return True

    def __init__(self):
        sg.set_options(font=('Noto Mono', 8))
        self.monitoring = False
        # a dummy dicitonary of dictionaries for now
        # this should be loaded from a database once the mapping is set
        foo = {
            '00':{
                'na':{'ip':'0.0.0.0', 'ch':'000'},
                'nb':{'ip':'0.0.0.0', 'ch':'001'},
                'sb':{'ip':'0.0.0.0', 'ch':'002'},
                'sa':{'ip':'0.0.0.0', 'ch':'003'}},

            '01':{
                'na':{'ip':'0.0.0.1', 'ch':'004'},
                'nb':{'ip':'0.0.0.1', 'ch':'005'},
                'sb':{'ip':'0.0.0.1', 'ch':'006'},
                'sa':{'ip':'0.0.0.1', 'ch':'007'}}}

        bar = {
            '00':{
                'na':{'ip':'1.0.0.0', 'ch':'100'},
                'nb':{'ip':'1.0.0.0', 'ch':'101'},
                'sb':{'ip':'1.0.0.0', 'ch':'102'},
                'sa':{'ip':'1.0.0.0', 'ch':'103'}},

            '01':{
                'na':{'ip':'1.0.0.1', 'ch':'104'},
                'nb':{'ip':'1.0.0.1', 'ch':'105'},
                'sb':{'ip':'1.0.0.1', 'ch':'106'},
                'sa':{'ip':'1.0.0.1', 'ch':'107'}}}

        biz = {'B0L0':foo, 'B1L1':bar}

        # A map wrapping the fields of this class
        self.dict = {barrel:INTT_Barrel_Graphics(barrel_map) for barrel, barrel_map in biz.items()}

        # A flattened map of mpod channels so we don't have to nest loops
        self.flat = {}
        for barrel, barrel_graphics in self.dict.items():
            for mpod_channel, mpod_channel_graphics in barrel_graphics.flat.items():
                if barrel + mpod_channel not in self.flat:
                    self.flat.update({barrel + mpod_channel:mpod_channel_graphics})

        self.layout = [
                [
                    sg.Button('Begin Monitoring',   key=lambda: self.BeginMonitoring()),
                    sg.Button('Stop Monitoring',    key=lambda: self.StopMonitoring()),
                    sg.Button('All On',             key=lambda: self.AllOn()),
                    sg.Button('All Off',            key=lambda: self.AllOff())],
                [
                    sg.TabGroup([[
                        sg.Tab(barrel, barrel_graphics.layout)
                        for barrel, barrel_graphics in self.dict.items()]])] ]

        self.window = sg.Window('Sample Text', self.layout)
