from MPOD_Layman_GUI import *

mpod_layman_gui = MPOD_Layman_GUI()

mpod_layman_gui.Loop()
mpod_layman_gui.StartUpdates()
while(mpod_layman_gui.Loop()):
    continue

mpod_layman_gui.window.close()
