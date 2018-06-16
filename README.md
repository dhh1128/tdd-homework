# tdd-homework

This homework teaches you the `write test -> prove failure -> fix code -> prove success`
cycle and the `refactor -> prove all tests pass` cycle at the heart of
Test-Driven Development (TDD):

![TDD cycles](tdd-cycles.png)

See [this slide deck](
https://docs.google.com/presentation/d/1eMJL074GPIWG632bq72NU0wc4I8jE1y9G-UZ-vU5SIk/edit
) for more information.

The homework assumes that you have a working knowledge of python and that your
workstation can run python code. It also makes use of regular
expressions, but it provides the regexes to use, to keep the focus on
the process instead of irrelevant details. It should take you about
30-60 minutes if you read the directions carefully and follow good TDD
practice.

### Scenario

Imagine that you are maintaining natural language processing (NLP) library
that does “entity extraction” on documents--it scans text, and identifies
chunks of text with interesting meanings. For example, it might scan docs
looking for strings that represent numbers (“25th, seventy-five, MCMLXVII”),
so the number values can be indexed as numbers as well as being indexed as
words.

You’ve been given a new story by your product owner:

    As a programmer who uses our NLP library, I want to be able to extract
    dates like "2015-07-25" from text, so I can process them as dates
    instead of just as words.

But there's an unusual constraint on your behavior: Alice the CEO is going
to stop by your desk periodically during the next hour, and you'll only
have 30 seconds of notice to give her a demo that shows the feature
implemented with solid tests. Alice has just been criticized by some
customers for selling poor quality software, so she worries about how the
code is tested. She wants to know that you are religiously following
Test-Driven Development (TDD).

### Assignment
1. Without opening `library.py`, spend a couple minutes studying the code
   in [`library_test.py`](library_test.py). Notice the 2 unit tests. Run the tests on your
   local machine (`python library_test.py -v`) and confirm that they pass.

2. Still without opening `library.py` at all, write a test that checks
   whether your code correctly extracts "2015-07-25" as a date from a
   sentence of text. You might copy and paste from `test_ingegers()`...
   Assume that `library.dates` is the second argument
   to `assert_extract`, as `library.integers` is the second argument to
   that function in one of the other unit tests.

3. Run your test.

   At this point, Alice walks past your desk and asks for a demo of your
   progress. You immediately rerun `python library_test.py -v` in your
   command prompt to show her a test error. You then open your test code
   and show her the offending test reporting an error, and explain that
   the error is because you wrote the test first and you haven't yet
   created an implementation. Alice asks to see `library.py` to see if
   you've written any code. You show it to her.

   If you have a single failing test at this point, and it's failing
   because `library.dates` is undefined, and if you have not modified
   `library.py` at all, then proceed to step 4; you are following TDD
   and Alice is happy. If not, please reset the repo to its initial
   state and start over; you are not following the TDD process, and
   Alice isn't happy.

4. Now open [`library.py`](library.py) and create a new extractor method by copying
   and pasting the `mixed_ordinals()` function and renaming it to
   `dates_iso8601()`. Create a new regex to match dates: `_date_iso8601_pat
   = _whole_word(r'\d{4}-\d{2}-\d{2'))`. Modify the body of `dates_iso8601()`
   so it uses this new pattern, and so it returns a tuple where the
   first member is `'date'`.

5. Get all tests to pass.

6. You don't want to match sequences where the middle number in the
   date is greater than 12 (December), or where the final number in the
   date is greater than 31. Write a new test that checks whether your
   function correctly ignores such values. Observe the test fail.

   At this point, Alice comes by again. If you've followed procedure
   exactly, such that you have a failing test, proceed. Otherwise, go
   back to step 1 and start over, following TDD exactly.

7. Make the test pass by modifying the definition of `_date_iso8601_pat`
   so its pattern is `_whole_word(r'\d{4}-(0\d|1[0-2])-(0[1-9]|[12][0-9]|3[01])')`.
   Confirm that all tests pass.

8. Now you want to handle dates in the format "25 Jan 2017". Write a test
   that checks whether the code extracts that type of date. Confirm that
   the test fails.

9. Now implement a function that matches such dates. Use the following regex:

   ```_whole_word(r'\d{2} (J[au]n|Feb|Ma[ry]|Apr|Jul|Aug|Sep|Oct|Nov|Dec) \d{4}'```.

   Confirm that all tests pass.

10. Now you decide that you don't like the readability of this last regex
    that you added; stuff like `J[au]n` and `Ma[ry]` would be better
    expanded for simplicity. Refactor the regex and confirm that all the
    tests still pass.

11. Now Alice comes by again. She gives you a pat on the back when she sees
    your demo and your tests. You're doing TDD! However, she gives you some
    new requirements:

    * When you're matching ISO 8601 dates, you should also handle dates
      with timestamps, like "2018-06-22 18:22:19.123". These dates might
      end with a time precision of minutes, or of seconds, or of milliseconds.
      The delimiter between the date and the time portion could be either
      a space or 'T'. And there might be a timezone specifier on the end--
      either a 3-letter abbreviation like "MDT" or the single letter "Z"
      (for "Zulu" or UTC), or an offset like "-0800".
    * When you're matching the other date format, you should match dates
      that have a comma after the month, as in "25 Jun, 2017".
    * When you're extracting numbers, you should support comma-separated
      groupings, as in "123,456,789".

    With these new requirements in mind, imagine at least 20 new tests
    that you will have to write. Code the tests. (In pure TDD, you would
    normally code them one at a time, but for this exercise we'll have you
    code them all at once.)

12. Run the tests and confirm that all of these new tests actually fail.

13. Save your work, commit your code to git, and push it to your repo.
    Show the tests to a friend and ask them if they can think of any
    tests you missed.