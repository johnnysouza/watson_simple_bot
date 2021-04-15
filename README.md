# watson_simple_bot
Watson simple chatbot

Bot Criado com IBM Watson (skill-Birô-de-crédito.json)
Seu propósito é simular alguns serviços disponibilizados por um birô de crédito, contendo retorno estáticos. Único serviço consultado é para realizar a consulta do score do usuário, que é um serviço criado com cloud function da IBM.

### Setup
Rodar pipenv install para instalar as dependências;

### Conversar com o bot
Basta abrir o index.html em um navegador e iniciar os diálogos com o Bot.

### Considerações sobre o trabalho
Como o Bot foi criado com o IBM Watson, o histórico de conversas fica na nuvem e portanto é necessário baixar o mesmo para conseguir fazer as análises das conversas com o Bot.
Para tal necessidade foi criado o fonte `export_watson_conversation.py` para exportar o json `output.json` contendo as conversações do bot.
O fonte `chatbot_analytics.ipynb` contém as análises e métricas extraídas das conversas realizadas com o bot, assim como a conversão das informações da estrutura json advinda do histórico de conversas do bot.
O fonte `get_score.py` contém o mesmo código que está executando como uma cloud function da IBM para retornar a consulta do score para o bot. Apenas uma implementação sem consultado a um banco de dados mas que gera um score de 1 a 999 como um distribuição normal.
O arquivo `skill-Birô-de-crédito.json` contém a estrutura do bot que foi exportada do Watson Assistant.
O arquivo `intenções_bot_biro_credito.pdf` contém os fluxos de diálogos para duas intenções iniciais.