**QMIX：**QMIX

**适用场景：**

​    合作型多智能体强化学习问题，即Dec-POMDP（所有智能体共享同一个Reward信号，但每个智能体有各自的观测集、动作集，所有智能体的联合观测可以只包含部分和环境状态S有关的信息）。虽然QMIX本身对每个智能体是否相同（Invariance）没有要求，但如果每个智能体彼此相同，则可以采用Weight sharing技巧来提高样本利用率（Sample Efficiency），从而加速训练。

**算法类型：**

开源实现

**算法简介：**



​    在QMIX被提出之前，通过集中训练-去中心化部署的途径解决合作型多智能体强化学习问题（Dec-POMDP）的主流方法是VDN（Value-Decomposition Networks）。该方法为了满足IGM（个体-全局最大化，individual-global maximization）条件所采取的主要手段是对Q函数进行加性分解，并通过反向传播来实现隐性信用分配。由于VDN采用加性分解，所以模型对联合Q函数的表达能力就受到了很大的局限（联合Q值必须是每个Q函数的加和）。QMIX算法放宽了模型对联合Q函数表达能力的限制，使得模型拟合的联合Q函数不再必需是关于每个智能体的Q函数的加和。因为本质上，VDN的加性Q分解之所以能够满足IGM条件，是可以利用求和函数的单调性通过反证法证明出来的。反过来，只要联合Q函数是关于每个智能体各自的Q函数的单调函数，就可以利用同样的论证来推出IGM条件。根据这个观察，就可以进一步放宽联合Q函数模型的函数集，由求和函数放宽至单调函数。QMIX通过对混合网络（Mixing network）的权重施加非负性约束来保证其单调性。根据Dugas等人于2009年给出的理论分析，施加了约束的混合网络可以以任意误差逼近任意单调函数。在实验方面，QMIX在多个星际争霸微操环境设定下性能均以较大的比分差距优于VDN算法。



**开源实现：**

https://github.com/starry-sky6688/StarCraft

**参考文献：**

[1] Tabish Rashid, Mikayel Samvelyan, Christian Schroeder de Witt, Gregory Farquhar, Jakob Foerster, Shimon Whiteson: “QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning”, 2018; arXiv:1803.11485.