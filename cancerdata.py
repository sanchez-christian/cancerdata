from flask import Flask, url_for, render_template, Markup
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/numbers")
def render_page1():
    return render_template('numbers.html', numbers = format_dict_as_graph_points())

@app.route("/rates")
def render_page2():
    return render_template('rates.html')
    


def format_dict_as_graph_points():
    with open('cancer.json') as numbers_data:
        data = json.load(numbers_data)
    graph_points = ""
#    state = request.args['State']
#    num = 0
    for s in data:
#        if s["State"] == state:
#            num = s["Numbers"]
        #{ label: "India", y: 7.1 },
        graph_points = graph_points + Markup('{label: "' + s["State"] + '" , y: ' + str(s["Total"]["Number"]) + '},' )
    graph_points = graph_points[:-1] #this will remove the last comma and space
    print(graph_points)
    return graph_points #will take it and send it back to line 12

if __name__=="__main__":
    app.run(debug=True)