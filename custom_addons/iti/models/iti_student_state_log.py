from odoo import models , fields , api


class ITIStudentStateLog(models.Model):
    _name = 'iti.student.log'

    description = fields.Char()
    student_id = fields.Many2one('iti.student')

