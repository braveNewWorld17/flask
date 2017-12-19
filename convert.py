from flask import Flask
from flask import request
app = Flask(__name__)
 
html = """
<center>
<form action='/convert' method='POST'>
{number_only}<br>
Pound:<input type='text' name='pound' value='{pound}'> = <span id='kilo'>{kilo}</span><br>
<input type='submit' value='Submit'>
</form>
"""

@app.route("/")
def index():
    lb = 0
    kg = 0
    return html.format(pound=lb, kilo=kg, number_only='')

@app.route("/convert", methods=['POST'])
def convert():
   lb = 0
   kg = 0
   try:
      lb = float(request.form["pound"])
      kg = lb * 0.45359237
   except ValueError:
      return html.format(pound=lb, kilo=kg, number_only='Please, Input only Number')

   return html.format(pound=lb, kilo=kg, number_only='')

 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


