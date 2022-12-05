# Copyright (c) 2022, wathig and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MsjedStudent(Document):
	# def validate(self):
	# 	frappe.throw(f"Person's age must be at least 18 <b>{self.student_name}</b>")
	def save(self, *args, **kwargs):

		use_doc = frappe.db.sql(f"""SELECT name FROM `tabUser` WHERE email="{self.email}"; """, as_dict=True)
		if not(use_doc):
			doc = frappe.get_doc({
				'doctype': 'User',
				'first_name': self.student_name,
				'email': self.email
				})
			doc.insert()	
		for line in self.preservation_review_ids:
			line.page_number = line.to_page - line.from_page
		super().save(*args, **kwargs)


	# def after_insert(self):
	# 	frappe.msgprint((f'Document {self.name} Insert successfully'))

	# def before_save(self):
	# 	frappe.msgprint((f'Document {self.name} Insert2 successfully'))
		