# coding: utf-8
import json
import requests
import webbrowser
from jinja2 import Template
from lxml import etree

provincias = ("Almeria","Cadiz","Cordoba","Granada","Huelva","Jaen","Malaga","Sevilla")
plantilla = open('Plantilla_weather.html','r')
resultado = open('weatherxml.html','w')
html = ''
url = 'http://api.openweathermap.org/data/2.5/weather'

ciudad = []
temp_minima = []
temp_maxima = []
viento = []
direccionviento = []

for i in provincias:
	dicc = {"q":i,"mode":"xml","units":"metric","lang":"es"}
	respuesta = requests.get(url,params = dicc)
	ciudad.append(i)
	dicc_xml = etree.fromstring(respuesta.text.encode("utf-8"))
	temperatura = dicc_xml.find("temperature")
	temp_minima.append(temperatura.attrib["min"])
	temp_maxima.append(temperatura.attrib["max"])
	wind_velocidad = dicc_xml.find("wind/speed")
	wind_direccion = dicc_xml.find("wind/direction")
	viento.append(wind_velocidad.attrib["value"])
	direccionviento.append(wind_direccion.attrib["name"])

for linea in plantilla:
	html += linea

miplantilla = Template(html)
salida = miplantilla.render(provincias = ciudad,temp_min = temp_minima,temp_max = temp_maxima,vel_viento = viento,direc_viento = direccionviento)

resultado.write(salida)
webbrowser.open("weatherxml.html")