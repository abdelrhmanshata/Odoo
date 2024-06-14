from odoo import models , fields , api
from odoo.exceptions import  ValidationError
from datetime import date

class ITIProductTemplate(models.Model):
    # get Database models from debug Mode->Edit Action -> Object : product.template
    _inherit = 'product.template'
    # _name = 'product.template2'

    barcode2 = fields.Char()

    barcode = fields.Char(required=True)
 

    