def test_dates_fmt2(self):
    self.assert_extract('I was born on 25 Jan 2017.', library.dates_fmt2, '25 Jan 2017')
