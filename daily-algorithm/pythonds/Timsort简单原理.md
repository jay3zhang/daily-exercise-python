**Timsort原理**

最好：O(n)
平均：O(nlogn)
最坏：O(nlogn)

**简单来说，Timsort是一种结合了归并排序和插入排序的混合算法，它基于一个简单的事实，实际中大部分数据都是部分有序（升序或降序）的。**

Timsort排序算法中定义数组中的有序片段为run，每个run都要求单调递增或严格单调递减（保证算法的稳定性），如下图所示

![timsort_run.png](http://image.3001.net/images/20150326/14273759403128.png!small)

抛开一些细节，Timsort排序算法可以概括成两步：

**第一步** 就是把待排数组划分成一个个run，当然run不能太短，如果长度小于minrun这个阈值，则用**插入排序**进行扩充。

**第二步** 将run入栈，当栈顶的run的长度**不满足**下列约束条件中任意一个时，
```
1. runLen[n-2] > runLen[n-1] + runLen[n]
2. runLen[n-1] > runLen[n]
```
则利用**归并排序**将其中最短的2个run合并成一个新run，最终栈空的时候排序也就完成了。

下面以一个实例进行说明，这个例子中我们设置minrun=4，也就是说run的最小长度不能小于4。每划分出一个run就将其入栈，如下图所示

![](http://image.3001.net/images/20150326/14273761027309.png!small "timsort_ex1.png")

**注意，此时栈顶的run是不满足约束条件的，因为此时runLen[0] < runLen[1]，所以要对这两个run进行归并，当然这个过程使用的是归并排序。**

如果遇到有序片段长度小于minrun，则要进行补齐，如下图所示

![](http://image.3001.net/images/20150326/14273761556221.png!small "timsort_ex2.png")

**注意，此时栈顶run是满足约束条件的，10 > 5 + 4，5 > 4，因此不需要进行归并。**

最后数组元素个数不足minrun了，只能作为一个run了

![](http://image.3001.net/images/20150326/14273761988859.png!small "timsort_ex3.png")

此时栈顶的run又不满足约束条件了，5 < 4 + 2，所以需要进行归并。后续过程如下图所示

![](http://image.3001.net/images/20150326/14273762306056.png!small "timsort_ex4.png")

这样排序过程就完成了~有的同学可能会有疑问，为什么要有那个奇怪的约束条件呢？每次入栈的时候直接进行归并不行吗？这主要是考虑到归并排序的效率问题，因为将一个长序列和一个短序列进行归并排序从效率和代价的角度来看是不划算的，而两个长度均衡的序列进行归并排序时才是比较合理的也比较高效的。

当然这里我们忽略了许多细节问题，如minrun的长度计算，插入排序和归并排序具体实现中的一些技巧。更多关于Timsort排序算法的细节请参考[OpenJDK 源代码阅读之 TimSort](http://blog.csdn.net/on_1y/article/details/30109975 "OpenJDK 源代码阅读之 TimSort")

**Timsort中的Bug**

了解了Timsort算法的过程和原理，好像没有什么逻辑上的问题，那么这个Bug到底出在哪呢？

这个Bug恰恰出现在那个约束条件上，因为Timsort算法设置这个约束条件的是为了**保证归并排序时两个子序列长度是均衡的**，隐含的一层意思是栈内所有run都应该满足该约束条件（即使不在栈顶），即对2 <= i <= StackSize-1，也必须满足

```
1. runLen[i-2] > runLen[i-1] + runLen[i]
2. runLen[i-1] > runLen[i]
```

在大多数情况下，仅检查栈顶的3个run是否满足这个约束条件是可以保证整个栈内所有run均满足该约束条件。但是在一些特殊的情况下就不行了，如下面这个栈（右侧为栈顶）
```120, 80, 25, 20, 30```

对照上面的源码，因为25 < 20 + 30，25 <30，所以将25和20两个run进行合并，此时栈内的情况变为 (**只能合并相邻的两个run**)
```120, 80, 45, 30```

**由于80 > 45 + 30，45 > 30，满足约束条件，此时归并就终止了。但是注意栈里的其他run，120 < 80 + 45，这是不满足约束条件的，而由于我们只判断了栈顶的run，因此在这里就留下了“隐患”。**

在大多数情况下，这个问题没什么大不了，不影响我们平时一般的排序操作，因为我们的数据没有那么多，更不会大量出现上述情况。但是这个国外技术团队精心构造了一个Array，成功的让Timsort算法报了java.lang.ArrayIndexOutOfBoundsException这个错误。他们还把复现这个错误的代码放在了github上，代码请戳[这里](https://github.com/abstools/java-timsort-bug)

* Timsort 相关资料：
1. [vimeo.com/146478455](https://vimeo.com/146478455) 概要的讲解timsort的实现以及timsort的bugs，因为是视频，所以相比论文我觉得更快看得懂，没字幕，听不懂怎么办，没事，[演讲者有一个文章重新梳理视频内容](http://www.envisage-project.eu/proving-android-java-and-python-sorting-algorithm-is-broken-and-how-to-fix-it/)

2. Tim peters自己写的论文  https://svn.python.org/projects/python/trunk/Objects/listsort.txt