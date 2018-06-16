_date_fmt2_pat = _whole_word(r'\d{2} (Jan|Feb|Mar]|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{4}')
def dates_fmt2(text):
    for match in _date_fmt2_pat.finditer(text):
        yield('date', match)
