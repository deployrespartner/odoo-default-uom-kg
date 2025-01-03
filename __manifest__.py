{
    'name': 'Default UoM Kilogram',
    'version': '17.0.1.0.0',
    'category': 'Product',
    'summary': 'Set default UoM to KG for all products',
    'description': '''
Default UoM Kilogram
===================
This module sets the default Unit of Measure to Kilogram (kg) for all products,
regardless of their detailed_type value.
    ''',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['product'],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}