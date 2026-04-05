from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ──────────────────────────────────────────
#  BASE DE DATOS FALSA  (lista en memoria)
#  Se reinicia cada vez que reinicias Flask
# ──────────────────────────────────────────
productos = [
    {"id": 1, "nombre": "cuadernoRayado",   "cantidad": 50, "precio": .50, "marca": "Norma"},
    {"id": 2, "nombre": "cuadernoCuadriculado",     "cantidad": 30, "precio": 0.40, "marca": "Marfil"},
    {"id": 3, "nombre": "cuadernoDobleLinea",   "cantidad": 20, "precio": 0.60, "marca": "Marfil"},
    {"id": 4, "nombre": "lapizNegro",   "cantidad": 10, "precio": 0.10, "marca": "Mongol"},
    {"id": 5, "nombre": "lapizRojo",   "cantidad": 15, "precio": 0.15, "marca": "Mongol"},
    {"id": 6, "nombre": "borrador",   "cantidad": 5, "precio": 0.20, "marca": "Nata"},
    {"id": 7, "nombre": "sacapuntas",   "cantidad": 8, "precio": 0.25, "marca": "Marfil"},
    {"id": 8, "nombre": "regla",   "cantidad": 12, "precio": 0.30, "marca": "Imagenes"},
    {"id": 9, "nombre": "compas",   "cantidad": 6, "precio": 0.50, "marca": "Faber-Castell"},
    {"id": 10, "nombre": "cajaColores",   "cantidad": 4, "precio": 0.80, "marca": "Primavera"},
    {"id": 11, "nombre": "marcadores",   "cantidad": 3, "precio": 0.90, "marca": "Primavera"},
    {"id": 12, "nombre": "carpeta",   "cantidad": 7, "precio": 0.50, "marca": "Norma"},
    {"id": 13, "nombre": "bolso",   "cantidad": 2, "precio": 1.50, "marca": "Totto"},
    {"id": 14, "nombre": "cartuchera",   "cantidad": 1, "precio": 0.20, "marca": "Scribe"},
    {"id": 15, "nombre": "calculadora",   "cantidad": 9, "precio": 1.00, "marca": "Casio"},
    {"id": 16, "nombre": "agenda",   "cantidad": 11, "precio": 0.75, "marca": "Imagenes"}, 
    {"id": 17, "nombre": "cintaAdhesiva",   "cantidad": 14, "precio": 0.35, "marca": "Nata"},  
]
siguiente_id = 4


# ── READ ──────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html", productos=productos)


# ── CREATE ────────────────────────────────
@app.route("/agregar", methods=["POST"])
def agregar():
    global siguiente_id
    productos.append({
        "id":       siguiente_id,
        "nombre":   request.form["nombre"],
        "marca":    request.form["marca"] ,
        "cantidad": int(request.form["cantidad"]),
        "precio":   float(request.form["precio"])
          
    })
    siguiente_id += 1
    return redirect(url_for("index"))


# ── UPDATE ────────────────────────────────
@app.route("/editar/<int:id>", methods=["POST"])
def editar(id):
    for p in productos:
        if p["id"] == id:
            p["nombre"]   = request.form["nombre"]
            p["marca"]    = request.form["marca"]
            p["cantidad"] = int(request.form["cantidad"])
            p["precio"]   = float(request.form["precio"])
    return redirect(url_for("index"))


# ── DELETE ────────────────────────────────
@app.route("/eliminar/<int:id>")
def eliminar(id):
    productos[:] = [p for p in productos if p["id"] != id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
