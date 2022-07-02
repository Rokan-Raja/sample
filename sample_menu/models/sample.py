from odoo import models, fields, api

class SampleModal(models.Model):
    
    _name='sample.model'
    _description='Sample Creation'
    
    name=fields.Char('Name')
    address=fields.Text('Address')
    phone=fields.Char('Phone')
    