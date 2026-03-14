from odoo import models, fields


class CRMChecklistItem(models.Model):
        _name = 'crm.checklist.item'
        _description = 'CRM Checklist Item'
        
        name = fields.Char(string='Task', required=True)
        active = fields.Boolean(default=True)