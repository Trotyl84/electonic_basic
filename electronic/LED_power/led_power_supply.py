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

def calculations(Uc,Ud,I):
    """
    :param Uc: [ V ] Supply voltage
    :param Ud: [ V ] Voltage of correct operation of the diode.
    :param I:  [ mA ]  Diode operating current consumed
    :return R,Wd,Wr,:
        R: [ kOHM ] Value matching resistor expressed in Kilohms
        Wd: [ mW ] The power emitted by the diode. Value expressed in milliwatts
        Wr: [ mW ] The power released on the resistor. Value expressed in milliwatts
    """
    Ur = Uc-Ud
    R  = Ur/I
    Wr = Ur*I
    Wd = Ud*I
    return R, Wd, Wr


if __name__ == "__main__":
    """
    # Data example:
    Uc = 5
    Ud = 1.5
        MAX voltage:
        Infrared—1.6V
        Red—1.8 to 2.1V
        Orange—2.2V
        Yellow—2.4V
        Green—2.6V
        Blue—3.0 to 3.5V (White same as blue)
        UltraViolet—3.5V
    I = 10 # [ mA ]
    """

    try:
        Uc = float(input("Plese insert supply voltage [ V ] :\n"))
        Ud = float(input("Plese insert LED voltage [ V ] :\n"))
        I = float(input("Diode operating current consumed [ mA ] :\n"))

    except ValueError:
        print( """Enter the number as a digit. 
        Use dots to mark the tenth part""")

    finally:
        print("""       %5.3f [ kOHM ] Value matching resistor expressed in Kilohms.
    %5.0f [ mW ] The power emitted by the diode. Value expressed in milliwatts.
    %5.0f [ mW ] The power released on the resistor. Value expressed in milliwatts
    """ % calculations( Uc, Ud, I ))
# (Point 2)