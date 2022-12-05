# Copyright (c) 2022, wathig and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MsjedEpisodes(Document):
	
	def get_full_name(self):
		if(self.student_ids):
			self.student_no = len(self.student_ids)
			return f"{self.student_no}"
			
	def save(self, *args, **kwargs):
		self.get_full_name()
		super().save(*args, **kwargs)


		

