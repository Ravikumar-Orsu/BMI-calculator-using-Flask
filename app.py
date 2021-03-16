from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    bmi=""
    if request.method=="POST" and 'weight' in request.form:
        weight=float(request.form.get('weight'))
        height=float(request.form.get('height'))
        bmi=round(weight / (height * height), 2)


    return render_template("index.html",bmi=bmi)
app.debug=True
app.run()
app.run(debug=True)