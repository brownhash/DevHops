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

@app.route("/load")
def load():
    f=open("count.txt","r")
    r=f.read()
    counter=int(r)
    f.close()
    return (counter)

@app.route('/password_gen')
def password_gen():
    import random as rand
    l = ["#", "*"]
    l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
    l2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']
    l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    a = rand.randint(2, 3)
    b = rand.randint(2, 3)
    c = rand.randint(1, 2)
    rand.shuffle(l1)
    rand.shuffle(l2)
    rand.shuffle(l3)
    rand.shuffle(l)
    s1 = ""
    s = ""
    for i in range(0, a):
        s += str(l2[i])
    for i in range(0, a):
        s += str(l3[i])
    for i in range(0, a):
        s += str(l1[i])
    for i in l:
        s += str(i)
    rand.shuffle(l2)
    for i in range(0, c):
        s1 += str(l2[i])

    result = list(s)
    rand.shuffle(result)
    s2 = ""
    for i in result:
        s2 += i
    return(s1 + s2)

if __name__ == "__main__":
    app.run(debug=True)
