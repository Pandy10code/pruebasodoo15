# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from tokenize import Name
from unicodedata import name
from odoo import models, fields, api

class EscuelaPersona(models.AbstractModel):
    _name = 'escuela.persona'
    _description = "Campos comunes"

    nombre_completo = fields.Char('Nombre completo',compute="_completar_nombre")
    name = fields.Char('Nombre', default=" ")
    lastname = fields.Char('Apellido', default=" ")
    edad = fields.Integer('Edad')
    cedula = fields.Char('Cedula')

    @api.depends('name','lastname')
    def _completar_nombre(self):
        return True
    
