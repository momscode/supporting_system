# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "supporting_system"
app_title = "Supporting System"
app_publisher = "Momscode Technologies Pvt.ltd"
app_description = "Track customer tickets and issues, maintain server levels and track response and resolutions"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@momscode.in"
app_license = "GNU General Public Licence"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/supporting_system/css/supporting_system.css"
# app_include_js = "/assets/supporting_system/js/supporting_system.js"

# include js, css files in header of web template
# web_include_css = "/assets/supporting_system/css/supporting_system.css"
# web_include_js = "/assets/supporting_system/js/supporting_system.js"
doctype_js = {
    "Issue" : "public/js/issue.js"
    }
# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "supporting_system.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "supporting_system.install.before_install"
# after_install = "supporting_system.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "supporting_system.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
   "Issue":{
 "after_insert":"supporting_system.supporting_system.doctype.issue.issue_custom.on_issue_on_save"
   }
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"supporting_system.tasks.all"
# 	],
# 	"daily": [
# 		"supporting_system.tasks.daily"
# 	],
# 	"hourly": [
# 		"supporting_system.tasks.hourly"
# 	],
# 	"weekly": [
# 		"supporting_system.tasks.weekly"
# 	]
# 	"monthly": [
# 		"supporting_system.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "supporting_system.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "supporting_system.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "supporting_system.task.get_dashboard_data"
# }
fixtures = ["Custom Field"]

