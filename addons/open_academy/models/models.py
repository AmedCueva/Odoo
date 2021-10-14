# -*- coding: utf-8 -*-

 from odoo import models, fields


 class Course(models.Model):
     _name = 'open__academy.course'
     _description = 'open__academy.AmedCueva'

     name = fields.Char(String="Titulo", required=True)
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
