'''
Module of Linux API for plyer.devicename.
'''

import socket
from plyer.facades import DeviceName


class LinuxDeviceName(DeviceName):
    '''
    Implementation of Linux DeviceName API.
    '''

    def _get_device_name(self):
        return socket.gethostname()


def instance():
    '''
    Instance for facade proxy.
    '''
    return LinuxDeviceName()
