_date_iso8601_pat = _whole_word(r'\d{4}-\d{2}-\d{2')
def dates_iso8601(text):
    for match in _date_iso8601_pat.finditer(text):
        yield('date', match)
