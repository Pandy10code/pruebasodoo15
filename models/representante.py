from odoo import models, fields, api

class Representante(models.Model):
    _name = 'escuela.representante'
    _inherits = {'res.partner': 'partner_id'}
    _description = 'Administra los datos del representante de los estudiantes'

    partner_id = fields.Many2one('res.partner', ondelete='cascade', required=True)
    estudiante_ids = fields.One2many('escuela.estudiante', 'representante_id', string='estudiante')

    sueldo = fields.Float('Sueldo')
    tipos_pension = fields.Selection([
        ('norm', 'Normal'),
        ('descher', 'Descuento Hermanos'),
        ('disca', 'Discapacitados'),
        ('beca', 'Becado'),
    ], string='Tipos Pension')
    