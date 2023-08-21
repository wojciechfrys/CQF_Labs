import numpy as np
import pandas as pd

import itertools
import typing as T

from IPython.display import display_html

IDX = pd.IndexSlice


def as_df(
    func: T.Callable[[pd.DataFrame], pd.DataFrame]
) -> T.Callable[[pd.DataFrame], pd.DataFrame]:
    """Wrapper for lambdas so they can be used with pd.DataFrame.pipe and still provide correct type"""
    return func


def as_sr(func: T.Callable[[pd.DataFrame], pd.Series]) -> T.Callable[[pd.DataFrame], pd.Series]:
    """Wrapper for lambdas so they can be used with pd.DataFrame.pipe and still provide correct type"""
    return func


def pd_row_display(*dfs: pd.DataFrame, titles: T.List[str] = None):
    """Displays DataFrames in a row"""
    if titles == None:
        titles = itertools.repeat("")

    def parse_df(data: T.Union[pd.DataFrame, np.ndarray], title):
        if isinstance(data, np.ndarray):
            data = pd.DataFrame(data)

        if isinstance(data, pd.DataFrame):
            data = data.style

        return data.set_table_attributes("style='display:inline'").set_caption(str(title)).to_html()

    display_html(
        "".join(parse_df(df, title) for df, title in zip(dfs, titles)),
        raw=True,
    )


def pd_row_display_d(*dfss: T.Dict[str, pd.DataFrame]):
    for dfs in dfss:
        pd_row_display(*dfs.values(), titles=dfs.keys())
