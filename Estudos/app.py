#Mesmo código
from flask import Flask, request, send_file, render_template_string
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import io

print("Iniciando Flask...")

app = Flask(__name__)

#criando classe 
class Pessoa:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

#Página inicial com formulário
@app.route('/')
def index():
    with open("index.html", "r", encoding="utf-8") as f:
        return render_template_string(f.read())
    
#Rota para o PDF
@app.route('/gerar_pdf', methods=["POST"])
def gerar_pdf():
    nome = request.form.get("nome")
    email = request.form.get("email")

    pessoa = Pessoa(nome, email)

    #criar pdf em memória
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    pdf.setTitle("Dados do usuário")

    pdf.setFont("Helvetica", 14)
    pdf.drawString(100,750, f"Nome:{pessoa.nome}")
    pdf.drawString(100,750, f"E-mail:{pessoa.email}")

    pdf.save()
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name="dados_usuario.pdf", mimetype="application/pdf")

if __name__=="_main_":
    print("Rodando servidor Flask em http://127.0.0.1:5000")
    print("Sucesso!")
    app.run(debug=True)

