import pyflight
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet_format("REAPER")
print(ascii_banner)

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid Target")

print("-" * 50)
print("Reaping Ports: " + target)
print("Reap Started at: " + str(datetime.now()))

try:
    for port in range(1.1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soccket.setdefaulttimeout(1)

except  KeyboardInterrupt:
    print("\n Exiting Reaper !!!")
    sys.exit()

except socket.gaierror:
    print("\n Hostname could not be Reaped for Open Ports")
    sys.exit()

except socket.error:
    print("\n service not responding to Probes !!!!")        