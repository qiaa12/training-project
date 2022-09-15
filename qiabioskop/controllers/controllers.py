from odoo import http, models, fields
from odoo.http import request
from datetime import datetime
import json

class Qiabioskop(http.Controller):
    @http.route('/qiabioskop/gettiket', auth='public', method=['GET'])
    def getTiket(self, **kw):
        tiket = request.env['qiabioskop.tiket'].search([])
        isi = []
        for kk in tiket:
            isi.append({
                'kode_tiket' : kk.name,
                'harga_jual' : kk.harga_jual,
                'stok' : kk.stok,
                'kursi' : kk.kursi_id[0].name
            })
        return json.dumps(isi)

    @http.route('/qiabioskop/getfilm', auth='public', method=['GET'])
    def getFilm(self, **kw):
        film = request.env['qiabioskop.film'].search([])
        sup = []
        for ss in film:
            sup.append({
                'judul_film' : ss.name, 
                'durasi' : ss.durasi,
                'produser' : ss.produser,
                'sutradara' : ss.sutradara,
                'penulis' : ss.penulis,
                'aktor' : ss.aktor,
                'sinopsis' : ss.sinopsis,
                'genre' : ss.genre_no[0].name,
                'studio' : ss.studio_ids[0].name,
                'jadwal' : ss.jadwal_ids.name   
                }) 
        
        def date_handler(obj):
            return obj.isoformat() if hasattr(obj, 'isoformat') else obj
        return json.dumps(sup, default=date_handler)
    
    # @http.route('/qiabioskop/getgenre', auth='public', method=['GET'])
    # def getGenre(self, **kw):
    #     genre = request.env['qiabioskop.genre'].search([])
    #     gen = []
    #     for gg in genre:
    #         gen.append({
    #             'nama_genre' : gg.name,
    #             'kode_genre' : gg.kd_genre,
    #             'daftar_film' : gg.film_ids[0].genre_no,
    #             'jumlah_film' : gg.jml_film,
    #             'pilihan' : gg.pilihan
    #         })
    #     return json.dumps(gen)