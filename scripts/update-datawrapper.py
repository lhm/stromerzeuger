from datawrapper import Datawrapper
import pandas as pd
from utils import root

chart_id = "SOAhK"
df = pd.read_csv(root / "data" / "nettonennleistung.csv")

dw = Datawrapper()
dw.add_data(chart_id, df)
dw.publish_chart(chart_id, display=False)

chart = dw.chart_properties("SOAhK")
print(f'Updated: https:{chart["publicUrl"]}')
