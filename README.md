# CryptocurrencyDjango
Se creo aplicacion web usando los siguientes framework: Django, Bootstrap(front-end); librerias: jquery, datatables; gestor de base de datos(Mysql):Mariadb.
Para ejecutar la app primero se crea un carpeta donde se intalará un entorno virtual:
pip install virtualenv myenv-
luego se activa el entorno virtual-
myenv/script/
activate
dentro de la carpeta se instaló django y django_filter y se colocó el proyecto 
crear una base de datos en mariadb llamada wtFinance
luego en utils/cryptocurrencyUtil.py introducir la api-key de usuario de la aplicacion coinmarketcap 
debido a restricciones de usuario solo se realizó la prueba para el endpoint https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest
