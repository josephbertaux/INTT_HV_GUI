from MPOD_Channel_Graphics import *

class INTT_Barrel_Graphics():
    def __init__(self, _map):
        # _map is a map of ladders to maps of sensors to mpod channel parameters
        # e.g. {ladder:{sensor:{parameter_map}}}

        # A map wrapping the fields of this class
        self.dict = {
            ladder:{
                sensor:MPOD_Channel_Graphics(sensor_map)
                for sensor, sensor_map in ladder_map.items()}
            for ladder, ladder_map in _map.items()}

        # A flattened map we don't have to nest loops
        self.flat = {}
        for ladder, ladder_map in self.dict.items():
            for sensor, mpod_channel_graphics in ladder_map.items():
                if ladder + sensor not in self.flat:
                    self.flat.update({ladder+sensor:mpod_channel_graphics})

        self.layout = []

        for ladder, ladder_map in self.dict.items():
            row = [sg.Text(ladder, s=2, justification='right')]
            for sensor, mpod_channel_graphics in ladder_map.items():
                row += [sg.Frame('', [[gui_element for gui_key, gui_element in mpod_channel_graphics.layman_elements.items()]])]
            self.layout += [row]

        for ladder, ladder_map in self.dict.items():
            row = [sg.Text('', s=2)] # Text above the ladder labels
            for sensor, mpod_channel_graphics in ladder_map.items():
                row += [sg.Text(sensor, s=46, justification='center')]  # Gotta guess the size lmao
            self.layout = [row] + self.layout
            break
