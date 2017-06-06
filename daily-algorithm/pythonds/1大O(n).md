
## 大O(n)
O(n)用来描述当规模 n 增加时，T(n)函数(表示程序执行步长的函数)中增长最快的部分。

**作业1：**
编写两个 Python 函数来寻找一个列表中的最小值，不改变列表。函数一将列表中的每个数都与其他数作比较，数量级是 O(n²).函数二的数量级是 O(n)。

```
# O(n²)
# 列表中每个数都与其他数比较，小于所有数为True，如果大于某个数为False
# 有个改进的方法"if i>j and issmallest"
def findMin(alist):
	min = alist[0]
	for i in alist:
		issmallest = True
		for j in alist:
			if i > j:
				issmallest = False
		if issmallest:
			min = i
	return min
```

```
# O(n)
# 使用一个额外变量
def findMin(alist):
	minsofar = alist[0]
	for i in alist:
		if i<minsofar:
			minsofar = i
	return minsofar
```

## 乱序字符串检查
乱序字符串是指一个字符串是另一个字符串的重新排列。例如，'heart' 和 'eahrt' 就是乱序字符串。'python' 和 'typhon' 也是。为了简单起见，我们假设这两个字符串具有**相等的长度**，并且他们由 26 个小写字母集合组成。

* 方法1-检查s1中的字符是否全部出现在s2中
将s2转换为列表。检查s1中的每个字符是否存在于第二个列表中，如果存在，第二个列表相应位置替换成 None。
时间复杂度O(n^2)

* 方法2-将两个字符串按字母顺序排序，看结果是否相同
时间复杂度取决于排序算法，O(nlogn)~O(n^2)

* 方法3-比较两个字符串是否具有相同数目的 a, b, c 等字符
用一个长度为 26 的列表，每个可能的字符占一个位置。每次看到一个特定的字符，就增加该位置的计数器。最后如果两个列表的计数器一样，则字符串为乱序字符串。
时间复杂度O(n)，空间复杂度O(1)，占用了两个额外列表的空间

方法1和2长度不同时不可用，方法3可在长度不同时使用


## python 列表
append() 比拼接快
```
def test1():	#拼接
    l = []
    for i in range(1000):
        l = l + [i]

def test2():	#append()
    l = []
    for i in range(1000):
        l.append(i)

def test4():	#列表构造函数，最快
    l = list(range(1000))
```

当列表末尾调用 pop 时，它需要 O(1), 但是当在列表中第一个元素或者中间任何地方调用 pop, 它是 O(n)。这样迥然不同的结果是由 Python 对列表的执行方式造成的。在 Python 的执行过程中，当从列表的第一位删除一个元素，其后的每一位元素都将向前挪动一位。你可能觉得这种操作很愚蠢，但这种执行方式会让 index 索引操作的复杂度降为 O(1)。

**作业二**
写一个寻找随机数列中第 k 小的数的 O(nlogn)的算法 。把算法改进为 O(n)。
```
# O(nlogn)-排序，取第k个数

```
