# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom_employee(models.Model):
    _inherit = 'hr.employee'

    AadharNumber = fields.Char('Aadhar No')