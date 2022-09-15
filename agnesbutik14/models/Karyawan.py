from odoo import api, fields, models


class Karyawan(models.Model):
    _name = 'agnesbutik14.karyawan'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Datetime(string='Tanggal Lahir')

    id_karyawan = fields.Char(string='ID Karyawan')
    
    

class Kasir(models.Model):
    _name = 'agnesbutik14.kasir'
    _inherit = 'agnesbutik14.karyawan'
    _description = 'New Description'

    id_kasir = fields.Char(string='ID Kasir')

