from MPOD_Channel_Graphics import *

class MPOD_Layman_GUI():
    def Update(self, _s):
        k = parse('{}___{}___{}', _s).fixed
        self.window.perform_long_operation(self.dict[k[0]][k[1]][k[2]].Update, _s)

    def StartUpdates(self):
        for k, v in self.dict.items():          # Barrels
            for kk, vv in v.items():            # Ladders
                for kkk, vvv in vv.items():     # Sensors/MPOD_Channel_Graphics
                    self.Update(k + '___' + kk + '___' + kkk)
    def Loop(self):
        event, values = self.window.read()

        if event == sg.WIN_CLOSED:
            return False

        if callable(event):
            self.window.perform_long_operation(event, '___USER___')
            return True

        elif event == '___USER___':
            # Do nothing
            # A thread started by user input has finished
            return True

        else:
            # An update thread has finished
            if(values[event]):
                print('flag for event: ' + event + 'was set')

            # Restart the thread
            self.Update(event)
            return True

    def __init__(self):

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
        print(biz['B0L0']['00']['na']['ip'])

        self.dict = {
            k:{                                                                                     # Barrel
                kk:{                                                                                # Ladder
                    kkk:MPOD_Channel_Graphics(vvv['ip'], vvv['ch']) for kkk, vvv in vv.items()}     # Sensor/MPOD_Channel
                for kk, vv in v.items()}
            for k, v in biz.items()}

        self.tab_groups = {k:[] for k, v in self.dict.items()}
        for k, v in self.dict.items():
            for kk, vv in v.items():
                row = [sg.VSeperator(), sg.Text(k + kk, s=6)]
                for kkk, vvv in vv.items():
                    for i in vvv.layman_elements:
                        row += [i]
                    row += [sg.VSeperator()]
                self.tab_groups[k] += [row]

        self.layout = [[sg.TabGroup([[sg.Tab(k, v) for k, v in self.tab_groups.items()]])]]

        self.window = sg.Window('Sample Text', self.layout)
