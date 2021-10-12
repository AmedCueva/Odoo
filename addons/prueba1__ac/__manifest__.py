# -*- coding: utf-8 -*-
{
    'name': "prueba1_AC",

    'summary': """
        Esta es una prueba de creacion de un nuevo modulo en Odoo
        Clase: Industria del Software, Ing. Elmer Padilla""",

    'description': """
        Prueba 1 - Industria del Software
    """,

    'author': "Amed Cueva",
    'website': "amed.cueva@unah.hn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Pruebas',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
