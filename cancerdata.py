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
    return render_template('rates.html', rates = format_dict_as_graph_points2())
    


def format_dict_as_graph_points():
    with open('cancer.json') as numbers_data:
        num = json.load(numbers_data)
    graph_numbers = ""
#    state = request.args['State']
#    num = 0
    for s in num:
#        if s["State"] == state:
#            num = s["Numbers"]
        #{ label: "India", y: 7.1 },
        graph_numbers = graph_numbers + Markup('{label: "' + s["State"] + '" , y: ' + str(s["Total"]["Number"]) + '},' )
    graph_numbers = graph_numbers[:-1] #this will remove the last comma and space
    print(graph_numbers)
    return graph_numbers #will take it and send it back to line 12

def format_dict_as_graph_points2():
    with open('cancer.json') as rates_data:
        rate = json.load(rates_data)
    graph_rates = ""
    for r in rate:
        graph_rates = graph_rates + Markup('{label: "' + r["State"] + '" , y: ' + str(r["Total"]["Rate"]) + '},' )
    graph_rates = graph_rates[:-1] #this will remove the last comma and space
    print(graph_rates)
    return graph_rates #will take it and send it back to line 12

if __name__=="__main__":
    app.run(debug=True)