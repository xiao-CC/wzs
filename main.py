from pyecharts import options as opts
from pyecharts.charts import Map

# 创建中国地图
def china_map():
    provinces = ['北京', '天津', '上海', '重庆', '河北', '河南', '云南', '辽宁', '黑龙江', '湖南', '安徽', '山东', '新疆', '江苏', '浙江', '江西', '湖北', '广西', '甘肃', '山西', '内蒙古', '陕西', '吉林', '福建', '贵州', '广东', '青海', '西藏', '四川', '宁夏', '海南', '台湾', '香港', '澳门']
    
    # 创建中国地图
    map_chart = Map(init_opts=opts.InitOpts(chart_id='china_map'))
    map_chart.add("中国", [list(z) for z in zip(provinces, [1]*len(provinces))], "china")
    
    map_chart.set_global_opts(
        title_opts=opts.TitleOpts(title="中国地图"),
        visualmap_opts=opts.VisualMapOpts(is_show=False),
    )
    
    map_chart.add_js_funcs('''
        chart_china_map.on('click', function (params) {
            var provinceName = params.name;
            window.location.href = provinceName + '_map.html';
        });               
    ''')
    map_chart.render("china_map.html")
china_map()


# 生成具体省份地图（例如北京）
def province_map(province):
    map_chart = Map()
    map_chart.add(province, [(province, 1)], province)
    map_chart.set_global_opts(
        title_opts=opts.TitleOpts(title=f"{province}地图"),
        visualmap_opts=opts.VisualMapOpts(is_show=False),
    )
    map_chart.render(f"{province}"+"市"+"_map.html")

# 生成某省地图（例如北京）
province_map("北京")
