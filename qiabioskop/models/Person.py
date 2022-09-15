from odoo import api, fields, models


class Person(models.Model):
    _name = 'qiabioskop.person'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Datetime(string='Tanggal Lahir')

class Kasir(models.Model):
    _name = 'qiabioskop.kasir'
    _inherit = 'qiabioskop.person'
    _description = 'New Description'

    id_kasir = fields.Char(string='ID Kasir')
    _sql_constraints = [
        ('id_kasir_uniq', 'unique(id_kasir)', 'ID Kasir yang anda Inputkan Sudah Terdaftar !'),
    ]

class CleaningService(models.Model):
    _name = 'qiabioskop.cleaningservice'   
    _inherit = 'qiabioskop.person'
    _description = 'New Description'
    
    id_cln = fields.Char(string='ID Cleaning Service')
    _sql_constraints = [
        ('id_cln_uniq', 'unique(id_cln)', 'ID Cleaning Service yang anda Inputkan Sudah Terdaftar !'),
    ]
    

