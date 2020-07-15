# nbk2qif

This script converts National Bank of Kuwait (NBK) online statements from Excel spreadsheets into the QIF or CSV formats, making them easier to import into accounting, personal finance software, or as cleaned up spreadsheets.

## Installing Dependencies

```sh
pip install -r requirements.txt
```

## Usage

```sh
python nbk2qif.py input-filename.xls > output-filename.qif
```

Alternatively, you can export the data in a CSV format using the `--csv` command line argument:

```sh
python nbk2qif.py --csv input-filename.xls > output-filename.csv
```

## License
MIT.