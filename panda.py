import pandas as pd

dados = pd.read_csv('/Users\User/Documents/QAaula/allyph/aula/aula2/aula3/panda')



df = pd.dataframe(data=dados)

print(df)[df("idade") >  45]
print(df)[df("renda") > 5000]
print(df)[df("renda") > 15000]