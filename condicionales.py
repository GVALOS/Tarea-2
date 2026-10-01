from flask import Flask, render_template_string, request

app = Flask(__name__)

PAGINA = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Estado del expediente</title>
    <style>
        :root {
            --marino: #003478;
            --gris-azul: #7C8BAE;
            --fondo: #E8EDF6;
            --azul: #2563EB;
            --amarillo: #F0BC4C;
            --rojo: #FF0000;
        }
        * { box-sizing: border-box; }
        body {
            margin: 0;
            font-family: "Segoe UI", Arial, sans-serif;
            background: var(--fondo);
            color: var(--marino);
        }
        header {
            background: white;
            padding: 20px 40px;
            border-bottom: 4px solid var(--marino);
        }
        header h1 {
            margin: 0;
            font-size: 1.6rem;
            letter-spacing: 1px;
            text-transform: uppercase;
        }
        header p {
            margin: 4px 0 0;
            font-size: 0.8rem;
            letter-spacing: 2px;
            color: var(--gris-azul);
            text-transform: uppercase;
        }
        .franja {
            background: var(--azul);
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 0.95rem;
        }
        main {
            max-width: 520px;
            margin: 40px auto;
            padding: 0 16px;
        }
        .tarjeta {
            background: white;
            border-radius: 16px;
            padding: 28px;
            box-shadow: 0 4px 14px rgba(0, 52, 120, 0.12);
        }
        .perfil {
            margin: 0 0 16px;
            color: var(--gris-azul);
        }
        .perfil strong { color: var(--marino); }
        ul {
            list-style: none;
            margin: 0 0 24px;
            padding: 0;
        }
        li {
            display: flex;
            justify-content: space-between;
            padding: 12px 0;
            border-bottom: 1px solid var(--fondo);
        }
        .si { color: var(--azul); font-weight: 600; }
        .no { color: var(--rojo); font-weight: 600; }
        .estado {
            text-align: center;
            padding: 16px;
            border-radius: 12px;
            font-size: 1.2rem;
            font-weight: 700;
            color: white;
        }
        .estado.completo { background: var(--azul); }
        .estado.incompleto { background: var(--amarillo); color: var(--marino); }
        .estado.ninguno { background: var(--rojo); }
        .estado.desconocido { background: var(--gris-azul); }
    </style>
</head>
<body>
    <header>
        <h1>Hospital de Diagnóstico</h1>
        <p>Expedientes digitales</p>
    </header>
    <div class="franja">Estado del expediente del empleado</div>
    <main>
        <div class="tarjeta">
            <p class="perfil">Empleado: <strong>{{ empleado if empleado else "sin especificar" }}</strong></p>
            <p class="perfil">Perfil: <strong>{{ perfil if perfil else "sin especificar" }}</strong></p>
            {% if documentos %}
            <ul>
                {% for nombre, presentado in documentos.items() %}
                <li>
                    <span>{{ nombre }}</span>
                    <span class="{{ 'si' if presentado else 'no' }}">
                        {{ "Presentado" if presentado else "Falta" }}
                    </span>
                </li>
                {% endfor %}
            </ul>
            {% endif %}
            <div class="estado {{ clase }}">{{ estado }}</div>
        </div>
    </main>
</body>
</html>
"""


@app.route("/expediente")
def evaluarExpediente():
    # Los datos llegan por query string: ?empleado=Nombre&tipo=medico&dui=si&poli=si&carne=no&cv=si&solvencia=si
    empleado = request.args.get("empleado", "")
    tipo = request.args.get("tipo", "").lower()
    dui = request.args.get("dui", "no").lower() == "si"
    poli = request.args.get("poli", "no").lower() == "si"
    carne = request.args.get("carne", "no").lower() == "si"
    cv = request.args.get("cv", "no").lower() == "si"
    solvencia = request.args.get("solvencia", "no").lower() == "si"

    if tipo == "medico":
        # El médico necesita DUI, antecedentes, carnet, CV y solvencia
        documentos = {"DUI": dui, "Antecedentes penales": poli, "Carnet médico": carne, "CV": cv, "Solvencia de la Policía": solvencia}
        if dui == False and poli == False and carne == False and cv == False and solvencia == False:
            estado = "Ningún documento adjuntado"
            clase = "ninguno"
        elif dui == True and poli == True and carne == True and cv == True and solvencia == True:
            estado = "Completo"
            clase = "completo"
        else:
            estado = "Incompleto"
            clase = "incompleto"
    elif tipo == "otro":
        # El resto del personal necesita DUI, antecedentes, CV y solvencia
        documentos = {"DUI": dui, "Antecedentes penales": poli, "CV": cv, "Solvencia de la Policía": solvencia}
        if dui == False and poli == False and cv == False and solvencia == False:
            estado = "Ningún documento adjuntado"
            clase = "ninguno"
        elif dui == True and poli == True and cv == True and solvencia == True:
            estado = "Completo"
            clase = "completo"
        else:
            estado = "Incompleto"
            clase = "incompleto"
    else:
        # Caso por defecto: el perfil no encaja en ninguno esperado
        documentos = {}
        estado = "Perfil no reconocido"
        clase = "desconocido"

    return render_template_string(
        PAGINA, empleado=empleado, perfil=tipo, documentos=documentos, estado=estado, clase=clase
    )


if __name__ == "__main__":
    app.run(debug=True)