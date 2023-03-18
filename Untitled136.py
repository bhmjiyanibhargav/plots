#!/usr/bin/env python
# coding: utf-8

# # question 01

# In[1]:


from bokeh.plotting import figure, output_file, show
output_file("my_plot.html")
p = figure(plot_width=400, plot_height=400, title="My Plot", x_axis_label="X", y_axis_label="Y")
p.line(x_data, y_data)
show(p)


# # question 02
Q2. What are glyphs in Bokeh, and how can you add them to a Bokeh plot? Explain with an example.
# In[2]:


from bokeh.plotting import figure, output_file, show

# Define the data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Define the output file
output_file("my_plot.html")

# Create the figure object
p = figure(plot_width=400, plot_height=400)

# Add circles to the plot
p.circle(x, y, size=10, color="navy", alpha=0.5)

# Display the plot
show(p)

In this example, we first define two lists of data points x and y. Then, we define the output file where the plot will be saved using output_file. Next, we create a new figure object with the desired size and no title or axis labels. Finally, we add circles to the plot using the circle function, and set the size, color, and transparency of the circles using the size, color, and alpha arguments.

Bokeh also offers a range of other customization options for glyphs, such as changing the line style, adding hover tooltips, and using categorical data.
# # question 03
How can you customize the appearance of a Bokeh plot, including the axes, title, and legendChange the title and axis labels: You can set the title of the plot and the labels for the x and y axes using the title, x_axis_label, and y_axis_label attributes of the figure object.
# In[4]:


p = figure(title="My Plot", x_axis_label="X Axis", y_axis_label="Y Axis")

Customize the tick marks and gridlines: You can customize the tick marks and gridlines of the plot using the xaxis, yaxis, xgrid, and ygrid attributes of the figure object. For example, you can set the number of tick marks on the x-axis using xaxis[0].ticker.num_minor_ticks = 4.
# In[5]:


p.xaxis[0].ticker.num_minor_ticks = 4
p.ygrid.grid_line_color = 'gray'

Change the color and style of the plot elements: You can set the color and style of the plot elements such as lines, markers, and text using the line_color, line_width, marker, and text_color attributes of the plot elements.
# In[6]:


p.line(x, y, line_width=2, line_color='red')
p.circle(x, y, size=10, color="navy", alpha=0.5)
p.text(x, y, text=["Point 1", "Point 2", "Point 3"], text_color="red")

Add a legend: You can add a legend to the plot using the legend attribute of the plot elements. You can set the location of the legend using the location argument.
# In[7]:


p.line(x1, y1, line_width=2, line_color='red', legend_label="Line 1")
p.line(x2, y2, line_width=2, line_color='blue', legend_label="Line 2")
p.legend.location = "top_left"


# # question 04
Q4. What is a Bokeh server, and how can you use it to create interactive plots that can be updated in
real time?
Bokeh server is a tool in Bokeh that allows creating interactive plots that can be updated in real time, through user interactions or streaming of data. A Bokeh server application runs on a server and can be accessed through a web browser.

To create a Bokeh server application, you can define a function or class that creates the plot and defines the interactive behavior. The function or class should also specify which properties of the plot can be updated in real time. Then, you can run the application with the bokeh serve command.

For example, let's say you have a scatter plot that shows the relationship between two variables, x and y, and you want to allow the user to adjust the color and size of the markers. You can create a Bokeh server application that defines the scatter plot and the interactive behavior as follows:
# In[8]:


from bokeh.plotting import figure
from bokeh.layouts import column
from bokeh.models import ColumnDataSource
from bokeh.server.server import Server
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler

def make_plot():
    source = ColumnDataSource(data=dict(x=[1, 2, 3], y=[4, 5, 6]))
    plot = figure(title="Scatter Plot", x_axis_label='X', y_axis_label='Y')
    plot.circle('x', 'y', source=source, size=10, color='blue')
    return plot

def modify_doc(doc):
    plot = make_plot()
    controls = column([Select(options=['red', 'green', 'blue'], value='blue', title='Color'),
                       Slider(start=5, end=20, step=1, value=10, title='Size')])
    
    def update(attrname, old, new):
        if controls.children[0].value == 'red':
            color = 'red'
        elif controls.children[0].value == 'green':
            color = 'green'
        else:
            color = 'blue'
        size = controls.children[1].value
        plot.circle('x', 'y', source=source, size=size, color=color)
    
    for control in controls.children:
        control.on_change('value', update)
    
    doc.add_root(column(plot, controls))

handler = FunctionHandler(modify_doc)
app = Application(handler)
server = Server({'/': app})
server.start()


# # question 05
How can you embed a Bokeh plot into a web page or dashboard using Flask or Django?
To embed a Bokeh plot into a web page or dashboard using Flask or Django, you can follow these steps:

Create a Bokeh plot as usual using Python code.
In Flask, create a route that renders an HTML template containing the Bokeh plot.
In the HTML template, use the {{ script }} and {{ div }} variables provided by the bokeh.embed module to embed the Bokeh plot into the page.
In Flask, render the HTML template using the bokeh.embed.components function to generate the script and div variables for the Bokeh plot.
In Django, you can use a similar approach, but instead of a Flask route, you would create a Django view function that returns an HTTP response containing the HTML template.
Here is an example of embedding a Bokeh plot into a Flask app:
# In[ ]:


from flask import Flask, render_template
from bokeh.plotting import figure
from bokeh.embed import components

app = Flask(__name__)

@app.route('/')
def index():
    # create a Bokeh plot
    plot = figure()
    plot.line([1, 2, 3], [4, 5, 6])

    # generate the script and div components for the plot
    script, div = components(plot)

    # render the HTML template with the plot embedded
    return render_template('index.html', script=script, div=div)

if __name__ == '__main__':
    app.run()


# In[ ]:




