# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CicleModulo(models.Model):
    _name = 'cicle.modulo'
    _description = "modulos"

    nombre = fields.Char("Nombre", required=True)
    formatiu = fields.Many2one('cicle.formatiu')
    profesor = fields.Many2one('cicle.profesor')
    alumno = fields.Many2many('cicle.alumno')