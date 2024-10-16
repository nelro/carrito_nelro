from flask import Flask, render_template,request,session,redirect,url_for
app = Flask(__name__)

app.secret_key="nelro"

@app.route("/")
def carrito():

    if "lista" not in session:
        session["lista"] = []
    return  render_template("index.html", lista=session["lista"])

@app.route("/procesar", methods=["post"])
def procesar():
    producto = request.form.get("producto")
    if "lista" in session and producto:
        #producto adicionando a la lista
        session["lista"].append(producto)
        #aseguramos que la secion a sido modificada
        session.modified =  True
    return redirect(url_for("carrito"))

@app.route("/vaciar", methods=["get"])
def vaciar():
    #elimina la sesion de las lista 
    session.pop("lista",None)
    return redirect(url_for("carrito"))


if __name__ == "__main__":
   app.run(debug=True)
