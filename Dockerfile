# Usar una imagen oficial de Python como imagen base
FROM python:3.10-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de dependencias al directorio de trabajo
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación al directorio de trabajo
COPY . .

# Exponer el puerto 8000
EXPOSE 8000

# Ejecutar la aplicación cuando se inicie el contenedor
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]