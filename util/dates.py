import datetime
strptime = datetime.datetime.strptime

DATE_FORMAT = '%B %d, %Y (%A)'

AFTER_MIDNIGHT = '(After Midnight)'


def parse_date_header(date_header):
    if '–' in date_header:
        date_str, note = [
            piece.strip()
            for piece
            in date_header.split('–', maxsplit=1)
        ]
    else:
        date_str, note = date_header.strip(), ''
    
    date_str = date_str.removesuffix(AFTER_MIDNIGHT).strip()

    date = strptime(date_str, DATE_FORMAT).date()

    return date, note.strip() or None
