<h2>608. Tree Node</h2><h3>Medium</h3><hr><div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></a></div><div><p>Given a table <code>tree</code>, <b>id</b> is identifier of the tree node and <b>p_id</b> is its parent node's <b>id</b>.</p>

<pre>+----+------+
| id | p_id |
+----+------+
| 1  | null |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+
</pre>
Each node in the tree can be one of three types:

<ul>
	<li>Leaf: if the node is a leaf node.</li>
	<li>Root: if the node is the root of the tree.</li>
	<li>Inner: If the node is neither a leaf node nor a root node.</li>
</ul>

<p>&nbsp;</p>
Write a query to print the node id and the type of the node. Sort your output by the node id. The result for the above sample is:

<p>&nbsp;</p>

<pre>+----+------+
| id | Type |
+----+------+
| 1  | Root |
| 2  | Inner|
| 3  | Leaf |
| 4  | Leaf |
| 5  | Leaf |
+----+------+
</pre>

<p>&nbsp;</p>

<p><b>Explanation</b></p>

<p>&nbsp;</p>

<ul>
	<li>Node '1' is root node, because its parent node is NULL and it has child node '2' and '3'.</li>
	<li>Node '2' is inner node, because it has parent node '1' and child node '4' and '5'.</li>
	<li>Node '3', '4' and '5' is Leaf node, because they have parent node and they don't have child node.</li>
	<br>
	<li>And here is the image of the sample tree as below:
	<p>&nbsp;</p>

	<pre>			  1
			/   \
                      2       3
                    /   \
                  4       5
</pre>

	<p><b>Note</b></p>

	<p>If there is only one node on the tree, you only need to output its root attributes.</p>
	</li>
</ul>
</div>