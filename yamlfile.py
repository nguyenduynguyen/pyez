import json
import yaml
import sys
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
dev= Device(host="10.254.200.5",user= "nguyennd",passwd ="bh6k8mfmnpk5bkh")
try:
    dev.open()
    data = dev.facts
    # print(data)
    # print(yaml.dump(data))
    # print(json.dump(data))
    print(json.dumps(dev.facts))
    # print(yaml.dump(dev.facts))
    dev.close()
except ConnectError as err:
    print("Can not connect to Device : {0}".format(err))
    sys.exit(1)