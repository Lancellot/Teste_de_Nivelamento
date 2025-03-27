from flask import Flask, request, jsonify
from flask_cors import CORS  # Importe o CORS
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Configurações do Pandas
pd.set_option('display.max_columns', None)

try:
    df = pd.read_csv('Relatorio_cadop.csv', delimiter=';', encoding='utf-8', dtype=str)
    df.columns = df.columns.str.strip()
    df = df.fillna('')
except Exception as e:
    print(f"Erro ao carregar CSV: {str(e)}")
    df = pd.DataFrame()

@app.route('/buscar', methods=['GET'])
def buscar_operadora():
    termo = request.args.get('termo', '').lower().strip()
    
    if not termo:
        return jsonify({'erro': 'Informe um termo de busca'}), 400
    
    try:
        mask = (
            df['Nome_Fantasia'].str.lower().str.contains(termo, na=False) |
            df['Razao_Social'].str.lower().str.contains(termo, na=False)
        )
        resultados = df[mask].replace({np.nan: None}).to_dict(orient='records')
        
        return jsonify({
            'total_resultados': len(resultados),
            'dados': resultados
        })
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)