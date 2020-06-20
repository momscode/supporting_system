from __future__ import unicode_literals
import frappe
from frappe.model.mapper import get_mapped_doc  
from frappe.model.document import Document
from frappe.model.document import get_doc
from frappe.model.document import Document
@frappe.whitelist()
def make_bom(source_name, target_doc=None):
    target_doc = get_mapped_doc("Issue", source_name, {
        "Issue": {
            "doctype": "BOM",
            "field_map": {
                "name": "issue"
        }
        }
    }, target_doc)
    return target_doc
@frappe.whitelist()
def make_material_request1(source_name, target_doc=None):
    target_doc = get_mapped_doc("Issue", source_name, {
        "Issue": {
            "doctype": "Material Request",
            "field_map": {
                "name": "issue"
                }
                 },
                }, target_doc)
    target_doc.material_request_type = "Material Issue" 

    return target_doc
@frappe.whitelist()
def make_expense_claim(source_name, target_doc=None):
    target_doc = get_mapped_doc("Issue", source_name, {
        "Issue": {
            "doctype": "Expense Claim",
            "field_map": {
                "name": "issue"
                }
                },
                }, target_doc) 

    return target_doc  
def on_issue_on_save(doc, handler=""):
    if doc.chargable == 1:
        project = frappe.new_doc('Item')
        project.name = doc.name +'_'+ doc.customer
        project.item_group = 'Issue'
        project.stock_uom = 'Nos'
        project.is_sales_item = 1
        project.allow_alternative_item = 1
        project.flags.ignore_permissions  = True
        project.update({
            'item_code': project.name,
            'item_group':project.item_group,
            'stock_uom': project.stock_uom,
            'is_sales_item':project.is_sales_item,
            'allow_alternative_item':project.allow_alternative_item

            }).insert()
        frappe.msgprint(msg = ' Issue Item Created',title = 'Notification',indicator = 'green')
@frappe.whitelist()
def get_project_details(customer):
    
    project_list = frappe.db.sql(""" select distinct project_issue from `tabService Level Agreement` where customer= %s""",(customer),as_dict=1)

    return project_list


