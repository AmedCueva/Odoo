# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class openacademy_ac(models.Model):
#     _name = 'openacademy_ac.openacademy_ac'
#     _description = 'openacademy_ac.openacademy_ac'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


from odoo import models, fields, api


class Course(models.Model):
     _name = 'openacademy_ac.course'
     _description = 'openacademy_ac. Cursos Industria'
     _rec_name = 'description'

     name = fields.Char(string="Titulo", required=True)
     description = fields.Text()
