from odoo import models, fields, api, _
from odoo.exceptions import UserError


class HrSalaryRule(models.Model):
    _inherit = 'hr.salary.rule'

    total_section = fields.Boolean(string='Total of section', default=False)
