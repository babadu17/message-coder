from flask import Flask, request, render_template

app = Flask(__name__)

# Alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

# Fonctions de codage et décodage
def codage(clef, message):
    message_chiffre = [alphabet.index(lettre) for lettre in message]
    message_code = [(message_chiffre[i] + clef[i]) % len(alphabet) for i in range(len(message_chiffre))]
    message_coder = [alphabet[index] for index in message_code]
    return ''.join(message_coder)

def decodage(clef, message):
    message_chiffre = [alphabet.index(lettre) for lettre in message]
    message_decode = [(message_chiffre[i] - clef[i]) % len(alphabet) for i in range(len(message_chiffre))]
    message_decoder = [alphabet[index] for index in message_decode]
    return ''.join(message_decoder)

# Routes Flask
@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        message = request.form["message"]
        cle = request.form["cle"]
        action = request.form["action"]

        clef = [alphabet.index(lettre) + 1 for lettre in cle] * 100

        if action == "encode":
            result = codage(clef, message)
        elif action == "decode":
            result = decodage(clef, message)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
