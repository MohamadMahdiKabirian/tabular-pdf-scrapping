import sqlite3
import tabula
from pandas import DataFrame
import warnings
import pandas as pd

warnings.simplefilter(action='ignore', category=FutureWarning)

pdf = tabula.read_pdf('pdftest2.pdf',pages='all')
conn = sqlite3.connect('sql.db')

if pdf:
    df = pd.concat(pdf)
    df.to_sql('pdftest', conn, if_exists='replace', index=True)

    conn.commit()
    conn.close()

print("done")