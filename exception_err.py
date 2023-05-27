
import sys
from jnpr.junos import Device
from getpass import getpass
from jnpr.junos.exception import ConnectError
hostname = "10.254.200.5"
username = "nguyennd"
password = "bh6k8mfmnpk5bk2h"
dev= Device(host=hostname,user = username,passwd=password)
try: 
    dev.open()
except ConnectError as err:
    print("Can not connect to the Device: {0}".format(err))
    sys.exit(1)
except Exception as err:
    print(err)
    sys.exit(1)
print(dev.facts)
dev.close()
