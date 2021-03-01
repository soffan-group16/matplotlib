# Report for assignment 3

<!-- This is a template for your report. You are free to modify it as needed.
It is not required to use markdown for your report either, but the report
has to be delivered in a standard, cross-platform format. -->

## Project

Name: `matplotlib`

URL: https://github.com/matplotlib/matplotlib

One or two sentences describing it

A Python library that is used to visualize data and create graphs.

## Onboarding experience

Did it build and run as documented?

<!-- See the assignment for details; if everything works out of the box,
there is no need to write much here. If the first project(s) you picked
ended up being unsuitable, you can describe the "onboarding experience"
for each project, along with reason(s) why you changed to a different one. -->

**Project 1:** mypy
The project has written instructions about how to start building and running the project but we quickly ran into trouble. One requirement was to use both Python 3 and Python 2 which caused the issue that forced us to abandon this project. The test command would not execute properly due to importing issues.

**Project 2:** matplotlib
The onboarding experience for matplotlib was for the most part better compared to mypy. You were not required to have two different python versions installed in order to run the tests, and the tests could simply be run with the flag `--cov` to include a coverage analysis in the testing. There was a few issues with dependencies since the package needed a few external non-python dependencies to run some of it's tests but after that was figured out, almost all tests ran without problem.

## Complexity

**What are your results for ten complex functions?**

> Running lizard on the lib folder excluding the test code and sorting on cyclomatic_complexity listed the following functions as the first ten:

```
CCN: 44,    function: key_press_handler,      file: lib/matplotlib/backend_bases.py
CCN: 41,    function: subsuper,               file: lib/matplotlib/_mathtext.py
CCN: 36,    function: _to_rgba_no_colorcycle, file: lib/matplotlib/colors.py
CCN: 33,    function: run,                    file: lib/matplotlib/sphinxext\plot_directive.py
CCN: 29,    function: _plot_args,             file: lib/matplotlib/axes\_base.py
CCN: 29,    function: to_rgba_array,          file: lib/matplotlib/colors.py
CCN: 28,    function: _pcolorargs,            file: lib/matplotlib/axes\_axes.py
CCN: 28,    function: tick_values,            file: lib/matplotlib/ticker.py
```
### Manual CC count ##
- function: key_press_handler, file: file:lib/matplotlib/backend_bases.py <!-- JA: counted 51 (not sure if counting correctly), jt: counted 44 (excluding the sub method) -->

- function: subsuper, file: lib/matplotlib/\_mathtext.py <!--jt: counted 41, de: counted 36-->

- function: \_to_rgba_no_colorcycle, file: lib/matplotlib/colors.py <!-- de: counted 35, supposed to be 36 , jt: counted 36-->

<!-- function: _run_, file: lib/matplotlib/sphinxext\plot_directive.py jt: counted 33, JA: counted 33 -->

<!-- Use at least two group members to count the complexity separately, to get a reliable results. Use a
third member if the two counts differ. -->

- function: _plot_args, file: lib/matplotlib/axes\_base.py <!--JA: counted 27 --><!--jt: i count 27-->


1. What are your results? Did everyone get the same result? Is there something that is unclear? If you have a tool, is its result the same as yours?

    > We used a few different manual methods and the different methods did not always give the same results, possibly because we misunderstood how to use them. It was at times difficult to calculate the amount of branches from a single if statement or loop, and there was a bit of uncertainty around how try catch statements was to be handled. We found one method that we used on all functions which returned the same value as `lizard` for every function. This method was formulated `CCN(F) = P + 1` where `P` was the count of nodes in the control flow graph of the function which branched. (node that contains condition)

2. Are the functions/methods with high CC also very long in terms of LOC?

    > Yes the functions with the most CC generally have high LOC as well.

3. What is the purpose of these functions? Is it related to the high CC?

    #### `key_press_handler` ####
    > Handles events caused by the user in the canvas and toolbar, such as key presses or mouse movements.

    #### `subsuper` ####
    > This function helps solve problems with mathematical formulas (Tex). There is a lot of string parsing and formatting which requires a lot of branching.
    No documentation for its details.

    #### `_to_rgba_no_colorcycle` ####
    > Converts a color to RGBA format, the function converts a vast ammount of different color formats to rgba, to identify and handle every case a lot of branching is needed.

    #### `run` ####
    > PlotDirective class is a directive for including a Matplotlib plot in a Sphinx document and `run` is the method to run this class. Many options and configs lead to a high CCN.

    #### `_plot_args` ####
    > In Matplotlib, multiple data sets can be plotted together. _plot_args is a private method dealing with a single data set. It analyses what the arguments represent because there are a lot of different cases. Thus, there is a high complexity.

    #### `to_rgba_array` ####
    > This function changes matplotlib's color interpretation into RGBA colors. The function takes in an array of the colors and returns an array of RGBA translated color.

    #### `_pcolorargs` ####
    > This function handles the verification and occasionally creation of the necessary arguments for the `pcolor` function which draws a colored plot, for example a heat map. The user can give the `pcolor` function varying number of arguments to specify the looks of the plot on different levels and `_pcolorargs` fills in what the user is not specifying with default values and veryfining that the arguments are correct. Since users are unpredictable, many cases need to be handled which is the reason to the high CC.

    #### `tick_values` ####
    > Returns locations of generated ticks within a specified interval.


4. If your programming language uses exceptions: Are they taken into account by the tool? If you think of an exception as another possible branch (to the catch block or the end of the function), how is the CC affected?

    > We think that the tool counts the try except statements as well. If the except raises an error it would be handled as a return point.

5. Is the documentation of the function clear about the different possible outcomes induced by different branches taken?

    > No, for all functions the documentation describes loosely what the function does but not the different outcomes it could produce. The documentation is lacking overall.

## Coverage

### Tools

**Document your experience in using a coverage tool.**
> We used the Coverage module for python which was very convenient to use.

**How well was the tool documented? Was it possible/easy/difficult to integrate it with your build environment?**
> In general to use the module you could simply "wrap it" around the most common python testing modules, such as pytest, and it measures the coverage of the tests and produces a report automatically. However for the matplotlib module coverage was already integrated and could be run in the normal building/testing procedure by including the --cov launch option.
We found the coverage for matplotlib to be  ~80%, it varied a bit depending upon which operating system was used since different operating systems skips different tests etc.

### Your own coverage tool

Our coverage tool can be found on the branch `coverage` in the file [lib/matplotlib/coverage.py](lib/matplotlib/coverage.py). In addition to this tool we have created a parser which can be found on the same branch in the file [covparser.py](covparser.py).

**Show a patch (or link to a branch) that shows the instrumented code to gather coverage measurements.**

This shows an example of instrumented code but not the instrumentation for all functions:
`git show 073c3a196c2e8abece05e6f5ec0896ddacc29eaf`

### Evaluation

1. What is the quality of your own coverage measurement? Does it take into account ternary operators (condition ? yes : no) and exceptions, if available in your language?

    > Our coverage tool shows the ID of the branches which are covered, branches that are not covered, and the percentage of the coverage. Our coverage tool does not handle conditions within lambda functions or conditional assignements i.e. (a = 1 if b else 2) statements.

2. What are the limitations of your tool? How would the instrumentation change if you modify the program?

    > One limitation is that the ID of the branches have to be manually added into the source code itself. There are no options for it. For example to run it silent or only showing branch hits.

3. If you have an automated tool, are your results consistent with the ones produced by existing tool(s)?

    > There is no way of getting the branch coverage percentage for a single function in the tool `Coverage.py` but looking at what lines of code where run acording to this tool, the results seem to be consistent with out tool.

## Coverage improvement
Test cases added:

### `_to_rgba_no_colorcycle` tests ###
**Requirements:**
- The alpha value of the hex color value with format `#rrggbbaa` should be overwritten by the alpha argument value.
- The alpha value of the hex color value with format `#rgba` should be overwritten by the alpha argument value.

`git show 568c871ea5ce16242c3c0ce817f178d2538c6e3e`

[Report of old coverage](coverage-reports/_to_rgba_no_colorcycle.reportparsedold)

[Report of new coverage](coverage-reports/_to_rgba_no_colorcycle.reportparsed)

### `_create_lookup_table`  tests ###
**Requirement:** Should raise ValueError when data has the wrong format.

`git show 20ab107654ba0589c5e4b4d89024d35c8273fff4`

[Report of old coverage](coverage-reports/_to_rgba_no_colorcycle.reportparsedold)

[Report of new coverage](coverage-reports/_to_rgba_no_colorcycle.reportparsed)

### `pdfRepr` tests ###
**Requirements:**
- A none argument should return a byte representation of null.
- An invalid argument object should raise a TypeError.
- An infinite argument should raise a ValueError.

`git show 5551dc8d4b1cd4542684cc1e99c9e75f86e91d11`

[Report of old coverage](coverage-reports/pdfRepr.reportparsedold)

[Report of new coverage](coverage-reports/pdfRepr.reportparsed)

### `segment_hits` tests ###
**Requirements:** If x is only 1 element then return all the non zero element of the evaluated function.

`git show 2ee70b3e8f7ae49ef23aa574e21ee24f5a682603`

[Report of old coverage](coverage-reports/segment_hits.reportparsedold)

[Report of new coverage](coverage-reports/segment_hits.reportparsed)

### `key_press_handler` tests ###
**Requirements:**
- If the y-axis at the mouse position has a linear scale, then a generated keyEvent with key value "l" should change the scale of that y-axis to logarithmic
- If the y-axis at the mouse position has a logarithmic scale, then a generated keyEvent with key value "l" should change the scale of that y-axis to linear
- If the x-axis at the mouse position has a linear scale, then a generated keyEvent with key value "k" should change the scale of that x-axis to logarithmic
- If the x-axis at the mouse position has a logarithmic scale, then a generated keyEvent with key value "k" should change the scale of that x-axis to linear
`git show 941c8e89eef8f6cfd572a662d452eed0559da5b2`

[Report of old coverage](coverage-reports/key_press_handler.reportparsedold)

[Report of new coverage](coverage-reports/key_press_handler.reportparsed)

### `_plot_args` tests ###
**Requirements:**
- If the shapes of x and y do not match, it should not work. A ValueError with a message should be raised.
- If the dimension of data is larger than or equal to 3, it should not work. A valueError with a message should be raised.

`git show 446956a76dbb4adac210ce193222379b6d5072ca`

[Report of old coverage](coverage-reports/_plot_args.reportparsedold)

[Report of new coverage](coverage-reports/_plot_args.reportparsed)

### `git_versions_from_keywords` tests ###
**Requirements:**
- If git version is >= 1.8.3 and there is a tag prefix 'v' in a tag, this method should return the code version correctly.
- If git version is >= 1.8.3 but there is not a tag prefix 'v' in a tag, this method should return an unknown version.
- If the argument `verbose` equals `True`, this method should be able to print more useful messages.

`git show d89b93433d8c2d19c05526cf22f0882f586c61a6`

[Report of old coverage](coverage-reports/git_versions_from_keywords.reportparsedold)

[Report of new coverage](coverage-reports/git_versions_from_keywords.reportparsed)

Number of test cases added: 15

## Refactoring

<!-- **Plan for refactoring complex code:**
**Estimated impact of refactoring (lower CC, but other drawbacks?).** -->

### _mathtext.py - subsuper
lines 2606 - 2864

We could split the function into multiple subfuctions that does exactly what it did before. It is not really necessary but it would make it easier to read the function and reduce the cyclomatic complexity. The drawbacks could be reduced speed due to additional method calls.

1. (2617 - 2695) Make the if else block statement about toks be a separate function. Since this block is only handling toks, it should be fine to move it.
2. (2752 - 2854) Make this block statement into another separate function. Since the block is handling the kerning of the last letter and is quite big it should also be fine to move it.

The subsuper function would then need to call these functions, give appropriate parameters, and get the output if needed.

### colors.py - _to_rgba_no_colorcycle
lines 206 - 333

This function contains a pattern (line 230-234, 236-240...) that is repeating 4 times which contains a regex matching process and some logic thats dependent on the match. This pattern can be extracted to a separate function to reduce the complexity of this function quite a lot. This new function would presumably take the regex pattern as an argument and have a unified set of logic to handle the different cases of RGB strings. The naming and docs of this function would have to be clear though so that it does not introduce any confusion on what it's doing.


### backend_bases.py - key_press_handler
lines 2475 - 2714

There are some occurrences of duplicated code. For instance both elif statements with id 31 and 32. The only difference is whether the action should be performed on the x or y axis. This could be abstracted into a separate function taking x or y as an additional parameter. One might also consider moving the function _get_uniform_gridstate outside the function.
A side effect of that however is that it gets callable from outside the function.

Another improvement might be to componentize the second half of the function, as some of the functionality might be reusable for other functions.

### _base.py - _plot_args
lines 409 - 539

A basic idea is to split this method.
A sub method for checking conflicts between argument `fmt` and keyword arguments(`kwargs`) can be created. It is because this part is too long (lines 465 - 487) and has a high complexity.
There are also some code which process x and y data in a similar way, for example, lines 465-468 and lines 506-509. Some small methods can be created to deal with x or y in one line code.
The branch which is possible to raise ValueError('third arg must be a format string') can be removed because the method which calls `_plot_args` have tried to convert the third argument to `str` or raise an error. Thus, a redundant condition can be deleted.


## Self-assessment: Way of working

|State|Checklist|Status|
|-----|---------|------|
|Principles Established|Principles and constraints are committed to by the team.| Yes |
| ^ |Principles and constraints are agreed to by the stakeholders.| Yes |
| ^ |The tool needs of the work and its stakeholders are agreed.| Yes |
| ^ |A recommendation for the approach to be taken is available.| Yes |
| ^ |The context within which the team will operate is understood.| Yes |
| ^ |The constraints that apply to the selection, acquisition, and use of practices and tools are known.| Yes |
|Foundation Established|The key practices and tools that form the foundation of the way-of-working are selected.|Yes|
| ^ |Enough practices for work to start are agreed to by the team.|Yes|
| ^ |All non-negotiable practices and tools have been identified.|Yes|
| ^ |The gaps that exist between the practices and tools that are needed and the practices and tools that are available have been analyzed and understood.|Yes|
| ^ |The capability gaps that exist between what is needed to execute the desired way of working and the capability levels of the team have been analyzed and understood.|Yes|
| ^ |The selected practices and tools have been integrated to form a usable way-of-working.|Yes|
|In Use|The practices and tools are being used to do real work.|Yes|
| ^ |The use of the practices and tools selected are regularly inspected.|Yes|
| ^ |The practices and tools are being adapted to the team’s context|Yes|
| ^ |The use of the practices and tools is supported by the team.|Yes|
| ^ |Procedures are in place to handle feedback on the team’s way of working.|No|
| ^ |The practices and tools support team communication and collaboration.|Yes|
|In Place|The practices and tools are being used by the whole team to perform their work|Yes|
| ^ |All team members have access to the practices and tools required to do their work.|Yes|
| ^ |The whole team is involved in the inspection and adaptation of the way-of-working.|Yes|
|Working Well|Team members are making progress as planned by using and adapting the way-of-working to suit their current context.|No|
| ^ |The team naturally applies the practices without thinking about them.|No|
| ^ |The tools naturally support the way that the team works.|No|
| ^ |The team continually tunes their use of the practices and tools.|No|
|Retired|The team's way of working is no longer being used.|No|
| ^ |Lessons learned are shared for future use.|No|

Current state according to the Essence standard: In Use

Was the self-assessment unanimous? Any doubts about certain items?
Yes, we thought some of the points where hard to apply to our specific context. It seems like this is mainly directed to groups in the industry and since we are are student it does not always apply perfectly. Since our group is so small and we have the benefit of knowing quite well how the overall team progress is. This results in the team agreeing to the self-assessment unanimously.

How have you improved so far?
We have improved the way that we worked as a team since the first project. One area of improvement is with communication about the assignments. The workflow with git and Github has become smoother and smoother where suitable commits are the norm and issues are used to track requirements.

Where is potential for improvement?
We think that there is still room to improve the workflow, the way we work with git could probably be even more effective.

## What's more

In the `refactor` branch:

### Refactor _plot_args() in axes/_base.py:

**Lizard**: CCN 29 -> 17 (41.4%)

**Pytest** (on Windows10): 2 failed, 6415 passed, 1450 skipped, 13 xfailed in 328.57s (0:05:28)

**diff**:
`git show 824ccdab595478a0a6ec69563499c9038cc4feb0`

### Refactor _to_rgba_no_colorcycle() in colors.py

**Lizard**: CCN 36 -> 23 (36.1%)

**Pytest** (on Windows10): 2 failed, 6415 passed, 1450 skipped, 13 xfailed in 335.76s (0:05:35)

**diff**:
`git show 1f3387e22655314abad1575212e0e6aed23936da`

## For P+
- We have written 16 new test cases.
- We used the issue tracker and systematic commit messages.
- We are proud of our coverage tool and believe that this could count as extraordinary.
