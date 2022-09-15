from odoo import api, fields, models
# from odoo.addons.kursi import kursi


class Kursi(models.Model):
    _name = 'qiabioskop.kursi'
    _description = 'Kursi'

    name = fields.Char(string='Nomor Kursi')
    kd_kursi = fields.Char(string='Kode Kursi')
    _sql_constraints = [
        ('kd_kursi_uniq', 'unique(kd_kursi)', 'Kode Kursi yang anda Inputkan Sudah Terdaftar !'),
    ]
    
    tiket_ids = fields.One2many(comodel_name='qiabioskop.tiket', 
                                inverse_name='kursi_id', string='Tiket')
    studio_id = fields.Many2one(comodel_name='qiabioskop.studio', string='Daftar Studio')
    
    
    