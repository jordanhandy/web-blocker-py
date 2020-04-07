# Website Blocker
This program takes defined websites in a Python lists, and adds them to the user's hosts file, pointing to the system loopback IP, simulating a block.

The scipt checks the current time, to only enforce the block during certain hours.
It runs once an hour to check the current time
## To-Do

* Implement User input to allow for modification of website URLs instead of directly modifying script.  Either:
  * cmd line
  * GUI