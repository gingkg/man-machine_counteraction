**A\*：**A\*

**适用场景：**

类似于启发式搜索，A\*需要利用额外信息来优化搜索过程。该额外信息是指定义在每个图节点上的损失函数，其作用是供算法决定搜索的优先级。（对于地图上的寻路任务而言，该函数通常定义为地图上的每个点到目标点的欧氏距离。）因此，A\*算法不适用于无法获取这类额外信息的路径搜索问题。此外，由于采用了图预处理的算法比A\*具有更低的最坏情况空间复杂度，因此A\*算法更适用于那些无法靠预处理图来提升性能的场景。（例如：假设某个任务只需要在每张图上做一遍寻路，而非同一张图反复更换起点和终点去做很多遍寻路，那么就没有预

**算法类型：**

开源实现

**算法简介：**

A\*（中文通常读作A星，英文读作A-Star）是一种图遍历和路径搜索算法，因具有良好的完整性（Completeness）、最优性（Optimality）、优效性（Optimal efficiency）而经常被用在很多计算机科学的领域。直到今天，A\*依然在游戏AI中被广泛应用。尽管有着种种优点，但A\*也并非完美。事实上，A\*应用在工程实践中有较多的限制，其中的一个主要的缺点是它的空间复杂度过高（O(b^d)），这主要是由于它将所有生成的节点存储到内存中。因此，在现实中的寻路导航软件中，A\*的性能往往被可以通过图预处理来获得更高性能的其它算法所超越。

**开源实现：**

https://gist.github.com/jamiees2/5531924

**参考文献：**

[1] Hart, P. E.; Nilsson, N. J.; Raphael, B. (1968). "A Formal Basis for the Heuristic Determination of Minimum Cost Paths". IEEE Transactions on Systems Science and Cybernetics. 4 (2): 100–107. doi:10.1109/TSSC.1968.300136.
[2] Russell, Stuart J. (2018). Artificial intelligence a modern approach. Norvig, Peter (4th ed.). Boston: Pearson. ISBN 978-0134610993. OCLC 1021874142.
[3] Delling, D.; Sanders, P.; Schultes, D.; Wagner, D. (2009). "Engineering Route Planning Algorithms". Algorithmics of Large and Complex Networks: Design, Analysis, and Simulation. Lecture Notes in Computer Science. 5515. Springer.