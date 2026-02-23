from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/competicao", methods=["POST"])
def competicao():
    dados = request.get_json()
    competidores = dados.get("competidores",[])
    resultados = []

    for competidor in competidores:
        nome = competidor.get("nome")
        tamanhos = competidor.get("tamanhos",[])
        total = sum(tamanhos)
        maior_peixe = max(tamanhos) if tamanhos else 0
        resultados.append({"nome": nome, "total": total, "maior_peixe": maior_peixe})

    ranking = sorted(resultados, key=lambda x: (x["total"], x["maior_peixe"]), reverse=True)
    podio = ranking[:5]
    peixe_trofeu = max(podio, key=lambda x: x["maior_peixe"])
    return jsonify({"ranking": podio, "peixe_trofeu": peixe_trofeu})

if __name__ == "__main__":
    app.run()
