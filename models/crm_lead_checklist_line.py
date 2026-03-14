from odoo import models, fields


class CrmLeadChecklistLine(models.Model):
    _name = 'crm.lead.checklist.line'
    _description = 'CRM Lead Checklist Line'

    lead_id = fields.Many2one('crm.lead', required=True, ondelete='cascade')
    item_id = fields.Many2one('crm.checklist.item', required=True, ondelete='cascade')
    
    name = fields.Char(related='item_id.name', readonly=True)
    done = fields.Boolean(default=False)