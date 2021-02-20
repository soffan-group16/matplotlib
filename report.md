# Report for assignment 3

<!-- This is a template for your report. You are free to modify it as needed.
It is not required to use markdown for your report either, but the report
has to be delivered in a standard, cross-platform format. -->

## Project

Name: matplotlib

URL:https://github.com/matplotlib/matplotlib

One or two sentences describing it

A Python library that helps with creating graphs.

## Onboarding experience

Did it build and run as documented?

<!-- See the assignment for details; if everything works out of the box,
there is no need to write much here. If the first project(s) you picked
ended up being unsuitable, you can describe the "onboarding experience"
for each project, along with reason(s) why you changed to a different one. -->

Project 1: mypy
The project has written instructions about how to start building and running the project but we quickly ran into trouble. One requirement was to use both Python 3 and Python 2 which caused the issue that forced us to abandon this project. The test command would not execute properly due to importing issues.

Project 2: matplotlib
The onboarding experience for matplotlib was for the most part better compared to mypy. You were not required to have two different python versions installed in order to run the tests, and the tests could simply be run with the flags --cov to include a coverage analysis in the testing.

## Complexity

**1. What are your results for ten complex functions?**
Running lizard on the lib folder excluding the test code and sorting on cyclomatic_complexity listed the follosing functions:

================================================

---

     CCN: 44,    function: key_press_handler,      file: file:lib/matplotlib/backend_bases.py
     CCN: 41,    function: subsuper,               file: lib/matplotlib/_mathtext.py
     CCN: 36,    function: _to_rgba_no_colorcycle, file: lib/matplotlib/colors.py
     CCN: 33,    function: run,                    file: lib/matplotlib/sphinxext\plot_directive.py
     CCN: 29,    function: _plot_args,             file: lib/matplotlib/axes\_base.py
     CCN: 29,    function: to_rgba_array,          file: lib/matplotlib/colors.py
     CCN: 28,    function: _pcolorargs,            file: lib/matplotlib/axes\_axes.py
     CCN: 28,    function: tick_values,            file: lib/matplotlib/ticker.py
     CCN: 27,    function: autoscale_view,         file: lib/matplotlib/axes\_base.py
     CCN: 27,    function: draw,                   file: lib/matplotlib/axes\_base.py

function: key_press_handler, file: file:lib/matplotlib/backend_bases.py <!-- counted 44 (not sure if counting correctly) -->
function: subsuper, file: lib/matplotlib/\_mathtext.py <!--counted 39 (5th attempt), should be 41?-->
function: \_to_rgba_no_colorcycle, file: lib/matplotlib/colors.py <!-- counted 35, supposed to be 36 -->
function: run, file: lib/matplotlib/sphinxext\plot_directive.py

<!-- Use at least two group members to count the complexity separately, to get a reliable results. Use a
third member if the two counts differ. -->

- Did all methods (tools vs. manual count) get the same result?
  The different methods did not get the same results. It can at times be difficult to calculate the ammount of branches from a single if statement or loop, and there is a bit of uncertanty around how try catch statements should be handeled. Overall the manual counting returned a smaller value than the automatic one.
- Are the results clear?

**2. Are the functions just complex, or also long in terms of LOC?**

function: key_press_handler, file: file:lib/matplotlib/backend_bases.py
Complex with a lot of if else statements. Quite long with about 200 lines of code without comment (eyeball guess)

function: subsuper, file: lib/matplotlib/\_mathtext.py
Both long and complex

function: \_to_rgba_no_colorcycle, file: lib/matplotlib/colors.py

function: run, file: lib/matplotlib/sphinxext\plot_directive.py

3. What is the purpose of the functions?

4. Are exceptions taken into account in the given measurements?

5. Is the documentation clear w.r.t. all the possible outcomes?

## Refactoring

Plan for refactoring complex code:

Estimated impact of refactoring (lower CC, but other drawbacks?).

Carried out refactoring (optional, P+):

git diff ...

## Coverage

### Tools

Document your experience in using a "new"/different coverage tool.

How well was the tool documented? Was it possible/easy/difficult to
integrate it with your build environment?

### Your own coverage tool

Show a patch (or link to a branch) that shows the instrumented code to
gather coverage measurements.

The patch is probably too long to be copied here, so please add
the git command that is used to obtain the patch instead:

git diff ...

What kinds of constructs does your tool support, and how accurate is
its output?

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

## Self-assessment: Way of working

Current state according to the Essence standard: ...

Was the self-assessment unanimous? Any doubts about certain items?

How have you improved so far?

Where is potential for improvement?

## Overall experience

What are your main take-aways from this project? What did you learn?

Is there something special you want to mention here?
