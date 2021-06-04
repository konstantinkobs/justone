#%%
from glob import glob
import easyocr
from tqdm import tqdm

#%%
reader = easyocr.Reader(['de','en'], gpu=False)

#%%
files = glob("images/*.jpg")
print(files)

#%%
words = []

for f in tqdm(files):
    results = reader.readtext(f, detail=0)

    words += results

#%%
print(words)

#%%
result = [r for r in words if len(r) > 1]
print(result)
print(len(result))

#%%
with open("wordlist.txt", "w") as f:
    f.write("\n".join(result))

# %%
