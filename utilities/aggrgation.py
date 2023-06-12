import pandas as pd

FINAL_COLUMNS = [
    "labels",
    "park_perc",
    "job_perc",
    "comp_access",
    "bach_degr",
    "empl_rate",
    "rent_under30",
    "subway_sbs",
    "infant_mortality_per1000",
    "PUMA_count",
]

CLUSTER_LABELS = {
    "0": "Cluster 0\n(In-Between)",
    "3": "Cluster 1\n(Accessible Infra. / Resource-Neglected)",
    "1": "Cluster 2\n(Low Density Perim.)",
    "2": "Cluster 3\n(Center City)",
}


def round_percentage_data(data: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    for column in columns:
        data[column] = data[column].apply(lambda x: round(x, 2))
    return data


def set_cluster_labels(data: pd.DataFrame) -> pd.DataFrame:
    data_relabeled = data.copy()
    data_relabeled["labels"] = data_relabeled["labels"].astype(str)
    data_relabeled = data_relabeled.replace(
        to_replace={"labels": CLUSTER_LABELS},
    )
    return data_relabeled


def clean_cluster_outputs(full_data: pd.DataFrame) -> pd.DataFrame:
    full_data_staged = full_data.rename(
        columns={
            "PUMA": "PUMA_count",
        }
    )

    full_data_staged["infant_mortality_per1000"] = (
        100 - full_data_staged["inf_mortality_inverse"]
    ) / 10

    clusters_grouped = (
        full_data_staged.groupby(["labels"])
        .agg(
            {
                "park_perc": "mean",
                "job_perc": "mean",
                "comp_access": "mean",
                "bach_degr": "mean",
                "empl_rate": "mean",
                "rent_under30": "mean",
                "subway_sbs": "mean",
                "infant_mortality_per1000": "mean",
                "PUMA_count": "count",
            }
        )
        .reset_index()
    )

    columns_to_round = [
        "park_perc",
        "job_perc",
        "comp_access",
        "bach_degr",
        "empl_rate",
        "rent_under30",
        "subway_sbs",
        "infant_mortality_per1000",
    ]
    clusters_grouped = round_percentage_data(clusters_grouped, columns_to_round)

    return clusters_grouped.sort_values(by="labels", ignore_index=True)
