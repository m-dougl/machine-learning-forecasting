import argparse


def parser():
    dataset_parameters = argparse.ArgumentParser(description="Dataset informations")
    dataset_parameters.add_argument("-n", "--n_samples", type=int, default=1000)
    dataset_parameters.add_argument("-h", "--forecast_h", type=int, default=10)
    dataset_parameters.add_argument(
        "-t", "--series_type", type=str, default="stationary"
    )


def main():
    pass


if __name__ == "__main__":
    main()
