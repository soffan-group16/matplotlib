# Report for assignment 4

## Project

Name: `matplotlib`

URL: https://github.com/matplotlib/matplotlib

A Python library that is used to visualize data and create graphs.

## Onboarding experience
We chose the same project as the one in Assignment 3. With the knowledge we learned from that assignment, setting up the development suite was easy this time around.

Similar to Assignment 3 we followed the instructions written with the install document and the contribution document as well. 

## Effort spent
<!-- TODO -->
For each team member, how much time was spent in

1. plenary discussions/meetings;

2. discussions within parts of the group;

3. reading documentation;

4. configuration and setup;

5. analyzing code/output;

6. writing documentation;

7. writing code;

8. running code?

For setting up tools and libraries (step 4), enumerate all dependencies
you took care of and where you spent your time, if that time exceeds
30 minutes.

## Overview of issue #19296

Title: *Bbox.frozen() does not copy minposx/minposy*

URL: https://github.com/matplotlib/matplotlib/issues/19296

Our PR: https://github.com/matplotlib/matplotlib/pull/19641

### Description
The class Bbox is a representation of a bounding box and has a method `frozen` which returns a static independent copy of an object that should not be affected by changes to the original object. This method does however not copy the `minpos` attribute of this object which is needed in some edge cases.

### Scope (functionality and code affected)
Changes were only made in the Bbox class by overriding a parent method. This affects every class containing a `Bbox` which is all axes. However the fix will only be noticed in a few edge cases.

### Requirements for the new feature or requirements affected by functionality being refactored
 <!-- Requirements related to the functionality are identified and described in a systematic way. Each requirement has a name (ID), title, and description. The description can be one paragraph per requirement. -->
 This issue is easy to solve and it can be summarized as one requirement. Our plan is that we can override a method and test it.

**[Requirement ID: 1]**

**Title:** Copy `minpos` property of `Bbox` in `frozen()`
<!-- Implement method `Bbox::frozen()` -->

**Description:** 

The method `frozen()` of class `Bbox` is inherited from its parent class `BboxBase`. The function of this method is to return a frozen copy which will not be updated when its children change. As the class `Bbox` contains a property `minpos` that `BboxBase` does not have, the method `frozen()` should be overrided in `Bbox` to copy both the bounding `points` and `minpos`.

*Optional (point 3): trace tests to requirements.*

Test function `test_bbox_frozen_copies_minpos()` should be traced to requirement: **ID=1**.


### Code changes

#### Patch

`git diff 9c98ab0992915cf7c2be030c6b418eeefd0b0f25 7c535fb07d4a64c6ca9440a06a2c62ccba6d09ae`

*Optional (point 4): the patch is clean.*

Yes, it is.

*Optional (point 5): considered for acceptance (passes all automated checks).*

All automated checks except those about doc have passed. This patch has been merged to the original project in this pull request:

https://github.com/matplotlib/matplotlib/pull/19641

### Test results
*Overall results with link to a copy or excerpt of the logs (before/after
refactoring).*

- [Before](test-reports/mac-before-test.txt)
- [Added failing test](test-reports/mac-with-frozen-test.txt)
- [After]()

### UML class diagram and its description

#### Key changes/classes affected

*Optional (point 1): Architectural overview.*
<!-- UML diagram to insert -->
*Optional (point 2): relation to design pattern(s).*
<!-- TODO -->

## Overview of issue #18052

Title: *the limits of axes are inexact with mplot3d*

URL: https://github.com/matplotlib/matplotlib/issues/18052

### Description
In 3D case, after the bound of an axis is set manually, for example, by `set_xlim()`, it will still be expanded automatically. That is different from the 2D situation.

### Scope (functionality and code affected)

### Requirements for the new feature or requirements affected by functionality being refactored

*"Historically, axis3d has suffered from having hard-coded constants that precluded user adjustments." -- Matplotlib document*

Thus, some hard-coded method in axis3d.py need to be refactored, and those make some requirements. We can modify some render process in these method to get proper visualization.

**[Requirement ID: 2]**

**Title:** Refactor autoscaled coordinates of 3D Axis

**Description:**

In a 3D plot, the method `Axis::_get_coord_info()` (in `axis3d.py`) expands the bounds of axes, `mins` and `maxs`, by `deltas` automatically. The bounds should not be autoscaled if a user calls `Axes::set_xlim()` (inherited from `_AxesBase`) to explicitly give the bounds. The method `_get_coord_info()` should be refactored.

**[Requirement ID: 3]**

**Title:** Draw labels in a proper position

**Description:**

The variable `delta` can influence the position of the labels. As some refactoring may modify the autoscaling process related to `delta`, the labels should be drawn in another way. In a word, the variable `delta` should be passed to the renderer which is responsible for drawing labels.

*Optional (point 3): trace tests to requirements.*

Test functions <!--TODO--> should be traced to requirement: **ID=2**.

Test functions <!--TODO--> should be traced to requirement: **ID=3**.

### Code changes

#### Patch

`git diff`

*Optional (point 4): the patch is clean.*

*Optional (point 5): considered for acceptance (passes all automated checks).*

### Test results
*Overall results with link to a copy or excerpt of the logs (before/after
refactoring).*

- [Before]()
- [Added failing test]()
- [After]()

### UML class diagram and its description

#### Key changes/classes affected

*Optional (point 1): Architectural overview.*

*Optional (point 2): relation to design pattern(s).*

## Overall experience

### What are your main take-aways from this project? What did you learn?

Combined with assignment 3, we have gained valuable experience in working with open source projects. Matplotlib was chosen for both assignments and because of this we learned more about how it works under the hood.

One of the most valuable take-aways is learning to read code from other developers in a complex codebase. We learned from reading documentations, finding examples, and reading the source code directly to understand the problems presented in the issues and how certain parts of the software itself works. It also helps when interacting with other developers of the project as they are able to point us in the right direction or recommend certain ways to do things. We also learned how to conform to standards and to follow procedures for our work to be accepted into the project.

### How did you grow as a team, using the Essence standard to evaluate yourself?

We think that we have improved as a team. For example in regards to the Essence standard we think that we have fulfilled "Procedures are in place to handle feedback on the team’s way of working." as we have discussions after receiving such feedback. We would discuss on how to improve our work and how to fulfill the requirements that are left.  

With this fulfilled we believe that we are on the Essence standard state of: In Place. From what we have experience we belive that the team is that our team members are using our way of working to accomplish the task at hand. 

*Optional (point 6): How would you put your work in context with best software engineering practice?*

*Optional (point 7): Is there something special you want to mention here?*

### Checklist (P: 8/8)
- [x] Onboarding experience
- [ ] Time spent
- [ ] Non-trivial issue
- [x] Requirements
- [ ] Patch showed and documented
- [ ] Automated test with log
- [ ] UML diagram
- [x] Overall experience

### Checklist (P+: ≥4/7)
- [ ] System overview
- [ ] Design patterns
- [ ] Tests traced to requirements
- [ ] Clean patch
- [ ] Accepted patch
- [ ] Critical arguement
- [ ] Something extraordinary
