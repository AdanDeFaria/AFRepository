import pandas as pd

df = pd.read_csv(r'C:\Users\gsi-Adan\Documents\Aquila\Por_Equipe.csv',
                 encoding="UTF-8",
                 sep=";")
print(df)
df.to_excel(r'C:\Users\gsi-Adan\Documents\Aquila\Por_Equipe.xlsx',
            index=False)

