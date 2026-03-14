from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'
    
    checklist_line_ids = fields.One2many(
        'crm.lead.checklist.line',
        'lead_id',
        string='Checklist',
    )
    
    checklist_progress = fields.Float(
        compute='_compute_checklist_progress'
    )
    
    @api.model_create_multi
    def create(self, vals_list):
        """
            When creating a new lead, add a checklist line for every configured item.
        """
        leads = super().create(vals_list)
        items = self.env['crm.checklist.item'].search([])
        for lead in leads:
            for item in items:
                self.env['crm.lead.checklist.line'].create({
                    'lead_id': lead.id,
                    'item_id': item.id,
                })
                
        return leads
    
    @api.depends('checklist_line_ids.done')
    def _compute_checklist_progress(self):
        for lead in self:
            lines = lead.checklist_line_ids
            total = len(lines)
            done = len(lines.filtered('done'))
            lead.checklist_progress = (done / total * 100) if total else 0.0
    