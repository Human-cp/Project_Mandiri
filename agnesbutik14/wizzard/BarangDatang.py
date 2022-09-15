from odoo import api, fields, models


class BarangDatang(models.TransientModel):
        _name = 'agnesbutik14.barangdatang'

        barang_id = fields.Many2one(
            comodel_name='agnesbutik14.barang', 
            string='Nama Barang',
            required=True
            )
        
        jumlah = fields.Integer(string='Jumlah',required=False)

        def button_barang_datang(self):
            for rec in self:
                self.env['agnesbutik14.barang'] \
                    .search([('id', '=', rec.barang_id.id)]) \
                    .write({'stock': rec.barang_id.stock + rec.jumlah})
        