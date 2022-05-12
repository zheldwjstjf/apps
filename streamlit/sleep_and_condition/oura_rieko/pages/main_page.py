import datetime
import pandas as pd
import altair as alt

class MainPage:

    def __init__(self, streamlit) -> None:

        self.st = streamlit

    # ===================================
    # main page
    # ===================================
    def main_page(self, df):

        col1, col2, col3 = self.st.columns((1,1,2))

        try:
            # set index
            df = df.set_index("項目")
            # print("\n"*3 + "csv data 2 : ", df)

            # multiselect
            utility_costs = col3.multiselect(
                "▶︎ 光熱費項目", list(df.index), ["電 気 代", "ガ ス 代", "水 道 代"],
            )
            if not utility_costs:
                col3.error("１つ以上の項目を選んでください。")


            # =================
            # table data
            table_data = df.loc[utility_costs]


            # =================
            # graph
            self.st.write("\n")
            self.st.write("\n##### 光熱費金額グラフ")

            # stack option
            graph_stack_type = col1.selectbox(
                '▶︎ 金額のタイプ',
                ('個別金額', '合計金額')
            )
            if graph_stack_type == "個別金額":
                stack_val = False
            elif graph_stack_type == "合計金額":
                stack_val = True
            else:
                stack_val = None

            # make graph data
            graph_data = table_data.T.reset_index()
            # print("\n"*3 + "graph_data 1 : ", graph_data)
            graph_data = pd.melt(graph_data, id_vars=["index"]).rename(
                columns={"index": "年月", "value": "金額 (円)"}
            )
            # print("\n"*3 + "graph_data 2 : ", graph_data)

            # write graphs
            line = (
                alt.Chart(graph_data
                )
                .mark_line(opacity=0.9)
                .encode(
                    x="年月",
                    y=alt.Y("金額 (円):Q", stack=stack_val),
                    color="項目:N",
                )
            )

            area = (
                alt.Chart(graph_data
                )
                .mark_area(opacity=0.9)
                .encode(
                    x="年月",
                    y=alt.Y("金額 (円):Q", stack=stack_val),
                    color="項目:N",
                )
            )

            bar = (
                alt.Chart(graph_data
                )
                .mark_bar(opacity=0.9)
                .encode(
                    x="年月",
                    y=alt.Y("金額 (円):Q", stack=stack_val),
                    color="項目:N",
                )
            )

            # graph option
            chart = line

            graph_type = col2.selectbox(
                '▶︎ グラフのタイプ',
                ('LINE', 'AREA', 'BAR')
            )
            if graph_type == "LINE":
                chart = line
            elif graph_type == "AREA":
                chart = area
            elif graph_type == "BAR":
                chart = bar
            else:
                pass

            self.st.altair_chart(chart, use_container_width=True)


            # =================
            # table
            self.st.write("\n")
            self.st.write("\n##### 光熱費金額表", table_data)


        except Exception as e:
            self.st.error(e)