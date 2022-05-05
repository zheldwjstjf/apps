from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models import DataTable, TableColumn, HTMLTemplateFormatter
from streamlit_bokeh_events import streamlit_bokeh_events
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame({
        "links": ["https://www.google.com", "https://streamlit.io", "https://outlokk"],
})
# create plot
cds = ColumnDataSource(df)
columns = [
TableColumn(field="links", title="links", formatter=HTMLTemplateFormatter(template='<a href="<%= value %>"target="_blank"><%= value %>')),
]

# define events
cds.selected.js_on_change(
"indices",
CustomJS(
        args=dict(source=cds),
        code="""
        document.dispatchEvent(
        new CustomEvent("INDEX_SELECT", {detail: {data: source.selected.indices}})
        )
        """
)
)
p = DataTable(source=cds, columns=columns, css_classes=["my_table"])
result = streamlit_bokeh_events(bokeh_plot=p, events="INDEX_SELECT", key="foo", refresh_on_update=False, debounce_time=0, override_height=100)
if result:
        if result.get("INDEX_SELECT"):
                st.write(df.iloc[result.get("INDEX_SELECT")["data"]])