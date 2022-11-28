[![PyPI Version](https://img.shields.io/pypi/v/KeynoteSlideStopwatch)](https://pypi.org/project/KeynoteSlideStopwatch/)
[![License](https://img.shields.io/github/license/casiez/KeynoteSlideStopwatch)](LICENSE)

# Keynote Slide Stopwatch

Allows to measure the time spent on each slide during a presentation with Apple Keynote.

Install using ```pip install keynoteSlideStopwatch --upgrade```

1. run ```keynoteSlideStopwatch``` from a terminal
1. play your presentation. The time spent on a slide is automatically measured from the previous slide change to the next one.

The time spent for each slide will appear in the terminal as such:

```
Press CTRL+C to quit
slide 8 - 00:16
slide 9 - 00:10
slide 10 - 00:03
slide 11 - 00:10
Total - 00:00:39
```

Limitations:
- the time for the first slide displayed is not measured
- navigating slides backwards is not supported yet
