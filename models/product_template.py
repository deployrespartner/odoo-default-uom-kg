from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _get_default_uom_id(self):
        ICP = self.env['ir.config_parameter'].sudo()
        default_type = self.env.context.get('default_detailed_type', 'consu')
        
        # Récupération des paramètres en fonction du type
        if default_type == 'service':
            uom_id = int(ICP.get_param('product_default_uom.default_uom_service', 
                                     self.env.ref('uom.product_uom_unit').id))
        elif default_type == 'product':
            uom_id = int(ICP.get_param('product_default_uom.default_uom_product', 
                                     self.env.ref('uom.product_uom_kgm').id))
        else:  # consu
            uom_id = int(ICP.get_param('product_default_uom.default_uom_consu', 
                                     self.env.ref('uom.product_uom_kgm').id))
        
        return self.env['uom.uom'].browse(uom_id)

    uom_id = fields.Many2one(
        'uom.uom',
        'Unit of Measure',
        default=_get_default_uom_id,
        required=True,
        help="Default unit of measure used for all stock operations."
    )

    @api.onchange('detailed_type')
    def _onchange_detailed_type(self):
        ICP = self.env['ir.config_parameter'].sudo()
        
        if self.detailed_type == 'service':
            self.invoice_policy = 'order'
            uom_id = int(ICP.get_param('product_default_uom.default_uom_service', 
                                     self.env.ref('uom.product_uom_unit').id))
        elif self.detailed_type == 'product':
            uom_id = int(ICP.get_param('product_default_uom.default_uom_product', 
                                     self.env.ref('uom.product_uom_kgm').id))
        else:  # consu
            uom_id = int(ICP.get_param('product_default_uom.default_uom_consu', 
                                     self.env.ref('uom.product_uom_kgm').id))
        
        uom = self.env['uom.uom'].browse(uom_id)
        self.uom_id = self.uom_po_id = uom