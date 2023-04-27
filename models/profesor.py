# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Profesor(models.Model):
    _name = 'escuela.profesor'
    _inherit = ['escuela.persona']
    _description = 'Administra los datos de los maestros'

    telefono = fields.Char(string="Telefono")
    titulo = fields.Char(string="Titulo")
    area = fields.Char(string="Area")

    @api.depends('name','lastname')
    def _completar_nombre(self):
        for record in self:
            record.nombre_completo =  record.lastname + record.name
        return True