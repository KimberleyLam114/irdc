import pathlib
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from dataSource import *

def readData(fileName):
    PATH = pathlib.Path(__file__).parent
    DATA_PATH = PATH.joinpath("assets/data").resolve()
    return pd.read_csv(DATA_PATH.joinpath(fileName))

def cleanCurMonStaff(data):
    cur_mon_staff = readData(data)
    cur_mon_staff['预估填报率'] = pd.to_numeric(cur_mon_staff['预估填报率'], errors='coerce')
    cur_mon_staff = cur_mon_staff.replace(np.nan, 0, regex=True)
    cur_mon_staff['理论填报率'] = pd.to_numeric(cur_mon_staff['理论填报率'], errors='coerce')
    cur_mon_staff = cur_mon_staff.replace(np.nan, 0, regex=True)
    cur_mon_staff = cur_mon_staff[~cur_mon_staff['员工所属部门'].isin(['智慧体育业务','新零售业务','亚太研发中心','创新业务部'])]
    cur_mon_staff = cur_mon_staff[~cur_mon_staff['员工组'].isin(['人力外包'])]
    return cur_mon_staff

def filterCurMonStaff(data, tableValue, filterValue):
    return cleanCurMonStaff(data)[cleanCurMonStaff(data)[tableValue] == filterValue]


def monStaff_businessLine(data, businessLine):
    return cleanCurMonStaff(data)[cleanCurMonStaff(data).业务线.str.contains(businessLine)]

def cleanstaff_apartment_tb():
    staff_apartment_tb = readData(本月业务线维度())
    return staff_apartment_tb.iloc[0:-1, :]

def cleanbusiness_line_tb():
    business_line_tb = readData(本月业务线维度())
    业务线汇总 = business_line_tb.iloc[0:-1, :]
    return 业务线汇总.replace('inf%', None)


def cleanstaff_apartment_table():
    staff_apartment_tb = readData(本月员工所属部门())
    return staff_apartment_tb.iloc[0:-1, :]

def cleanbusiness_line_table():
    business_line_tb = readData(本月员工所属部门())
    业务线汇总 = business_line_tb.iloc[0:-1, :]
    return 业务线汇总.replace('inf%', None)


def 业务线pie(type):
    业务线汇总 = cleanbusiness_line_table()
    业务线pie = 业务线汇总[["员工所属部门", "员工数", type]]
    return 业务线pie.groupby('员工所属部门').agg({'员工数': 'sum', type: 'sum'})


def 岗位pie(type):
    cur_mon_staff = cleanCurMonStaff(本月人员维度())
    return cur_mon_staff.groupby('资源池').agg({type: 'sum'})

def 业务线汇总(type):
    cur_mon_staff = cleanCurMonStaff(本月人员维度())
    业务线汇总 = cur_mon_staff[["业务线", "员工组", type]].rename(columns={type: "总工时"})
    业务线汇总['工时类别'] = 业务线汇总['业务线'].apply(lambda row: type[0:2])
    return 业务线汇总

def 对比业务线汇总(type1,type2):
    temp = 业务线汇总(type1).append(业务线汇总(type2)).reset_index(drop=True)
    return temp.groupby(["业务线", "员工组","工时类别"]).agg({"总工时":'sum'}).reset_index()


def 部门汇总(type):
    cur_mon_staff = cleanCurMonStaff(本月人员维度())
    部门汇总 = cur_mon_staff[["员工所属部门", "员工组", type]].rename(columns={type: "总工时"})
    部门汇总['工时类别'] = 部门汇总['员工所属部门'].apply(lambda row: type[0:2])
    return 部门汇总

def 对比部门汇总(type1,type2):
    temp = 部门汇总(type1).append(部门汇总(type2)).reset_index(drop=True)
    return temp.groupby(["员工所属部门", "员工组","工时类别"]).agg({"总工时":'sum'}).reset_index()

# 预估业务线汇总 = cur_mon_staff[["业务线", "员工组", "预估人天"]].rename(columns={"预估人天": "总工时"})
# 预估业务线汇总['工时类别'] = 预估业务线汇总['业务线'].apply(lambda row: '预估')

# cur_mon_staff['预估填报率'] = cur_mon_staff['预估填报率'].astype(int)
# cur_mon_staff['理论填报率'] = cur_mon_staff['理论填报率'].astype(int)

# last_mon_wbs = pd.read_csv(DATA_PATH.joinpath("11月WBS维度.csv"))
# cur_mon_wbs = pd.read_csv(DATA_PATH.joinpath("12月WBS维度.csv"))

def logic_rate_abnormal_tb():
    理论填报filterData = cleanCurMonStaff(本月人员维度())[['员工姓名', '员工组', '员工所属部门', '实际人天', '理论人天', '理论填报率', '理论填报', '岗位名称']]
    return 理论填报filterData[~理论填报filterData['理论填报'].str.contains('合理')]

def actual_wbs_tb(data):
    return data.loc[(data['实际人天'] > 0) & (data['WBS类型'] != 'Z')]

def wbs_type_number(data):
    wbs_type = ['P','R','D','M']
    data = actual_wbs_tb(data)
    testdict =  dict(data['WBS类型'].value_counts())
    diff = set(wbs_type).difference(set(list(testdict.keys())))
    if len(diff) == 1:
        testdict[list(diff)[0]] = 0
    else:
        for i in list(diff):
            testdict[i] = 0
    return testdict


def 本月wbs预估不满():
    本月WBS维度().loc[(本月WBS维度()['WBS类型'] != 'Z') & (本月WBS维度()['预估填报'] == '不满')]

def 本月wbs预估超载():
    本月WBS维度().loc[(本月WBS维度()['WBS类型'] != 'Z') & (本月WBS维度()['预估填报'] == '超载')]


def 新增wbs(new_wbs, last_wbs):
    new_wbs = new_wbs[new_wbs['实际人天'] > 0 ]
    new_wbs = new_wbs[~new_wbs['WBS类型'].isin(['Z'])].reset_index(drop=True)
    last_wbs = last_wbs[last_wbs['实际人天'] > 0]
    last_wbs = last_wbs[~last_wbs['WBS类型'].isin(['Z'])].reset_index(drop=True)
    return set(list(new_wbs['项目编号'])).difference(set(list(last_wbs['项目编号'])))

def 减少wbs(new_wbs, last_wbs):
    new_wbs = new_wbs[new_wbs['实际人天'] > 0 ]
    new_wbs = new_wbs[~new_wbs['WBS类型'].isin(['Z'])].reset_index(drop=True)
    last_wbs = last_wbs[last_wbs['实际人天'] > 0]
    last_wbs = last_wbs[~last_wbs['WBS类型'].isin(['Z'])].reset_index(drop=True)
    return set(list(last_wbs['项目编号'])).difference(set(list(new_wbs['项目编号'])))

def 新增wbs_tb(new_wbs, last_wbs, tableValue1, tableValue2):
    new_wbs = new_wbs[new_wbs['实际人天'] > 0 ]
    new_wbs = new_wbs[~new_wbs['WBS类型'].isin(['Z'])].reset_index(drop=True)
    last_wbs = last_wbs[last_wbs['实际人天'] > 0]
    last_wbs = last_wbs[~last_wbs['WBS类型'].isin(['Z'])].reset_index(drop=True)
    return new_wbs[new_wbs[tableValue1].isin(list(set(list(new_wbs[tableValue1])).difference(set(list(last_wbs[tableValue1])))))].reset_index(drop=True).sort_values(by=[tableValue2,tableValue1],ascending=False)

def 减少wbs_tb(new_wbs, last_wbs, tableValue1, tableValue2):
    new_wbs = new_wbs[new_wbs['实际人天'] > 0 ]
    new_wbs = new_wbs[~new_wbs['WBS类型'].isin(['Z'])].reset_index(drop=True)
    last_wbs = last_wbs[last_wbs['实际人天'] > 0]
    last_wbs = last_wbs[~last_wbs['WBS类型'].isin(['Z'])].reset_index(drop=True)
    return last_wbs[last_wbs[tableValue1].isin(list(set(list(last_wbs[tableValue1])).difference(set(list(new_wbs[tableValue1])))))].reset_index(drop=True).sort_values(by=[tableValue2,tableValue1],ascending=False)


def wbs部门pie(type):
    wbs = readData(本月WBS维度())[['WBS所属部门','实际人天','预估人天']]
    return wbs.groupby('WBS所属部门').agg({type: 'sum'})

def wbs类型pie(type):
    wbs = readData(本月WBS维度())[['WBS类型','实际人天','预估人天']]
    return wbs.groupby('WBS类型').agg({type: 'sum'})

# def wbs利润中心pie(type):
#     wbs = readData(本月WBS维度())[['利润中心','实际人天','预估人天']]
#     return wbs.groupby('利润中心').agg({type: 'sum'})

def wbs_top5_actual():
    data = readData(本月WBS维度()).sort_values(by='实际人天',ascending=False)
    data = data[~data['WBS类型'].isin(['Z'])].reset_index(drop=True).head(5)
    rate = 1
    for i in range(len(data)):
        data.loc[i, 'Rate'] = 'Top '+ str(int(rate))
        rate += 1
    data.insert(4, 'PM姓名', data.pop('PM姓名'))
    data.insert(0, 'Rate', data.pop('Rate'))
    return data

def wbs_top5_distribution():
    data = readData(本月WBS维度()).sort_values(by='实际人天',ascending=False)
    data = data[~data['WBS类型'].isin(['Z'])].reset_index(drop=True).head(5)
    rate = 1
    for i in range(len(data)):
        data.loc[i, 'Rate'] = 'Top '+ str(int(rate))
        rate += 1
    data.insert(4, 'PM姓名', data.pop('PM姓名'))
    data.insert(0, 'Rate', data.pop('Rate'))
    others_act_days = readData(本月WBS维度())['实际人天'].sum() - data['实际人天'].sum()
    other_row = {'项目名称':'Others','实际人天':others_act_days,'Rate':'Others'}
    data = data.append(other_row, ignore_index=True)
    return data


def logic_rate_abnormal_tb_WBS():
    理论填报filterData = readData(本月WBS维度())[['WBS所属部门', '项目编号', '项目名称', 'WBS类型',  'PM姓名', '实际人天', '预估人天','预估填报率','预估填报']]
    理论填报filterData = 理论填报filterData[~理论填报filterData['WBS类型'].isin(['Z'])]
    理论填报filterData = 理论填报filterData[理论填报filterData['实际人天'] > 0 ]
    return 理论填报filterData[~理论填报filterData['预估填报'].str.contains('合理')]

def less_1_yr_wbs(data):
    now = datetime.now().date() - timedelta(days=365)
    less_one_yr = []
    for i in range(len(data)):
        wbs_date = datetime(2000 + data.loc[i, 'WBS年份'], data.loc[i, 'WBS月份'], 1).date()
        if now > wbs_date:
            less_one_yr.append(i)
    return less_one_yr

def wbs_abg(df, value):
    data = df[df['实际人天'] > 0]
    data = data[~data['WBS类型'].isin(['Z'])]
    data = data[~data['WBS所属部门'].isin(['智慧娱乐', '中东云平台', '海外研发中心',"海外智能终端与应用","新零售业务",'创新业务部'])]
    temp = []
    for i, row in data.iterrows():
        if row['项目编号'][2:4] == value:
            temp.append(i)
    return data.loc[temp]

def get_wbs_list(df, reName):
    last = df[df['WBS类型'] !='Z'].rename(columns={'预估人天':reName})
    last = last[last['实际人天'] == 0]
    return list(last['项目编号'])

def find_common(list1, list2):
    common = []
    for i in list1:
        if i in (list2):
            common.append(i)
    return common

def est_twice_wbs():
    last = readData(上月WBS维度()).rename(columns={'预估人天':'上月预估'})
    cur = readData(本月WBS维度()).rename(columns={'预估人天': '本月预估'})
    cur_wbs_list = get_wbs_list(readData(本月WBS维度()), '本月预估')
    last_wbs_list = get_wbs_list(readData(上月WBS维度()), '上月预估')
    common = find_common(cur_wbs_list, last_wbs_list)
    last_common = last[last['项目编号'].isin(common)].reset_index(drop=True)
    cur_common = cur[cur['项目编号'].isin(common)].reset_index(drop=True)
    for i in range(len(last_common)):
        for j in range(len(cur_common)):
            if last_common.loc[i, '项目编号'] == cur_common.loc[j, '项目编号']:
                last_common.loc[i, '本月预估'] = cur_common.loc[j, '本月预估']
    return last_common

def not_fill_workHour_twice():
    cur = readData(本月未填工时名单())
    last = readData(上月未填工时名单())
    cur_no_list = list(cur['员工姓名'])
    last_no_list = list(last['员工姓名'])
    common = find_common(cur_no_list,last_no_list)
    last_common = last[last['员工姓名'].isin(common)].reset_index(drop=True)
    cur_common = cur[cur['员工姓名'].isin(common)].reset_index(drop=True)
    for i in range(len(last_common)):
        for j in range(len(cur_common)):
            if last_common.loc[i, '员工姓名'] == cur_common.loc[j, '员工姓名']:
                last_common.loc[i, '未填次数'] = '2'
            else:
                last_common.loc[i, '未填次数'] = '1'
    return last_common

def expires_morethan_a_year(date_str):
    """date_str format must be like this: 09/25/2022"""
    contract_end_date = datetime.strptime(date_str, "%m/%d/%Y")
    today = datetime.now()
    one_year = timedelta(days=365)
    one_year_within = today - one_year
    return contract_end_date < one_year_within

def get_more_than1yr_wbs():
    data = readData(本月WBS维度())[['项目编号','项目名称','WBS所属部门','WBS年份','WBS月份']]
    more_than1yr = []
    for i in range(len(data)):
        month = int(data.loc[i,'WBS月份'])
        if month == 0:
            month = 10
        year = data.loc[i,'WBS年份']
        if expires_morethan_a_year(str(month)+'/1/20'+str(int(year))) == True:
            more_than1yr.append(i)
    return data.loc[more_than1yr].drop_duplicates().reset_index(drop = True)[['项目编号','项目名称','WBS所属部门','WBS年份']]

def act_no_est_df():
    data = readData(本月WBS维度())
    data = data[data['预估人天'] == 0]
    data = data[~data['WBS类型'].isin(['Z'])]
    return data

def est_no_act_df():
    data = readData(本月WBS维度())
    data = data[data['实际人天'] == 0]
    data = data[~data['WBS类型'].isin(['Z'])]
    return data

def clean_gpu_usage():
    gpu_df = readData(历史GPU使用情况())
    gpu_df.columns = ['日期', '时间', '分区', '使用量']
    gpu_df = gpu_df[gpu_df['分区'] != 'Util%'].reset_index(drop=True)
    gpu_df['分区'] = gpu_df['分区'].str.replace('IRDCSG', 'SG2/IRDCSG')
    gpu_df['分区'] = gpu_df['分区'].str.replace('vi_irdc', 'ABUD/vi_irdc')
    gpu_df['分区'] = gpu_df['分区'].str.replace('IRDC_Share', 'SH40/IRDC_Share')
    for i in range(len(gpu_df)):
        gpu_df.loc[i, 'year'] = gpu_df.loc[i, '日期'].split('/')[0]
        gpu_df.loc[i, 'month'] = gpu_df.loc[i, '日期'].split('/')[1]
    for i in range(len(gpu_df)):
        gpu_df.loc[i, 'Time'] = gpu_df.loc[i, '时间'][0:2]
        gpu_df.loc[i, 'Used'] = gpu_df.loc[i, '使用量'].split("/")[0]
        gpu_df.loc[i, 'All'] = gpu_df.loc[i, '使用量'].split("/")[1]

    # caculate usage percentage
    for i in range(len(gpu_df)):
        gpu_df.loc[i, '使用率'] = round(int(gpu_df.loc[i, 'Used']) / int(gpu_df.loc[i, 'All']) * 100, 2)

    gpu_df[["year", "month", 'Time', 'Used', 'All']] = gpu_df[["year", "month", 'Time', 'Used', 'All']].apply(pd.to_numeric)
    return gpu_df[gpu_df['Time'].isin([10, 14, 18, 22])].reset_index(drop=True)

def clean_gpu_avg_usage():
    gpu_df_per_day = clean_gpu_usage().groupby(['日期', '分区']).agg({'Used': 'sum', 'All': 'sum'}).reset_index()
    for i in range(len(gpu_df_per_day)):
        gpu_df_per_day.loc[i, '使用率'] = round(
            int(gpu_df_per_day.loc[i, 'Used']) / int(gpu_df_per_day.loc[i, 'All']) * 100, 2)
    return gpu_df_per_day

def gpu_monthly_df(year, month):
    return clean_gpu_usage().loc[(clean_gpu_usage()['year'] == year) & (clean_gpu_usage()['month'] == month)].reset_index(drop =True)

def gpu_monthly_usage(year, month, cardName):
    gpu_monthly_per_card = gpu_monthly_df(year, month).groupby(['分区']).agg({'Used': 'sum', 'All': 'sum'}).reset_index()
    for i in range(len(gpu_monthly_per_card)):
        gpu_monthly_per_card.loc[i, '使用率'] = round(
            int(gpu_monthly_per_card.loc[i, 'Used']) / int(gpu_monthly_per_card.loc[i, 'All']) * 100, 2)
    return gpu_monthly_per_card[gpu_monthly_per_card['分区'] == cardName].reset_index(drop=True)['使用率'][0]

def gpu_monthly_usage_time(year, month, cardName, time):
    gpu_monthly_per_card = gpu_monthly_df(year, month).groupby(['分区','Time']).agg({'Used': 'sum', 'All': 'sum'}).reset_index()
    for i in range(len(gpu_monthly_per_card)):
        gpu_monthly_per_card.loc[i, '使用率'] = round(
            int(gpu_monthly_per_card.loc[i, 'Used']) / int(gpu_monthly_per_card.loc[i, 'All']) * 100, 2)
    return gpu_monthly_per_card.loc[(gpu_monthly_per_card['分区'] == cardName) & (gpu_monthly_per_card['Time'] == time)].reset_index(drop=True)['使用率'][0]