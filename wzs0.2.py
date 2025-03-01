from pyecharts import options as opts
from pyecharts.charts import Map
import pandas as pd
import os,sys
import tkinter as tk
from tkinter.filedialog import askopenfilename
from cefpython3 import cefpython as cef

# settings = {
#     'resources_dir_path': '.\\resource',  # 设置资源文件路径
# }
# cef.Initialize(settings=settings)

root = tk.Tk()
root.withdraw()  # 隐藏主窗口
file_path = askopenfilename(
    title="选择业务数据文件",
    filetypes=[("Excel 文件", "*.xlsx *.xls"), ("所有文件", "*.*")]  # 文件类型过滤
)

# 检查用户是否选择了文件
if file_path:
    df = pd.read_excel(file_path,engine='openpyxl')
    print("文件读取成功！")
else:
    print("未选择文件。")


#创建吉林地图
def jilin_map():

    data = df.groupby('承保市')[['赔款', '保费']].sum().reset_index()
    data['城市赔付率'] = (data['赔款'] / data['保费']).round(4)*100
    city_pfv = data[['承保市', '城市赔付率']].values.tolist()
    city_pk = data[['承保市', '赔款']].values.tolist()
    city_bf=data[['承保市', '保费']].values.tolist()
    
    # 创建吉林地图
    jilin_chart = Map(init_opts=opts.InitOpts(chart_id='jilin_map'))
    jilin_chart.add("吉林地图", city_pfv, "吉林")
    
    jilin_chart.set_global_opts(
        title_opts=opts.TitleOpts(title="吉林省"),
        visualmap_opts=opts.VisualMapOpts(max_=100, min_=0),
        tooltip_opts=opts.TooltipOpts(
            formatter='赔付率：{c}%'
        )
    )
    
    jilin_chart.add_js_funcs('''
        chart_jilin_map.on('click', function (params) {
            var cityName = params.name;
            window.location.href = cityName + '_map.html';                  
        });               
    ''')

    jilin_chart.render("jilin_map.html")
jilin_map()


# 生成城市地图
def city_map(city):
    cityMap_chart = Map()
    cityMap_chart.add(city, [(city, 1)], city)
    cityMap_chart.set_global_opts(
        title_opts=opts.TitleOpts(title=f"{city}地图"),
    )
    cityMap_chart.render(f"{city}"+"市"+"_map.html")
