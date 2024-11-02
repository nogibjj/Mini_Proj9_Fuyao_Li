from mylib.lib import (
    load_dataset,
    grab_mean,
    grab_median,
    grab_std,
    create_bar,
    create_line,
)


dataset = "https://raw.githubusercontent.com/fivethirtyeight/data/master/births/US_births_1994-2003_CDC_NCHS.csv"


def test_load_dataset():
    df = load_dataset(dataset)
    assert df.height == 10  # Check the number of rows
    assert df.width == 2    # Check the number of columns


def test_grab_mean():
    df_year = load_dataset(dataset)
    mean = grab_mean(df_year)
    assert round(mean, 1) == 3972213.7


def test_grab_median():
    df_year = load_dataset(dataset)
    median = grab_median(df_year)
    assert round(median, 1) == 3956092.0


def test_grab_std():
    df_year = load_dataset(dataset)
    std = grab_std(df_year)
    assert round(std, 2) == 73265.11


def test_create_bar():
    df_year = load_dataset(dataset)
    create_bar(df_year)


def test_create_line():
    df_year = load_dataset(dataset)
    create_line(df_year)


if __name__ == "__main__":
    test_load_dataset()
    test_grab_mean()
    test_grab_median()
    test_grab_std()
    test_create_bar()
    test_create_line()
