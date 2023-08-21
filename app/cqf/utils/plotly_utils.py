import typing as T

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

from plotly.graph_objs import Figure as goFigure
from plotly.basedatatypes import BaseTraceType as goTrace


def update_legend(name_mapper: T.Dict[str, str]) -> T.Callable[[goTrace], goTrace]:
    """To be pasted into fig.for_each_trace."""

    def update_legend_inner(t: T.Union[goTrace, go.Scatter]) -> goTrace:
        return t.update(name=name_mapper[t.name])

    return update_legend_inner
