# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class Estudiante(models.Model):
    _name = 'escuela.estudiante'
    _inherits = {'res.partner': 'partner_id'}
    _description = 'Administra los datos del estudiante'

    partner_id = fields.Many2one('res.partner', ondelete='cascade', required=True)
    representante_id = fields.Many2one('escuela.representante', string='representante')
    
    representante = fields.Char(string="Representante")
    curso = fields.Char(string="Curso")
    hermanos = fields.Char(string='Hermanos')
    calificacion = fields.Float('calificacion', default=0)
    edad = fields.Integer('edad', default=0)

    @api.depends('name','lastname')
    def _completar_nombre(self):
        print(self)
        self.nombre_completo = self.name + self.lastname
        return True
    
    def cambiar_calificacion(self):
        for record in self:
            record.calificacion = 15
        return True

    def limpiar_calificacion(self):
        for record in self:
            record.calificacion = 0
        return True

    def action_calcular_edad(self):
        today = date.today()
        age = today.year - self.date.year - ((today.month, today.day) < (self.date.month, self.date.day))
        self.edad = age
        return True
