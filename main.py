from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/result',methods = ['POST'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

@app.route('/terminal')
def terminal():
    return render_template("terminal.html",result = result)

@app.route('/term',methods = ['POST'])
def term():
   if request.method == 'POST':
       sudo_com="sudo -p "
       result = request.form
       sudo=result.get("sudo")
       password=str(result.get("password"))
       command=str(result.get("command"))
       if(sudo == "sudoyes"):
           sudo_com+=password
           sudo_command=sudo_com+" "+command
           command=sudo_command
       import os
       term_result=os.popen(command).readlines()
       s=""
       for i in term_result:
           s+=str(i)+" | "
       return (s)

if __name__ == "__main__":
    app.run(debug=True)
