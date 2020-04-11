
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

def string_from_kurucz_code(kurucz_code):
    kurucz_float = float(kurucz_code)
    atom, ion = [int(x) for x in f"{kurucz_float:.2f}".split('.')]
    return "{}{}".format(atomic_number_to_symbol[atom], encode_roman_numeral(ion+1))

def decode_roman_numeral(roman):
    """Calculate the numeric value of a Roman numeral (in capital letters)"""
    # CREDITS: 200_success, https://codereview.stackexchange.com/questions/141402/converting-from-roman-numerals-to-arabic-numbers
    trans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    values = [trans[r] for r in roman]
    return sum(
        val if val >= next_val else -val
        for val, next_val in zip(values[:-1], values[1:])
    ) + values[-1]

def encode_digit(digit, one, five, nine):
    # CREDITS: 200_success, https://codereview.stackexchange.com/questions/141402/converting-from-roman-numerals-to-arabic-numbers
    return (
        nine                     if digit == 9 else
        five + one * (digit - 5) if digit >= 5 else
        one + five               if digit == 4 else
        one * digit              
    )

def encode_roman_numeral(num):
    # CREDITS: 200_success, https://codereview.stackexchange.com/questions/141402/converting-from-roman-numerals-to-arabic-numbers
    num = int(num)
    return (
        'M' * (num // 1000) +
        encode_digit((num // 100) % 10, 'C', 'D', 'CM') +
        encode_digit((num //  10) % 10, 'X', 'L', 'XC') +
        encode_digit( num         % 10, 'I', 'V', 'IX') 
    )

atomic_number_to_symbol = {
      1:'H' ,
      2:'He',
      3:'Li',
      4:'Be',
      5:'B' ,
      6:'C' ,
      7:'N' ,
      8:'O' ,
      9:'F' ,
     10:'Ne',
     11:'Na',
     12:'Mg',
     13:'Al',
     14:'Si',
     15:'P' ,
     16:'S' ,
     17:'Cl',
     18:'Ar',
     19:'K' ,
     20:'Ca',
     21:'Sc',
     22:'Ti',
     23:'V' ,
     24:'Cr',
     25:'Mn',
     26:'Fe',
     27:'Co',
     28:'Ni',
     29:'Cu',
     30:'Zn',
     31:'Ga',
     32:'Ge',
     33:'As',
     34:'Se',
     35:'Br',
     36:'Kr',
     37:'Rb',
     38:'Sr',
     39:'Y' ,
     40:'Zr',
     41:'Nb',
     42:'Mo',
     43:'Tc',
     44:'Ru',
     45:'Rh',
     46:'Pd',
     47:'Ag',
     48:'Cd',
     49:'In',
     50:'Sn',
     51:'Sb',
     52:'Te',
     53:'I' ,
     54:'Xe',
     55:'Cs',
     56:'Ba',
     57:'La',
     58:'Ce',
     59:'Pr',
     60:'Nd',
     61:'Pm',
     62:'Sm',
     63:'Eu',
     64:'Gd',
     65:'Tb',
     66:'Dy',
     67:'Ho',
     68:'Er',
     69:'Tm',
     70:'Yb',
     71:'Lu',
     72:'Hf',
     73:'Ta',
     74:'W' ,
     75:'Re',
     76:'Os',
     77:'Ir',
     78:'Pt',
     79:'Au',
     80:'Hg',
     81:'Tl',
     82:'Pb',
     83:'Bi',
     84:'Po',
     85:'At',
     86:'Rn',
     87:'Fr',
     88:'Ra',
     89:'Ac',
     90:'Th',
     91:'Pa',
     92:'U' ,
     93:'Np',
     94:'Pu',
     95:'Am',
     96:'Cm',
     97:'Bk',
     98:'Cf',
     99:'Es',
    100:'Fm',
    101:'Md',
    102:'No',
    103:'Lr',
    104:'Rf',
    105:'Db',
    106:'Sg',
    107:'Bh',
    108:'Hs',
    109:'Mt',
    110:'Ds',
    111:'Rg',
    112:'Cn',
    113:'Nh',
    114:'Fl',
    115:'Mc',
    116:'Lv',
    117:'Ts',
    118:'Og',
}