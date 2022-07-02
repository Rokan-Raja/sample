# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class sample_menu(models.Model):
    _name = 'sample_menu.sample_menu'
    _description = 'sample_menu.sample_menu'

    name = fields.Many2one('hr.employee',required=True)
    value = fields.Many2one(string='Address',related='name.address_id')
    date_of_birth=fields.Date(string='Date of Birth')
    value2 = fields.Float()
    description = fields.Char(related='name.work_location')    
    note = fields.Text('Note')
    
    @api.constrains('value','date_of_birth')
    def _check_value(self):
        for rec in self:
            if rec.value <= 100:
                raise ValidationError(("Minimum Value is 100"))
            if rec.date_of_birth >= fields.Date.today():
                raise ValidationError(("Date of Birth is Not accepted"))
            
    @api.model
    def _check_date(self):
        a = fields.Date.today() if self._context.get('default_type', 'entry') in ('in_invoice', 'in_refund', 'in_receipt') else False
        print(a)




    

    
    
    
    