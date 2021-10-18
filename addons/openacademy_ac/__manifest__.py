# -*- coding: utf-8 -*-
{
    'name': "Open Academy - Cueva",

    'summary': """Manage trainings""",

    'description': """
    Modulo Open Academy - Industria del Software
    """,

    'author': "Amed Cueva",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Examen',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],


    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml', 
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}