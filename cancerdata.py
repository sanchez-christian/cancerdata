from flask import Flask, url_for, render_template, Markup
from flask import request
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

@app.route("/ages")
def render_page3():
    if "state" not in request.args:
        return render_template('ages.html', ages_dropdown = dropdown())
    else:
        user_input = request.args["state"]
        return render_template('ages.html', ages = format_dict_as_graph_points3(), ages_dropdown = dropdown(), state = request.args["state"])
    


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
    return graph_numbers #will take it and send it back to line 13

def format_dict_as_graph_points2():
    with open('cancer.json') as rates_data:
        rate = json.load(rates_data)
    graph_rates = ""
    for r in rate:
        graph_rates = graph_rates + Markup('{label: "' + r["State"] + '" , y: ' + str(r["Total"]["Rate"]) + '},' )
    graph_rates = graph_rates[:-1] #this will remove the last comma and space
    print(graph_rates)
    return graph_rates #will take it and send it back to line 12

def format_dict_as_graph_points3():
    state_select = request.args["state"]
    with open('cancer.json') as ages_data:
        state = json.load(ages_data)
    output = ""
    for s in state:
        if s["State"] == state_select:
            for a in s["Rates"]["Age"]:
                output += Markup ('{label: "' + a + '" , y: ' + str(s["Rates"]["Age"][a]) + '},' )
    output = output[:-1]
    print(output)
    print(state_select)
    return output

def dropdown():
    with open('cancer.json') as ages_dropdown:
        states = json.load(ages_dropdown)
    options=""
    for s in states:
        options += Markup("<option value=\"" + s["State"] + "\">") #Use Markup so <, >, " are not escaped lt, gt, etc.
    return options

    
if __name__=="__main__":
    app.run(debug=True)