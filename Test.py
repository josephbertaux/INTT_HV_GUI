from Wrapper import HV_Wrapper

hv_wrapper = HV_Wrapper()

my_args = {'ip': '1234.5678.9101112', 'channel': '1253215235616', 'value': '100'}

hv_wrapper.TryCommand('set_v', my_args)
hv_wrapper.TryCommand('get_v', my_args)
hv_wrapper.TryCommand('not in dictionary', my_args)
