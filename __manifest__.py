# -*- coding: utf-8 -*-
{
    'name': "escuela",

    'summary': """
        Management school""",

    'description': """
        Module to managment school 
    """,

    'author': "TexacoTuMoco",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/estudiante_view.xml',
        'views/representante_view.xml',
        'views/profesor_view.xml',
        'views/templates.xml',
        'views/escuela_menu.xml',
        'reports/templates/lista_estudiantes_template.xml',
        'reports/templates/lista_representantes_template.xml',
        'reports/escuela_reports.xml',
        
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
