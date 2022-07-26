def connect(self):
    """Attempts to initiate a connection with the device.

    :return: `True` if connection was successful, `False` otherwise
    :rtype: bool
    """
    try:
        super().connect(self.addr,
                        addrType=self.addrType,
                        iface=self.iface)
    except BTLEException as ex:
        self._connected = False
        return (False, ex)
    self._connected = True
    return True