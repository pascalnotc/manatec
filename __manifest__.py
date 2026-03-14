# -*- coding: utf-8 -*-
{
    'name': "CRM - Checkboxes for leads",
    'summary': """
        Adds configurable checkboxes to leads."
    """,
    'description': """
        This module adds configurable checkboxes to leads.\n
        - Adds checklist item configuration to CRM -> Configuration -> Checklist items\n
        - Adds a notebook page to the lead form view, displaying the checkboxes and its progress for this lead\n
        - Adds a progressbar to the kanban cards
    """,
    'author': "PS 4 manatec",
    'category': 'CRM',
    'version': '17.0.1.0.0',
    'depends': ['base', 'crm'],
    'application': False,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
        'views/crm_lead_checklist_item_view.xml'
    ],
    'license': 'AGPL-3'
}
