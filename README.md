# Utilidades-Kappa

En primera instancia es necesario configurar la librería "pygsheets", que es la que escribe en las hojas de cálculo de Google, a continuación dejo la documentación oficial, está un poco desactualizada, pero los pasos con similares.

https://pygsheets.readthedocs.io/en/stable/authorization.html

copia el contenido del archivo JSON generado en los pasos anteriores al archivo "credentials/credential.json". **Es necesario compartir tu hoja de google con el correo dentro del JSON**

A continuación listaré para que sirven cada uno de los archivos .py

#### UtilsRun.py

Para no sobrecargar la pantalla este notebook ejecuta las funciones creadas, por ahora las funciones principales son **RCRulesGen** y **DCQRRulesGen**. Es necesario definir variables de entorno para leer los archivos CONF.

#### Code/DCDQRules.py

Crea y escribe el dataframe del Hammuraitor, tiene dos variables:

- **list** : Que recibe una lista de archivos CONF guardados en la carpeta "Resource".
- **spreedsheet** : Que recibe el codigo spreedsheet de tu hoja de google.

Esta función itera sobre  los objetos de "Code/Objetos.py" aplicando el método "decide" y crea linea por linea el hammuraitor.

#### Code/RCRules.py

Crea y escribe el dataframe del RC-INGESTA, tiene dos variables:

- **list** : Que recibe una lista de archivos CONF guardados en la carpeta "Resource".
- **spreedsheet** : Que recibe el codigo spreedsheet de tu hoja de google.

Esta función itera sobre algunos objetos de "Code/Objetos.py" aplicando el método "decide" en campos que pasan del CONF al RC-Ingesta sin modificacíón o usando la salida del método "decide" como llave de un diccionario en "Code/Diccionario.py" para inferir el valor a registrar en RC-Ingesta, como la función anterior, está crea linea por línea.

#### Code/Clases.py

Al leer una ruta en un archivo CONF si está no existe se generar el error ConfigMissingException. Ya que necesitamos leer todos los posibles caminos se crea esta clase que tiene como atributo el path del CONF (e.g. "hammurabi.input.type") y un método que decide si el path es nulo o no.

Ya que las rutas pueden guardar Strings, Listas o Config se han creado varias clases que heredan de la clase principal "Dato" y sobreescriben el método "decide" según conveniencia.

#### Code/Objetos.py

Este noteebook instancia los objetos según su dato esperado, es necesario pasarle un path del CONF para instanciarlo, es aquí donde hace falta un poco de trabajo, ya que no tengo todas las rutas, aquellos objetos de los cuales falta la ruta fueron instanciados con una ruta provisional "config.none".

#### Code/Diccionario.py

Diccionarios y algunas funciones que deciden que escribir en el archivo RC-Ingesta, ya que muchos campos se deducen del tipo de regla.

## Perspectivas

Aún falta mucho trabajo para que esta libreria funcione de manera más cómoda, por lo tanto, espero que a futuro podamos implementar lo siguiente:

- Acomodar de mejor manera el codigo.
- Hacer que el hammuraitor funcione con todos los path.
- Cambiar el lenguaje a Scala para integrarlo a Skynet.
- Hacer más ammigable la ejecución, tal vez con parametros como el runConfigurations.
- Integrar otras utilidades como el Generador de Data Dummy o el de Data Objects
