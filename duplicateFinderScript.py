import datetime,os,sys,hashlib

class DuplicateFinder:

	def __init__(self, path):
		self.path=path

	def find_duplicates(self):
            new_dict = {}
            duplicate_files=[]
            for dirpath, _, filenames in os.walk(self.path):
                for element in filenames:
                    with open(os.path.join(dirpath,element), 'rb') as f:
                        sha256=hashlib.sha256(f.read()).hexdigest()
                        if sha256 not in new_dict:
                            new_dict[sha256] = []
                        new_dict[sha256].append(element)
            for values in new_dict.values():
                if len(values)>1:
                    duplicate_files.append(values)
            return duplicate_files


# x=DuplicateFinder(r"C:\Users\iulim\OneDrive\Desktop\test\New folder")
# print(x.find_duplicates())