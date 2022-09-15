from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools.misc import unique


class Penjualan(models.Model):
    _name = 'qiabioskop.penjualan'
    _description = 'New Description'

    name = fields.Char(string='No Nota')
    nama_pembeli = fields.Many2one(comodel_name="res.partner", string='Nama Pembeli')
    id_member = fields.Char(
        compute="_compute_id_member",
        string='Id_member',
        required=False)
    tgl_penjualan = fields.Datetime(string='Tgl. Transaksi', default= fields.datetime.now())
    total_bayar = fields.Integer(compute='_compute_total_bayar', string='Total Pembayaran')
    detailpenjualan_ids = fields.One2many(comodel_name='qiabioskop.detailpenjualan', 
                                          inverse_name='penjualan_id', string='Detail Penjualan')
    
    state = fields.Selection(
        string='Status',
        selection=[
            ('draft', 'Draft'), 
            ('confirm', 'Confirm'),
            ('done', 'Done'),
            ('cancelled', 'Cancelled'),
            ],
        required=True, readonly=True, default='draft'
    )

    @api.depends('nama_pembeli')
    def _compute_id_member(self):
        for rec in self:
            rec.id_member = rec.nama_pembeli.id_member

    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})

    def action_draft(self):
        self.write({'state': 'draft'})

    @api.depends('detailpenjualan_ids')

    def _compute_total_bayar(self):
        for rec in self:
            a = sum(self.env['qiabioskop.detailpenjualan'].search([('penjualan_id','=',rec.id)]).mapped('subtotal'))
            rec.total_bayar = a

    # @api.ondelete(at_uninstall=False)
    # def __ondelete_penjualan(self):
    #     if self.detailpenjualan_ids:
    #         a =[]
    #         for rec in self:
    #             a = self.env['qiabioskop.detailpenjualan'].search([('penjualan_id','=',rec.id)])
    #             print(a)
    #         for ob in a:
    #             print(str(ob.tiket_id.name) + ' ' + str(ob.qty))
    #             ob.tiket_id.stok += ob.qty

    def unlink(self):
        if self.filtered(lambda line: line.state != 'draft'):
            raise UserError("Tdak dapat menghapus jika status BUKAN DRAFT")
        else:

            if self.detailpenjualan_ids:
                a=[]
                for rec in self:
                    a = self.env['qiabioskop.detailpenjualan'].search([('penjualan_id','=',rec.id)])
                    print(a)
                for ob in a:
                    print(str(ob.tiket_id.name) + ' ' + str(ob.qty))
                    ob.tiket_id.stok += ob.qty
            record = super(Penjualan,self).unlink()
    
    def write(self,vals):
        for rec in self:
            a = self.env['qiabioskop.detailpenjualan'].search([('penjualan_id','=',rec.id)])
            print(a)
            for data in a:
                print(str(data.tiket_id.name)+' '+str(data.qty)+' '+str(data.tiket_id.stok))
                data.tiket_id.stok += data.qty
        record = super(Penjualan,self).write(vals)
        for rec in self:
            b = self.env['qiabioskop.detailpenjualan'].search([('penjualan_id','=',rec.id)])
            print(a)
            print(b)
            for databaru in b:
                if databaru in a:
                    print(str(databaru.tiket_id.name)+' '+str(databaru.qty)+' '+str(databaru.tiket_id.stok))
                    databaru.tiket_id.stok -= databaru.qty
                else:
                    pass
        return record

    _sql_constraints = [
        # (<nama constraint>,<constraintnya><pesanconstrain>)
        ('no_nota_unik','unique(name)','Nomor Nota Ini Sudah Terdaftar Di Sistem!')
    ]

class DetailPenjualan(models.Model):
    _name = 'qiabioskop.detailpenjualan'
    _description = 'New Description'
    
    name = fields.Char(string='Nama')
    penjualan_id = fields.Many2one(comodel_name='qiabioskop.penjualan', string='Detail Penjualan')
    tiket_id = fields.Many2one(comodel_name='qiabioskop.tiket', string='List tiket')
    harga_satuan = fields.Integer(string='Harga Satuan')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Sub Total')

    @api.depends('harga_satuan','qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.qty * rec.harga_satuan
        
    @api.onchange('tiket_id')
    def _onchange_tiket_id(self):
        if(self.tiket_id.harga_jual):
           self.harga_satuan = self.tiket_id.harga_jual
        
    @api.model
    def create(self,vals):
        record = super(DetailPenjualan,self).create(vals)
        if record.qty:
            self.env['qiabioskop.tiket'].search([('id','=',record.tiket_id.id)]).write({'stok' : record.tiket_id.stok - record.qty})
        return record
        # if record.qty:
        #     record.tiket_id.stok = record.tiket_id.stok - record.qty
    
    @api.constrains('qty')
    def check_quantity(self):
        for rec in self:
            if rec.qty <1:
                raise ValidationError("Quantity {} harus dimasukan terlebih dahulu".format(rec.tiket_id.name))
            elif (rec.tiket_id.stok < rec.qty):
                raise ValidationError("Maaf Stok {} tidak mencukupi, hanya tersedia {} pcs".format(rec.tiket_id.name,rec.tiket_id.stok))

