# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CicleProfesor(models.Model):
    _name = 'cicle.profesor'
    _description = "profesor"

    nombre = fields.Char("Nombre", required=True)
    apellidos = fields.Char("Apellidos")
    edad = fields.Char("edad")
    modulo = fields.One2many('cicle.modulo','profesor',string='modulo')