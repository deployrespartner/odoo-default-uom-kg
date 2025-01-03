from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # Champs de configuration pour chaque type de produit
    default_uom_product = fields.Many2one(
        'uom.uom',
        string='Default UoM for Storable Products',
        config_parameter='product_default_uom.default_uom_product'
    )
    default_uom_consu = fields.Many2one(
        'uom.uom',
        string='Default UoM for Consumable Products',
        config_parameter='product_default_uom.default_uom_consu'
    )
    default_uom_service = fields.Many2one(
        'uom.uom',
        string='Default UoM for Services',
        config_parameter='product_default_uom.default_uom_service'
    )