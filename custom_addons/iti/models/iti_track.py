from odoo import models,fields

class ITITrack(models.Model):
    _name = "iti.track"
    #display Name
    _rec_name='track_name'
    
    track_name = fields.Char(string="Name",required=True)
    capacity = fields.Integer()
    is_opened = fields.Boolean(default=False)
    
    student_list = fields.One2many('iti.student','track_id')
    
    
    