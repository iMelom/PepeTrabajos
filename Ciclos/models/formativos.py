# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CicleFormatiu(models.Model):
    _name = 'cicle.formatiu'
    _description = "ciclos formativos de los institutos"

    nombre = fields.Char("Nombre", required=True)
    modulo = fields.One2many('cicle.modulo','formatiu',string='modulo')