# -*- coding: utf-8 -*-

from odoo import models, fields


class Marca (models.Model):
    _name = 'marcas.marca'

    name = fields.Char(
        required=True,
        string='Marca',
    )

    color = fields.Integer('Color Index', default=0)

    class MarcaStock(models.Model):
        _inherit = "product.template"

        marca_ids = fields.Many2many(
            'marcas.marca', 'marcas_marca_rel',
            'src_id', 'dest_id',
            string='Marca')
