from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
app=Flask("__main__")

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///site.db"
app.config["SCRECT_KEY"]="4546845684653"

db=SQLAlchemy(app)

class Reg(db.Model):
     id=db.Column(db.Integer,primary_key=True)
     name=db.Column(db.String(50),nullable=True)
     email=db.Column(db.String(150),unique=True,nullable=True)
     phone=db.Column(db.String(10),unique=True,nullable=True)
     address=db.Column(db.String(200),nullable=True)
     city=db.Column(db.String(50),nullable=True)
     pincode=db.Column(db.String(6),nullable=True)
     eventName=db.Column(db.String(50),nullable=True)
     funRange=db.Column(db.String(50),nullable=True)
     doe=db.Column(db.String(50),nullable=True)
     rom=db.Column(db.String(50))
     menu=db.Column(db.String(50))
     photo=db.Column(db.String(50))
     theme=db.Column(db.String(100))
     venue=db.Column(db.String(100))
     parking=db.Column(db.String(10))
     entertainment=db.Column(db.String(50))
     waiter=db.Column(db.String(50))
     ac=db.Column(db.String(5))
     dj=db.Column(db.String(5))
     invitations=db.Column(db.String(50))
     invitation_quantity=db.Column(db.Integer)
     hotel_rooms=db.Column(db.String(10))
     hotel_rooms_no=db.Column(db.Integer)
     pay=db.Column(db.String(10)) 
     
     def __repr__(self): 
         return f"User('{self.name}','{self.email}','{self.phone},'{self.eventName}','{self.funRange}','{self.doe}','{self.rom}','{self.menu}','{self.photo}','{self.theme}','{self.venue}','{self.ac}','{self.parking}','{self.entertainment}','{self.waiter}','{self.dj}','{self.invitation_quantity}','{self.hotel_rooms_no}','{self.pay}')"     
@app.route("/")
@app.route("/home")
def home():
    return render_template("tab.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


@app.route("/registration",methods=["GET","POST"])
def registrationform():
    if request.method == "POST":
                 name = request.form.get("name")
                 age= request.form.get("age")
                 dob=request.form.get("dob")
                 ph =request.form.get("phoneNumber")
                 address=request.form.get("aadress")
                 city=request.form.get("city")
                 pincode=request.form.get("pincode")
                 email=request.form.get("email")
                 print(name,age,dob,ph,city,pincode,email,address)
                 eventName=request.form.get("event")
                 funRange=request.form.get("quant1") 
                 rom=request.form.get("rom")
                 doe=request.form.get("doe")
                 menu=request.form.get("menu")
                 photo=request.form.get("photo")
                 theme=request.form.get("theme")
                 venue=request.form.get("venue")
                 parking=request.form.get("parking")
                 entertainment=request.form.get("entertainment")
                 waiters=request.form.get("waiters")
                 ac=request.form.get("ac")
                 dj=request.form.get("dj")
                 invitations=request.form.get("invitations")
                 invitation_quantity=request.form.get("invitation-quantity")
                 hotel_rooms=request.form.get("hotel-rooms")
                 hotel_rooms_no=request.form.get("hotel-quantity")
                 pay=request.form.get("payment")
                 user=Reg(name=name,email=email,phone=ph,address=address,city=city,pincode=pincode,eventName=eventName,funRange=funRange,rom=rom,doe=doe,menu=menu,photo=photo,theme=theme,venue=venue,parking=parking,entertainment=entertainment,waiter=waiters,ac=ac,dj=dj,invitations=invitations,invitation_quantity=invitation_quantity,hotel_rooms=hotel_rooms,hotel_rooms_no=hotel_rooms_no,pay=pay)
                 print(user)
                 db.session.add(user)
                 print(user)
                 db.session.commit()
                 return redirect(url_for("home"))
    return render_template("registrationform.html")
@app.route("/service")
def services():
    return render_template("servicepage.html")

@app.route("/works")
def works():
    return render_template("workspage.html")
@app.route("/samphome")
def samphome():
   return render_template("samphome.html")
@app.route("/about")
def about():
     return render_template("about.html")
@app.route("/hover")
def hover():
     return render_template("hover.html")

@app.route("/login" ,methods=["GET","POST"])
def login():
    if request.method == "POST":
            id=request.form.get("id")
            password=request.form.get("password")
            if password=="helloWorld":
                 return redirect(url_for("eventmanage"))
    return render_template("login.html")

@app.route("/eventmanage")
def eventmanage():
     return render_template("tab.html")

@app.route("/mcombo")
def mcombo():
     return render_template("mcombo.html")


@app.route("/bcombo")
def bcombo():
     return render_template("bcombo.html")
@app.route("/costumer")
def coustomer():
     x=Reg.query.all()
     return  render_template("customerList.html",l=x)
     

if __name__ =="__main__":
    app.run(debug=True)