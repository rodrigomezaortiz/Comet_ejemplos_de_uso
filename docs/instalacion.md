# Entorno python

Vamos a crear un entorno Python para nuestro proyecto. Esto no existe en las máquinas una vez clonado el repositorio pero podemos reproducirlo sencillamente creando un entorno virtual. Abriremos un terminal y ejecutaremos:

```py
python -m venv .venv
```

Esto creará usando el interprete python 3 por defecto una carpeta _.venv_ que almacenará las librerías específicas de nuestro proyecto. Podéis también crear un entorno conda para el proyecto a través del Anaconda Navigator.

Entornos como VSCode suelen automáticamente detectar el entorno pero en caso no fuer así ejecutad en el terminal:

```py
source .venv/bin/activate
```

En entornos Windows esto puede ser algo más complejo (usaremos el fichero activate.bat tal que `C:\Users\...\.venv\Scripts\activate.bat`).

Con el entorno activo, es fácil instalar las dependencias bajo el fichero [requirements.txt](../requirements.txt).

```py
pip install -r requirements.txt
```

Este entorno virtual está exento de versionado como podéis ver en el fichero [.gitignore](../.gitignore) que se emplea para indicar que carpetas o ficheros no se deben versionar.
