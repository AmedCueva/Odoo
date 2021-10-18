# -*- coding: utf-8 -*-
# from odoo import http


# class P3Ac(http.Controller):
#     @http.route('/p3__ac/p3__ac/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/p3__ac/p3__ac/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('p3__ac.listing', {
#             'root': '/p3__ac/p3__ac',
#             'objects': http.request.env['p3__ac.p3__ac'].search([]),
#         })

#     @http.route('/p3__ac/p3__ac/objects/<model("p3__ac.p3__ac"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('p3__ac.object', {
#             'object': obj
#         })
