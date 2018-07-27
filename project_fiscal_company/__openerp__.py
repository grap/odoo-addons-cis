# coding: utf-8
# Copyright (C) 2018-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'CAE - Project Module',
    'version': '8.0.1.0.0',
    'category': 'CAE',
    'summary': 'Manage Cooperatives of Activities and Employment',
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'base_fiscal_company',
        'project',
    ],
    'data': [
        'views/view_project_category.xml',
        'views/view_project_project.xml',
        'views/view_project_task.xml',
        'views/view_project_task_type.xml',
        'security/ir_rule.xml',
    ],
    'installable': True,
    'auto_install': True,
}
