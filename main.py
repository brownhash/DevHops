from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

f=open("count.txt","w")
f.write("0")
f.close()

@app.route("/loadbalancer")
def loadbalancer():
    f=open("count.txt","r")
    r=f.read()
    counter=int(r)
    f.close()

    r_string="Simultaneous logins : "+str(counter)
    return(r_string)

@app.route("/login",methods = ['POST'])
def login():
    if request.method == 'POST':
       result = request.form
       user=result.get("username")
       passw=result.get("password")
       if(user=="admin" and passw=="root"):
           f=open("count.txt","r")
           r=f.read()
           counter=int(r)
           f.close()

           counter+=1

           f=open("count.txt","w")
           f.write(str(counter))
           f.close()
           if(counter < 3):
               return redirect("http://www.google.com")
           elif(counter > 2 and counter < 6):
               return redirect("http://www.facebook.com")
           else:
               return ("Server over loaded")
       else:
           return render_template("loginerror.html")

@app.route("/logout")
def logout():
    f=open("count.txt","r")
    r=f.read()
    counter=int(r)
    f.close()

    counter-=1

    f=open("count.txt","w")
    f.write(str(counter))
    f.close()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
