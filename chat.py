# importing Flask and other modules
from flask import Flask, request, render_template
 
# Flask constructor
app = Flask(__name__)

responses = []
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       msg = request.form.get("message") 
       responses.append(msg)
       print(responses)
    return render_template("session.html", responses=responses)
 
if __name__=='__main__':
   app.run()