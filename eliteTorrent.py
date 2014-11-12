#!/usr/bin/env python
# coding: utf-8
import urllib2
import codecs


# Aquí vamos añadiendo las posibles excepciones que no podemos ir encontrando con los nombres de las series
def Excepciones(cadena):
    cadena = cadena.replace('Intelligence', 'Intelligence (2014)')
    cadena = cadena.replace('La Caza (The Fall)', 'La Caza')
    cadena = cadena.replace('Resurrection (The Returned)', 'Resurrection')
    cadena = cadena.replace('Vikings', 'Vikingos')
    cadena = cadena.replace('Sillicon Valley', 'Silicon Valley')
    cadena = cadena.replace('The bridge', 'The bridge (2013)')
    cadena = cadena.replace('The Bridge', 'The Bridge (2013)')
    return cadena


#Primer paso: descargarnos el RSS
rss = urllib2.urlopen('http://elitetorrent.net/rss.php')
localFile = open('rss.php', 'w')
localFile.write(rss.read())
localFile.close()
localFile = open('rss.php', 'r')
rssEntrada = localFile.read()
localFile.close()
rssEntrada = Excepciones(rssEntrada)

#Segundo paso: crear un nuevo fichero RSS con la estructura SickBeard
#  Creamos la cabecera
fichero = open('/ruta_donde_quieres_dejar_el_fichero/elitetorrent.php', 'w')
###
fichero.write('<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n')
fichero.write('<channel>\n')
fichero.write('<title>Elitetorrent.net</title>\n')
fichero.write('<description>Bt-Chat Latest Torrents</description>\n')
fichero.write('<link>http://www.elitetorrent.net/</link>\n')
fichero.write('<language>en-en</language>\n')
fichero.write('<ttl>15</ttl>\n')
fichero.write('<image>\n')
fichero.write('\t<title>Elitetorrent.net</title>\n')
fichero.write('\t<url>http://www.elitetorrent.net</url>\n')
fichero.write('\t<link>http://www.elitetorrent.net</link>\n')
fichero.write('</image>\n')
#  Tenemos que insertar cada uno de los item's del rss original al rss de salida
puntitos = ''
posInicio = rssEntrada.find('<item>')
while (posInicio > 0):
    puntitos = puntitos+'.'
    print puntitos
    posFin = rssEntrada.find('</item>')
    if posFin <= 0:
        break

    item = rssEntrada[posInicio:posFin]
    fichero.write('<item>\n')
    fichero.write('\t<title>' + item[item.find('<title>')+7:item.find('</title>')] +'</title>\n')
    fichero.write('\t<category>'+item[item.find('<description>Categoría:')+25:item.find(' | Detalles: ')]+'</category>\n')
    fichero.write('\t<link>http://www.elitetorrent.net/get-torrent/')
    fichero.write(item[item.find('torrent')+20:item.find('torrent')+20+5] + '</link>\n')
    fichero.write('\t<pubDate>' + item[item.find('<pubDate>')+9:item.find('</pubDate>')]+'</pubDate>\n')
    fichero.write('</item>\n')

    #tenemos que leer lo que nos quede de fichero
    rssEntrada = rssEntrada[posFin+1:99999999999999999]

    posInicio = rssEntrada.find('<item>')
    if posInicio <= 0:
        print '\nFinish\n'
        break

#  Cerramos las etiquetas del rss para finalizar
fichero.write('</channel>\n')
fichero.write('</rss>\n')
fichero.close()
