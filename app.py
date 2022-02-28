from  flask import Flask, jsonify
import json, random, string
from lib2to3.pygram import Symbols

length = int(10) 

from config import PORT

app = Flask(__name__)  
app.config["DEBUG"] = True                   

upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

ALPHABETS = upper
SYMBOLS = symbols
NUMBER = num
ALL = upper + symbols + num

@app.route('/')
def home():
    return '''
            <!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="UTF-8">
      <h1 class="project-name">Welcome to Captcha API 🔑👨‍💻🌐</h1>
      <h2 class="project-tagline">An API returns random Captcha</h2
<h2 id="usage">Usage:</h2>
<ul>
<p>These Are The Endpoints Of The API</p>
  <li><code class="language-plaintext highlighter-rouge">/all</code> will return Captcha with mix of ALPHABETS,SYMBOLS,NUMBERS at length of 10</li>
  <li><code class="language-plaintext highlighter-rouge">/alphabets</code> will return Captcha filled with ALPHABETS only</li>
      <li><code class="language-plaintext highlighter-rouge">/numbers</code> will return Captcha filled with NUMBERS only</li>
    <li><code class="language-plaintext highlighter-rouge">/symbols</code> will return Captcha filled with SYMBOLS only</li>
</ul>
    </main>
  </body>
</html>
 '''

@app.route('/alphabets', methods=['GET'])
def alphabets():
    alphabets_list = []
    temp = random.sample(ALPHABETS,length)
    password = "".join(temp)
    Alpha = {
    'Cache': password,
    }
    alphabets_list.append(Alpha)
    New_List = json.dumps(alphabets_list, indent =2)
    with open("baby.json", "w", encoding="utf-8") as file:
      file.write(str(New_List)) 
    return jsonify(alphabets_list)

@app.route('/symbols', methods=['GET'])
def symbol():
    symbols_list = []
    temp = random.sample(SYMBOLS,length)
    password = "".join(temp)
    Symba = {
    'Cache': password,
    }
    symbols_list.append(Symba)
    New_List = json.dumps(symbols_list, indent =2)
    with open("baby.json", "w", encoding="utf-8") as file:
      file.write(str(New_List)) 
    return jsonify(symbols_list)

@app.route('/numbers', methods=['GET'])
def numbers():
    numbers_list = []
    temp = random.sample(NUMBER,length)
    password = "".join(temp)
    temp = random.sample(NUMBER,length)
    password = "".join(temp)
    Numba = {
    'Cache': password,
    }
    numbers_list.append(Numba)
    New_List = json.dumps(numbers_list, indent =2)
    with open("baby.json", "w", encoding="utf-8") as file:
      file.write(str(New_List)) 
    return jsonify(numbers_list)
  

@app.route('/all', methods=['GET'])
def all():
    all_list = []
    temp = random.sample(ALL,length)
    password = "".join(temp)
    temp = random.sample(ALL,length)
    password = "".join(temp)
    All = {
    'Cache': password,
    }
    all_list.append(All)
    New_List = json.dumps(all_list, indent =2)
    with open("baby.json", "w", encoding="utf-8") as file:
      file.write(str(New_List)) 
    return jsonify(all_list)
   

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port= PORT)
