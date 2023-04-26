# Win_Condition_Minimax

<h4> This was written in partial fulfillment of the requirements for the Degree of Master of Science in Computer Science at Bridgewater State University </h4>

<h2> Running and Configuring </h2>
Compile and run however you would with a python program. The only files that needs to be edited will be the `Domineering_Simulation.py` file which contains the main method, and graphs.txt to change the graph the Minimax functions are run on. The board is stored as a matrix (array of arrays), and so to add a domino to the board one needs to put a tuple of ordered pairs [ (yx) (yx) ]. 


The three tests located in the main file are 
<h2> Speed Test </h2>
Wincon Minimax's speed is compared to Traditional Minimax's speed. In more scenarios, Traditional Minimax should excel in this category.

<h2> Depth Test </h2>
Wincon Minimax is run and when one or more wins are found, the algorithm does not travel any deeper. The depth Wincon Minimax went to is then saved, and Traditional Minimax is run to see if it finds any end-of-game board states at the same depth. Wincon should excel.

<h2> Accuracy Test </h2>
Wincon Minimax finds as many wins as it can given a certain recursive depth. The list of boards in which it declares a win is saved and Traditional Minimax is run until the end of those games to verify whether Wincon Minimax correctly assumed victory. To do this, it checks every possible end game, and records whether the winning player is vertical or horizontal. It then displays two percentages: The percentage of games in which a win for the AI player is confirmed, and the percentage of total end games in which the AI wins (as boards may contain, say, 3 ways for the AI to win and 1 way for the opponent to win, we want to account for this percentage as well). The first percentage should be nearly 100%. The second percentage should be, Ideally, above 50% in every scenario.
