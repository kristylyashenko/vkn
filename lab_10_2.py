import os

txts = []
docs = []
docxs = []

print(os.path.realpath("./TEXT"))

for file in os.listdir("./TEXT"):
        if file.endswith(".txt"):
                txts.append(file)
        if file.endswith(".doc"):
                docs.append(file)
        if file.endswith(".docx"):
                docxs.append(file)

with open("my_files.txt", "w") as f:
        f.write(f"txt: {str(txts)}\n")
        f.write(f"doc: {str(docs)}\n")
        f.write(f"docx: {str(docxs)}\n")
