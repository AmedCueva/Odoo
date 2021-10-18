# -*- coding: utf-8 -*-
# from odoo import http


# class OpenacademyAc(http.Controller):
#     @http.route('/openacademy_ac/openacademy_ac/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openacademy_ac/openacademy_ac/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openacademy_ac.listing', {
#             'root': '/openacademy_ac/openacademy_ac',
#             'objects': http.request.env['openacademy_ac.openacademy_ac'].search([]),
#         })

#     @http.route('/openacademy_ac/openacademy_ac/objects/<model("openacademy_ac.openacademy_ac"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openacademy_ac.object', {
#             'object': obj
#         })
