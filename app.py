from flask import Flask, render_template, request
import ast
app = Flask(__name__)


twochar = {
    "a": "ा",
    "b": "ब",
    "c": "स",
    "d": "ड",
    "e": "े",
    "f": "फ",
    "g": "जी",
    "h": "ह",
    "i": "इ",
    "j": "ज",
    "k": "क",
    "l": "ल",
    "m": "म",
    "n": "न",
    "o": "ु",
    "p": "प",
    "r": "र",
    "s": "श",
    "t": "ट",
    "y": "य",
    "u": "ू",
    "w": "व",
    "v": "भ",
    "z": "ज"
}

def transString(string, reverse=0):

 
    for k, v in twochar.items():

      if not reverse:
            string = string.replace(v, k)
      else:
            string = string.replace(k, v)

    return string
 

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/predict', methods = ['POST', "GET"])
def predict():
    
    if request.method == 'POST':
        print(request.form.get('NewYork'))
        try:
            NewYork = request.form['NewYork']
            NewYorkstrip = NewYork.strip()
            NewYorkLower = NewYorkstrip.lower()
            valueresult  = transString(NewYorkLower, 1)
        except ValueError:
            return "Please check if the values are entered correctly"
    return render_template('home.html', prediction = valueresult )

if __name__ == "__main__":
    app.run()