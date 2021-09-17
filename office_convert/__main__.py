from office_convert.app import OfficeFileConverter
import logging


def main():
    logging.basicConfig()
    chris_app = OfficeFileConverter()
    chris_app.launch()


if __name__ == "__main__":
    main()
