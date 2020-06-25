frappe.ui.form.on('Issue',{ 
    refresh: function(frm){
        frm.set_df_property('chargable',  'read_only',  frm.doc.__islocal ? 0 : 1);
        if (!frm.doc.__islocal && frm.doc.docstatus<2) {
            frm.add_custom_button(__('Material Request'),
            cur_frm.cscript['create_material_request'], __("Make"));
            frm.add_custom_button(__('Expense Claim'),
            cur_frm.cscript['create_expense_claim'], __("Make"));
        }
    },
});
cur_frm.cscript.create_material_request = function(doc){
    frappe.model.open_mapped_doc({
        method: "supporting_system.supporting_system.doctype.issue.issue_custom.make_material_request1",
        frm: cur_frm
    }) 
};
cur_frm.cscript.create_expense_claim = function(doc){
    frappe.model.open_mapped_doc({
        method: "supporting_system.supporting_system.doctype.issue.issue_custom.make_expense_claim",
        frm: cur_frm
    }) 
};
frappe.ui.form.on('Issue',{
    refresh:function(frm,cdt,cdn){
        if(frm.doc.chargable == 1){
            frm.add_custom_button(__(" Create BOM"), function (){
                frappe.model.open_mapped_doc({
                    method: "supporting_system.supporting_system.doctype.issue.issue_custom.make_bom",
                    frm: cur_frm
                }) 
            });
        }
    },
    project_issue: function(frm,cdt,cdn){
        
        var d = locals[cdt][cdn];
        frappe.call({
            method:"frappe.client.get_value",
            args: {
                doctype:"Service Level Agreement",
                filters: {
                    'project_issue': d.project_issue,
                },
            fieldname:['name','warrantyamc_status','end_date']
            }, 
            callback: function(r){
                if(!r.exc){
                    if(r.message.end_date>=frappe.datetime.nowdate()){
                        frappe.model.set_value(d.doctype, d.name,"service_level_agreement",r.message.name)
                        frappe.model.set_value(d.doctype, d.name,"warrantyamc_status",r.message.warrantyamc_status)
                        //frappe.model.set_value(d.doctype, d.name,"project_issue",r.message.project_issue)
                    }
                    else{
                        var a="Out of Warranty/AMC";
                        frappe.model.set_value(d.doctype, d.name,"service_level_agreement",r.message.name)
                        frappe.model.set_value(d.doctype, d.name,"warrantyamc_status",a) 
                        //frappe.model.set_value(d.doctype, d.name,"project_issue",r.message.project_issue)
                    }
                }
            }
        });
    },
    customer: function(frm,cdt,cdn){
        var d = locals[cdt][cdn];
        var customer =d.customer;
        frappe.call({
            method: "supporting_system.supporting_system.doctype.issue.issue_custom.get_project_details",
            args:{
                'customer': d.customer
            },
            callback:function(r){
                if(!r.exc){
                    var df = frappe.meta.get_docfield("Issue","project_issue", cur_frm.doc.name);
                    var q_options = [];
                    for (var i=0; i<r.message.length; i++){
                        var a = r.message[i].project_issue;
                        q_options.push(a)
                    }
                    df.options = q_options;
                    frm.refresh_field("project_issue");
                }
            }
        });
       /* frappe.call({
            method:"frappe.client.get_value",
            args: {
                doctype:"Service Level Agreement",
                filters: {
                    'customer': customer,
                },
                fieldname:['name','warrantyamc_status','project_issue','end_date']
            }, 
            callback: function(r) { 
                if(!r.exc){
                    if(r.message.end_date>=frappe.datetime.nowdate()){
                        frappe.model.set_value(d.doctype, d.name,"service_level_agreement",r.message.name)
                        frappe.model.set_value(d.doctype, d.name,"warrantyamc_status",r.message.warrantyamc_status)
                        frappe.model.set_value(d.doctype, d.name,"project_issue",r.message.project_issue)
                    }
                    else{
                        var a="Out of Warranty/AMC";
                        frappe.model.set_value(d.doctype, d.name,"service_level_agreement",r.message.name)
                        frappe.model.set_value(d.doctype, d.name,"warrantyamc_status",a) 
                        frappe.model.set_value(d.doctype, d.name,"project_issue",r.message.project_issue)
                    }
                }

            }
        });*/
    },
});
