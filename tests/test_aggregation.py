import pytest
import pandas as pd
from utilities.data_io import load_data_file, save_data_file
from utilities.aggrgation import clean_cluster_outputs

test_data_full_path = "tests/data/cluster_8v_results_full.csv"
test_data_cleaned_path = "tests/data/cluster_8v_results_cleaned.csv"


def test_clean_cluster_outputs():
    data_full = load_data_file(f"{test_data_full_path}")
    
    data_cleaned_actual = clean_cluster_outputs(data_full)

    data_cleaned_expected = load_data_file(test_data_cleaned_path)

    pd.testing.assert_frame_equal(data_cleaned_actual, data_cleaned_expected)
