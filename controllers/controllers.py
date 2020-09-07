# -*- coding: utf-8 -*-
from odoo import http

# class PayrollReportMod(http.Controller):
#     @http.route('/payroll_report_mod/payroll_report_mod/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/payroll_report_mod/payroll_report_mod/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('payroll_report_mod.listing', {
#             'root': '/payroll_report_mod/payroll_report_mod',
#             'objects': http.request.env['payroll_report_mod.payroll_report_mod'].search([]),
#         })

#     @http.route('/payroll_report_mod/payroll_report_mod/objects/<model("payroll_report_mod.payroll_report_mod"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('payroll_report_mod.object', {
#             'object': obj
#         })