"""import os
path = 'notebook/first/second/research.ipynb'
path2 = 'notebook/first/second/research2.ipynb'
print(path)
dir, file = os.path.split(path)
print(dir)
print(file)
os.makedirs(dir, exist_ok=True)
with open(path, "w") as f:
    pass
with open(path2, "w") as t:
    pass

    """

from src.DimondPricePridiction.pipelines.prediction_pipeline import CustomData

custdataobj= CustomData(1.52,62.2,58.0,7.27,7.33,4.55,"Premium","F","VS2")

data= custdataobj.get_data_as_dataframe()

print(data)