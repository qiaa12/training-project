from odoo import api, fields, models


class Jadwal(models.Model):
    _name = 'qiabioskop.jadwal'
    _description = 'Jadwal'
       
    name = fields.Date(string='Tanggal Tayang')
    jam_mulai = fields.Datetime(string='Jam Mulai')
    jam_berakhir = fields.Datetime(string='Jam Berakhir')
    pelanggan_id = fields.Many2one(comodel_name='res.partner', 
                                   string='Daftar Pelanggan',
                                   ondelete='cascade')
    film_id = fields.Many2one(comodel_name='qiabioskop.film', string='Daftar Film')
    
    
    
    
    
    
    