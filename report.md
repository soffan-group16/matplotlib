# Report for assignment 4

## Project

Name: `matplotlib`

URL: https://github.com/matplotlib/matplotlib

A Python library that is used to visualize data and create graphs.

## Onboarding experience
We chose the same project as the one in Assignment 3. With the knowledge we learned from that assignment, setting up the development suite was easy this time around.

## Effort spent

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

### Description
The class Bbox is a representation of a bounding box and has a method `frozen` which returns a static independent copy of an object that should not be affected by changes to the original object. This method does however not copy the `minpos` attribute of this object which is needed in some edge cases.

### Scope (functionality and code affected)
Changes were only made in the Bbox class by overriding a parent method. This affects every class containing a `Bbox` which is all axes. However the fix will only be noticed in a few edge cases.

### Requirements for the new feature or requirements affected by functionality being refactored
The `frozen` method of the `Bbox` class should return a copy of a `Bbox` object containing both the bounding `points` and `minpos`.

*Optional (point 3): trace tests to requirements.*

### Code changes

#### Patch

`git diff 9c98ab0992915cf7c2be030c6b418eeefd0b0f25 7c535fb07d4a64c6ca9440a06a2c62ccba6d09ae`

*Optional (point 4): the patch is clean.*

*Optional (point 5): considered for acceptance (passes all automated checks).*

### Test results
*Overall results with link to a copy or excerpt of the logs (before/after
refactoring).*

- [Before](test-reports/mac-before-test.txt)
- [Added failing test](test-reports/mac-with-frozen-test.txt)
- [After]()

### UML class diagram and its description

#### Key changes/classes affected

*Optional (point 1): Architectural overview.*

*Optional (point 2): relation to design pattern(s).*

## Overview of issue #

Title:

URL:

### Description

### Scope (functionality and code affected)

### Requirements for the new feature or requirements affected by functionality being refactored
 <!-- Requirements related to the functionality are identified and described in a systematic way. Each requirement has a name (ID), title, and description. The description can be one paragraph per requirement. -->
 **Name:** Bbox frozen implementation (**ID: 1**)

**Title:** Implement method `Bbox::frozen()`

**Description:** 

The method `frozen()` of class `Bbox` is inherited from its parent class `BboxBase`. The function of this method is to return a frozen copy which will not be updated when its children change. As the class `Bbox` contains a property `minpos` that `BboxBase` does not have, the method `frozen()` should be overrided in `Bbox` to copy this property.

*Optional (point 3): trace tests to requirements.*
Test function `test_bbox_frozen_copies_minpos()` should be traced to requirement: **ID=1**.

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

What are your main take-aways from this project? What did you learn?

How did you grow as a team, using the Essence standard to evaluate yourself?

*Optional (point 6): How would you put your work in context with best software engineering practice?*

*Optional (point 7): Is there something special you want to mention here?*
