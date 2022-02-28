from flask import *
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
    temp = random.sample(ALPHABETS,length)
    password = "".join(temp)
    data_set = {'CAPTCHA': password}
    json_dump = json.dumps(data_set)
    return json_dump

@app.route('/symbols', methods=['GET'])
def symbol():
    temp = random.sample(SYMBOLS,length)
    password = "".join(temp)
    data_set = {'CAPTCHA': password}
    json_dump = json.dumps(data_set) 
    return json_dump

@app.route('/numbers', methods=['GET'])
def numbers():
    temp = random.sample(NUMBER,length)
    password = "".join(temp)
    data_set = {'CAPTCHA': password}
    json_dump = json.dumps(data_set) 
    return json_dump   

@app.route('/all', methods=['GET'])
def all():
    temp = random.sample(ALL,length)
    password = "".join(temp)
    data_set = {'CAPTCHA': password}
    json_dump = json.dumps(data_set)  
    return json_dump    

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port= PORT)
