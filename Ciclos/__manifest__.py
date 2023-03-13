# -*- coding: utf-8 -*-
{
    'name': "Cicloos",  # Titulo del módulo
    'summary': "Ciclos ",  # Resumen de la funcionaliadad
    'description': """
Gestion de ciclos formativos
==============
    """,  

    #Indicamos que es una aplicación
    'application': True,
    'author': "Pepe",
    'website': "pepe.com",
    'category': 'Tools',
    'version': '1',
    'depends': ['base'],

    'data': [
        
        'security/ir.model.access.csv',
        #Cargamos la vista del hospital
        'views/alumno.xml',
        'views/profesor.xml',
        'views/formatiu.xml',
        'views/modulo.xml'
    ],
   
}
