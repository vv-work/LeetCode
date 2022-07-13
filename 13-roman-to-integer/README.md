<h2><a href="https://leetcode.com/problems/roman-to-integer/">13. Roman to Integer</a></h2><h3>Easy</h3><hr><div><p>Roman numerals are represented by seven different symbols:&nbsp;<code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">I</code>, <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">V</code>, <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">X</code>, <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">L</code>, <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">C</code>, <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">D</code> and <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">M</code>.</p>

<pre style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 206) !important;"><strong>Symbol</strong>       <strong>Value</strong>
I             1
V             5
X             10
L             50
C             100
D             500
M             1000</pre>

<p>For example,&nbsp;<code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">2</code> is written as <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">II</code>&nbsp;in Roman numeral, just two ones added together. <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">12</code> is written as&nbsp;<code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">XII</code>, which is simply <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">X + II</code>. The number <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">27</code> is written as <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">XXVII</code>, which is <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">XX + V + II</code>.</p>

<p>Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">IIII</code>. Instead, the number four is written as <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">IV</code>. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">IX</code>. There are six instances where subtraction is used:</p>

<ul>
	<li><code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">I</code> can be placed before <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">V</code> (5) and <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">X</code> (10) to make 4 and 9.&nbsp;</li>
	<li><code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">X</code> can be placed before <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">L</code> (50) and <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">C</code> (100) to make 40 and 90.&nbsp;</li>
	<li><code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">C</code> can be placed before <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">D</code> (500) and <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">M</code> (1000) to make 400 and 900.</li>
</ul>

<p>Given a roman numeral, convert it to an integer.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 206) !important;"><strong>Input:</strong> s = "III"
<strong>Output:</strong> 3
<strong>Explanation:</strong> III = 3.
</pre>

<p><strong>Example 2:</strong></p>

<pre style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 206) !important;"><strong>Input:</strong> s = "LVIII"
<strong>Output:</strong> 58
<strong>Explanation:</strong> L = 50, V= 5, III = 3.
</pre>

<p><strong>Example 3:</strong></p>

<pre style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 206) !important;"><strong>Input:</strong> s = "MCMXCIV"
<strong>Output:</strong> 1994
<strong>Explanation:</strong> M = 1000, CM = 900, XC = 90 and IV = 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">1 &lt;= s.length &lt;= 15</code></li>
	<li><code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">s</code> contains only&nbsp;the characters <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">('I', 'V', 'X', 'L', 'C', 'D', 'M')</code>.</li>
	<li>It is <strong>guaranteed</strong>&nbsp;that <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">s</code> is a valid roman numeral in the range <code style="background-color: rgb(25, 26, 27) !important; color: rgb(183, 198, 205) !important;">[1, 3999]</code>.</li>
</ul>
</div>