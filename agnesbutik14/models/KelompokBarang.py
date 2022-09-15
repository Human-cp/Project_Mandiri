from odoo import api, fields, models


class KelompokBarang(models.Model):
    _name = 'agnesbutik14.kelompokbarang'
    _description = 'New Description'

    name = fields.Selection([
        ('atasan', 'Atasan') , 
        ('dress', 'Dress'), 
        ('outer', 'Outer'),
        ('kaos', 'Kaos'),
        ('kemeja', 'Kemeja'),
        ('celanapanjang', 'Celana Panjang')
    ], string='Nama Kelompok')
    
    kode_produk= fields.Char(string='Kode Produk')

    @api.onchange('name')
    def _onchange_kode_produk(self):
        if (self.name=='atasan'):
            self.kode_produk = 'ATS_A'
        elif(self.name == 'dress'):
            self.kode_produk = 'DRS_B'
        elif(self.name == 'outer'):
            self.kode_produk = 'OUT_C'
        elif(self.name == 'kaos'):
            self.kode_produk = 'KS_D'
        elif(self.name == 'kemeja'):
            self.kode_produk = 'KMJ_E'
        elif(self.name == 'celanapanjang'):
            self.kode_produk = 'CLNPJ_F'


    barang_ids = fields.One2many(comodel_name='agnesbutik14.barang', 
                                 inverse_name='kelompokbarang_id', 
                                 string='Daftar Barang')

    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah Item')
    
    @api.depends('barang_ids')
    def _compute_jml_item(self):
        for rec in self:
            a = self.env['agnesbutik14.barang'].search([('kelompokbarang_id','=',rec.id)]).mapped('name')
            b = len(a)
            rec.jml_item = b
