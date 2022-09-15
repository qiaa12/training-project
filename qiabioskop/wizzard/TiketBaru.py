from odoo import api, fields, models


class TiketBaru(models.TransientModel):
    _name = 'qiabioskop.tiketbaru'

    tiket_id = fields.Many2one(
    comodel_name='qiabioskop.tiket', 
    string='Nama Tiket',
    required=True)

    jumlah = fields.Integer(
    string='Jumlah', 
    required='False')

    def button_tiket_baru(self):
        for rec in self:
            self.env['qiabioskop.tiket'].search([('id','=', rec.tiket_id.id)]).write({'stok': rec.tiket_id.stok + rec.jumlah})


    
