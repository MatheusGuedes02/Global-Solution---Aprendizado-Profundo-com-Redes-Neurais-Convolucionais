# Global Solution: Aprendizado Profundo com Redes Neurais Convolucionais

**Tema:** Segurança Pública Inteligente de São Paulo - classificação de ocorrências com MLP

## Equipe

* Matheus Guedes Grigorio - RM: \[568086]
* Vinicius Fernandes Silva Souza - RM: \[567977]



## Objetivo do Projeto

O objetivo deste projeto é construir, treinar e avaliar uma rede neural do tipo Multilayer Perceptron (MLP) capaz de classificar ocorrências de seguranca publica na capital paulista. O modelo analisa as características de um registro (como periodo do dia, tipo de local e tipo de veiculo) e identifica se a ocorrencia e mais compativel com "Roubo" (art. 157) ou "Furto" (art. 155).

## Base de Dados

A base de dados escolhida foi a de "Veiculos Subtraidos" no ano de 2024, disponibilizada pela Secretaria da Seguranca Publica do Estado de Sao Paulo (SSP-SP). Ela contem registros detalhados de ocorrencias de roubo e furto de veiculos, incluindo dados geograficos, temporais e caracteristicas do local.

* **Fonte:** Portal de Estatisticas SSP-SP
* **Recorte Geografico:** Filtro aplicado exclusivamente para o municipio de "S.PAULO".

## Bibliotecas Utilizadas

Para o desenvolvimento do modelo de Machine Learning e da aplicacao web, foram utilizadas as seguintes bibliotecas principais:

* **TensorFlow / Keras:** Construcao, treinamento e exportacao da rede neural MLP.
* **Scikit-learn:** Pre-processamento de dados (Label Encoding, divisao de treino/teste) e avaliacao de metricas (Acuracia, Precision, Recall, F1-Score, Matriz de Confusao).
* **Pandas:** Manipulacao de dados estruturados e aplicacao do One-Hot Encoding.
* **NumPy:** Suporte a operacoes matematicas e manipulacao de arrays.
* **Matplotlib \& Seaborn:** Criacao de graficos para a Analise Exploratoria de Dados (EDA) e visualizacao do desempenho do modelo.
* **Joblib:** Exportacao e carregamento da estrutura de colunas (features) exigidas pelo modelo.
* **Flask:** Criacao do servidor backend em Python para integrar o modelo treinado com a interface HTML.
* **Random:** Fixacao de sementes (seeds) para garantir a reprodutibilidade dos resultados.

## Instalacao de Dependencias

Para executar o Jupyter Notebook e a aplicacao web localmente, e necessario instalar as bibliotecas mencionadas. Recomenda-se o uso de um ambiente virtual (venv).

Execute o seguinte comando no terminal do seu sistema operacional para instalar todos os pacotes necessarios de uma so vez:

```bash
pip install pandas numpy tensorflow scikit-learn matplotlib seaborn joblib flask
```

## Como Executar o Projeto

### 1\. Exploracao e Treinamento (Jupyter Notebook)

Todo o processo de limpeza de dados, analise exploratoria, comparacao de tres diferentes arquiteturas MLP e escolha do melhor modelo esta documentado no arquivo principal `.ipynb`.
Basta abrir o notebook em um ambiente como Jupyter local ou Google Colab e executar as celulas sequencialmente. Ao final, o script gerara automaticamente os arquivos `modelo\_mlp\_seguranca.keras` e `colunas\_entrada.pkl`.

### 2\. Aplicacao Web (Flask)

O projeto conta com uma interface web responsiva desenvolvida em HTML/CSS/JS que se comunica com a nossa rede neural treinada.

**Como funciona:**
A pagina apresenta um formulario onde o usuario seleciona as caracteristicas da ocorrencia (Periodo, Local, Veiculo). O arquivo `app.py` (servidor Flask) recebe esses dados, transforma-os no formato adequado (One-Hot Encoding mapeado pelo arquivo `.pkl`), realiza a inferencia usando o modelo `.keras` carregado e devolve as probabilidades reais na tela do navegador.

**Passo a passo para rodar:**

1. Certifique-se de que os arquivos `modelo\_mlp\_seguranca.keras` e `colunas\_entrada.pkl` estao no diretorio raiz.
2. Certifique-se de que o arquivo `index.html` esta dentro de uma pasta chamada `templates/`.
3. Abra o terminal no diretorio raiz do projeto e inicie o servidor com o comando:

```bash
   python app.py
   ```

4. O terminal exibira um endereco local (geralmente `http://127.0.0.1:5000`). Acesse este link pelo seu navegador para utilizar a ferramenta de classificacao.

