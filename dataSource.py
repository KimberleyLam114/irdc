# modify value below before deploy the web page
def 本月():
    return 1

def 上月():
    return 12

def 本年():
    return 2023

def 上年():
    return 2022

def 更新时间():
    return str("2023/2/20")

def 本月人员维度():
    return str(本月())+"月人员维度.csv"

def 上月人员维度():
    return str(上月())+"月人员维度.csv"

def 本月WBS维度():
    return str(本月())+"月WBS维度.csv"

def 上月WBS维度():
    return str(上月())+"月WBS维度.csv"

def 本月未填工时名单():
    return str(本月())+'月未填工时名单.csv'

def 上月未填工时名单():
    return str(上月())+'月未填工时名单.csv'

def 本月业务线维度():
    return str(本月())+"月业务线维度.csv"

def 上月业务线维度():
    return str(上月())+"月业务线维度.csv"

def 本月员工所属部门():
    return str(本月())+"月员工所属部门.csv"

def 历史部门实际人均人天():
    return '历史部门实际人均人天.csv'

def 历史部门理论填报率():
    return '历史部门理论填报率.csv'

def 本月业务线员工组():
    return str(本月())+"月部门员工组.csv"

def 本月员工所属部门():
    return str(本月())+"月员工所属部门.csv"

def 历史WBS类型实际人天():
    return '历史WBS类型实际人天.csv'

def 历史GPU使用情况():
    return '历史gpu使用率.csv'