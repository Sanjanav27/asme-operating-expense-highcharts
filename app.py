from flask import Flask,render_template, jsonify, request
import random
import json
import data



app  = Flask(__name__)
PORT = 3000

@app.route("/", methods=["GET","POST"])
def startpy():
    
    result = {

        "Greetings" : "Tactlabs welcomes you"
    }

    #return jsonify(result)
    return render_template("index.html") 

'''
http://0.0.0.0:3091/api/data


'''
@app.route("/api/data", methods=["GET"])
def api_get_data():

    result = data.get_data()

    # result_dict = {

    #     ''       : year,
    #     'pytorch'    : pytorch,
    #     'tensorFlow' : tensorFlow

    # }

    return jsonify(result)

@app.route("/api/add", methods=["GET"])
def api_add_data():

    Topics                 = request.values.get('Topics')
    Expenses             = request.values.get('Expenses')

    result = {
        'Topics'                  : Topics,
        'Expenses'                : Expenses
    }
    result_data = data.add_row(Topics, Expenses )

   

    return jsonify(result)








if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0",port = PORT)