
import pandas as pd

def _read_fixed_width_data(file_name, format_string, column_names=None,skiprows=0,comment='#'):
    """
    Reading fixed width data
    """
    columns = _create_columns_from_format_string(format_string)
    data = pd.read_fwf(file_name, colspecs=columns, header=None,skiprows = skiprows,comment=comment)
    if column_names is not None:
        data.columns = column_names
    return data

def _create_columns_from_format_string(format_string):
    """
    "+++00^^++" -> ((0,3),(5,7),(7,9))
    0 stands for column to ommit
    """
    columns = []
    last_change_idx = 0
    last_character = -1
    for i, c in enumerate(format_string+"x"): # add 'x' to introduce change at the end
        if last_character != c:
            if last_change_idx != i and last_character != '0':
                columns.append((last_change_idx,i))
            last_change_idx = i
            last_character = c
    return tuple(columns)