FROM python:3.11-slim

# Répertoire de travail
WORKDIR /app

# Copier le fichier requirements et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY . .

# Exposer le port de l'API
EXPOSE 5000

# Commande de lancement
CMD ["python", "app.py"]
