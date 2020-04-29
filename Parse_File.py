"""Methods for file processing"""

import re #regular expression
import io #UTF8 processing
from bs4 import BeautifulSoup #HTML parser library

#get number of new cases from created file
def case_num(file):
    with io.open(file, "r+", encoding="UTF8") as f:
        first_line = f.readlines()
    #explicit statement of number of cases
    x = re.search(r"公\w+新增([0-9]+)例", str(first_line))
    u = re.search(r"其中([0-9]+)例確診", str(first_line))
    #one cases
    y= re.search(r"第[0-9]+例\S+", str(first_line))
    #no cases
    z = re.search(r"無新增", str(first_line))
    #exceptions
    w1 = re.search(r"新增([0-9]+)確診", str(first_line))
    w2 = re.search(r"新增([0-9]+)例確定病例", str(first_line))
    #return case numbers
    if x and not u:
        cases = x.group(1)
        return cases
    elif x and u:
        cases = u.group(1)
        return cases
    elif y:
        return "1"
    elif z:
        return "0"
    elif w1:
        return w1.group(1)
    elif w2:
        return w2.group(1)
    else:
        return "N/A"

#get date from created file
def get_date(file):
    with io.open(file, "r+", encoding="UTF8") as f:
        first_line = f.readlines(0)
    x = re.search(r"發佈日期.*(\d\d\d\d-\d\d-\d\d)", str(first_line))
    return x.group(1)

#--------------ongoing----------------------------------------
#return list of case ids
#build cases from
#案62為北部60多歲女性
def case_id(f):
    case_id=[]
    x= re.search(r"第([0-9]+)例\S+", str(f[0]))
    people = re.findall(r"案\w+性", str(f))
    if x:
        case_id.append(x.group(1))
        return case_id
    if people:
        for y in people:
            x = re.search(r"案([0-9]+)", y)
            case_id.append(x.group(1))
            case_id= list(dict.fromkeys(case_id))
        return case_id

#need to build cases here
#案65至67為南部2名50多歲女性及1名60多歲男性
