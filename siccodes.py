import io
import requests
import zipfile

# Fama French Industries

# get different groups txt, if needed
groups = ['Siccodes5', 'Siccodes10', 'Siccodes12', 'Siccodes17', 'Siccodes30', 'Siccodes38', 'Siccodes48', 'Siccodes49']
url = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/"
for s in groups:
    r = requests.get(url+s+'.zip')
    f = io.BytesIO(r.content)
    f = zipfile.ZipFile(f)
    f.extractall()

# Set up a dictionary with keys = industry name, values = corresponding intervals of SIC codes
# Inputs: Siccodes5.txt, Siccodes10.txt, Siccodes12.txt, Siccodes17.txt, Siccodes30.txt, Siccodes38.txt,
#         Siccodes48.txt, Siccodes49.txt
def sic2industry(txt):
    f = open(txt, 'r', encoding='utf-8')
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    f.close()

    # categorize the industry name and sic codes
    dict = {}
    for line in lines:
        first = line.split(' ')[0]
        # If the first element is a number, the industry name should be the second element of this line
        if len(line) > 0 and len(first) < 3:
            industry = line.split(' ')[1]
            dict[industry] = []
        # When the industry name is retrieved, the sic codes below all belong to this category
        if len(line) > 0 and len(first) >= 3:
            line_interval = line.replace('-', ' ').split(' ')
            interval = [int(line_interval[0]), int(line_interval[1])]
            dict[industry].append(interval)

    return dict

# Functions for FFIndustry
# ff5
def ff5(sic):
    dict_ff5 = sic2industry('Siccodes5.txt')
    for industry in dict_ff5:
        for interval in dict_ff5[industry]:
            if sic >= interval[0] and sic <= interval[1]:
                return industry
    return 'Other'

# ff10
def ff10(sic):
    dict_ff10 = sic2industry('Siccodes10.txt')
    for industry in dict_ff10:
        for interval in dict_ff10[industry]:
            if sic >= interval[0] and sic <= interval[1]:
                return industry
    return 'Other'

# ff12
def ff12(sic):
    dict_ff12 = sic2industry('Siccodes12.txt')

    for industry in dict_ff12:
        for interval in dict_ff12[industry]:
            if sic >= interval[0] and sic <= interval[1]:
                return industry
    return 'Other'

# ff17
def ff17(sic):
    dict_ff17 = sic2industry('Siccodes17.txt')

    for industry in dict_ff17:
        for interval in dict_ff17[industry]:
            if sic >= interval[0] and sic <= interval[1]:
                return industry
    return 'Other'

# ff30
def ff30(sic):
    dict_ff30 = sic2industry('Siccodes30.txt')

    for industry in dict_ff30:
        for interval in dict_ff30[industry]:
            if sic >= interval[0] and sic <= interval[1]:
                return industry
    return 'Other'

# ff38
def ff38(sic):
    dict_ff38 = sic2industry('Siccodes38.txt')

    for industry in dict_ff38:
        for interval in dict_ff38[industry]:
            if sic >= interval[0] and sic <= interval[1]:
                return industry
    return 'Other'

# ff48
def ff48(sic):
    dict_ff48 = sic2industry('Siccodes48.txt')

    for industry in dict_ff48:
        for interval in dict_ff48[industry]:
            if sic >= interval[0] and sic <= interval[1]:
                return industry
    return 'Other'

# ff49
def ff49(sic):
    dict_ff49 = sic2industry('Siccodes49.txt')

    for industry in dict_ff49:
        for interval in dict_ff49[industry]:
            if sic >= interval[0] and sic <= interval[1]:
                return industry
    return 'Other'

# Example:
ff5(4920)


# GM: 1999 paper by by Grinblatt and Moskowitz
dict_GM = {'Mining': [[10, 14]],
           'Food': [[20, 20]],
           'Apparel': [[22, 23]],
           'Paper': [[26, 26]],
           'Chemical': [[28, 28]],
           'Petroleum': [[29, 29]],
           'Construction': [[32, 32]],
           'Prim. Metals': [[33, 33]],
           'Fab. Metals': [[34, 34]],
           'Machinery': [[35, 35]],
           'Electrical Eq.': [[36, 36]],
           'Transport Eq.': [[37, 37]],
           'Manufacturing': [[38, 39]],
           'Railroads': [[40, 40]],
           'Other Transport.': [[41, 47]],
           'Utilities': [[49, 49]],
           'Dept. Stores': [[53, 53]],
           'Retail': [[50, 52], [54, 59]],
           'Financial': [[60, 69]],
           }

# Function for GMIndustry
def GMindustry(sic):
    for industry in list(dict_GM.keys()):
        for interval in dict_GM[industry]:
            if sic >= interval[0] and sic <= interval[1]:
                return industry
    return 'Other'

# Example
# GMindustry(49)