from pathlib import Path
import pandas as pd
from matplotlib.axes import Axes


def load_data_file(filepath: str) -> pd.DataFrame:
    file_extension = Path(filepath).suffix
    if file_extension == ".csv":
        data = pd.read_csv(filepath).reset_index(drop=True)
    elif file_extension == ".xlsx":
        data = pd.read_excel(filepath).reset_index(drop=True)
    else:
        raise NotImplementedError(
            f"Unsupported source data file extension: {file_extension}"
        )

    return data


def save_data_file(data: pd.DataFrame, filepath: str) -> None:
    Path.mkdir(Path(filepath).parent, exist_ok=True)
    file_extension = Path(filepath).suffix
    if file_extension == ".csv":
        data = data.to_csv(filepath, index=False)
    elif file_extension == ".xlsx":
        data.to_excel(filepath, index=False)
    else:
        raise NotImplementedError(
            f"Unsupported output data file extension: {file_extension}"
        )


def save_figure(figure_axis: Axes, file_path: str):
    figure_axis.get_figure().savefig(
        file_path,
        bbox_inches="tight",
    )
