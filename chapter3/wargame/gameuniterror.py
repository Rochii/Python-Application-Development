"""gameuniterror

Shows how to create a custom exception class for the Attack of the Orcs game

This module is compatible with Python 3.5.x. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

The use of this module is illustrated in Chapter 2, exception handling.

RUNNING THE PROGRAM:
--------------------
This is NOT run as a standalone program. See `attackoftheorcs_v_1_1.py`

# --------------------------------------------------------------------------
# Alternate implementation where you subclass the custom exception,
# GameUniError. The following code would eliminate the need of
# maintaining an error_dict object in GameUnitError. See the chapter for
# further details.
# --------------------------------------------------------------------------
# class GameUnitError(Exception):
#     def __init__(self, message=''):
#         super().__init__(message)
#         self.padding = '~'*50 + '\n'
#         self.error_message = " Unspecified Error!"
#
# class HealthMeterException(GameUnitError):
#     def __init__(self, message=''):
#         super().__init__(message)
#         self.error_message = (self.padding +
#                              "ERROR: Health Meter Problem" +
#                              '\n' + self.padding )
#
# class AttackException(GameUnitError):
#     # Code similar to that of HealthMeterException .
#     pass

.. seealso:: `attackoftheorcs_v_1_1.py`, `heal_exception_example.py`

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""

class GameUnitError(Exception):
    """Custom exceptions class for the `AbstractGameUnit` and its subclasses"""
    def __init__(self, message=""):
        super().__init__(message)
        self.padding = "~"*50 + "\n"
        self.error_message = "Unspecified Error!"

class HealthMeterException(GameUnitError):
    """Custom exception to report Health Meter related problems"""
    def __init__(self, message=""):
        super().__init__(message)
        self.error_message = (self.padding +
                             "ERROR: Health Meter Problem" +
                             "\n" + self.padding)

class HutError(Exception):
    def __init__(self, code):
        self.error_message = ""

        self.error_dict = {
            000: "E000: Unspecified Error!",
            101: "E101: Out of range: Number > 5!",
            102: "E102: Out of range, negative number",
            103: "E103: Not a number",
        }

        try:
            self.error_message += self.error_dict[code]
        except KeyError:
            self.error_message += self.error_dict[000]

        print("\n Error message:", self.error_message)


class HutErrorNumberHigherThanFive(HutError):
    pass


class HutErrorNegativeNumber(HutError):
    pass