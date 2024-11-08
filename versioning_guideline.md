## Versioning guidelines

### How module version works?
The goal of versioning is to make certain that any pipeline that uses a module
will keep on working after the modules as been updated to a new version. Therefore 
these are the rules that must be followed:

**Module version format: INPUT/OUTPUT.VALUES.INTERN ie: 10.2.42**

### Summary
The rule of thumb is: 

- If you add or remove an input or output, increment the **INPUT/OUPUT** number.
- If your changes modify in ANY WAY the values coming out of your outputs or the expected values for your input increment the **VALUES** number.
- If your change only impact the inner working of the module and has no impact outside of it, increment the **INTERN** number.

### INTERN number
Update the **INTERN** number when making a change that has no impact outside of the
working of the module.

- Refactoring your code.
- Adding comments.
- Adding logs.
- Performance improvements.
- Changing the category of a module.

### VALUES number
Update the **VALUES** number whenever you make a change that modify in ANY WAY the
values expected from the inputs or going out of your outputs. The goal is to identify the versions that 
modify the result of a module.

> **_NOTE:_**  Reset the **INTERN** number to zero when incrementing the **VALUES** number, ie: 9.2.1 -> 9.3.0

### INPUT/OUPUT number
Update the **INPUT/OUPUT** number whenever you add or remove an input or output. These changes has a tendency to break a pipeline.

> **_NOTE:_**  Reset the **INTERN** and **VALUES** numbers to zero when incrementing the **INPUT/OUPUT** number, ie: 9.2.1 -> 10.0.0

# How package version works?
The package's version is directly related to its modules and follow the same format:

**Module version format: INPUT.OUTPUT.INTERN, ie: 10.2.42**

### Summary
The rule of thumb is: 

- Increment the **INTERN** number if it contains ONLY **INTERN** modification.
- Increment the **VALUES** number if it contains ANY **VALUES** modifications. (Reset the **INTERN** number to zero)
- Increment the **INPUT/OUTPUT** number if it contains ANY **INPUT/OUTPUT** modification. (Reset the **INTERN** and **VALUES** numbers to zero)