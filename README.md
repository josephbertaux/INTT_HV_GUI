# INTT_HV_GUI
Repository backup for development of the INTT High Voltage GUI. Things like IP addresses are not stored here, but will be read from local files in a separate directory.

Current Workflow:
	MPOD_Channel_Wrapper is a class wrapper to implement necessary snmp commands through a singular MPOD Channel
	MPOD_Graphic_Wrapper is a class wrapper that implements the channel wrapper through internally maintained GUI elements
	MPOD_Layman_GUI
