from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Tenta carregar o modelo e as colunas ao iniciar o servidor
try:
    # Verifique se os nomes dos arquivos batem com os que gerou!
    modelo = tf.keras.models.load_model('modelo_mlp_seguranca.keras')
    colunas_entrada = joblib.load('colunas_entrada.pkl')
    print("Modelo e colunas carregados com sucesso!")
except Exception as e:
    print(f"Erro ao carregar arquivos: {e}")

@app.route('/')
def home():
    # Renderiza o index.html que está na pasta templates/
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Recebe os dados do formulário HTML
        dados_usuario = request.json
        
        # 1. Cria um DataFrame com 1 linha apenas com zeros, usando as colunas do One-Hot Encoding
        df_input = pd.DataFrame(0, index=[0], columns=colunas_entrada)
        
        # 2. Preenche com '1' apenas as opções que o usuário escolheu
        for feature, valor in dados_usuario.items():
            nome_coluna = f"{feature}_{valor}"
            if nome_coluna in df_input.columns:
                df_input[nome_coluna] = 1
                
        # 3. Faz a previsão com a MLP
        prob_roubo_array = modelo.predict(df_input)
        prob_roubo = float(prob_roubo_array[0][0])
        prob_furto = 1.0 - prob_roubo
        
        # 4. Define a classe final (Threshold de 0.5)
        classe = "ROUBO" if prob_roubo > 0.5 else "FURTO"
        
        return jsonify({
            'classe': classe,
            'prob_roubo': round(prob_roubo * 100, 2),
            'prob_furto': round(prob_furto * 100, 2)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)