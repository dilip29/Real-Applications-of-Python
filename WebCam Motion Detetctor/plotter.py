
from object_motion_detector import df
from bokeh.plotting import output_file,show,figure
from bokeh.models import HoverTool,ColumnDataSource



df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["Exit_string"]=df["Exit"].dt.strftime("%Y-%m-%d %H:%M:%S")
cf=ColumnDataSource(df)

f=figure(height=300,width=1000,title="Object motion graph",x_axis_type='datetime')



hover=HoverTool(tooltips=[("Start","@Start_string"),("Exit","@Exit_string")])
f.add_tools(hover)


f.quad(top=1,bottom=0,left="Start",right="Exit",source=cf)

f.yaxis.minor_tick_line_color=None

f.ygrid[0].ticker.desired_num_ticks=1

output_file("object_timestamp.html")

show(f)
