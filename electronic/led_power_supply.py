# coding: utf-8
"""
Schematic:

Uc  I
   o
   |
  | | R
  | |
   |
  \/  D_LED
  --
  |
  o GND

"""

# Data example:
Uc = 5
Ud = 1.5
I = 10 # [ mA ]

def calculations(Uc,Ud,I):
    """
    :param Uc: [ V ] Supply voltage
    :param Ud: [ V ] Voltage of correct operation of the diode.
    :param I:  [ mA ]  Diode operating current consumed
    :return R,Wd,Wr,Ur:
        R: [ kOHM ] Value matching resistor expressed in Kilohms
        Wd: [ mW ] The power emitted by the diode. Value expressed in milliwatts
        Wr: [ mW ] The power released on the resistor. Value expressed in milliwatts

    """
    Ur = Uc-Ud
    R  = Ur/I
    Wr = Ur*I
    Wd = Ud*I
    return R,Wd,Wr


print("""%5.3f [ kOHM ] Value matching resistor expressed in Kilohms.
%5.0f [ mW ] The power emitted by the diode. Value expressed in milliwatts.
%5.0f [ mW ] The power released on the resistor. Value expressed in milliwatts
""" %calculations(Uc,Ud,I))

