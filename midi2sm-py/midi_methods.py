import io
import os
import typing
# Needed for sign conversion
from ctypes import c_uint32, c_uint16, c_uint8

def uint32(file: io.FileIO):
    to_parse = file.read(4)
    rval = 0x00

    if len(to_parse) != 4:
        raise IOError("Not enough bytes found")

    to_parse = [c_uint32(x).value for x in to_parse]  # Convert any unwanted negatives away

    rval |= to_parse[0] << 0
    rval |= to_parse[1] << 8
    rval |= to_parse[2] << 16
    rval |= to_parse[3] << 24


    return rval

def uint24(file: io.FileIO) -> int:
    to_parse = file.read(3)
    rval = 0x00

    if len(to_parse) != 3:
        raise IOError("Not enough bytes found")

    to_parse = [c_uint32(x).value for x in to_parse]

    rval |= to_parse[0] << 0
    rval |= to_parse[1] << 8
    rval |= to_parse[2] << 16

    return rval

def uint16(file: io.FileIO) -> int:
    to_parse = file.read(2)
    rval = 0x00

    if len(to_parse) != 2:
        raise IOError("Not enough bytes found")

    to_parse = [c_uint16(x).value for x in to_parse]

    rval |= to_parse[0] << 0
    rval |= to_parse[1] << 8

    return rval

def uint7(file: io.FileIO) -> int:
    to_parse = file.read(1)
    if len(to_parse) != 1:
        raise IOError("Not enough bytes found")

    rval = (to_parse[0] & 0x7F)
    return rval

def parse_pitch_wheel(file: io.FileIO) -> (int, int):
