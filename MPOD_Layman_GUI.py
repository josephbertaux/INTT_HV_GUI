from MPOD_Layman_Graphic_Wrapper import *

class MPOD_Layman_GUI():
    def Loop(self):
        event, values = self.window.read()

        if event == sg.WIN_CLOSED:
            return False

        return True

    def __init__(self):

        # a dummy dicitonary of dictionaries for now
        # this should be loaded from a database once the mapping is set
        foo = {
            'B0L000':{
                'na':{'ip':'0.0.0.0', 'ch':'000'},
                'nb':{'ip':'0.0.0.0', 'ch':'001'},
                'sb':{'ip':'0.0.0.0', 'ch':'002'},
                'sa':{'ip':'0.0.0.0', 'ch':'003'}},

            'B0L001':{
                'na':{'ip':'0.0.0.1', 'ch':'004'},
                'nb':{'ip':'0.0.0.1', 'ch':'005'},
                'sb':{'ip':'0.0.0.1', 'ch':'006'},
                'sa':{'ip':'0.0.0.1', 'ch':'007'}}}

        self.refresh_time = 1
        self.dict = {k:MPOD_Layman_Graphic_Wrapper(v) for k, v in foo.items()}

        self.rows = {
            k:{                                                             #   Ladder key
                kk:{                                                        #   Sensor key
                    kkk:{kkkk:vvvv for kkkk, vvvv in vvv['gui'].items()}    #   Monitoring field key:[key:associated gui elements]
                    for kkk, vvv in vv['monitor'].items()}
                for kk, vv in v.dict.items()}
            for k, v in self.dict.items()}

        self.layout = [[]]
        for v in self.rows.values():                # Ladder dict               {sensor_key:{...}}
            row = []
            for vv in v.values():                   # Sensor dict               {monitoring_field:{...}}
                for vvv in vv.values():             # Monitoring field dict     {gui_key:gui_element}
                    for vvvv in vvv.values():       # gui_element
                        row += [vvvv]

            self.layout += [row]

        self.window = sg.Window('Sample Text', self.layout)
