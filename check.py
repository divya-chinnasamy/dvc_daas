import os
print("----------------------------------------------------------------")
print(os.getcwd())
print("----------------------------------------------------------------")

dvc_files = ["Car.csv.dvc","insurance1.csv.dvc"]
os.path.splitext(os.path.basename(dvc_files))[0]