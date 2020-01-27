'''from __future__ import print_function
import psutil

dps = psutil.disk_partitions()
print(dps)
fmt_str = "{:<8} {:<7} {:<7}"
print(fmt_str.format("Drive", "Type", "Opts"))
# Only show a couple of different types of devices, for brevity.
#print(fmt_str.format(dps.device, dps.fstype, dps.opts))'''

import subprocess

def uname_func():
    uname="uname"
    uname_arg="-a"
    print("Gathering system information with %s command:\n", uname.sub)