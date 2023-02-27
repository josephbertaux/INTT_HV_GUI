from MPOD_Channel import MPOD_Channel


mpod = MPOD_Channel('00.000.00', '4')
mpod.PrintArgs()
mpod.UpdateArg('v_min', 7.0)
mpod.PrintArgs()
