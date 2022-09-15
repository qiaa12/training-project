from odoo import api, fields, models


class Studio(models.Model):
    _name = 'qiabioskop.studio'
    _description = 'Studio'

    name = fields.Selection([
        ('stroom', 'Stroom'), 
        ('ndroom', 'Ndroom'), 
        ('rdroom', 'Rdroom'),
        ('throom', 'Throom'),
        ], string='Nama Studio')
        
    kd_studio = fields.Char(onchange='_compute_kd_studio', string='Kode Studio')

    @api.onchange('name')
    def _onchange_kd_studio(self):
        if (self.name == 'stroom'):
            self.kd_studio = 'S001'
        elif (self.name == 'ndroom'):
            self.kd_studio = 'S002'
        elif (self.name == 'rdroom'):
            self.kd_studio = 'S003'
        elif (self.name == 'throom'):
            self.kd_studio = 'S004'

    # _sql_constraints = [
    #     ('kd_studio_uniq', 'unique(kd_studio)', 'Kode Sistem yang anda Inputkan Sudah Terdaftar !'),
    # ]
    kursi_ids = fields.One2many(comodel_name='qiabioskop.kursi', 
                                inverse_name='studio_id', string='Daftar Kursi')
    
    jml_kursi = fields.Char(compute='_compute_jml_kursi', string='Jumlah Kursi', ondelete='cascade')
    
    @api.depends('kursi_ids')
    def _compute_jml_kursi(self):
        for rec in self:
            a = self.env['qiabioskop.kursi'].search([('studio_id','=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_kursi = b
            rec.pilihan = a
    
    pilihan = fields.Char(string='Pilihan Kursi')
    film_studio_id = fields.Many2one(comodel_name='qiabioskop.film', string='Daftar Film')
    

    
    