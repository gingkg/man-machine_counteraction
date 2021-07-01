**D\*：** D\*

**适用场景：**

D\*的算法名称源自“Dynamic A\*”的缩写。顾名思义，该算法适合处理“动态图”。首次使用A\*和使用D\*寻路在效率上没有区别。但是如果在完成寻路之后图发生了更改（比如机器人移动的过程中出现了新的障碍物，又比如导航仪在已经寻路之后的路径中遇到了拥堵需要绕路），如果采用A\*算法则需要重新执行算法以便找到一条新的路径，但如果采用D\*则只需要花较短的时间（通常很短，具体取决于对图修改的情况）即可修正原有路径从而得到新的路径。因此D\*适用于那些对图进行频繁小规模修改，对时间复杂度要求高的场景。

**算法类型：**

开源实现

**算法简介：**

D\*（中文通常读作D星，英文读作D-Star）算法实际上是三个增量搜索算法的统称，分别是原始D\*、Focused D\*和D\* Lite，这三种搜索算法均被设计用于解决基于假设的路径规划问题。譬如在自由空间假设下做路径规划——采用D\*算法的机器人在一片未知的地形中完成导航至一个给定的坐标的任务时，会首先假设那些地形中不可见的部分没有障碍物。机器人跟随按照这个假设所规划出的路径进行移动。当机器人发现新的地图信息（如新的障碍物）时，会把这个信息添加到地图上，然后重新规划一个从当前坐标到目标的最短路径，并不断重复这个流程直到抵达目的地，或者发现目的地无法抵达。当机器人行走在未知的地形时，会频繁发现新的障碍物，因此更新路径的运行速度必须足够快。增量式搜索算法通过缓存过往数据来加速搜索当前的路径，假设目的地不变的情况下，D\*的三个分支在重规划上的运行效率均快过A*。

**开源实现：**

https://github.com/mdeyo/d-star-lite

# d-star-lite

This poject is based on the original [D* Lite paper](http://idm-lab.org/bib/abstracts/papers/aaai02b.pdf) by Sven Koenig and Maxim Likhachev.

The D* Lite algorithm was written to be a "novel fast replanning method for robot navigation in unknown terrain". It searches "from the goal vertex towards the current vertex of the robot, uses heuristics to focus the search" and efficiently uses the priortity queue to minimize reordering.

### Use of the project

Currently written for Python 3 and the biggest requirement is having Pygame. Instructions for installing pygame can be found at https://www.pygame.org/wiki/GettingStarted.

Run the example demo with `python3 main.py` (or `python main.py` if you have Python 3 installed as such on your system or in your environment). The demo shows off the dynamic replanning ability of the path planning algorithm by allowing the user to add obstacles by clicking on cells in the grid. Our mobile agent is the red circle, while the goal cell is green. The agent has a visibility range, shown by the thin black lines, and added obstacles are not taken into account by the agent until they are visible and change to darker grey. Pressing space bar makes the agent observe new obstacles, replan if necessary, and advances on the current best path until the goal is reached.

More notes to come on how the code is organized...

Feel free to add more specific questions about the project in comments on issue #1, so that I can add better documentation.



**参考文献：**

[1] Stentz, Anthony (1994), "Optimal and Efficient Path Planning for Partially-Known Environments", Proceedings of the International Conference on Robotics and Automation: 3310–3317, CiteSeerX 10.1.1.15.3683
[2] Stentz, Anthony (1995), "The Focussed D* Algorithm for Real-Time Replanning", Proceedings of the International Joint Conference on Artificial Intelligence: 1652–1659, CiteSeerX 10.1.1.41.8257
[3] Hart, P.; Nilsson, N.; Raphael, B. (1968), "A Formal Basis for the Heuristic Determination of Minimum Cost Paths", IEEE Trans. Syst. Science and Cybernetics, SSC-4 (2): 100–107, doi:10.1109/TSSC.1968.300136
[4] Koenig, S.; Likhachev, M. (2005), "Fast Replanning for Navigation in Unknown Terrain", Transactions on Robotics, 21 (3): 354–363, CiteSeerX 10.1.1.65.5979, doi:10.1109/tro.2004.838026