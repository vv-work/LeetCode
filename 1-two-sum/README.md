<h2><a href="https://leetcode.com/problems/two-sum/">1. Two Sum</a></h2><h3>Easy</h3><hr><div><p>Given an array of integers <code style="background-color: rgb(34, 36, 37) !important; color: rgb(194, 207, 213) !important;">nums</code>&nbsp;and an integer <code style="background-color: rgb(34, 36, 37) !important; color: rgb(194, 207, 213) !important;">target</code>, return <em style="color: rgb(234, 238, 241) !important;">indices of the two numbers such that they add up to <code style="background-color: rgb(34, 36, 37) !important; color: rgb(234, 238, 240) !important;">target</code></em>.</p>

<p>You may assume that each input would have <strong><em style="color: rgb(234, 238, 241) !important;">exactly</em> one solution</strong>, and you may not use the <em style="color: rgb(234, 238, 241) !important;">same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre style="background-color: rgb(34, 36, 37) !important; color: rgb(194, 207, 214) !important;"><strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong>Example 2:</strong></p>

<pre style="background-color: rgb(34, 36, 37) !important; color: rgb(194, 207, 214) !important;"><strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong>Example 3:</strong></p>

<pre style="background-color: rgb(34, 36, 37) !important; color: rgb(194, 207, 214) !important;"><strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code style="background-color: rgb(34, 36, 37) !important; color: rgb(194, 207, 213) !important;">2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code style="background-color: rgb(34, 36, 37) !important; color: rgb(194, 207, 213) !important;">-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code style="background-color: rgb(34, 36, 37) !important; color: rgb(194, 207, 213) !important;">-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than&nbsp;<code style="background-color: rgb(34, 36, 37) !important; color: rgb(194, 207, 213) !important;">O(n<sup>2</sup>)&nbsp;</code>time complexity?</div>