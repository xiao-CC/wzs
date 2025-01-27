from pyecharts.charts import Map
from pyecharts import options as opts


# def create_province_map():
#     data_guangdong = [("广州市", 150), ("深圳市", 120), ("珠海市", 30)]
#     province_map = (
#         Map()
#         .add("业务量", data_guangdong, "广东")
#         .set_global_opts(
#             title_opts=opts.TitleOpts(title="业务量分布"),
#             visualmap_opts=opts.VisualMapOpts(min_=0, max_=150, range_=[0, 150]),
#         )
#     )
#     return province_map


def create_qu_map():
    data_guangdong = [("广州市", 150), ("深圳市", 120), ("珠海市", 30)]
    province_map = (
        Map()
        .add("业务量", data_guangdong, "长春")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="业务量分布"),
            visualmap_opts=opts.VisualMapOpts(min_=0, max_=150, range_=[0, 150]),
        )
    )
    return province_map
# 生成 HTML 文件
if __name__ == "__main__":
    chart = create_qu_map()
    chart.render("china_map.html")