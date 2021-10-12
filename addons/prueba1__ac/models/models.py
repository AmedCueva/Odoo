# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class prueba1__ac(models.Model):
#     _name = 'prueba1__ac.prueba1__ac'
#     _description = 'prueba1__ac.prueba1__ac'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
