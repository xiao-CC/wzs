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
    city_data=df.groupby('承保市')[['赔款'].sum/['保费'].sum()]
    
    # 创建吉林地图
    map_chart = Map(init_opts=opts.InitOpts(chart_id='jilin_map'))
    map_chart.add("吉林", [list(z) for z in zip(city_data, [1]*len(city_data))], "jilin")
    
    map_chart.set_global_opts(
        title_opts=opts.TitleOpts(title="吉林省"),
    )
    
    map_chart.add_js_funcs('''
        jilin_map.on('click', function (params) {
            var city = params.name;
            window.location.href = cityName + '_map.html';
        });               
    ''')
    map_chart.render("jilin_map.html")
jilin_map()


# 生成城市地图
def city_map(city):
    map_chart = Map()
    map_chart.add(city, [(city, 1)], city)
    map_chart.set_global_opts(
        title_opts=opts.TitleOpts(title=f"{city}地图"),
    )
    map_chart.render(f"{city}"+"市"+"_map.html")

# 生成某省地图（例如北京）
city_map("长春农安")
