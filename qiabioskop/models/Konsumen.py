from odoo import api, fields, models


class Pelanggan(models.Model):
   _inherit = 'res.partner'
   _description = 'pelanggan'

   poin = fields.Integer(string='Poin')
   jadwal_ids = fields.One2many(comodel_name='qiabioskop.jadwal', inverse_name='pelanggan_id', string='Daftar Jadwal')
   
   
