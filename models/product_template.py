from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _get_default_uom_id(self):
        # Si le contexte indique que c'est un service, on utilise l'unité
        if self.env.context.get('default_detailed_type') == 'service':
            return self.env.ref('uom.product_uom_unit')
        # Pour les produits stockables et consommables, on utilise kg
        return self.env.ref('uom.product_uom_kgm')

    # Surcharge du champ pour utiliser notre nouvelle méthode par défaut
    uom_id = fields.Many2one(
        'uom.uom',
        'Unit of Measure',
        default=_get_default_uom_id,
        required=True,
        help="Default unit of measure used for all stock operations."
    )

    @api.onchange('detailed_type')
    def _onchange_detailed_type(self):
        # On reprend la logique d'origine pour les services
        if self.detailed_type == 'service':
            self.invoice_policy = 'order'
            self.uom_id = self.uom_po_id = self.env.ref('uom.product_uom_unit')
        # Pour les consommables et stockables, on force en kg
        elif self.detailed_type in ['consu', 'product']:
            self.uom_id = self.uom_po_id = self.env.ref('uom.product_uom_kgm')