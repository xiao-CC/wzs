from pyecharts.charts import Map
from pyecharts import options as opts

# 创建一个简单的中国地图
def create_china_map():
    data = [("松原", 100), ("长春, 200), ("广东", 300)]
    map_chart = (
        Map()
        .add("业务量", data, "吉林")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="业务量分布"),
            visualmap_opts=opts.VisualMapOpts(max_=300),
        )
    )
    return map_chart

def create_province_map(province):
    data_guangdong = [("广州", 150), ("深圳", 120), ("珠海", 30)]
    province_map = (
        Map()
        .add("业务量", data_guangdong, "广东")
        .set_global_opts(
            title_opts=opts.TitleOpts(title=f"{province}业务量分布"),
            visualmap_opts=opts.VisualMapOpts(max_=150),
        )
    )
    return province_map

# 生成 HTML 文件
if __name__ == "__main__":
    chart = create_china_map()
    chart.render("china_map.html")