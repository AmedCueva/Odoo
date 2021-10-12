# -*- coding: utf-8 -*-
# from odoo import http


# class Prueba2Ac(http.Controller):
#     @http.route('/prueba2_ac/prueba2_ac/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prueba2_ac/prueba2_ac/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('prueba2_ac.listing', {
#             'root': '/prueba2_ac/prueba2_ac',
#             'objects': http.request.env['prueba2_ac.prueba2_ac'].search([]),
#         })

#     @http.route('/prueba2_ac/prueba2_ac/objects/<model("prueba2_ac.prueba2_ac"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prueba2_ac.object', {
#             'object': obj
#         })
