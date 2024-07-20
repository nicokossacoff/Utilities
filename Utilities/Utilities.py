import pandas as pd
import numpy as np

class Charts():
    def axis_format(self, units: str, decimals: int, x, pos):
        '''
        This function returns a string to format the axes.

        :params units: str | The units in the axis number.
        :params decimals: str | The number of decimals in the format.
        '''

        # Error handling: value types
        if not isinstance(units, str):
            raise ValueError(f"Expected 'units' to be 'str', but received '{type(units).__name__}' instead.")
        if not isinstance(decimals, int):
            raise ValueError(f"Expected 'units' to be 'str', but received '{type(units).__name__}' instead.")
        
        try:
            if units == 'thousands':
                return f'{x / 1000: .{decimals}f}K'
            elif units == 'millions':
                return f'{x / 1000000: .{decimals}f}K'
        except:
            raise Exception('An exception ocurred')