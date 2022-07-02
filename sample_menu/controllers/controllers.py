# -*- coding: utf-8 -*-
from odoo import http


class SampleMenu(http.Controller):
    @http.route('/sample_menu/sample_menu/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/sample_menu/sample_menu/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('sample_menu.listing', {
            'root': '/sample_menu/sample_menu',
            'objects': http.request.env['sample_menu.sample_menu'].search([]),
        })

    @http.route('/sample_menu/sample_menu/objects/<model("sample_menu.sample_menu"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('sample_menu.object', {
            'object': obj
        })
