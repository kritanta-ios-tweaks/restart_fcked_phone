from pymobiledevice.diagnostics_relay import DIAGClient

x = DIAGClient()

try:
    x.restart()
    # this will throw an error, but it should work :)
except Exception:
    pass

print ('Request sent, should be restarting now :)')
