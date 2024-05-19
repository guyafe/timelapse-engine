import ee


def main():
    print("Starting timelapse engine...")
    ee.Authenticate()
    ee.Initialize(project = 'timelapse-sample')


if __name__ == "__main__":
    main()
