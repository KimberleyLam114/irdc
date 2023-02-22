from cleanData import *
from dataSource import *
import pathlib
from dash import Dash
import dash_auth
from datetime import datetime
from dash import Dash, dcc, html, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from dash.exceptions import PreventUpdate


all_actual_days = readData(历史部门实际人均人天())
all_logic_percentage = readData(历史部门理论填报率())
cur_bus_line_summary = readData(本月业务线维度())
last_bus_line_summary = readData(上月业务线维度())
cur_staff_apartment = readData(本月员工所属部门())
business_line_staff_type = readData(本月业务线员工组())
cur_mon_staff = cleanCurMonStaff(本月人员维度())
last_mon_staff = cleanCurMonStaff(上月人员维度())
staff_apartment_tb = cleanstaff_apartment_table()
business_line_tb = cleanbusiness_line_table()

员工所属部门汇总1 = cleanstaff_apartment_table()
预估业务线pie = 业务线pie("预估人天")
实际业务线pie = 业务线pie("实际人天")
理论业务线pie = 业务线pie("理论人天")
实际岗位pie = 岗位pie('实际人天')
理论岗位pie = 岗位pie('理论人天')
理论业务线汇总 = 业务线汇总('理论人天')
实际业务线汇总 = 业务线汇总('实际人天')
理论实际业务线汇总 = 对比部门汇总('理论人天','实际人天')
实际部门wbspie = wbs部门pie("实际人天")
预估部门wbspie = wbs部门pie("预估人天")
实际类型wbspie = wbs类型pie("实际人天")
预估类型wbspie = wbs类型pie("预估人天")
# 实际利润中心wbspie = wbs利润中心pie("实际人天")
# 预估利润中心wbspie = wbs利润中心pie("预估人天")

# indicator summary for sx
cur_mon_staff_sx = monStaff_businessLine(本月人员维度(),'SX')
last_mon_staff_sx = monStaff_businessLine(上月人员维度(),'SX')
cur_mon_staff_sx_ibg = monStaff_businessLine(本月人员维度(),'SX-IBG')
last_mon_staff_sx_ibg = monStaff_businessLine(上月人员维度(),'SX-IBG')
cur_mon_staff_sx_abg = monStaff_businessLine(本月人员维度(),'SX-ABG')
last_mon_staff_sx_abg = monStaff_businessLine(上月人员维度(),'SX-ABG')

# indicator summary for ir
cur_mon_staff_ir = monStaff_businessLine(本月人员维度(),'IR')
last_mon_staff_ir = monStaff_businessLine(上月人员维度(),'IR')

# indicator summary for aiot
cur_mon_staff_aiot = monStaff_businessLine(本月人员维度(),'AIOT')
last_mon_staff_aiot = monStaff_businessLine(上月人员维度(),'AIOT')

# indicator summary for dx
cur_mon_staff_dx = monStaff_businessLine(本月人员维度(),'DX')
last_mon_staff_dx = monStaff_businessLine(上月人员维度(),'DX')
cur_mon_staff_dx_ty = monStaff_businessLine(本月人员维度(),'DX-TY')
last_mon_staff_dx_ty = monStaff_businessLine(上月人员维度(),'DX-TY')
cur_mon_staff_dx_sku = monStaff_businessLine(本月人员维度(),'DX-SKU')
last_mon_staff_dx_sku = monStaff_businessLine(上月人员维度(),'DX-SKU')

# indicator summary for si
cur_mon_staff_si = monStaff_businessLine(本月人员维度(),'SI')
last_mon_staff_si = monStaff_businessLine(上月人员维度(),'SI')

def indicator_logic_percentage(cur_in_actual_day, cur_in_lo_day,last_in_actual_day, last_in_lo_day,reName):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = round(cur_in_actual_day/cur_in_lo_day*100,1),
        number={"suffix": "%"},
        delta = {"reference": round(last_in_actual_day/last_in_lo_day*100,1), "valueformat": ".0f",},
        title = {"text": reName},
        align="center",
        ))
    indicator.update_traces(
        domain_column=2, domain_row=2,delta_font_size=12,number_font_size=18,title_font_size=13
    )
    indicator.update_layout(
        height=80,width=88,
    )
    return indicator

# indicator summary
def indicator_bg(cur_data, last_data, tableValue, reName):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = len(cur_data[tableValue]),
        delta = {"reference": len(last_data[tableValue]), "valueformat": ".0f"},
        title = {"text": reName},
        align="center",
        ))
    indicator.update_traces(
        domain_column=1, domain_row=3,delta_font_size=12,number_font_size=28,title_font_size=15
    )
    indicator.update_layout(
        height=120,width=135,
    )
    return indicator

def indicator_large(cur_data, last_data, tableValue, reName):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = len(cur_data[tableValue]),
        delta = {"reference": len(last_data[tableValue]), "valueformat": ".0f"},
        title = {"text": reName},
        align="center",
        ))
    indicator.update_traces(
        domain_column=1, domain_row=3,delta_font_size=16,number_font_size=30,title_font_size=18
    )
    indicator.update_layout(
        height=240,width=150,
    )
    return indicator

def indicator_large_ppl(cur_data, last_data, tableValue, reName):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = len(cur_data[tableValue]),
        delta = {"reference": len(last_data[tableValue]), "valueformat": ".0f"},
        title = {"text": reName},
        align="center",
        ))
    indicator.update_traces(
        domain_column=1, domain_row=3,delta_font_size=16,number_font_size=26,title_font_size=18
    )
    indicator.update_layout(
        height=242,width=133,
    )
    return indicator

def indicator_wbs_sum(cur_data, last_data, tableValue, reName):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = len(cur_data[tableValue]),
        delta = {"reference": len(last_data[tableValue]), "valueformat": ".0f"},
        title = {"text": reName},
        align="center",
        ))
    indicator.update_traces(
        domain_column=1, domain_row=3,delta_font_size=16,number_font_size=30,title_font_size=18
    )
    indicator.update_layout(
        height=320,width=150,
    )
    return indicator

def indicator_wbs_number(cur_data, last_data, tableValue, reName):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = cur_data[tableValue],
        delta = {"reference": last_data[tableValue], "valueformat": ".0f"},
        title = {"text": reName},
        align="center",
        ))
    indicator.update_traces(
        domain_column=2, domain_row=2, delta_font_size=12, number_font_size=20, title_font_size=15
    )
    indicator.update_layout(
        height=80, width=100,
    )
    return indicator

def indicator_wbs_number2(cur_data, last_data, reName):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = cur_data,
        delta = {"reference": last_data, "valueformat": ".0f"},
        title = {"text": reName},
        align="center",
        ))
    indicator.update_traces(
        domain_column=2, domain_row=2, delta_font_size=12, number_font_size=20, title_font_size=15
    )
    indicator.update_layout(
        height=80, width=100,
    )
    return indicator

def indicator_wbs_act(cur_data, last_data, tableValue,reName):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = round(cur_data[tableValue].sum(),1),
        delta = {"reference": round(last_data[tableValue].sum(),1), "valueformat": ".0f"},
        title = {"text": reName},
        align="center",
        ))
    indicator.update_traces(
        domain_column=1, domain_row=3,delta_font_size=16,number_font_size=30,title_font_size=18
    )
    indicator.update_layout(
        height=320,width=150,
    )
    return indicator


def indicator_wbs_type(cur_data, last_data, type, tableValue1, tableValue2, reName):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = round(cur_data[cur_data[tableValue1] == type][tableValue2].sum()/cur_data[tableValue2].sum()*100,1),
        number={"suffix": "%"},
        title = {"text": reName},
        align="center",
        delta={"reference": round(
            last_data[last_data[tableValue1] == type][tableValue2].sum() / last_data[tableValue2].sum() * 100, 1),
               "valueformat": ".0f"},
    ))
    indicator.update_traces(
        domain_column=2, domain_row=2, delta_font_size=12, number_font_size=20, title_font_size=15
    )
    indicator.update_layout(
        height=80, width=100,
    )
    return indicator


def indicator_wbs_type_sum(cur_data, last_data, type, tableValue1, tableValue2, reName):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = round(cur_data[cur_data[tableValue1] == type][tableValue2].sum(),1),
        title = {"text": reName},
        align="center",
        delta={"reference": round(
            last_data[last_data[tableValue1] == type][tableValue2].sum(), 1),
               "valueformat": ".0f"},
    ))
    indicator.update_traces(
        domain_column=2, domain_row=2, delta_font_size=12, number_font_size=20, title_font_size=15
    )
    indicator.update_layout(
        height=80, width=100,
    )
    return indicator


def indicator_wbs_percentage(cur_data, last_data, type, wbsApartment, tableValue1, tableValue2, reName):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = round(cur_data[cur_data[wbsApartment] == type][tableValue2].sum()/cur_data[cur_data[wbsApartment] == type][tableValue1].sum()*100,1),
        number={"suffix": "%"},
        title = {"text": reName},
        align="center",
        delta={"reference": round(last_data[last_data[wbsApartment] == type][tableValue2].sum()/last_data[last_data[wbsApartment] == type][tableValue1].sum()*100,1),
               "valueformat": ".0f"},

    ))
    indicator.update_traces(
        domain_column=2, domain_row=2, delta_font_size=12, number_font_size=20, title_font_size=15
    )
    indicator.update_layout(
        height=80, width=100,
    )
    return indicator

def indicator_irdc_sum(cur_data, last_data, tableValue,reName):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = round(cur_data[tableValue].sum(),1),
        delta = {"reference": round(last_data[tableValue].sum(),1), "valueformat": ".0f"},
        title = {"text": reName},
        align="center",
        ))
    indicator.update_traces(
        domain_column=1, domain_row=3,delta_font_size=16,number_font_size=26,title_font_size=18
    )
    indicator.update_layout(
        height=242,width=133,
    )
    return indicator

def indicator_irdc_per(cur_data, last_data, tableValue1, tableValue2,reName):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = round(cur_data[tableValue1].sum()/len(cur_data[tableValue2]),1),
        delta = {"reference": round(last_data[tableValue1].sum()/len(last_data[tableValue2]),1), "valueformat": ".0f"},
        title = {"text": reName},
        align="center",
        ))
    indicator.update_traces(
        domain_column=1, domain_row=3,delta_font_size=16,number_font_size=26,title_font_size=18
    )
    indicator.update_layout(
        height=242,width=133,
    )
    return indicator


def indicator_irdc_type_per(cur_in_actual_day, cur_in_staff_number, last_in_actual_day, last_in_staff_number, reName):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = round(cur_in_actual_day/cur_in_staff_number,1),
        delta = {"reference": round(last_in_actual_day/last_in_staff_number,1), "valueformat": ".0f"},
        title = {"text": reName},
        align="center",
        ))
    indicator.update_traces(
        domain_column=2, domain_row=2,delta_font_size=12,number_font_size=18,title_font_size=13
    )
    indicator.update_layout(
        height=80,width=88,
    )
    return indicator



def indicator_sum(cur_data, last_data, businessLine, tableValue):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = cur_data[cur_data['业务线'].str.contains(businessLine)][tableValue].sum(),
        delta = {"reference": last_data[last_data['业务线'].str.contains(businessLine)][tableValue].sum(), "valueformat": ".0f"},
        title = {"text": tableValue},
        align="center",
        ))
    indicator.update_traces(
        domain_column=1, domain_row=3,delta_font_size=12,number_font_size=28,title_font_size=15
    )
    indicator.update_layout(
        height=120,width=135,
    )
    return indicator


def indicator_value0(cur_data, last_data, businessLine, tableValue,reName):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = cur_data[cur_data['业务线'] == businessLine][tableValue].values[0],
        delta = {"reference": last_data[last_data['业务线'] == businessLine][tableValue].values[0], "valueformat": ".0f"},
        title = {"text": reName},
        align="center",
        ))
    indicator.update_traces(
        domain_column=1, domain_row=3, delta_font_size=12, number_font_size=28, title_font_size=15
    )
    indicator.update_layout(
        height=120,width=135,
    )
    return indicator


def indicator_avg(cur_data, last_data, businessLine, tableValue1, tableValue2, reName):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = cur_data[cur_data['业务线'].str.contains(businessLine)][tableValue1].sum()/cur_data[cur_data['业务线'].str.contains(businessLine)][tableValue2].sum(),
        delta = {"reference": last_data[last_data['业务线'].str.contains(businessLine)][tableValue1].sum()/last_data[last_data['业务线'].str.contains(businessLine)][tableValue2].sum(), "valueformat": ".0f"},
        title = {"text": reName},
        align="center",
        ))
    indicator.update_traces(
        domain_column=1, domain_row=3, delta_font_size=12, number_font_size=28, title_font_size=15
    )
    indicator.update_layout(
        height=120,width=135,
    )
    return indicator


def indicator_irdc_rate(cur_data, last_data, tableValue1, tableValue2, reName):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = round(cur_data[tableValue1].sum()/cur_data[tableValue2].sum()*100,1),
        number={"suffix": "%"},
        title = {"text": reName},
        align="center",
        delta={"reference": round(last_data[tableValue1].sum() / last_data[tableValue2].sum() * 100, 1),
               "valueformat": ".0f", 'relative': True},

    ))
    indicator.update_traces(
        domain_column=1, domain_row=3,delta_font_size=16,number_font_size=26,title_font_size=18
    )
    indicator.update_layout(
        height=242,width=133,
    )
    return indicator


def indicator_rate(cur_data, last_data, businessLine, tableValue1, tableValue2, reName):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = round(cur_data[cur_data['业务线'].str.contains(businessLine)][tableValue1].sum()/cur_data[cur_data['业务线'].str.contains(businessLine)][tableValue2].sum()*100,1),
        number={"suffix": "%"},
        title = {"text": reName},
        align="center",
        delta={"reference": round(last_data[last_data['业务线'].str.contains(businessLine)][tableValue1].sum() /
                                  last_data[last_data['业务线'].str.contains(businessLine)][tableValue2].sum() * 100,
                                  1), "valueformat": ".0f", 'relative': True},

    ))
    indicator.update_traces(
        domain_column=1, domain_row=3,delta_font_size=12,number_font_size=28,title_font_size=15
    )
    indicator.update_layout(
        height=120,width=135,
    )
    return indicator


def indicator_gpu_percentage_large(cur_data,last_data,reName):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = round(cur_data,1),
        number={"suffix": "%"},
        delta = {"reference": round(last_data,1), "valueformat": ".0f",},
        title = {"text": reName},
        align="center",
        ))
    indicator.update_traces(
        domain_column=1, domain_row=3,delta_font_size=16,number_font_size=30,title_font_size=18
    )
    indicator.update_layout(
        height=320,width=150,
    )
    return indicator

def indicator_gpu_percentage_small(cur_data,last_data,reName):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = round(cur_data,1),
        number={"suffix": "%"},
        title = {"text": reName},
        align="center",
        delta={"reference": round(last_data,1),
               "valueformat": ".0f"},

    ))
    indicator.update_traces(
        domain_column=2, domain_row=2, delta_font_size=12, number_font_size=20, title_font_size=15
    )
    indicator.update_layout(
        height=80, width=100,
    )
    return indicator

def try_except(value, default):
    try:
        return value
    except KeyError:
        return default

def indicator_lessMore(cur_data, last_data, businessLine, tableValue, lessMore, reName):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = try_except(cur_data[cur_data['业务线'] == businessLine][tableValue].value_counts()[lessMore], 0),
        delta = {"reference": try_except(last_data[last_data['业务线'] == businessLine][tableValue].value_counts()[lessMore], 0), "valueformat": ".0f"},
        title = {"text":reName},
        align="center",
        ))
    indicator.update_traces(
        domain_column=1, domain_row=3, delta_font_size=12, number_font_size=28, title_font_size=15
    )
    indicator.update_layout(
        height=120,width=135,
    )
    return indicator


def indicator(cur_data, last_data, reName):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = cur_data,
        delta = {"reference": last_data, "valueformat": ".0f"},
        title = {"text": reName},
        align="center"
        ))
    indicator.update_traces(
        domain_column=2, domain_row=2,delta_font_size=12,number_font_size=20,title_font_size=15
    )
    indicator.update_layout(
        height=80,width=100,
    )
    return indicator


def indicator_ppl(cur_data, last_data, reName):
    indicator = go.Figure(go.Indicator(
        mode = "number+delta",
        value = cur_data,
        delta = {"reference": last_data, "valueformat": ".0f"},
        title = {"text": reName},
        align="center"
        ))
    indicator.update_traces(
        domain_column=2, domain_row=2,delta_font_size=12,number_font_size=18,title_font_size=13
    )
    indicator.update_layout(
        height=80,width=88,
    )
    return indicator


def irdc_summary_large(id, fig):
    return dcc.Graph(id=id, figure=fig, config={'displayModeBar': False},
              style={
                  # "border-radius": "5px",
                     "background-color": "#f9f9f9",
                     "box-shadow": "2px 2px 2px lightgrey",
                     "position": "relative",
                     "margin-bottom": "20px",
                     "width":'150px'
                     })

def irdc_summary_large_ppl(id, fig):
    return dcc.Graph(id=id, figure=fig, config={'displayModeBar': False},
              style={
                     "background-color": "#f9f9f9",
                     "box-shadow": "1px 1px 1px lightgrey",
                     "position": "relative",
                  "margin-bottom": "1px",
                     "width":'130px'
                     })

def irdc_summary_smWider_ppl(id, fig):
    return dcc.Graph(id=id, figure=fig, config={'displayModeBar': False},
              style={
                  "background-color": "#f9f9f9",
                  "box-shadow": "1px 1px 1px lightgrey",
                  "position": "relative",
                  "margin-bottom": "1px",
                  "margin-left": "-12px",
                  "width": '95px'
                     })

def irdc_summary_smWider(id, fig):
    return dcc.Graph(id=id, figure=fig, config={'displayModeBar': False},
              style={
                  # "border-radius": "5px",
                     "background-color": "#f9f9f9",
                     "box-shadow": "1px 1px 1px lightgrey",
                     "position": "relative",
                     "margin-bottom": "1px",
                  "width":"100px",
                     })


def irdc_graph(id, fig):
    return dcc.Graph(id=id, figure=fig, config={'displayModeBar': False},
              style={"border-radius": "5px",
                     "background-color": "#f9f9f9",
                     "box-shadow": "2px 2px 2px lightgrey",
                     "position": "relative",
                     "margin-bottom": "15px"
                     }
              )


def collapse_btn_table(btn_id, tb_id, tb_data,output_id):
    return html.Div([
        dbc.Button(
            "查看数据原表",
            id=btn_id,
            className= "mb-3",
            color="info",
            n_clicks=0,
        ),
        dbc.Collapse(
            dash_table.DataTable(
                id=tb_id,
                columns=[{"name": i, "id": i, } for i in tb_data.columns],
                sort_action="native",
                sort_mode="multi",
                page_size=10,
                data=tb_data.to_dict('records'),
                style_header={
                    'backgroundColor': 'rgb(210, 210, 210)',
                    'color': 'black',
                    'fontWeight': 'bold',
                    'border': '1px solid white'
                },
                style_data_conditional=[
                    {
                        'if': {
                            'filter_query': '{预估填报} = 不满',
                            'column_id': '预估填报'
                        },
                        'color': 'orange',
                        'fontWeight': 'bold'
                    },
                    {
                        'if': {
                            'filter_query': '{理论填报} = 不满',
                            'column_id': '理论填报'
                        },
                        'color': 'orange',
                        'fontWeight': 'bold'
                    },
                    {
                        'if': {
                            'filter_query': '{预估填报} = 超载',
                            'column_id': '预估填报'
                        },
                        'color': 'tomato',
                        'fontWeight': 'bold'
                    },
                    {
                        'if': {
                            'filter_query': '{理论填报} = 超载',
                            'column_id': '理论填报'
                        },
                        'color': 'tomato',
                        'fontWeight': 'bold'
                    },
                    {
                        'if': {
                            'filter_query': '{预估填报} = 合理',
                            'column_id': '预估填报'
                        },
                        'color': 'green',
                        'fontWeight': 'bold'
                    },
                    {
                        'if': {
                            'filter_query': '{理论填报} = 合理',
                            'column_id': '理论填报'
                        },
                        'color': 'green',
                        'fontWeight': 'bold'
                    }
                ],
                style_cell={'border': '1px solid lightgrey'}
            ),
            is_open=False,
            id=output_id
        ),
    ])

def data_bars(df, column):
    n_bins = 100
    bounds = [i * (1.0 / n_bins) for i in range(n_bins + 1)]
    ranges = [
        ((df[column].max() - df[column].min()) * i) + df[column].min()
        for i in bounds
    ]
    styles = []
    for i in range(1, len(bounds)):
        min_bound = ranges[i - 1]
        max_bound = ranges[i]
        max_bound_percentage = bounds[i] * 100
        styles.append(
            {
            'if': {
                'filter_query': (
                    '{{{column}}} >= {min_bound}' +
                    (' && {{{column}}} < {max_bound}' if (i < len(bounds) - 1) else '')
                ).format(column=column, min_bound=min_bound, max_bound=max_bound),
                'column_id': column
            },
            'background': (
                """
                    linear-gradient(90deg,
                    #0074D9 0%,
                    #0074D9 {max_bound_percentage}%,
                    white {max_bound_percentage}%,
                    white 100%)
                """.format(max_bound_percentage=max_bound_percentage)
            ),
        })
    return styles

def collapse_btn_table2(btn_id, tb_id, tb_data,output_id,tableValue):
    return html.Div([
        dbc.Button(
            "查看数据原表",
            id=btn_id,
            className= "mb-3",
            color="info",
            n_clicks=0,
        ),
        dbc.Collapse(
            dash_table.DataTable(
                id=tb_id,
                columns=[{"name": i, "id": i, } for i in tb_data.columns],
                sort_action="native",
                sort_mode="multi",
                data=tb_data.to_dict('records'),
                # style_header={
                #     'backgroundColor': 'rgb(210, 210, 210)',
                #     'color': 'black',
                #     'fontWeight': 'bold',
                #     'border': '1px solid white'
                # },
                style_data_conditional=(data_bars(tb_data, tableValue)),
                style_cell={
                    'width': '100px',
                    'minWidth': '100px',
                    'maxWidth': '100px',
                    'overflow': 'hidden',
                    'textOverflow': 'ellipsis',
                    'border': '1px solid lightgrey'
                },
            ),
            is_open=False,
            id=output_id
        ),
    ])


def dash_table_not_collapse(tb_id, tb_data):
    return dash_table.DataTable(
                                    id=tb_id,
                                    columns=[{"name": i, "id": i, } for i in tb_data.columns],
                                    sort_action="native",
                                    sort_mode="multi",
                                    data=tb_data.to_dict('records'),
                                    page_size = 10,
                                    style_header={
                                        'backgroundColor': 'rgb(210, 210, 210)',
                                        'color': 'black',
                                        'fontWeight': 'bold',
                                        'border': '1px solid white'
                                    },
                                    style_data_conditional=[
                                        {
                                            'if': {
                                                'filter_query': '{预估填报} = 不满',
                                                'column_id': '预估填报'
                                            },
                                            'color': 'orange',
                                            'fontWeight': 'bold'
                                        },
                                        {
                                            'if': {
                                                'filter_query': '{理论填报} = 不满',
                                                'column_id': '理论填报'
                                            },
                                            'color': 'orange',
                                            'fontWeight': 'bold'
                                        },
                                        {
                                            'if': {
                                                'filter_query': '{预估填报} = 超载',
                                                'column_id': '预估填报'
                                            },
                                            'color': 'tomato',
                                            'fontWeight': 'bold'
                                        },
                                        {
                                            'if': {
                                                'filter_query': '{理论填报} = 超载',
                                                'column_id': '理论填报'
                                            },
                                            'color': 'tomato',
                                            'fontWeight': 'bold'
                                        },
                                        {
                                            'if': {
                                                'filter_query': '{预估填报} = 合理',
                                                'column_id': '预估填报'
                                            },
                                            'color': 'green',
                                            'fontWeight': 'bold'
                                        },
                                        {
                                            'if': {
                                                'filter_query': '{理论填报} = 合理',
                                                'column_id': '理论填报'
                                            },
                                            'color': 'green',
                                            'fontWeight': 'bold'
                                        },
                                        {
                                            'if': {
                                                'filter_query': '{未填次数} contains "2"'
                                            },
                                            'backgroundColor': 'red',
                                            'color': 'white'
                                        },
                                    ],
                                    style_cell={'border': '1px solid lightgrey'}
                                )


def fig员工所属部门汇总():
    # graph staff apartment
    fig员工所属部门汇总 = go.Figure()
    fig员工所属部门汇总.add_bar(x=list(员工所属部门汇总1.员工所属部门)
                                , y=list(员工所属部门汇总1.预估人天)
                                , name="预估人天")
    fig员工所属部门汇总.add_bar(x=list(员工所属部门汇总1.员工所属部门)
                                , y=list(员工所属部门汇总1.理论人天)
                                , name="理论人天")
    fig员工所属部门汇总.add_trace(
        go.Scatter(x=list(员工所属部门汇总1.员工所属部门), y=list(员工所属部门汇总1.实际人天), mode='markers',
                   name='实际人天', marker=dict(
                color='black', size=10,
                line=dict(
                    color='MediumPurple',
                    width=2))))
    fig员工所属部门汇总.update_layout(title='部门总工时', template='plotly_white', yaxis_title='总工时/小时')
    return fig员工所属部门汇总


def fig员工所属部门人均人天():
    fig员工所属部门人均人天 = go.Figure()
    fig员工所属部门人均人天.add_bar(x=list(员工所属部门汇总1.员工所属部门)
                                    , y=list(员工所属部门汇总1.预估人均)
                                    , name="预估人均")
    fig员工所属部门人均人天.add_bar(x=list(员工所属部门汇总1.员工所属部门)
                                    , y=list(员工所属部门汇总1.实际人均)
                                    , name="实际人均")
    fig员工所属部门人均人天.add_bar(x=list(员工所属部门汇总1.员工所属部门)
                                    , y=list(员工所属部门汇总1.理论人均)
                                    , name="理论人均")
    fig员工所属部门人均人天.add_trace(go.Scatter(
        x=list(员工所属部门汇总1.员工所属部门),
        y=list(员工所属部门汇总1.部门实际人均),
        mode="markers+lines",
        name="部门实际人均人天",
        line=dict(
            color="black")))
    fig员工所属部门人均人天.update_layout(title='部门人均人天', template='plotly_white', yaxis_title='人均人天')
    return fig员工所属部门人均人天



# fig员工所属部门实际填报率 = go.Figure()
# fig员工所属部门实际填报率.add_trace(
#     go.Scatter(x=list(员工所属部门汇总1.员工所属部门), y=list(员工所属部门汇总1.预估填报率),
#                mode="markers+lines", name="预估填报率", line=dict(color="blue")))
# fig员工所属部门实际填报率.add_trace(
#     go.Scatter(x=list(员工所属部门汇总1.员工所属部门), y=list(员工所属部门汇总1.理论填报率),
#                mode="markers+lines", name="理论填报率", line=dict(color="red")))
# fig员工所属部门实际填报率.update_layout(title='员工所属部门预估实际填报率', template='plotly_white',
#                                         yaxis_title='工时填报率%')


# fig = px.line(df, x="月份", y="lifeExp", color='country')


def fig业务线pie():
    labels业务线 = list(实际业务线pie['实际人天'].keys())
    fig业务线pie = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])
    fig业务线pie.add_trace(go.Pie(labels=labels业务线, values=list(实际业务线pie['实际人天']), name="实际"), 1, 1)
    fig业务线pie.add_trace(go.Pie(labels=labels业务线, values=list(理论业务线pie['理论人天']), name="理论"), 1, 2)
    fig业务线pie.update_traces(hole=.4, hoverinfo="label+percent+name")
    fig业务线pie.update_traces(textposition='inside')
    fig业务线pie.update_layout(uniformtext_minsize=15, uniformtext_mode='hide',
                               title_text="部门总工时",
                               annotations=[dict(text='实际', x=0.205, y=0.5, font_size=20, showarrow=False),
                                            dict(text='理论', x=0.795, y=0.5, font_size=20, showarrow=False)])
    return fig业务线pie


def fig岗位pie():
    labels岗位 = list(实际岗位pie['实际人天'].keys())
    fig岗位pie = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])
    fig岗位pie.add_trace(go.Pie(labels=labels岗位, values=list(实际岗位pie['实际人天']), name="实际"), 1, 1)
    fig岗位pie.add_trace(go.Pie(labels=labels岗位, values=list(理论岗位pie['理论人天']), name="理论"), 1, 2)
    fig岗位pie.update_traces(hole=.4, hoverinfo="label+percent+name")
    fig岗位pie.update_traces(textposition='inside')
    fig岗位pie.update_layout(uniformtext_minsize=15, uniformtext_mode='hide',
                               title_text="岗位总工时",
                               annotations=[dict(text='实际', x=0.205, y=0.5, font_size=20, showarrow=False),
                                            dict(text='理论', x=0.795, y=0.5, font_size=20, showarrow=False)])
    return fig岗位pie



def fig员工部门员工组():
    fig员工部门员工组 = px.bar(理论实际业务线汇总, x="工时类别", y="总工时", facet_col="员工所属部门", color="员工组")
    fig员工部门员工组.update_layout(title='部门员工组工时', yaxis_title='总工时/小时')
    fig员工部门员工组.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    return fig员工部门员工组


def fig历史实际人均人天():
    fig历史实际人均人天 = px.line(all_actual_days, x="月份", y=all_actual_days.columns,
              # hover_data={"月份": "x"},
              title='部门实际人均人天趋势',
            )
    fig历史实际人均人天.update_layout(yaxis_title='实际人均人天',template='plotly_white',legend_title_text='业务线')
    return fig历史实际人均人天


def fig历史实际人均人天_irdc():
    fig历史实际人均人天_irdc = px.line(all_actual_days[['月份','海外研发中心']], x="月份", y=all_actual_days[['月份','海外研发中心']].columns,
              # hover_data={"月份": "x"},
              title='部门实际人均人天趋势',
            )
    fig历史实际人均人天_irdc.update_layout(yaxis_title='实际人均人天',template='plotly_white', legend_title_text='IRDC')
    return fig历史实际人均人天_irdc


def fig历史理论填报率():
    fig历史理论填报率 = px.line(all_logic_percentage, x="月份", y=all_logic_percentage.columns,
              # hover_data={"月份": "|%B, %Y"},
              title='部门填报率')
    fig历史理论填报率.update_layout(yaxis_title='理论填报率',template='plotly_white', legend_title_text='业务线')
    return fig历史理论填报率


def fig历史理论填报率_irdc():
    fig历史理论填报率_irdc = px.line(all_logic_percentage[['月份','海外研发中心']], x="月份", y=all_logic_percentage[['月份','海外研发中心']].columns,
              # hover_data={"月份": "|%B, %Y"},
              title='部门填报率')
    fig历史理论填报率_irdc.update_layout(yaxis_title='理论填报率', template='plotly_white',legend_title_text='IRDC')
    return fig历史理论填报率_irdc


def fig全量实际vs理论人天():
    fig全量实际vs理论人天 = px.scatter(cur_mon_staff, x="实际人天", y="理论人天", color="业务线",
                 size='实际人天', hover_data=['员工姓名'])
    fig全量实际vs理论人天.update_layout(
        title='员工"实际人天"v."理论人天"by业务线',
        xaxis=dict(
            title='实际人天',
            gridcolor='white',
    #         type='log',
            gridwidth=2,
        ),
        yaxis=dict(
            title='理论人天',
            gridcolor='white',
            gridwidth=2,
        ),
    )
    return fig全量实际vs理论人天


def fig理论填报分布():
    理论填报filterData = cur_mon_staff[['员工姓名', '员工组', '员工所属部门', '实际人天', '理论人天', '理论填报率', '理论填报', '岗位名称']]
    fig理论填报分布 = px.pie(理论填报filterData, values=理论填报filterData['理论填报'].value_counts().values,
                             names=理论填报filterData['理论填报'].value_counts().index)
    # fig理论填报分布.update_traces(hoverinfo='label+percent', textinfo='value')
    fig理论填报分布.update_layout(
        title='理论填报情况',
    )
    return fig理论填报分布

def fig未填工时分布():
    未填工时filterData = readData(本月未填工时名单())
    fig未填工时分布 = px.pie(未填工时filterData, values=未填工时filterData['员工所属部门'].value_counts().values,
                             names=未填工时filterData['员工所属部门'].value_counts().index)
    fig未填工时分布.update_layout(
        title='未填工时情况',
    )
    return fig未填工时分布



def figWBS部门pie():
    labelsWBS = list(实际部门wbspie['实际人天'].keys())
    figWBSpie = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])
    figWBSpie.add_trace(go.Pie(labels=labelsWBS, values=list(实际部门wbspie['实际人天']), name="实际"), 1, 1)
    figWBSpie.add_trace(go.Pie(labels=labelsWBS, values=list(预估部门wbspie['预估人天']), name="预估"), 1, 2)
    figWBSpie.update_traces(hole=.4, hoverinfo="label+percent+name")
    figWBSpie.update_traces(textposition='inside')
    figWBSpie.update_layout(uniformtext_minsize=15, uniformtext_mode='hide',
                               title_text="WBS部门总工时",
                               annotations=[dict(text='实际', x=0.205, y=0.5, font_size=20, showarrow=False),
                                            dict(text='预估', x=0.795, y=0.5, font_size=20, showarrow=False)])
    return figWBSpie


def figWBS类型pie():
    labelsWBS = list(实际类型wbspie['实际人天'].keys())
    figWBSpie = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])
    figWBSpie.add_trace(go.Pie(labels=labelsWBS, values=list(实际类型wbspie['实际人天']), name="实际"), 1, 1)
    figWBSpie.add_trace(go.Pie(labels=labelsWBS, values=list(预估类型wbspie['预估人天']), name="预估"), 1, 2)
    figWBSpie.update_traces(hole=.4, hoverinfo="label+percent+name")
    figWBSpie.update_traces(textposition='inside')
    figWBSpie.update_layout(uniformtext_minsize=15, uniformtext_mode='hide',
                               title_text="WBS类型总工时",
                               annotations=[dict(text='实际', x=0.205, y=0.5, font_size=20, showarrow=False),
                                            dict(text='预估', x=0.795, y=0.5, font_size=20, showarrow=False)])
    return figWBSpie


def figWBS预估填报分布():
    理论填报filterData = readData(本月WBS维度())[['WBS所属部门', '项目编号', '项目名称', 'WBS类型', 'PM姓名', '实际人天', '预估人天','预估填报率','预估填报']]
    fig理论填报分布 = px.pie(理论填报filterData, values=理论填报filterData['预估填报'].value_counts().values,
                             names=理论填报filterData['预估填报'].value_counts().index)
    # fig理论填报分布.update_traces(hoverinfo='label+percent', textinfo='value')
    fig理论填报分布.update_layout(
        title='实际WBS填报情况',
    )
    return fig理论填报分布

def figWBS预估填报异常部门分布():
    fig理论填报分布 = px.pie(logic_rate_abnormal_tb_WBS(), values=logic_rate_abnormal_tb_WBS()['WBS所属部门'].value_counts().values,
                             names=logic_rate_abnormal_tb_WBS()['WBS所属部门'].value_counts().index)
    # fig理论填报分布.update_traces(hoverinfo='label+percent', textinfo='value')
    fig理论填报分布.update_layout(
        title='WBS填报异常部门情况',
    )
    return fig理论填报分布

def figWBStop5填报分布():
    fig理论填报分布 = px.pie(wbs_top5_distribution(), values='实际人天',
                             names='Rate')
    fig理论填报分布.update_layout(
        title='Top5 WBS实际人天占比情况',
    )
    return fig理论填报分布


def figWBS预估无实际分布():
    未填报filterData = est_no_act_df()
    fig理论填报分布 = px.pie(未填报filterData, values=未填报filterData['WBS所属部门'].value_counts().values,
                             names=未填报filterData['WBS所属部门'].value_counts().index)
    # fig理论填报分布.update_traces(hoverinfo='label+percent', textinfo='value')
    fig理论填报分布.update_layout(
        title='预估并未实际填写WBS情况',
    )
    return fig理论填报分布

def figWBS实际未预估填报分布():
    未填报filterData = act_no_est_df()
    fig理论填报分布 = px.pie(未填报filterData, values=未填报filterData['WBS所属部门'].value_counts().values,
                             names=未填报filterData['WBS所属部门'].value_counts().index)
    # fig理论填报分布.update_traces(hoverinfo='label+percent', textinfo='value')
    fig理论填报分布.update_layout(
        title='实际填写并未预估WBS情况',
    )
    return fig理论填报分布

def figWBS连续预估2月未填写分布():
    fig理论填报分布 = px.pie(est_twice_wbs(), values=est_twice_wbs()['WBS所属部门'].value_counts().values,
                             names=est_twice_wbs()['WBS所属部门'].value_counts().index)
    # fig理论填报分布.update_traces(hoverinfo='label+percent', textinfo='value')
    fig理论填报分布.update_layout(
        title='连续两月预估无实际填写WBS情况',
    )
    return fig理论填报分布

def figWBS超过1年分布():
    fig未填工时分布 = px.pie(get_more_than1yr_wbs(), values=get_more_than1yr_wbs()['WBS所属部门'].value_counts().values,
                             names=get_more_than1yr_wbs()['WBS所属部门'].value_counts().index)
    fig未填工时分布.update_layout(
        title='建立超过1年WBS情况',
    )
    return fig未填工时分布

def figWBS部门Top5():
    figWBS部门Top5 = go.Figure()
    data = wbs_top5_actual()
    figWBS部门Top5.add_bar(x=list(data.Rate)
                                , y=list(data.实际人天)
                                , name="实际人天")
    figWBS部门Top5.add_bar(x=list(data.Rate)
                                , y=list(data.预估人天)
                                , name="预估人天")
    figWBS部门Top5.update_layout(title='WBS项目TOP5实际工时', template='plotly_white', yaxis_title='总工时/小时',)
    return figWBS部门Top5


def fig历史WBS类型():
    fig历史WBS类型 = px.line(readData(历史WBS类型实际人天()), x="月份", y=readData(历史WBS类型实际人天()).columns,
              title='WBS类型实际人天趋势',)
    fig历史WBS类型.update_layout(yaxis_title='实际总人天',template='plotly_white',legend_title_text='WBS类型')
    return fig历史WBS类型

def fig历史gpu使用():
    fig历史gpu使用 = px.line(clean_gpu_avg_usage(), x="日期",  y='使用率', color='分区',
              title='GPU历史使用情况',template='plotly_white')
    return fig历史gpu使用

def fig历史gpu使用具体时间点(time):
    data = clean_gpu_usage()[clean_gpu_usage()['Time'] == time]
    fig历史gpu使用 = px.line(data, x="日期",  y='使用率', color='分区',
              title='GPU历史使用情况',template='plotly_white')
    return fig历史gpu使用

