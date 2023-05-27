from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError
from jnpr.junos.exception import LockError
from jnpr.junos.exception import UnlockError
from jnpr.junos.exception import CommitError
from jnpr.junos.exception import ConfigLoadError
def main():
    try:
        dev = Device(host= "10.254.200.5",user="nguyennd",passwd="bh6k8mfmnpk5bkh")
        dev.open()
    except ConnectError as err:
        print("Can not connect to Device: {0}".format(err))
        return
    dev.bind(cu=Config)
    # lock the configuration
    print("locking the configuration")
    try:
        dev.cu.lock()
    except LockError as err:
        print("unable to lock configuration : {0}".format(err))
        dev.close()
        return
    # load the configuration
    print("load configuration changes ")
    try:
        dev.cu.load('set system services netconf traceoptions file test.log',format='set')
    except (ConfigLoadError,Exception) as err:
        print("unable to load configuration changes : {0}".format(err))
        print("unlocking the configuration")
        try:
            dev.cu.unlock()
        except UnlockError as err:
            print("unable to unlock the configuration: {0}".format(err))
        dev.close()
    print("commit the configuration")
    try:
        dev.cu.commit()
    except CommitError as err:
        print("unable to commit the configuration: {0}".format(err))
        print("unlocking the configuration")
        try:
            dev.cu.unlock()
        except UnlockError as err:
            print("unable to unlock the configuration : {0}".format(err))
        dev.close()
    print("unlocking the configuration")
    try:
        dev.cu.unlock()
    except UnlockError as err:
        print("unable to unlock the configuration : {0}".format(err))
    dev.close()
if __name__== "__main__":
        main()