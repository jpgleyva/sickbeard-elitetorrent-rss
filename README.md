#sickbeard-elitetorrent-rss
________

####_Obtener fichero RSS compatible con Sick Beard de la web Elitetorrent dot net para descargar series y películas en Español_

Con este script obtenemos un fichero RSS que es compatible con Sick Beard a partir del que pone a nuestra disposición elitetorrent.

--


####Instrucciones
* descargar el fichero "eliteTorrent.py" al directorio que deseemos
* abrir el fichero con un editor de texto y modificar la siguiente línea ```fichero = open('/ruta-donde-quieres-dejar-el-fichero/elitetorrent.php', 'w')``` poner la ruta donde queremos que deje el archivo RSS para que pueda acceder sickbeard, por ejemplo, si tienes un servidor montado: ```fichero = open('/var/www/elitetorrent.php', 'w')```
* dar permisos de ejecución: 
```sudo chmod +x eliteTorrent.py```
* ahora tenemos 2 opciones:
	+ lanzarlo manualmente: ```./ruta_descarga_fichero/eliteTorrent.py``` 

	+ incluirlo en nuestro [crontab](http://es.wikipedia.org/wiki/Cron_(Unix)) y ejecutarlo cada 3 horas por ejemplo añadiendo la siguiente línea a nuestro fichero "/etc/crontab"
	``` *	*/3	*	*	*	usuario	./ruta_descarga_fichero/eliteTorrent.py```
* añadimos el proveedor de torrent a Sick Beard:

  ![alt text](http://oi59.tinypic.com/2ufc7ig.jpg "añadir proveedor torrent")


--
#### Agradecimientos
>>> Thanks  	__dragor__
