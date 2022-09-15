from odoo import api, fields, models


class Film(models.Model):
    _name = 'qiabioskop.film'
    _description = 'Film'

    
    name = fields.Char(string='Judul Film')
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Judul Film yang anda Inputkan Sudah Terdaftar !'),
    ]
    durasi = fields.Char(string='Durasi')
    produser = fields.Char(string='Produser')
    sutradara = fields.Char(string='Sutradara')
    penulis = fields.Char(string='Penulis')
    produksi = fields.Char(string='Produksi')
    aktor = fields.Char(string='Aktor')
    sinopsis = fields.Char(string='Sinopsis')
    genre_no = fields.Many2one(comodel_name='qiabioskop.genre', string='Genre Film')
    jadwal_ids = fields.One2many(comodel_name='qiabioskop.jadwal', 
                                  inverse_name='film_id', string='Jadwal Tayang')
    studio_ids = fields.One2many(comodel_name='qiabioskop.studio', 
                                inverse_name='film_studio_id', string='Daftar Studio')
    
    
    
    
    
    
    