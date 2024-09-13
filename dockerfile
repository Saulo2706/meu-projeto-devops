# Use uma imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos da aplicação para o container
COPY . /app

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que a aplicação usará
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
