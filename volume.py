from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
def volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None )
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    current = volume.GetMasterVolumeLevel()
    print(current)


    #print(34.75468063354492-33.33053970336914)
    tak_vol = float(input("Enter volume percent: "))

    #tak_vol = 1.4241409301757812 * tak_vol
    volume.SetMasterVolumeLevel(tak_vol, None)             # volume 1.4241409301757812 = 1%
    volume.SetMute(0, None)                                          # Mute (1) and unmute (0)























































































































