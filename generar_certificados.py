#!/usr/bin/env python
#-*- encoding: utf-8 -*-
 
from csv import reader
import subprocess
 
print 'Abriendo listado...',
# Esto se puede poner feo...
listado = reader(open('asistentes.csv','r'))
total = len(list(listado))
listado = reader(open('asistentes.csv','r'))
print 'listo.'
 
print 'Abriendo certificado...',
certificado = open('certificado.rst').read()
print 'listo.'
 
print listado
print 'Encontrados', total, 'asistentes:'
for nro, asistente in enumerate(listado):
    calidad = asistente[0]
    apellido = asistente[1]
    nombre = asistente[2]
    cedula = asistente[3]
    certificado_final = certificado.format(calidad,apellido,nombre,cedula)
 
    print 'Generando certificado para', apellido.upper(), nombre + '...',
 
    p = subprocess.Popen(['rst2pdf',
                        '-s',
                        'estilo.style,freetype-serif,a4-landscape,twelvepoint',
                        '--fit-background-mode=scale',
                        '-o',
                        './pdf/' + cedula + '.pdf'
                        ],
                        stdin=subprocess.PIPE
                        )
    p.stdin.write(certificado_final)
    p.communicate()
    print 'listo', str(nro+1), 'de', str(total) +'.'
