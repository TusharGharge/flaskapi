from flask import Flask, render_template,jsonify

app = Flask(__name__)

# index
@app.route('/')
def index():
    return "Hello"

# /me    
@app.route("/me", methods=["GET"])
def get_results():
    return "Dummy Result"
@app.route('/even/<int:n>')
def even(n):
    if(n%2==0):
        result={
            "number":n,
            "even":True,
            "server ip": "123.133.356.345",
        }
    else:
       result={
            "number":n,
            "even":"false",
            "server ip": "123.133.356.345",
        }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)