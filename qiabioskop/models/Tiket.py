from odoo import api, fields, models


class Tiket(models.Model):
    _name = 'qiabioskop.tiket'
    _description = 'Tiket'
    

    name = fields.Char(string='Kode Tiket')
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Kode Tiket yang anda Inputkan Sudah Terdaftar !'),
    ]
    harga_jual = fields.Integer(string='Harga',required=True)
    stok = fields.Integer(string='Stok')
    kursi_id = fields.Many2one(comodel_name='qiabioskop.kursi', string='nomor_kursi',
                      ondelete="cascade")
    _sql_constraints = [
        ('kursi_uniq', 'unique(kursi_id)', 'Only one kursi can be linked !'),
    ]
    
    
    
    
