from sciencelabx import DAtom
from sciencelabx.datasets import load_dataset
from sciencelabx.data import Data
from sciencelabx.analysis import Descriptive, Inferential


df = load_dataset("iris.csv")
dt = DAtom(df, show_info=False)

# print(dt.data.show_data)
# print(dt.data.columns)

data = Data(df, show_info=False)
# print(data.data)
ds = Descriptive(df, show_info=False)

print(dt.load("iris.csv").descriptive.mean())
print(ds.mean())