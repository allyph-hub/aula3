import pandas as pd

dados = {
    "nome": ["arthur", "michelli", "rodrigo", "felipe", "manuel", "andre", "joão"],
    "idade": [25,33,26,20,19,37,28],
    "cidade": ["recife", "recife", "recife", "salvador", "salvador", "são paulo", "manaus"],
}

df = pd.DataFrame(data=dados)


print(df)