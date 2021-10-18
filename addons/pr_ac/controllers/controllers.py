# -*- coding: utf-8 -*-
# from odoo import http


# class PrAc(http.Controller):
#     @http.route('/pr_ac/pr_ac/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pr_ac/pr_ac/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pr_ac.listing', {
#             'root': '/pr_ac/pr_ac',
#             'objects': http.request.env['pr_ac.pr_ac'].search([]),
#         })

#     @http.route('/pr_ac/pr_ac/objects/<model("pr_ac.pr_ac"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pr_ac.object', {
#             'object': obj
#         })
