from flask import Flask, url_for, render_template

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/p1")
def render_page1():
    format_dict_as_graph_points()
    return render_template('numbers.html')
    


def format_dict_as_graph_points():
    with open('cancer.json') as numbers_data:
        graph_points = ""
    for key in data:
        #{ label: "India", y: 7.1 },
        graph_points = graph_points + Markup('{ y: ' + str(data[key]) + ', label: "' + key + '" }, ')
    graph_points = graph_points[:-2] #this will remove the last comma and space
    print(graph_points)

if __name__=="__main__":
    app.run(debug=False)