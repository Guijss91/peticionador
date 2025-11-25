# Usa imagem oficial python leve
FROM python:3.9-slim

# Define diretório de trabalho
WORKDIR /app

# Evita arquivos .pyc e buffer de logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instala dependências do sistema (se necessário)
# RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Copia requirements e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Expõe a porta 5000
EXPOSE 5000

# Comando para iniciar com Gunicorn (Produção)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
