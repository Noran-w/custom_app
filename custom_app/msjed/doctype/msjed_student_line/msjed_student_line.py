# Copyright (c) 2022, wathig and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class MsjedStudentLine(Document):
	pass
	# def save(self, *args, **kwargs):

	# 	# uniq = frappe.db.sql(f"""SELECT name FROM `tabMsjed Student Line` WHERE email="{self.email}"; """, as_dict=True)
	# 	# _sql_constraints = [('user_id_uniq', 'UNIQUE (student_id, episodes_id)','User all already exists')]


	# 	super().save(*args, **kwargs)
    # def validate(self):
	# 	uniq = frappe.db.sql(f""" ALTER TABLE `tabMsjed Student Line` ADD UNIQUE `unique_index`(); """, as_dict=True )
	# 	if(uniq):
	# 		frappe.throw(f"Student line is uniqe <b>.....</b>")
