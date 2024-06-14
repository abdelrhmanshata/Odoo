from odoo import models,fields, api
from odoo.exceptions import  ValidationError
from datetime import date


class ITIStudent(models.Model):
    _name = "iti.student"
    #display Name
    _rec_name='name'
    
    name = fields.Char(string="Name",required=True)
    age = fields.Integer(required = False , compute = 'calculate_age' , store = True)
    graduate_age = fields.Integer(compute = 'calculate_age')
    birth_date = fields.Date()
    gender = fields.Selection([('Male','male'),('Female','female')])
    
    salary = fields.Float()
    info = fields.Text()
    
    is_accepted = fields.Boolean()
    
    cv = fields.Html()
    interview_time = fields.Datetime()
    is_working = fields.Boolean(default=False)
    summery = fields.Text()
    
    track_id = fields.Many2one('iti.track')
    track_capacity = fields.Integer(related='track_id.capacity')
    
    state_log = fields.One2many('iti.student.log' , 'student_id')

    _sql_constraints = [
        ('unique_student_name' , 'UNIQUE(name)' , 'This Student Already Created Before') ,
        ('age_check' ,'CHECK(age >=0)' , 'Age Can\'t be less than zero'  )
    ]
    
    
    state = fields.Selection([('level1' , 'Prep') , ('level2' , 'Sec') , ('level3' , 'Graduate')])
    def change_state(self):
        if self.state == 'level1':
            self.state = 'level2'
        elif self.state == 'level2':
             self.state = 'level3'
        else :
            self.state = 'level1'
            
    @api.onchange('is_working')
    def set_summary(self):
        for rec in self:
            if rec.is_working and rec.summery == False:
                rec.summery = 'This Student is Working'
            else :
                pass        
    
    # @api.onchange('state')
    # def warn_user(self):
    #     for rec in self:
    #         return {
    #         'warning':{
    #             'title':('State Change Warning'),
    #             'message': 'State Changed To %s'%rec.state
    #         }
    #         }
        
    
    # fun to create new log action state changed 
    @api.onchange('state')
    def log_state(self):
        for rec in self:
            rec.env['iti.student.log'].create(
                {'description': 'State changed %s'%rec.state ,
                 'student_id' : rec.id}
            )
        
    @api.constrains('age')
    def check_age(self):
        for rec in self :
            if rec.age <= 0 :
                raise ValidationError('Age Can\'t be less than or equal zero')


    @api.depends('birth_date')
    def calculate_age(self):
        for rec in self:
            if rec.birth_date:
                today = date.today()
                rec.age = today.year - rec.birth_date.year - (
                        (today.month, today.day) < (rec.birth_date.month, rec.birth_date.day))
            else:
                rec.age = 1
            rec.graduate_age = rec.age + 5