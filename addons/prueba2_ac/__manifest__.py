# -*- coding: utf-8 -*-
{
    'name': "prueba2_AMED_CUEVA",

    'summary': """
        Industria del Software UNAH""",

    'description': """
        Prueba Examen 1
    """,

    'author': "Aned Cueva",
    'website': "http://www.amedcueva.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
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
