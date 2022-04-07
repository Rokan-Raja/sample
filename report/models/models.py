# -*- coding: utf-8 -*-

from odoo import models, fields, api


class report(models.Model):

    _name = 'report.report'

class HrEmloyee(models.Model):
    _inherit = 'hr.employee'

    AadharNumber = fields.Char('Aadhar No')
