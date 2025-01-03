from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def default_get(self, fields_list):
        # Récupérer les valeurs par défaut standard
        defaults = super().default_get(fields_list)
        
        # Si uom_id est dans la liste des champs demandés
        if 'uom_id' in fields_list:
            # Définir l'unité de mesure par défaut à kg (ID: 12)
            defaults['uom_id'] = 12
            
            # Si uom_po_id est aussi dans la liste, on le met également à kg
            if 'uom_po_id' in fields_list:
                defaults['uom_po_id'] = 12
                
        return defaults

    @api.onchange('detailed_type')
    def _onchange_detailed_type(self):
        # Surcharge de la méthode pour empêcher la modification de l'UoM
        # Ne rien faire pour conserver l'UoM actuelle
        return