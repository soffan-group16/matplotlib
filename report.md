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

function: key_press_handler, file: file:lib/matplotlib/backend_bases.py <!-- JA: counted 51 (not sure if counting correctly), jt: counted 44 (excluding the sub method) -->

function: subsuper, file: lib/matplotlib/\_mathtext.py <!--jt: counted 41, de: counted 36-->

function: \_to_rgba_no_colorcycle, file: lib/matplotlib/colors.py <!-- de: counted 35, supposed to be 36 , jt: counted 36-->

function: run, file: lib/matplotlib/sphinxext\plot_directive.py <!-- jt: counted 33, JA: counted 33 -->

<!-- Use at least two group members to count the complexity separately, to get a reliable results. Use a
third member if the two counts differ. -->

function: _plot_args, file: lib/matplotlib/axes\_base.py <!--JA: counted 27 -->


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
    > PlotDirective class is a directive for including a Matplotlib plot in a Sphinx document and `run` is the method to run this class.

4. If your programming language uses exceptions: Are they taken into account by the tool? If you think of an exception as another possible branch (to the catch block or the end of the function), how is the CC affected?

    > We think that the tool counts the try except statements as well. If the except raises an error it would be handled as a return point.

5. Is the documentation of the function clear about the different possible outcomes induced by different branches taken?

    > No, for all functions the documentation describes loosely what the function does but not the different outcomes it could produce. The documentation is lacking overall.

## Coverage

### Tools

**Document your experience in using a "new"/different coverage tool.**
> We used the Coverage module for python which was very convenient to use.

**How well was the tool documented? Was it possible/easy/difficult to integrate it with your build environment?**
> In general to use the module you could simply "wrap it" around the most common python testing modules, such as pytest, and it measures the coverage of the tests and produces a report automatically. However for the matplotlib module coverage was already integrated and could be run in the normal building/testing procedure by including the --cov launch option.
We found the coverage for matplotlib to be  ~80%, it varied a bit depending upon which operating system was used since different operating systems skips different tests etc.

### Your own coverage tool

**Show a patch (or link to a branch) that shows the instrumented code to gather coverage measurements.**
> ...

**The patch is probably too long to be copied here, so please add the git command that is used to obtain the patch instead:**

    git diff ...

**What kinds of constructs does your tool support, and how accurate is its output?**

### Evaluation

1. How detailed is your coverage measurement?

2. What are the limitations of your own tool?

3. Are the results of your tool consistent with existing coverage tools?

## Coverage improvement

Show the comments that describe the requirements for the coverage.

Report of old coverage: [link]

Report of new coverage: [link]

Test cases added:

    git diff ...

Number of test cases added: two per team member (P) or at least four (P+).

## Refactoring

**Plan for refactoring complex code:**

**Estimated impact of refactoring (lower CC, but other drawbacks?).**

**Carried out refactoring (optional, P+):**

**git diff ...**

## Self-assessment: Way of working

Current state according to the Essence standard: ...

Was the self-assessment unanimous? Any doubts about certain items?

How have you improved so far?

Where is potential for improvement?

## Overall experience

What are your main take-aways from this project? What did you learn?

Is there something special you want to mention here?
