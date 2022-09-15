from odoo import api, fields, models


class Genre(models.Model):
    _name = 'qiabioskop.genre'
    _description = 'New Description'
    _rec_name = 'name'

    name = fields.Selection([
        ('horor', 'Horor'), 
        ('romance', 'Romance'), 
        ('thrilller', 'Thrilller'),
        ('action', 'Action'),
        ('drama', 'Drama'),
        ('komedi', 'Komedi'),
        ('animasi', 'Animasi'),
        ], string='Nama Genre')

    kd_genre = fields.Char(onchange='_compute_kd_genre', string='Kode Genre')

    @api.onchange('name')
    def _onchange_kd_genre(self):
        if (self.name == 'horor'):
            self.kd_genre = 'G001'
        elif (self.name == 'romance'):
            self.kd_genre = 'G002'
        elif (self.name == 'thrilller'):
            self.kd_genre = 'G003'
        elif (self.name == 'action'):
            self.kd_genre = 'G004'
        elif (self.name == 'drama'):
            self.kd_genre = 'G005'
        elif (self.name == 'komedi'):
            self.kd_genre = 'G006'
        elif (self.name == 'animasi'):
            self.kd_genre = 'G007'

    film_ids = fields.One2many(comodel_name='qiabioskop.film', 
                               inverse_name='genre_no', string='Daftar Film')
    jml_film = fields.Char(compute='_compute_jml_film', string='Jumlah Film', ondelete='cascade')
    
    @api.depends('film_ids')
    def _compute_jml_film(self):
        for rec in self:
            a = self.env['qiabioskop.film'].search([('genre_no','=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_film = b
            rec.pilihan = a
    
    pilihan = fields.Char(string='Pilihan Film')
    