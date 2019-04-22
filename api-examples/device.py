from runcible.core.device import Device
from runcible.core.callbacks import CBMethod
conf = {
    "meta": {
        "device": {
            "ssh": {
                "hostname": "192.168.122.41",
                "username": "cumulus",
                "password": "CumulusLinux!",
            },
            "default_management_protocol": "ssh",
            "driver": "cumulus"
        }
    },
    "system": {
        "hostname": "switch-test-2"
    }
}
d = Device("switch1", conf, callback_method=CBMethod.TERMINAL)
d.plan()
d.execute()
