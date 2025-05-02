# -*- coding: utf-8 -*-
# from odoo import http


# class AlquilerVehiculo(http.Controller):
#     @http.route('/alquiler_vehiculo/alquiler_vehiculo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alquiler_vehiculo/alquiler_vehiculo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('alquiler_vehiculo.listing', {
#             'root': '/alquiler_vehiculo/alquiler_vehiculo',
#             'objects': http.request.env['alquiler_vehiculo.alquiler_vehiculo'].search([]),
#         })

#     @http.route('/alquiler_vehiculo/alquiler_vehiculo/objects/<model("alquiler_vehiculo.alquiler_vehiculo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alquiler_vehiculo.object', {
#             'object': obj
#         })
