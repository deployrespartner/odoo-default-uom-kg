{
    'name': 'Default Product UoM Configuration',
    'version': '17.0.1.0.0',
    'category': 'Product',
    'summary': 'Configure default UoM for each product type',
    'description': '''
Default Product UoM Configuration
===============================
This module allows to configure the default Unit of Measure for each product type:
- Storable Products
- Consumable Products
- Services
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