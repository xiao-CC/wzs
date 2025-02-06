from pyecharts import options as opts
from pyecharts.charts import Map
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename


# 弹出文件选择对话框
file_path = askopenfilename(
    title="选择业务数据文件",  # 对话框标题
    filetypes=[("Excel 文件", "*.xlsx *.xls"), ("所有文件", "*.*")]  # 文件类型过滤
)

# 检查用户是否选择了文件
if file_path:
    # 读取 Excel 文件
    df = pd.read_excel(file_path)
    print("文件读取成功！")
else:
    print("未选择文件。")



# 创建中国地图
def jilin_map():

    city_data = df.groupby('承保市')[['赔款', '保费']].sum().reset_index()
    city_data['城市赔付率'] = city_data['赔款'] / city_data['保费']
    city_data_list=city_data[['承保市','城市赔付率']].values.tolist()
    
    # 创建吉林地图
    jilin_chart = Map(init_opts=opts.InitOpts(chart_id='jilin_map'))
    # jilin_chart = Map()
    jilin_chart.add("吉林地图", city_data_list, "吉林")
    jilin_chart.set_global_opts(
        title_opts=opts.TitleOpts(title="吉林省"),
        visualmap_opts=opts.VisualMapOpts(max_=1, min_=0),
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
