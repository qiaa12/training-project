from odoo import models, fields


class PartnerXlsx(models.AbstractModel):
    _name = 'report.qiabioskop.report_kursi_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, kursi):
        sheet = workbook.add_worksheet('Daftar kursi')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'Nomor Kursi')
        sheet.write(1, 1, 'Kode Kursi')
        sheet.write(1, 2, 'Tiket')
        sheet.write(1, 3, 'Daftar Studio')
        row = 2
        col = 0
        for obj in kursi:
            col = 0
            report_name = obj.name
            # One sheet by partner
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.kd_kursi)
            # sheet.write(row, col+2, obj.jam_berakhir)
            for aa in obj.tiket_ids:
                sheet.write(row, col+2, aa.name)
                col += 1
            row += 1
            for bb in obj.studio_id:
                sheet.write(row, col+2, bb.name)
                col += 1
            row += 1
        