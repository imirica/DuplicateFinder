import datetime,os,sys,hashlib

new_dict={}
class DuplicateFinder:

	def __init__(self, path):
		self.path=path

	def find_duplicates(self):
            for dirpath, _, filenames in os.walk(self.path):
                for element in filenames:
                    with open(os.path.join(dirpath,element), 'rb') as f:
                        sha256=hashlib.sha256(f.read()).hexdigest()
                        if sha256 not in new_dict:
                            new_dict[sha256] = []
                        new_dict[sha256].append(element)
            return new_dict.values()
