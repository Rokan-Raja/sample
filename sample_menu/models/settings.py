from os import name
from odoo import models,api,fields

class SampleSettings(models.TransientModel):
    
    _inherit = 'res.config.settings'
    
    name=fields.Char(string="Sample Settings")