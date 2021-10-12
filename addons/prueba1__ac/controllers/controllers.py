# -*- coding: utf-8 -*-
# from odoo import http


# class Prueba1Ac(http.Controller):
#     @http.route('/prueba1__ac/prueba1__ac/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prueba1__ac/prueba1__ac/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('prueba1__ac.listing', {
#             'root': '/prueba1__ac/prueba1__ac',
#             'objects': http.request.env['prueba1__ac.prueba1__ac'].search([]),
#         })

#     @http.route('/prueba1__ac/prueba1__ac/objects/<model("prueba1__ac.prueba1__ac"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prueba1__ac.object', {
#             'object': obj
#         })
