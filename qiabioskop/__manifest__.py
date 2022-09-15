# -*- coding: utf-8 -*-
{
    'name': "qiabioskop",

    'summary': """
        tentang bioskop""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizzard/tiketbaru_wizzard_view.xml',
        'wizzard/penjualanreport_wizzard_view.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/genre_view.xml',
        'views/film_view.xml',
        'views/person_view.xml',
        'views/kasir_view.xml',
        'views/cleaningservice_view.xml',
        'views/konsumen_view.xml',
        'views/jadwal_view.xml',
        'views/studio_view.xml',
        'views/kursi_view.xml',
        'views/tiket_view.xml',
        'views/penjualan_view.xml',
        'views/direksi_view.xml',
        'report/report.xml',
        'report/print_faktur_penjualan.xml',
        'report/wizzard_penjualanreport_template.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
