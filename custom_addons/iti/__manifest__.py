{
    'name':'ITI_Module',
    'description': 'Student Courses Tracking System ' ,
    'author':'iti',
    'wesbsite':'https://iti.gov.eg/home',
    # get depends from debug Mode->Edit Action -> External ID : sale.,,,,,,,
    'depends':['sale'],
    'data':[
        'views/iti_student_views.xml',
        'views/iti_track_views.xml',
        'views/iti_product_views.xml',
        # 'views/res_groups.xml',
        # 'security/ir.model.access.csv',
        'reports/iti_student_template.xml',
        'reports/reports.xml'
        ]
}