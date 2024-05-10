# __manifest__.py
# # Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Odoo 3skloud chatGpt module',
    'license': 'APGL-3',
    'summary': 'Integrate GPT-based chatbot into Odoo',
    'version': '1.0',
    'author': 'Refia Kosar',
    'website': 'https://www.google.com',
    'depends': ['base'],
    'data': [
        'security.ir.model.access.csv',
        'views/chat_gpt_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
