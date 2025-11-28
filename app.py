from flask import Flask, render_template, request, jsonify
import requests
import logging

app = Flask(__name__)

# Configuração de Logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# URL do seu Webhook n8n
N8N_WEBHOOK_URL = "https://n8nwebhook.ljit.com.br/webhook/peticionador"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/submit', methods=['POST'])
def submit_form():
    try:
        data = request.json
        
        # Log para debug
        logger.info(f"Enviando dados para n8n: {data}")

        # Envia para o n8n
        response = requests.post(
            N8N_WEBHOOK_URL, 
            json=data,
            headers={"Content-Type": "application/json"},
            timeout=600000 # Timeout generoso para geração de IA
        )
        
        response.raise_for_status()
        
        # Retorna a resposta do n8n para o frontend
        return jsonify(response.json())

    except requests.exceptions.RequestException as e:
        logger.error(f"Erro na comunicação com n8n: {e}")
        return jsonify({"error": "Falha ao comunicar com o servidor de processamento.", "details": str(e)}), 500
    except Exception as e:
        logger.error(f"Erro interno: {e}")
        return jsonify({"error": "Erro interno do servidor.", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
