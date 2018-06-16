def test_dates(self):
    self.assert_extract('I was born on 2015-07-25.', library.dates_iso8601, '2015-07-25')
