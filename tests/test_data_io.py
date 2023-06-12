from pathlib import Path
import pytest
import pandas as pd
from utilities.data_io import load_data_file, save_data_file

source_data_folder = "data/"
test_outputs_path = "tests/data/"

test_csv_filename = "access_to_jobs.csv"
test_excel_filename = "EDDT_UnitsAffordablebyAMI_2015-2019.xlsx"

test_data_minimal = pd.DataFrame(
    data={
        "column_a": ["1", 2],
        "column_b": ["3", 4],
    }
)


def test_load_data_file():
    csv_data = load_data_file(f"{source_data_folder}{test_csv_filename}")
    assert isinstance(csv_data, pd.DataFrame)
    assert len(csv_data.columns) == 2
    assert len(csv_data) == 55

    excel_data = load_data_file(f"{source_data_folder}{test_excel_filename}")
    assert isinstance(excel_data, pd.DataFrame)
    assert len(excel_data.columns) == 36
    assert len(excel_data) == 61

    missing_csv_path = f"{source_data_folder}does_not_exist.csv"
    with pytest.raises(FileNotFoundError):
        _ = load_data_file(missing_csv_path)

    unsupported_json_path = f"{source_data_folder}does_not_exist.json"
    with pytest.raises(NotImplementedError):
        _ = load_data_file(unsupported_json_path)


def test_save_data_file():
    test_output_file_path = f"{test_outputs_path}test_save_data_file.xlsx"
    data = test_data_minimal
    save_data_file(data, test_output_file_path)

    assert Path(test_output_file_path).is_file

    unsupported_json_path = f"{source_data_folder}does_not_exist.json"
    with pytest.raises(NotImplementedError):
        save_data_file(data, unsupported_json_path)
