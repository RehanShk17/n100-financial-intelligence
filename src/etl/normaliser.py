def normalize_year(year):
    try:
        return int(float(year))
    except:
        return None


def normalize_ticker(ticker):
    if ticker is None:
        return ""

    return str(ticker).strip().upper()


if __name__ == "__main__":
    print(normalize_year("2024"))
    print(normalize_ticker(" tcs "))