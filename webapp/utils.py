import binascii


class Bech32Utils: # borrowed from https://github.com/sipa/bech32/blob/master/ref/python/segwit_addr.py

    @classmethod
    def Convert_Pub_2_One_Address(cls, public_address):
        hex_address = binascii.a2b_hex(public_address)
        binary_address = Bech32Utils._convertbits(hex_address, 8, 5)
        return cls._bech32_encode('one', binary_address)

    @staticmethod
    def _convertbits(data, frombits, tobits, pad=True):
        """General power-of-2 base conversion."""
        acc = 0
        bits = 0
        ret = []
        maxv = (1 << tobits) - 1
        max_acc = (1 << (frombits + tobits - 1)) - 1
        for value in data:
            if value < 0 or (value >> frombits):
                return None
            acc = ((acc << frombits) | value) & max_acc
            bits += frombits
            while bits >= tobits:
                bits -= tobits
                ret.append((acc >> bits) & maxv)
        if pad:
            if bits:
                ret.append((acc << (tobits - bits)) & maxv)
        elif bits >= frombits or ((acc << (tobits - bits)) & maxv):
            return None
        return ret


def is_valid_address(address) -> bool:
    """
    Check if given string is valid one address
    NOTE: This function is NOT thread safe due to the C function used by the bech32 library.
    Parameters
    ----------
    address: str
        String to check if valid one address
    Returns
    -------
    bool
        Is valid address
    """
    import bech32
    if not address.startswith('one1'):
        return False
    hrp, _ = bech32.bech32_decode(address)
    if not hrp:
        return False
    return True


def convert_one_to_hex(addr):
    """
    Given a one address, convert it to hex checksum address
    """
    from bech32 import (
        bech32_decode,
        convertbits
    )
    from eth_utils import to_checksum_address

    if not is_valid_address(addr):
        return to_checksum_address(addr)
    hrp, data = bech32_decode(addr)
    buf = convertbits(data, 5, 8, False)
    address = '0x' + ''.join('{:02x}'.format(x) for x in buf)
    return to_checksum_address(address)
