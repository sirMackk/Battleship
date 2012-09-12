Battleship

What is it?

This program is a python 2.7.2 simulation of the classic board game called "Battleship".

Why?

To practic python, to learn using git, to learn how to do unit testing.

I'm still very new to python and completely new to unit testing as well as VCS so this is my training ground. Because of the nature of this project I won't accept any commits, however any pointers are more than welcome.

Who?

sirMackk on github.com

Update and Debriefing

The project is closed. There are a few bugs left. One is that ships can overlap, which hasn't happened before, this is due to a quick fix done earlier this week that messed up some other function. The other is that the CPU can hit the same spot twice and it will take away a ship's HP.

I decided to leave this project as it is and take all that I've learned and move onto other things. What have I learned?
 
- More unit testing. I should focus on a few main cases and a few edge cases. And write code for all classes and functions. For the past few days, since writing the last tests, I was using the debugger to figure stuff out, which in perspective takes more time and nerves.

- More OOP. This can be seen throughout the whole project. I could've divided the project into more classes and used inheritence. The board could have it's own class and it's own methods, for example. Or I could make a ship superclass and derive subclasses for specific ships. This would make things more tidy and easier to fix.

- Should have a blueprint at the start. When I started this project, all I had was a general outline of how the screen should look for the player and a few functions that made the whole thing work. No division into classes or into data+functions. I made everything up as I went along, hence the large number of fixes and the two final bugs, which I don't wanna fix now because it would involve digging through all the code - the code is mishmashed and it's hard to define exactly what thing does what.