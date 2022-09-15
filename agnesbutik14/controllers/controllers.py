from odoo import http, models, fields
from odoo.http import request
import json


class Agnesbutik14(http.Controller):
    @http.route('/agnesbutik14/getbarang', auth='public', method=['GET'])
    def getBarang(self, **kw):
        barang = request.env['agnesbutik14.barang'].search([])
        isi = []
        for bb in barang:
            isi.append({
                'nama_barang' : bb.name,
                'harga_jual' : bb.harga_jual,
                'stock' : bb.stock
            })
        return json.dumps(isi)


    @http.route('/agnesbutik14/getsupplier', auth='public', method=['GET'])
    def getSupplier(self, **kw):
        supplier = request.env['agnesbutik14.supplier'].search([])
        sup = []
        for s in supplier:
            sup.append({
                'nama_perusahaan' : s.name,
                'alamat' : s.alamat,
                'no_telepon' : s.no_telp,
                'barang' : s.barang_id[0].name
            })
        return json.dumps(sup)