from pyecharts import options as opts
from pyecharts.charts import Map

cityMap_chart = Map()
cityMap_chart.add("吉林市", [("昌邑", 1)], "吉林")
cityMap_chart.render("吉林市"+".html")