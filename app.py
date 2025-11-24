from flask import Flask, render_template, request, jsonify
import requests
from decimal import Decimal
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        # Recebe os dados JSON
        data = request.get_json()
        
        # Validação básica
        required_fields = ['tipo_acao', 'juizo', 'partes', 'fatos', 'pedido', 'valor_causa']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'success': False, 'error': f'Campo {field} é obrigatório'}), 400
        
        # Remove formatação do valor monetário para validação
        valor_causa = data.get('valor_causa', '').replace('R$', '').replace('.', '').replace(',', '.').strip()
        
        try:
            valor_decimal = float(valor_causa)
            if valor_decimal < 0:
                return jsonify({'success': False, 'error': 'Valor da causa deve ser positivo'}), 400
        except ValueError:
            return jsonify({'success': False, 'error': 'Valor da causa inválido'}), 400
        
        # Prepara dados para envio
        payload = {
            'tipo_acao': data['tipo_acao'],
            'juizo': data['juizo'],
            'partes': data['partes'],
            'fatos': data['fatos'],
            'pedido': data['pedido'],
            'valor_causa': valor_causa
        }
        
        # Envia para o webhook
        webhook_url = 'https://n8neditor.ljit.com.br/webhook-test/peticionador'
        response = requests.post(webhook_url, json=payload, timeout=10)
        
        if response.status_code in [200, 201, 202]:
            return jsonify({'success': True, 'message': 'Formulário enviado com sucesso!'}), 200
        else:
            return jsonify({'success': False, 'error': f'Erro ao enviar: {response.status_code}'}), 500
            
    except requests.exceptions.RequestException as e:
        return jsonify({'success': False, 'error': f'Erro de conexão: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'success': False, 'error': f'Erro interno: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
