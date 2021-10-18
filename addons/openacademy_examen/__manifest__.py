# -*- coding: utf-8 -*-
{
    'name': "Open Academy - Examen",

    'summary': """Manage Trainings""",

    'description': """
        Open Academy - Examen - modulo prueba
            - Cusos
            - Sesiones 
            - Registros de Estudiantes
    """,

    'author': "Amed Alejandro Cueva Nunez",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Examen',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data':[
        'views/security.xml',
        'security/ir.model.access.csv',
        #'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}