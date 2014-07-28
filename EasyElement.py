import sublime, sublime_plugin

class EasyElementCommand(sublime_plugin.TextCommand):
	def run(self,edit,element_start,element_end):
		for region in self.view.sel():
			if not region.empty():
				s = self.view.substr(region)
				n = element_start + s + element_end
				self.view.replace(edit,region,n)