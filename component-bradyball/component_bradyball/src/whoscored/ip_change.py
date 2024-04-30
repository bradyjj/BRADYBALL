from stem import Signal
from stem.control import Controller

def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password='your_password')  # If your Tor setup has a password
        controller.signal(Signal.NEWNYM)

try:
    renew_tor_ip()
    print("Tor IP renewed")
except Exception as e:
    print("Failed to renew Tor IP:", e)