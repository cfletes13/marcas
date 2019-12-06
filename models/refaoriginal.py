# -*- coding: utf-8 -*-

from odoo import models, fields


class RefaccionOriginal (models.Model):
    _name = 'marcas.refaoriginal'

    name = fields.Char(
        required=True,
        string='Refaccion Original',
    )

    color = fields.Integer('Color Index', default=0)


class RefaccionOrinalEti(models.Model):
    _inherit = "product.template"

    refaoriginal_ids = fields.Many2many(
        'marcas.refaoriginal', 'marcas_refaoriginal_rel', 'src_id', 'dest_id',
        string='Rafaccion Original')
