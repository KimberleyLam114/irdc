'''
 # @ Create Time: 2022-11-05 16:58:58.526050
 # @ Create by：Zhidian Lin
'''

import pathlib
from dash import Dash
import dash_auth
from datetime import datetime
from dash import Dash, dcc, html, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from buildChart import *
from dataSource import *
import flask
from dash.exceptions import PreventUpdate


indicator_Z_type_num_last = len(readData(上月WBS维度())[readData(上月WBS维度())['WBS类型'].isin(['Z'])])
indicator_Z_type_num_cur = len(readData(本月WBS维度())[readData(本月WBS维度())['WBS类型'].isin(['Z'])])
indicator_Z_type_act_last = readData(上月WBS维度())[readData(上月WBS维度())['WBS类型'].isin(['Z'])]['实际人天'].sum()
indicator_Z_type_act_cur = readData(本月WBS维度())[readData(本月WBS维度())['WBS类型'].isin(['Z'])]['实际人天'].sum()
others_numebr = indicator_wbs_number2(indicator_Z_type_num_cur, indicator_Z_type_num_last,'Others')
z_act= indicator_wbs_number2(indicator_Z_type_act_cur, indicator_Z_type_act_last,'休假/非项目')

indicator_scg_num_last = len(actual_wbs_tb(readData(本月WBS维度()))[actual_wbs_tb(readData(本月WBS维度()))['WBS所属部门'].isin(['新零售业务','创新业务部'])])
indicator_scg_num_cur = len(actual_wbs_tb(readData(本月WBS维度()))[actual_wbs_tb(readData(本月WBS维度()))['WBS所属部门'].isin(['新零售业务','创新业务部'])])
indicator_scg_act_last = actual_wbs_tb(readData(本月WBS维度()))[actual_wbs_tb(readData(本月WBS维度()))['WBS所属部门'].isin(['新零售业务','创新业务部'])]['实际人天'].sum()
indicator_scg_act_cur = actual_wbs_tb(readData(本月WBS维度()))[actual_wbs_tb(readData(本月WBS维度()))['WBS所属部门'].isin(['新零售业务','创新业务部'])]['实际人天'].sum()
scg_number = indicator_wbs_number2(indicator_scg_num_cur, indicator_scg_num_last,'SCG')
scg_act = indicator_wbs_number2(indicator_scg_act_cur, indicator_scg_act_last,'SCG')

indicator_sxibg_num_last = len(actual_wbs_tb(readData(本月WBS维度()))[actual_wbs_tb(readData(本月WBS维度()))['WBS所属部门'].isin(['中东云平台'])])
indicator_sxibg_num_cur = len(actual_wbs_tb(readData(本月WBS维度()))[actual_wbs_tb(readData(本月WBS维度()))['WBS所属部门'].isin(['中东云平台'])])
indicator_ssxibg_act_last = actual_wbs_tb(readData(本月WBS维度()))[actual_wbs_tb(readData(本月WBS维度()))['WBS所属部门'].isin(['中东云平台'])]['实际人天'].sum()
indicator_sxibg_act_cur = actual_wbs_tb(readData(本月WBS维度()))[actual_wbs_tb(readData(本月WBS维度()))['WBS所属部门'].isin(['中东云平台'])]['实际人天'].sum()
sx_number = indicator_wbs_number2(indicator_sxibg_num_cur, indicator_sxibg_num_last,'SX')
sx_act = indicator_wbs_number2(indicator_sxibg_act_cur, indicator_ssxibg_act_last,'SX')

indicator_ir_num_last = len(actual_wbs_tb(readData(本月WBS维度()))[actual_wbs_tb(readData(本月WBS维度()))['WBS所属部门'].isin(['智慧娱乐'])])
indicator_ir_num_cur = len(actual_wbs_tb(readData(本月WBS维度()))[actual_wbs_tb(readData(本月WBS维度()))['WBS所属部门'].isin(['智慧娱乐'])])
indicator_ir_act_last = actual_wbs_tb(readData(本月WBS维度()))[actual_wbs_tb(readData(本月WBS维度()))['WBS所属部门'].isin(['智慧娱乐'])]['实际人天'].sum()
indicator_ir_act_cur = actual_wbs_tb(readData(本月WBS维度()))[actual_wbs_tb(readData(本月WBS维度()))['WBS所属部门'].isin(['智慧娱乐'])]['实际人天'].sum()
ir_number = indicator_wbs_number2(indicator_ir_num_cur, indicator_ir_num_last,'IR')
ir_act = indicator_wbs_number2(indicator_ir_act_cur, indicator_ir_act_last,'IR')

indicator_aiot_num_last = len(actual_wbs_tb(readData(本月WBS维度()))[actual_wbs_tb(readData(本月WBS维度()))['WBS所属部门'].isin(['海外智能终端与应用'])])
indicator_aiot_num_cur = len(actual_wbs_tb(readData(本月WBS维度()))[actual_wbs_tb(readData(本月WBS维度()))['WBS所属部门'].isin(['海外智能终端与应用'])])
indicator_aiot_act_last = actual_wbs_tb(readData(本月WBS维度()))[actual_wbs_tb(readData(本月WBS维度()))['WBS所属部门'].isin(['海外智能终端与应用'])]['实际人天'].sum()
indicator_aiot_act_cur = actual_wbs_tb(readData(本月WBS维度()))[actual_wbs_tb(readData(本月WBS维度()))['WBS所属部门'].isin(['海外智能终端与应用'])]['实际人天'].sum()
aiot_number = indicator_wbs_number2(indicator_aiot_num_cur, indicator_aiot_num_last,'AIoT')
aiot_act = indicator_wbs_number2(indicator_aiot_act_cur, indicator_aiot_act_last,'AIoT')

indicator_irdc_num_last = len(actual_wbs_tb(readData(本月WBS维度()))[actual_wbs_tb(readData(本月WBS维度()))['WBS所属部门'].isin(['创新与赋能中心'])])
indicator_irdc_num_cur = len(actual_wbs_tb(readData(本月WBS维度()))[actual_wbs_tb(readData(本月WBS维度()))['WBS所属部门'].isin(['创新与赋能中心'])])
indicator_irdc_act_last = actual_wbs_tb(readData(本月WBS维度()))[actual_wbs_tb(readData(本月WBS维度()))['WBS所属部门'].isin(['创新与赋能中心'])]['实际人天'].sum()
indicator_irdc_act_cur = actual_wbs_tb(readData(本月WBS维度()))[actual_wbs_tb(readData(本月WBS维度()))['WBS所属部门'].isin(['创新与赋能中心'])]['实际人天'].sum()
chuangfu_number = indicator_wbs_number2(indicator_irdc_num_cur, indicator_irdc_num_last,'创新赋能')
chuangfu_act = indicator_wbs_number2(indicator_irdc_act_cur, indicator_irdc_act_last,'创新赋能')

wbs_chuangfu_percentage = indicator_wbs_percentage(actual_wbs_tb(readData(本月WBS维度())),actual_wbs_tb(readData(上月WBS维度())), '创新与赋能中心','WBS所属部门','预估人天','实际人天','创新赋能填报率')
wbs_sx_percentage = indicator_wbs_percentage(actual_wbs_tb(readData(本月WBS维度())),actual_wbs_tb(readData(上月WBS维度())), '中东云平台','WBS所属部门','预估人天','实际人天','SX填报率')
wbs_ir_percentage = indicator_wbs_percentage(actual_wbs_tb(readData(本月WBS维度())),actual_wbs_tb(readData(上月WBS维度())), '智慧娱乐','WBS所属部门','预估人天','实际人天','IR填报率')
wbs_aiot_percentage = indicator_wbs_percentage(actual_wbs_tb(readData(本月WBS维度())),actual_wbs_tb(readData(上月WBS维度())), '海外智能终端与应用','WBS所属部门','预估人天','实际人天','AIoT填报率')

indicator_abg_num_last = len(wbs_abg(actual_wbs_tb(readData(上月WBS维度())), 'AB'))
indicator_abg_num_cur = len(wbs_abg(actual_wbs_tb(readData(本月WBS维度())), 'AB'))
indicator_abg_act_last = wbs_abg(actual_wbs_tb(readData(上月WBS维度())), 'AB')['实际人天'].sum()
indicator_abg_act_cur = wbs_abg(actual_wbs_tb(readData(本月WBS维度())), 'AB')['实际人天'].sum()
abg_number = indicator_wbs_number2(indicator_abg_num_cur, indicator_abg_num_last,'ABG')
abg_act = indicator_wbs_number2(indicator_abg_act_cur, indicator_abg_act_last,'ABG')

indicator_ibg_num_last = len(wbs_abg(actual_wbs_tb(readData(上月WBS维度())), 'IB'))
indicator_ibg_num_cur = len(wbs_abg(actual_wbs_tb(readData(本月WBS维度())), 'IB'))
indicator_ibg_act_last = wbs_abg(actual_wbs_tb(readData(上月WBS维度())), 'IB')['实际人天'].sum()
indicator_ibg_act_cur = wbs_abg(actual_wbs_tb(readData(本月WBS维度())), 'IB')['实际人天'].sum()
ibg_number = indicator_wbs_number2(indicator_ibg_num_cur, indicator_ibg_num_last,'IBG')
ibg_act = indicator_wbs_number2(indicator_ibg_act_cur, indicator_ibg_act_last,'IBG')



external_stylesheets = ['https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sandstone/bootstrap.min.css']
layout = dict(
    autosize=True,
    automargin=True,
    margin=dict(l=3, r=3, b=5, t=2),
    hovermode="closest",
    plot_bgcolor="#F9F9F9",
    paper_bgcolor="#F9F9F9",
    legend=dict(font=dict(size=10), orientation="h"),
)
server = flask.Flask(__name__)
app = Dash(__name__, title="IRDC-Dashboard | 工时&资源看板", external_stylesheets=[dbc.themes.SANDSTONE], update_title='刷新中，请稍等...', server=server,
           meta_tags=[{'name': 'viewport',
                       'content': 'width=device-width, initial-scale=1.0'}])

# server = app.server

html.Img(src=app.get_asset_url('img/IRDC_removed_bg.png'), style={'width': '100%'})
VALID_USERNAME_PASSWORD_PAIRS = {
    'IRDC': 'IRDC666'
}
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

app.config.suppress_callback_exceptions = True





tabs_styles = {
    'height': '65px',
    'backgroundColor': '#F9F9F9',
    # 'borderBottom': '1px solid #d6d6d6',
    'borderLeft': 'None',
    'borderTop':'None',
    'borderRight':'None'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '10px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': 'None',
    'borderRight': 'None',
    'borderLeft': 'None',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#d6d6d6',
    'color': 'black',
    'padding': '10px'
}

# indicator summary for irdc
cur_in_staff_number = len(filterCurMonStaff(本月人员维度(), "员工组", "正式员工"))
last_in_staff_number = len(filterCurMonStaff(上月人员维度(), "员工组", "正式员工"))
cur_out_staff_number = len(filterCurMonStaff(本月人员维度(), "员工组", "外包员工"))
last_out_staff_number = len(filterCurMonStaff(上月人员维度(), "员工组", "外包员工"))
cur_intern_staff_number = len(filterCurMonStaff(本月人员维度(), "员工组", "实习生"))
last_intern_staff_number = len(filterCurMonStaff(上月人员维度(), "员工组", "实习生"))
last_in_actual_day = filterCurMonStaff(上月人员维度(), "员工组", "正式员工")['实际人天'].sum()
cur_in_actual_day = filterCurMonStaff(本月人员维度(), "员工组", "正式员工")['实际人天'].sum()
last_out_actual_day = filterCurMonStaff(上月人员维度(), "员工组", "外包员工")['实际人天'].sum()
cur_out_actual_day = filterCurMonStaff(本月人员维度(), "员工组", "外包员工")['实际人天'].sum()
last_intern_actual_day = filterCurMonStaff(上月人员维度(), "员工组", "实习生")['实际人天'].sum()
cur_intern_actual_day = filterCurMonStaff(本月人员维度(), "员工组", "实习生")['实际人天'].sum()

last_in_lo_day = filterCurMonStaff(上月人员维度(), "员工组", "正式员工")['理论人天'].sum()
cur_in_lo_day = filterCurMonStaff(本月人员维度(), "员工组", "正式员工")['理论人天'].sum()
last_out_lo_day = filterCurMonStaff(上月人员维度(), "员工组", "外包员工")['理论人天'].sum()
cur_out_lo_day = filterCurMonStaff(本月人员维度(), "员工组", "外包员工")['理论人天'].sum()
last_intern_lo_day = filterCurMonStaff(上月人员维度(), "员工组", "实习生")['理论人天'].sum()
cur_intern_lo_day = filterCurMonStaff(本月人员维度(), "员工组", "实习生")['理论人天'].sum()

staff_number_indicator = indicator_large_ppl(cur_mon_staff, last_mon_staff, "员工姓名", "员工数")
staff_in_indicator = indicator_ppl(cur_in_staff_number, last_in_staff_number, "正式")
staff_out_indicator = indicator_ppl(cur_out_staff_number, last_out_staff_number, "外包")
staff_intern_indicator = indicator_ppl(cur_intern_staff_number, last_intern_staff_number, "实习")


# actual all day
act_allday = indicator_irdc_sum(cur_mon_staff, last_mon_staff, "实际人天","实际人天")
act_in_day = indicator_ppl(cur_in_actual_day, last_in_actual_day, "正式")
act_out_day = indicator_ppl(cur_out_actual_day, last_out_actual_day, "外包")
act_intern_day = indicator_ppl(cur_intern_actual_day, cur_intern_actual_day, "实习")

# attendance
attend_allday = indicator_irdc_sum(cur_mon_staff, last_mon_staff, "实际人天","考勤人天")
attend_in_day = indicator_ppl(cur_in_actual_day, last_in_actual_day, "正式")
attend_out_day = indicator_ppl(cur_out_actual_day, last_out_actual_day, "外包")
attend_intern_day = indicator_ppl(cur_intern_actual_day, cur_intern_actual_day, "实习")

# actural per day
act_perday = indicator_irdc_per(cur_mon_staff, last_mon_staff, "实际人天", "员工姓名","实际人均")
act_in_perday = indicator_irdc_type_per(cur_in_actual_day, cur_in_staff_number, last_in_actual_day, last_in_staff_number, "正式")
act_out_perday = indicator_irdc_type_per(cur_out_actual_day, cur_out_staff_number, last_out_actual_day, last_out_staff_number, "外包")
act_intern_perday = indicator_irdc_type_per(cur_intern_actual_day, cur_intern_staff_number, last_intern_actual_day, last_intern_staff_number, "实习")

# est all day
est_allday = indicator_irdc_sum(cur_mon_staff, last_mon_staff, "预估人天","预估人天")
est_percentage = indicator_irdc_rate(cur_mon_staff, last_mon_staff, "实际人天", "预估人天", "预估填报率")

# logic all day
logic_allday = indicator_irdc_sum(cur_mon_staff, last_mon_staff, "理论人天","理论人天")
logic_percentage = indicator_irdc_rate(cur_mon_staff, last_mon_staff, "实际人天", "理论人天", "填报率")


#wbs
wbs_all_number = indicator_wbs_sum(actual_wbs_tb(readData(本月WBS维度())), actual_wbs_tb(readData(上月WBS维度())), '项目编号', "WBS个数")
wbs_p_numebr = indicator_wbs_number(wbs_type_number(readData(本月WBS维度())), wbs_type_number(readData(上月WBS维度())),'P','P个数')
wbs_m_numebr = indicator_wbs_number(wbs_type_number(readData(本月WBS维度())), wbs_type_number(readData(上月WBS维度())),'M','M个数')
wbs_r_numebr = indicator_wbs_number(wbs_type_number(readData(本月WBS维度())), wbs_type_number(readData(上月WBS维度())),'R','R个数')
wbs_d_numebr = indicator_wbs_number(wbs_type_number(readData(本月WBS维度())), wbs_type_number(readData(上月WBS维度())),'D','D个数')

wbs_more_numebr = indicator_wbs_number2(len(readData(本月WBS维度())), len(readData(上月WBS维度())),'增加')
wbs_less_numebr = indicator_wbs_number2(len(readData(上月WBS维度())), len(readData(本月WBS维度())),'减少')


wbs_actual_hrs = indicator_wbs_act(actual_wbs_tb(readData(本月WBS维度())), actual_wbs_tb(readData(上月WBS维度())), '实际人天','实际人天')
wbs_p_act_percentage = indicator_wbs_type(actual_wbs_tb(readData(本月WBS维度())), actual_wbs_tb(readData(上月WBS维度())), 'P','WBS类型','实际人天','P占比')
wbs_m_act_percentage = indicator_wbs_type(actual_wbs_tb(readData(本月WBS维度())), actual_wbs_tb(readData(上月WBS维度())), 'M','WBS类型','实际人天','M占比')
wbs_r_act_percentage = indicator_wbs_type(actual_wbs_tb(readData(本月WBS维度())), actual_wbs_tb(readData(上月WBS维度())), 'R','WBS类型','实际人天','R占比')
wbs_d_act_percentage = indicator_wbs_type(actual_wbs_tb(readData(本月WBS维度())), actual_wbs_tb(readData(上月WBS维度())), 'D','WBS类型','实际人天','D占比')

wbs_p_act = indicator_wbs_type_sum(actual_wbs_tb(readData(本月WBS维度())), actual_wbs_tb(readData(上月WBS维度())), 'P','WBS类型','实际人天','P人天')
wbs_m_act = indicator_wbs_type_sum(actual_wbs_tb(readData(本月WBS维度())), actual_wbs_tb(readData(上月WBS维度())), 'M','WBS类型','实际人天','M人天')
wbs_r_act = indicator_wbs_type_sum(actual_wbs_tb(readData(本月WBS维度())), actual_wbs_tb(readData(上月WBS维度())), 'R','WBS类型','实际人天','R人天')
wbs_d_act = indicator_wbs_type_sum(actual_wbs_tb(readData(本月WBS维度())), actual_wbs_tb(readData(上月WBS维度())), 'D','WBS类型','实际人天','D人天')

logic_in_percentage = indicator_logic_percentage(cur_in_actual_day, cur_in_lo_day,last_in_actual_day, last_in_lo_day,"正式")
logic_out_percentage = indicator_logic_percentage(cur_out_actual_day, cur_out_lo_day,last_out_actual_day, last_out_lo_day,"外包")
logic_intern_percentage = indicator_logic_percentage(cur_intern_actual_day, cur_intern_lo_day,last_intern_actual_day, last_intern_lo_day,"实习")

# gpu usage
gpu_abud_avg_usage = indicator_gpu_percentage_large(gpu_monthly_usage(本年(), 本月(), 'ABUD/vi_irdc'),gpu_monthly_usage(上年(), 上月(), 'ABUD/vi_irdc'),'ABUD平均使用率')
gpu_abud_10_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'ABUD/vi_irdc',10), gpu_monthly_usage_time(上年(), 上月(), 'ABUD/vi_irdc',10),'10点')
gpu_abud_14_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'ABUD/vi_irdc',14), gpu_monthly_usage_time(上年(), 上月(), 'ABUD/vi_irdc',14),'14点')
gpu_abud_18_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'ABUD/vi_irdc',18), gpu_monthly_usage_time(上年(), 上月(), 'ABUD/vi_irdc',18),'18点')
gpu_abud_22_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'ABUD/vi_irdc',22), gpu_monthly_usage_time(上年(), 上月(), 'ABUD/vi_irdc',22),'22点')

gpu_sg2_avg_usage = indicator_gpu_percentage_large(gpu_monthly_usage(本年(), 本月(), 'SG2/IRDCSG'),gpu_monthly_usage(上年(), 上月(), 'SG2/IRDCSG'),'SG2平均使用率')
gpu_sg2_10_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SG2/IRDCSG',10), gpu_monthly_usage_time(上年(), 上月(), 'SG2/IRDCSG',10),'10点')
gpu_sg2_14_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SG2/IRDCSG',14), gpu_monthly_usage_time(上年(), 上月(), 'SG2/IRDCSG',14),'14点')
gpu_sg2_18_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SG2/IRDCSG',18), gpu_monthly_usage_time(上年(), 上月(), 'SG2/IRDCSG',18),'18点')
gpu_sg2_22_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SG2/IRDCSG',22), gpu_monthly_usage_time(上年(), 上月(), 'SG2/IRDCSG',22),'22点')

gpu_sh40_avg_usage = indicator_gpu_percentage_large(gpu_monthly_usage(本年(), 本月(), 'SH40/IRDC_Share'),gpu_monthly_usage(上年(), 上月(), 'SH40/IRDC_Share'),'SH40平均使用率')
gpu_sh40_10_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SH40/IRDC_Share',10), gpu_monthly_usage_time(上年(), 上月(), 'SH40/IRDC_Share',10),'10点')
gpu_sh40_14_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SH40/IRDC_Share',14), gpu_monthly_usage_time(上年(), 上月(), 'SH40/IRDC_Share',14),'14点')
gpu_sh40_18_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SH40/IRDC_Share',18), gpu_monthly_usage_time(上年(), 上月(), 'SH40/IRDC_Share',18),'18点')
gpu_sh40_22_usage = indicator_gpu_percentage_small(gpu_monthly_usage_time(本年(), 本月(), 'SH40/IRDC_Share',22), gpu_monthly_usage_time(上年(), 上月(), 'SH40/IRDC_Share',22),'22点')


modal = html.Div(
    [
        dbc.Button("Open modal", id="open", n_clicks=0),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Header")),
                dbc.ModalBody("This is the content of the modal"),
                dbc.ModalFooter(
                    dbc.Button(
                        "Close", id="close", className="ms-auto", n_clicks=0,
                    )
                ),
            ],
            id="modal",
            is_open=False,
        ),
    ]
)


app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            dbc.Row([
                html.Img(src=app.get_asset_url("img/dash-logo.png"), id="plotly-image",
                         style={"height": "60px", "width": "auto"}),
            ]),
        ),
        dbc.Col([
            dbc.Row([
                    dbc.Col([html.P(更新时间() + ' updated')]),
            ]),
            dbc.Row([html.Div([
                dbc.Button("数据说明", id="open", n_clicks=0, color="transparent", ),
                dbc.Modal([
                    dbc.ModalBody(
                        html.Div(
                            className="markdown-text",
                            children=dcc.Markdown(
                                children=(
                                    """
                            ###### 【 ⏰ 工时数据说明】 
                            ###### 1、数据来源
                            上月26日-本月25日内OA工时填报已报送工时，中国内地全勤 `  17` 人天，新加坡全勤 `  19` 人天 ;
                            ###### 2、人员构成
                            部门正式员工、人力外包、实习生（不含外部门人员、项目外包成员、当月入离职员工）;
                            ###### 3、数据定义
                            理论工时，部门填写工时人数*当月工作日天数；
                            实际工时，OA工时填报中的已报送工时；
                            预计工时，PM对项目当月做出的[工时预估](https://docs.qq.com/sheet/DVkVZRUNseGJ4Q0tl?tab=7bdo9o)。
                            合理预估填报率：80% < 实际人天/预估人天 < 120%；
                            合理理论填报率：90% < 实际人天/理论人天 < 120%。
                            ###### 
                            ###### 【 💎 资源数据说明】 
                            ###### 1、GPU
                            数据来源于各集群每日10点、14点、18点与22点GPU卡使用情况，可关注企微群 ` IRDC内部GPU资源调度群`  每日推送；
                            ###### 2、数据采标
                            数据爬取自Sensebee各采集标注任务，可关注企微群 ` IRDC数据采标任务群`  每日推送；
                            ###### 3、Open Cloud、DCP存储
                            ###### 4、固定资产
        
                        """
                                )), ), ),
                    dbc.ModalFooter(
                        dbc.Button(
                            "Close", id="close", className="ms-auto", n_clicks=0
                        )
                    ),
                ],
                    id="modal",
                    size="lg",
                    is_open=False,
                ),
            ])]),
        ]),
        dbc.Col([
            dcc.Tabs(id="tabs-title", value='工时', children=[
                dcc.Tab(label='工时', value='工时', style=tab_style, selected_style=tab_selected_style),
                dcc.Tab(label='资源', value='资源', style=tab_style, selected_style=tab_selected_style),
                dcc.Tab(label='业务线', value='业务线', style=tab_style, selected_style=tab_selected_style),
                # dcc.Dropdown(id="业务线详细", options=['SX', 'IR', 'AIOT'], placeholder='业务线详细'),
            ]),
            # dcc.Dropdown(id="业务线详细", options=['SX', 'IR', 'AIOT', 'DX', 'SI'], placeholder='业务线详细',
            #              clearable=False),
        ], width=9)
    ]),
    dbc.Row([
        dbc.Col([
            html.Div(id='tabs-content')
        ])
    ])
], fluid=True)

@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output('pandas-output-container-1', 'value'),
    Input('业务线详细', 'value')
)
def select_bl(value):
    return value


@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
@app.callback(
    Output("collapse2", "is_open"),
    [Input("collapse-button2", "n_clicks")],
    [State("collapse2", "is_open")],
)
@app.callback(
    Output("collapse3", "is_open"),
    [Input("collapse-button3", "n_clicks")],
    [State("collapse3", "is_open")],
)
@app.callback(
    Output("collapse4", "is_open"),
    [Input("collapse-button4", "n_clicks")],
    [State("collapse4", "is_open")],
)
@app.callback(
    Output("collapse6", "is_open"),
    [Input("collapse-button6", "n_clicks")],
    [State("collapse6", "is_open")],
)
@app.callback(
    Output("collapse7", "is_open"),
    [Input("collapse-button7", "n_clicks")],
    [State("collapse7", "is_open")],
)
@app.callback(
    Output("collapse8", "is_open"),
    [Input("collapse-button8", "n_clicks")],
    [State("collapse8", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("fig全量实际vs理论人天-scatter", "figure"),
    Input("range-slider实际vs理论", "value"))
def update_bar_chart(slider_range):
    low, high = slider_range
    mask = (cur_mon_staff.理论填报率 > low) & (cur_mon_staff.理论填报率 < high)
    fig = px.scatter(cur_mon_staff[mask],
        title='员工"实际人天"v."理论人天"by业务线',
        x="实际人天", y="理论人天",
        color="业务线", size='实际人天', hover_data=['员工姓名'])
    return fig


@app.callback(Output('tabs-content', 'children'),
              Input('tabs-title', 'value'))
def render_content(tab):
    if tab == '工时':
        return dbc.Container([
            html.P("人员维度Summary"),
            dbc.Row([
                dbc.Col([
                    irdc_summary_large_ppl("staff_number_indicator", staff_number_indicator)
                ]),
                dbc.Col([
                    dbc.Row([
                        irdc_summary_smWider_ppl("staff_in_indicator", staff_in_indicator),
                        irdc_summary_smWider_ppl("staff_out_indicator", staff_out_indicator),
                        irdc_summary_smWider_ppl("staff_intern_indicator", staff_intern_indicator),
                    ])]),

                dbc.Col([
                    irdc_summary_large_ppl("logic_percentage", logic_percentage)
                ]),
                dbc.Col([
                    dbc.Row([
                        irdc_summary_smWider_ppl("logic_in_percentage", logic_in_percentage),
                        irdc_summary_smWider_ppl("logic_out_percentage", logic_out_percentage),
                        irdc_summary_smWider_ppl("logic_intern_percentage", logic_intern_percentage),
                    ])]),

                dbc.Col([
                    irdc_summary_large_ppl("act_allday", act_allday)
                ]),
                dbc.Col([
                    dbc.Row([
                        irdc_summary_smWider_ppl("act_in_day", act_in_day),
                        irdc_summary_smWider_ppl("act_out_day", act_out_day),
                        irdc_summary_smWider_ppl("act_intern_day", act_intern_day),
                    ])]),

                dbc.Col([
                    irdc_summary_large_ppl("act_perday", act_perday)
                ]),
                dbc.Col([
                    dbc.Row([
                        irdc_summary_smWider_ppl("act_in_perday", act_in_perday),
                        irdc_summary_smWider_ppl("act_out_perday", act_out_perday),
                        irdc_summary_smWider_ppl("act_intern_perday", act_intern_perday),
                ])]),
                dbc.Col([
                    irdc_summary_large_ppl("attend_allday", attend_allday)
                ]),
                dbc.Col([
                    dbc.Row([
                        irdc_summary_smWider_ppl("attend_in_day", attend_in_day),
                        irdc_summary_smWider_ppl("attend_out_day", attend_out_day),
                        irdc_summary_smWider_ppl("attend_intern_day", attend_intern_day),
                    ])]),
            ]),
            html.Br(),
            html.Div(
            dbc.Accordion(
                [
                    dbc.AccordionItem([

                        dbc.Row([
                            dbc.Col([
                                irdc_graph('员工所属部门汇总-summary', fig员工所属部门汇总())
                            ], xs=12, sm=12, md=6, lg=6, xl=6),
                            dbc.Col([
                                irdc_graph('员工所属部门汇总-bar', fig员工所属部门人均人天())
                            ], xs=12, sm=12, md=6, lg=6, xl=6),
                            dbc.Col([
                                html.Div([
                                    html.Div([
                                        dcc.RadioItems(
                                            id='radio_actual_per',
                                            options=[
                                                {'label': 'IRDC', 'value': 'graph_actual_per_irdc'},
                                                {'label': '业务线', 'value': 'graph_actual_per_all'},
                                            ],
                                            value='graph_actual_per_irdc',
                                            style={"width": "60%"},
                                            inline=True),
                                    ]),
                                    html.Div(
                                        dcc.Graph(id='graph_actual_per',
                                                  style={'height': 500,
                                                         "border-radius": "5px",
                                                         "background-color": "#f9f9f9",
                                                         "box-shadow": "2px 2px 2px lightgrey",
                                                         "position": "relative",
                                                         "margin-bottom": "15px"
                                                         },
                                                  config = {'displayModeBar': False},
                                                  ),
                                    ),

                                ])

                            ]),
                            # dbc.Col([
                            #     irdc_graph('历史部门实际人均人天-line2', fig历史实际人均人天())
                            # ]),
                            dbc.Col([
                                html.Div([
                                    html.Div([
                                        dcc.RadioItems(
                                            id='radio_logic_rate',
                                            options=[
                                                {'label': 'IRDC', 'value': 'graph_logic_rate_irdc'},
                                                {'label': '业务线', 'value': 'graph_logic_rate_all'},
                                            ],
                                            value='graph_logic_rate_irdc',
                                            style={"width": "60%"},
                                            inline=True),
                                    ]),
                                    html.Div(
                                        dcc.Graph(id='graph_logic_rate',
                                                  style={'height': 500,
                                                         "border-radius": "5px",
                                                         "background-color": "#f9f9f9",
                                                         "box-shadow": "2px 2px 2px lightgrey",
                                                         "position": "relative",
                                                         "margin-bottom": "15px"
                                                         },
                                                  config={'displayModeBar': False},
                                                  ),
                                    ),

                                ])

                            ]),
                            # dbc.Col([
                            #     irdc_graph('历史部门理论填报率-line', fig历史理论填报率())
                            # ]),
                        ]),
                        dbc.Row([
                            collapse_btn_table("collapse-button", "staff_apartment_tb", staff_apartment_tb,'collapse'),
                            html.Br(),
                        ]),
                        html.Br(),
                        dbc.Row([
                            irdc_graph('业务线汇总-pie', fig业务线pie()),
                        ]),
                        html.Br(),
                        dbc.Row([
                            irdc_graph('员工组汇总-bar', fig员工部门员工组()),
                        ]),
                        dbc.Row([
                            collapse_btn_table("collapse-button4", "business_line_staff_type_detailed", business_line_staff_type,'collapse4'),
                            html.Br(),
                        ]),
                        html.Br(),
                        dbc.Row([
                            irdc_graph('岗位汇总-pie', fig岗位pie()),
                        ]),
                        dbc.Row([
                            dbc.Col([
                                irdc_graph('理论填报分布-pie', fig理论填报分布())
                            ], xs=12, sm=12, md=6, lg=6, xl=6),
                            dbc.Col([
                                dbc.Row([
                                    html.P('本月工时填报异常人数：' + str(
                                        len(logic_rate_abnormal_tb())),
                                           style={"fontSize": 25}),
                                ]),
                                dash_table_not_collapse("logic_distribution_tb_id", logic_rate_abnormal_tb()),

                            ], xs=12, sm=12, md=6, lg=6, xl=6),

                        ]),
                        dbc.Row([
                            dbc.Col([
                                irdc_graph('未填工时分布-pie', fig未填工时分布())
                            ], xs=12, sm=12, md=6, lg=6, xl=6),
                            dbc.Col([
                                dbc.Row([
                                    html.P('本月未填工时人数：' + str(
                                        len(readData(本月未填工时名单()))) +'  (连续两月未填已标红)',
                                           style={"fontSize": 25}),
                                ]),
                                dash_table_not_collapse("no_actual_list_tb_id", not_fill_workHour_twice()),

                            ], xs=12, sm=12, md=6, lg=6, xl=6),

                        ]),
                        dbc.Row([
                            collapse_btn_table("collapse-button3", "cur_mon_staff_detailed", cur_mon_staff,
                                               'collapse3'),
                            html.Br(),
                        ]),
                        # dbc.Row([
                        #     dcc.Graph(id="staff_3d_graph",config={'displayModeBar': False},
                        #               style={"border-radius": "5px",
                        #                      "background-color": "#f9f9f9",
                        #                      "box-shadow": "2px 2px 2px lightgrey",
                        #                      "position": "relative",
                        #                      "margin-bottom": "15px",
                        #                      "height":'800px'
                        #                      }
                        # ),
                        #     html.P("理论填报率:"),
                        #     dcc.RangeSlider(
                        #         id='range-slider',
                        #         min=min(cur_mon_staff['理论填报率']), max=max(cur_mon_staff['理论填报率']), step=5,
                        #         marks={min(cur_mon_staff['理论填报率']): min(cur_mon_staff['理论填报率']), max(cur_mon_staff['理论填报率']): max(cur_mon_staff['理论填报率'])},
                        #         value = [0, 120]
                        #     ),
                        # ]),
                        # html.Br(),

                        # dbc.Row([
                        #     dbc.Col([
                        #         irdc_graph('fig全量实际vs理论人天-scatter', fig全量实际vs理论人天),
                        #         html.P("理论填报率:"),
                        #         dcc.RangeSlider(
                        #             id='range-slider实际vs理论',
                        #             min=cur_mon_staff.理论填报率.min(), max=cur_mon_staff.理论填报率.max(), step=1,
                        #             marks={
                        #                 cur_mon_staff.理论填报率.min(): {'label': str(cur_mon_staff.理论填报率.min()),
                        #                                                  'style': {'color': 'orange'}},
                        #                 90: {'label': '90%', 'style': {'color': 'green'}},
                        #                 120: {'label': '120%', 'style': {'color': 'green'}},
                        #                 cur_mon_staff.理论填报率.max(): {'label': str(cur_mon_staff.理论填报率.max()),
                        #                                                  'style': {'color': 'red'}}},
                        #             value=[cur_mon_staff.理论填报率.min(), cur_mon_staff.理论填报率.max()], allowCross=False,
                        #             tooltip={"placement": "bottom", "always_visible": True}
                        #         ),
                        #     ], xs=12, sm=12, md=6, lg=6, xl=6)
                        # ]),

                ],
                        title = '人员维度详细',
                    )
                ],
                flush=True,start_collapsed=True, id="accordtion-staff"
            ),
        ),

            html.Br(),
            html.P("WBS维度Summary"),
            dbc.Row([
                dbc.Col([
                    irdc_summary_large("wbs_all_number", wbs_all_number)
                ]),
                dbc.Col([
                    dbc.Row([
                        irdc_summary_smWider("wbs_d_numebr", wbs_d_numebr),
                        irdc_summary_smWider("wbs_p_numebr", wbs_p_numebr),
                        irdc_summary_smWider("wbs_r_numebr", wbs_r_numebr),
                        irdc_summary_smWider("wbs_m_numebr", wbs_m_numebr),
                    ])]),
                dbc.Col([
                    dbc.Row([
                        irdc_summary_smWider("scg_number", scg_number),
                        irdc_summary_smWider("abg_number", abg_number),
                        irdc_summary_smWider("ibg_number", ibg_number),
                        irdc_summary_smWider("others_numebr", others_numebr),
                    ])]),
                dbc.Col([
                    dbc.Row([
                        irdc_summary_smWider("sx_number", sx_number),
                        irdc_summary_smWider("ir_number", ir_number),
                        irdc_summary_smWider("aiot_number", aiot_number),
                        irdc_summary_smWider("chuangfu_number", chuangfu_number),
                    ])]),
                dbc.Col([
                    irdc_summary_large("wbs_actual_hrs", wbs_actual_hrs)
                ]),
                dbc.Col([
                    dbc.Row([
                        irdc_summary_smWider("wbs_d_act", wbs_d_act),
                        irdc_summary_smWider("wbs_p_act", wbs_p_act),
                        irdc_summary_smWider("wbs_r_act", wbs_r_act),
                        irdc_summary_smWider("wbs_m_act", wbs_m_act),
                    ])]),
                dbc.Col([
                    dbc.Row([
                        irdc_summary_smWider("wbs_d_act_percentage", wbs_d_act_percentage),
                        irdc_summary_smWider("wbs_p_act_percentage", wbs_p_act_percentage),
                        irdc_summary_smWider("wbs_r_act_percentage", wbs_r_act_percentage),
                        irdc_summary_smWider("wbs_m_act_percentage", wbs_m_act_percentage),
                    ])]),
                dbc.Col([
                    dbc.Row([
                        irdc_summary_smWider("scg_act", scg_act),
                        irdc_summary_smWider("abg_act", abg_act),
                        irdc_summary_smWider("ibg_act", ibg_act),
                        irdc_summary_smWider("z_act", z_act),
                    ])]),
                dbc.Col([
                    dbc.Row([
                        irdc_summary_smWider("sx_act", sx_act),
                        irdc_summary_smWider("ir_act", ir_act),
                        irdc_summary_smWider("aiot_act", aiot_act),
                        irdc_summary_smWider("chuangfu_act", chuangfu_act),
                    ])]),
                dbc.Col([
                    dbc.Row([
                        irdc_summary_smWider("wbs_sx_percentage", wbs_sx_percentage),
                        irdc_summary_smWider("wbs_ir_percentage", wbs_ir_percentage),
                        irdc_summary_smWider("wbs_aiot_percentage", wbs_aiot_percentage),
                        irdc_summary_smWider("wbs_chuangfu_percentage", wbs_chuangfu_percentage),
                    ])]),
            ]),
            html.Div(
                dbc.Accordion(
                    [
                        dbc.AccordionItem([
                            dbc.Row([
                                dbc.Col([
                                    irdc_graph('WBS部门Top5-bar', figWBS部门Top5())
                                ], xs=12, sm=12, md=6, lg=6, xl=6),
                                dbc.Col([
                                    irdc_graph('WBS部门Top5-pie', figWBStop5填报分布())
                                ], xs=12, sm=12, md=6, lg=6, xl=6),
                            ]),
                            dbc.Col([
                                dash_table_not_collapse("WBS部门Top5_id",
                                                        wbs_top5_actual()),
                            ]),
                            html.Br(),
                            dbc.Row([
                                dbc.Col([
                                    irdc_graph('历史WBS类型-line', fig历史WBS类型())
                                ]),
                            ]),
                            dbc.Row([
                                irdc_graph('WBS汇总类型-pie', figWBS类型pie()),
                            ]),
                            dbc.Row([
                                irdc_graph('WBS汇总部门-pie', figWBS部门pie()),
                            ]),

                            dbc.Row([
                                dbc.Col([
                                    irdc_graph('wbs预估填报分布-pie', figWBS预估填报分布())
                                ], xs=12, sm=12, md=6, lg=6, xl=6),
                                dbc.Col([
                                    dbc.Row([
                                        irdc_graph('WBS预估填报异常部门-pie', figWBS预估填报异常部门分布())
                                    ]),
                                ], xs=12, sm=12, md=6, lg=6, xl=6),
                            ]),
                            dbc.Row([
                                html.P('WBS填报异常个数: ' + str(len(logic_rate_abnormal_tb_WBS())),
                                       style={"fontSize": 25}),
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    dash_table_not_collapse("logic_distribution_tb_WBS_id",
                                                            logic_rate_abnormal_tb_WBS()),
                                ]),
                            ]),


                            dbc.Row([
                                collapse_btn_table2("collapse-button6", "wbs总表_table",
                                                    readData(本月WBS维度()).sort_values(by='实际人天', ascending=False),
                                                    'collapse6', '实际人天'),
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Row([
                                        html.P('预估并未实际填写WBS个数：' + str(len(est_no_act_df())),
                                               style={"fontSize": 25}),
                                    ]),
                                ], xs=12, sm=12, md=6, lg=6, xl=6),
                                dbc.Col([
                                    dbc.Row([
                                        html.P('实际填写并未预估WBS个数：' + str(len(act_no_est_df())),
                                               style={"fontSize": 25}),
                                    ]),
                                ], xs=12, sm=12, md=6, lg=6, xl=6),
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    irdc_graph('WBS预估未填报-pie', figWBS预估无实际分布())
                                ], xs=12, sm=12, md=6, lg=6, xl=6),
                                dbc.Col([
                                    irdc_graph('WBS实际未填报-pie', figWBS实际未预估填报分布())
                                ], xs=12, sm=12, md=6, lg=6, xl=6),
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Row([
                                        collapse_btn_table("collapse-button7", "WBS预估未填报-table", est_no_act_df()[['项目编号', '项目名称', 'PM姓名', '实际人天','预估人天']],
                                                           'collapse7'),
                                        html.Br(),
                                    ]),
                                ], xs=12, sm=12, md=6, lg=6, xl=6),
                                dbc.Col([
                                    dbc.Row([
                                        collapse_btn_table("collapse-button8", "WBS实际未填报-table", act_no_est_df()[['项目编号', '项目名称', 'PM姓名', '实际人天','预估人天']],
                                                           'collapse8'),
                                        html.Br(),
                                    ]),
                                ], xs=12, sm=12, md=6, lg=6, xl=6),
                            ]),
                            html.Br(),
                            dbc.Row([
                                dbc.Col([
                                    irdc_graph('连续两月预估无实际填写WBS-pie', figWBS连续预估2月未填写分布())
                                ], xs=12, sm=12, md=6, lg=6, xl=6),
                                dbc.Col([
                                    dbc.Row([
                                        html.P('连续两月预估无实际填写WBS个数：' + str(
                                            len(est_twice_wbs())),
                                               style={"fontSize": 25}),
                                    ]),
                                    dbc.Row([
                                        dbc.Col([
                                            dash_table_not_collapse('连续两月预估无实际填写WBS-table',est_twice_wbs()[['项目编号','项目名称','PM姓名','上月预估','本月预估']])
                                        ]),
                                    ]),
                                ], xs=12, sm=12, md=6, lg=6, xl=6),
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    irdc_graph('超过1年WBS-pie', figWBS超过1年分布())
                                ], xs=12, sm=12, md=6, lg=6, xl=6),
                                dbc.Col([
                                    dbc.Row([
                                        html.P('建立超过1年WBS个数：' + str(
                                            len(get_more_than1yr_wbs())),
                                               style={"fontSize": 25}),
                                    ]),
                                    dbc.Row([
                                        dbc.Col([
                                            dash_table_not_collapse('超过1年WBS-table', get_more_than1yr_wbs())
                                        ]),
                                    ]),
                                ], xs=12, sm=12, md=6, lg=6, xl=6),
                            ]),

                            dbc.Row([
                                html.P('较上月新增WBS个数：' + str(
                                    len(新增wbs(readData(本月WBS维度()), readData(上月WBS维度())))) , style={"fontSize":25}),
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    dash_table_not_collapse('wbs新增table',
                                                            新增wbs_tb(readData(本月WBS维度()), readData(上月WBS维度()),
                                                                       "项目编号", "实际人天")),
                                ]),
                            ]),
                            html.Br(),
                            dbc.Row([
                                html.P('较上月减少WBS个数：' + str(
                                    len(减少wbs(readData(本月WBS维度()), readData(上月WBS维度())))) , style={"fontSize":25}),
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    dash_table_not_collapse('wbs减少table',
                                                            新增wbs_tb(readData(上月WBS维度()), readData(本月WBS维度()),
                                                                       "项目编号", "实际人天")),
                                ]),
                            ]),
                        ],
                            title='WBS维度详细'
                        )
                    ],
                    flush=True, start_collapsed=True,
                ),
            ),

            # dbc.Row([
            #     dbc.Col([
            #         dcc.Dropdown(list(员工所属部门汇总1[部门']), list(员工所属部门汇总1['员工所属部门']),
            #                      multi=True,
            #                      placeholder="请选择员工所属部门"),
            #         html.Br(),
            #
            #         dcc.RangeSlider(0, 30, value=[10, 15], tooltip={"placement": "bottom", "always_visible": True},
            #                         allowCross=False)
            #     ])
            # ])

        ], fluid=True)

    elif tab == '资源':
        return dbc.Container([
            html.P("GPU使用情况"),
            dbc.Row([
                dbc.Col([
                    irdc_summary_large("gpu_sh40_avg_usage", gpu_sh40_avg_usage)
                ]),
                dbc.Col([
                    dbc.Row([
                        irdc_summary_smWider("gpu_sh40_10_usage", gpu_sh40_10_usage),
                        irdc_summary_smWider("gpu_sh40_14_usage", gpu_sh40_14_usage),
                        irdc_summary_smWider("gpu_sh40_18_usage", gpu_sh40_18_usage),
                        irdc_summary_smWider("gpu_sh40_22_usage", gpu_sh40_22_usage),
                    ])]),

                dbc.Col([
                    irdc_summary_large("gpu_sh40_avg_usage", gpu_sh40_avg_usage)
                ]),
                dbc.Col([
                    dbc.Row([
                        irdc_summary_smWider("gpu_sh40_10_usage", gpu_sh40_10_usage),
                        irdc_summary_smWider("gpu_sh40_14_usage", gpu_sh40_14_usage),
                        irdc_summary_smWider("gpu_sh40_18_usage", gpu_sh40_18_usage),
                        irdc_summary_smWider("gpu_sh40_22_usage", gpu_sh40_22_usage),
                    ])]),

                dbc.Col([
                    irdc_summary_large("gpu_abud_avg_usage", gpu_abud_avg_usage)
                ]),
                dbc.Col([
                    dbc.Row([
                        irdc_summary_smWider("gpu_abud_10_usage", gpu_abud_10_usage),
                        irdc_summary_smWider("gpu_abud_14_usage", gpu_abud_14_usage),
                        irdc_summary_smWider("gpu_abud_18_usage", gpu_abud_18_usage),
                        irdc_summary_smWider("gpu_abud_22_usage", gpu_abud_22_usage),
                    ])]),

                dbc.Col([
                    irdc_summary_large("gpu_sg2_avg_usage", gpu_sg2_avg_usage)
                ]),
                dbc.Col([
                    dbc.Row([
                        irdc_summary_smWider("gpu_sg2_10_usage", gpu_sg2_10_usage),
                        irdc_summary_smWider("gpu_sg2_14_usage", gpu_sg2_14_usage),
                        irdc_summary_smWider("gpu_sg2_18_usage", gpu_sg2_18_usage),
                        irdc_summary_smWider("gpu_sg2_22_usage", gpu_sg2_22_usage),
                    ])]),
            ]),
            html.Div(
            dbc.Accordion(
                [
                    dbc.AccordionItem([
                        dbc.Col([
                            html.Div([
                                html.Div([
                                    dcc.RadioItems(
                                        id='radio_gpu_use',
                                        options=[
                                            {'label': 'Avg', 'value': 'graph_gpu_avg'},
                                            {'label': '10点', 'value': 'graph_gpu_10'},
                                            {'label': '14点', 'value': 'graph_gpu_14'},
                                            {'label': '18点', 'value': 'graph_gpu_18'},
                                            {'label': '22点', 'value': 'graph_gpu_22'},
                                        ],
                                        value='graph_gpu_avg',
                                        style={"width": "60%"},
                                        inline=True),
                                ]),
                                html.Div(
                                    dcc.Graph(id='graph_gpu_use',
                                              style={'height': 500,
                                                     "border-radius": "5px",
                                                     "background-color": "#f9f9f9",
                                                     "box-shadow": "2px 2px 2px lightgrey",
                                                     "position": "relative",
                                                     "margin-bottom": "15px"
                                                     },
                                              config={'displayModeBar': False},
                                              ),
                                ),

                            ])

                        ]),
                ],
                        title = 'GPU使用详细',
                    )
                ],
                flush=True,start_collapsed=True, id="accordtion-gpu"
            ),
        ),

            html.Br(),
            html.P("数据采标情况"),
            dbc.Row([
            ]),
            html.Div(
                dbc.Accordion(
                    [
                        dbc.AccordionItem([

                            dbc.Row([
                                dbc.Col([
                                    dash_table_not_collapse('wbs减少table',
                                                            新增wbs_tb(readData(上月WBS维度()), readData(本月WBS维度()),
                                                                       "项目编号", "实际人天")),
                                ]),
                            ]),
                        ],
                            title='数据采标任务详细'
                        )
                    ],
                    flush=True, start_collapsed=True,
                ),
            ),

            html.Br(),
            html.P("OC与DCP存储"),
            dbc.Row([
            ]),
            html.Br(),
            html.Div(
            dbc.Accordion(
                [
                    dbc.AccordionItem([

                        dbc.Row([
                            dbc.Col([
                                irdc_graph('员工所属部门汇总-summary', fig员工所属部门汇总())
                            ], xs=12, sm=12, md=6, lg=6, xl=6),
                            dbc.Col([
                                irdc_graph('员工所属部门汇总-bar', fig员工所属部门人均人天())
                            ], xs=12, sm=12, md=6, lg=6, xl=6),
                            dbc.Col([
                                html.Div([
                                    html.Div([
                                        dcc.RadioItems(
                                            id='radio_actual_per',
                                            options=[
                                                {'label': 'IRDC', 'value': 'graph_actual_per_irdc'},
                                                {'label': '业务线', 'value': 'graph_actual_per_all'},
                                            ],
                                            value='graph_actual_per_irdc',
                                            style={"width": "60%"},
                                            inline=True),
                                    ]),
                                    html.Div(
                                        dcc.Graph(id='graph_actual_per',
                                                  style={'height': 500,
                                                         "border-radius": "5px",
                                                         "background-color": "#f9f9f9",
                                                         "box-shadow": "2px 2px 2px lightgrey",
                                                         "position": "relative",
                                                         "margin-bottom": "15px"
                                                         },
                                                  config = {'displayModeBar': False},
                                                  ),
                                    ),

                                ])

                            ]),
                            # dbc.Col([
                            #     irdc_graph('历史部门实际人均人天-line2', fig历史实际人均人天())
                            # ]),
                            dbc.Col([
                                html.Div([
                                    html.Div([
                                        dcc.RadioItems(
                                            id='radio_logic_rate',
                                            options=[
                                                {'label': 'IRDC', 'value': 'graph_logic_rate_irdc'},
                                                {'label': '业务线', 'value': 'graph_logic_rate_all'},
                                            ],
                                            value='graph_logic_rate_irdc',
                                            style={"width": "60%"},
                                            inline=True),
                                    ]),
                                    html.Div(
                                        dcc.Graph(id='graph_logic_rate',
                                                  style={'height': 500,
                                                         "border-radius": "5px",
                                                         "background-color": "#f9f9f9",
                                                         "box-shadow": "2px 2px 2px lightgrey",
                                                         "position": "relative",
                                                         "margin-bottom": "15px"
                                                         },
                                                  config={'displayModeBar': False},
                                                  ),
                                    ),

                                ])

                            ]),
                            # dbc.Col([
                            #     irdc_graph('历史部门理论填报率-line', fig历史理论填报率())
                            # ]),
                        ]),
                ],
                        title = 'OC与DCP存储详细',
                    )
                ],
                flush=True,start_collapsed=True,
            ),
            ),

            html.Br(),
            html.P("固定资产情况"),
            dbc.Row([
            ]),
            html.Br(),
            html.Div(
            dbc.Accordion(
                [
                    dbc.AccordionItem([

                        dbc.Row([
                            dbc.Col([
                                irdc_graph('员工所属部门汇总-summary', fig员工所属部门汇总())
                            ], xs=12, sm=12, md=6, lg=6, xl=6),
                            dbc.Col([
                                irdc_graph('员工所属部门汇总-bar', fig员工所属部门人均人天())
                            ], xs=12, sm=12, md=6, lg=6, xl=6),
                        ]),
                        dbc.Row([
                            collapse_btn_table("collapse-button3", "cur_mon_staff_detailed", cur_mon_staff,
                                               'collapse3'),
                            html.Br(),
                        ]),
                ],
                        title = '固定资产详细',
                    )
                ],
                flush=True,start_collapsed=True,
            ),
            ),

        ], fluid=True)

    # elif tab == '业务线':
    #     return dbc.Container([
    #         html.P("业务线明细"),
    #         dbc.Row([
    #             dbc.Col([
    #                 dcc.Graph(id='staff_number_indicator_sx', figure=staff_number_indicator_sx,config={'displayModeBar': False},
    #                           style={"border-radius": "5px",
    #                                  "background-color":"#f9f9f9",
    #                                  "box-shadow": "2px 2px 2px lightgrey",
    #                                  "position": "relative",
    #                                  "margin-bottom": "20px",
    #                                  "width":"135px"
    #                            }
    #             )]),
    #         ]),
    #         html.P("资源池明细"),
    #         dbc.Row([
    #             dbc.Col([
    #                 dcc.Graph(id='staff_number_indicator_sx', figure=staff_number_indicator_sx,
    #                           config={'displayModeBar': False},
    #                           style={"border-radius": "5px",
    #                                  "background-color": "#f9f9f9",
    #                                  "box-shadow": "2px 2px 2px lightgrey",
    #                                  "position": "relative",
    #                                  "margin-bottom": "20px",
    #                                  "width": "135px"
    #                                  }
    #                           )]),
    #
    #         ]),
    #     ], fluid=True)


@app.callback(
    Output('graph_actual_per', 'figure'),
    [Input(component_id='radio_actual_per', component_property='value')]
)
def build_graph_actual_per(value_actual_per):
    if value_actual_per == 'graph_actual_per_all':
        return fig历史实际人均人天()

    else:
        return fig历史实际人均人天_irdc()

@app.callback(
    Output('graph_logic_rate', 'figure'),
    [Input(component_id='radio_logic_rate', component_property='value')]
)
def build_graph_logic_rate(value_logic_rate):
    if value_logic_rate == 'graph_logic_rate_irdc':
        return fig历史理论填报率_irdc()

    else:
        return fig历史理论填报率()

@app.callback(
    Output('graph_gpu_use', 'figure'),
    [Input(component_id='radio_gpu_use', component_property='value')]
)
def build_graph_gpu_use(value_gpu_use):
    if value_gpu_use == 'graph_gpu_avg':
        return fig历史gpu使用()
    if value_gpu_use == 'graph_gpu_10':
        return fig历史gpu使用具体时间点(10)
    if value_gpu_use == 'graph_gpu_14':
        return fig历史gpu使用具体时间点(14)
    if value_gpu_use == 'graph_gpu_18':
        return fig历史gpu使用具体时间点(18)
    if value_gpu_use == 'graph_gpu_22':
        return fig历史gpu使用具体时间点(22)



# @app.callback(
#     Output('graph_actual_per', 'figure'),
#     [Input(component_id='radio_actual_per', component_property='value')]
# )
# def build_graph_actual_per(value):
#     if value == 'graph_irdc_actual_per':
#         return irdc_graph('1', fig历史实际人均人天_irdc())
#
#     else:
#         return irdc_graph('2', fig历史实际人均人天())
#


if __name__ == "__main__":
    app.run_server(debug=True)

# app.callback 里加上prevent_initial_callback=True,为了不要一开始就call back
# 用判断条件来看是是否要trigger，用state，然后def里的参数需要input 和state 几个
# return 记得用component_property 来放在def里return
# 用df作图，永远先copy 成新df来做！！！
# PreventUpdate 用来避免output update
# 有很多output，但有些不想update 用Dash.no_update
