from typing import Optional
import pandas as pd
import os

from utilities.utils_general import timestamp


def ensure_folder_exists(folder: str) -> None:
    """
    Ensure that the folder exists; if not, create it.
    :param folder: folder path
    :return: None
    """
    if not os.path.exists(folder):
        os.makedirs(folder)


def export_to_csv(
        data: pd.DataFrame,
        path: str,
        encoding: str,
        header: bool,
        line_ending: str) -> None:
    """
    Export DataFrame to a CSV file.
    :param data: dataframe to export
    :param path: path to save the file
    :param encoding: encoding to use for the file
    :param header: boolean indicating whether to include the header
    :param line_ending: line ending character(s) ('\n', '\r\n', etc.)
    :return: None
    """
    data.to_csv(path,
                index=False,
                encoding=encoding,
                header=header,
                lineterminator=line_ending)


def export_to_excel(
        data: pd.DataFrame,
        path: str,
        encoding: str,
        header: bool,
        file_type: str) -> None:
    """
    Export DataFrame to an Excel file.
    :param data: dataframe to export
    :param path: path to save the file
    :param encoding: encoding to use for the file
    :param header: boolean indicating whether to include the header
    :param file_type: type of Excel file ('xls' or 'xlsx')
    :return: None
    """
    engine = 'xlsxwriter' if file_type == 'xlsx' else 'xlwt'
    data.to_excel(path,
                  index=False,
                  encoding=encoding,
                  header=header,
                  engine=engine)


def export_to_fixed_width(
        data: pd.DataFrame,
        path: str,
        encoding: str,
        header: bool,
        line_ending: str,
        field_widths: list[int]) -> None:
    """
    Export DataFrame to a fixed-width file.
    :param data: dataframe to export
    :param path: path to save the file
    :param encoding: encoding to use for the file
    :param header: boolean indicating whether to include the header
    :param line_ending: line ending character(s) ('\n', '\r\n', etc.)
    :param field_widths: list of field widths for fixed-width file
    :return: None
    """
    if field_widths is None:
        raise ValueError("field_widths must be provided for fixed-width file type")
    if len(field_widths) != len(data.columns):
        raise ValueError("field_widths length must match the number of columns in the data")
    with open(path, 'w', encoding=encoding, newline=line_ending) as file:
        if header:
            header_line = ''.join([f"{col:<{field_widths[i]}}" for i, col in enumerate(data.columns)])
            file.write(header_line + line_ending)
        for _, row in data.iterrows():
            row_line = ''.join([f"{str(row[i]):<{field_widths[i]}}" for i in range(len(row))])
            file.write(row_line + line_ending)


def export_data(
        data: pd.DataFrame,
        schema: str,
        folder: str,
        file_type: str = 'csv',
        encoding: str = 'utf-8',
        header: bool = True,
        line_ending: str = '\n',
        field_widths: Optional[list[int]] = None
) -> str:
    """
    Export the data to a file.
    :param data: dataframe to export
    :param schema: name of the schema used to generate the data
    :param folder: folder to save the file
    :param file_type: type of file to export ('csv', 'xls', 'xlsx', 'fixed-width')
    :param encoding: file encoding
    :param header: whether to include the header in the export
    :param line_ending: line ending character(s) ('\n', '\r\n', etc.)
    :param field_widths: list of field widths for fixed-width file
    :return: name of the file
    """
    filename = f"{timestamp()}_{schema}_data.{file_type}"
    ensure_folder_exists(folder)
    path = os.path.join(folder, filename)

    if file_type == 'csv':
        export_to_csv(data, path, encoding, header, line_ending)
    elif file_type in {'xls', 'xlsx'}:
        export_to_excel(data, path, encoding, header, file_type)
    elif file_type == 'fixed-width':
        export_to_fixed_width(data, path, encoding, header, line_ending, field_widths)
    else:
        raise ValueError("Unsupported file type. Choose from 'csv', 'xls', 'xlsx', 'fixed-width'.")
    return filename
