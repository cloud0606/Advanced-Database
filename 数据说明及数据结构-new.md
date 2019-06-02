# 数据说明

---翻译整理于ml-latest.zip内的 README.txt

## 数据集
该数据集（ml-latest）描述了电影推荐服务[MovieLens]（http://movielens.org） 的5星评级和自由文本标记活动。 它包含57598部电影的27753444个评级和1108997个标签应用程序。 这些数据是由，共有283228位用户在1995年1月9日到2018年9月26日期间创建的。这个数据库是在2018年9月26日生成的。

* 数据集
![Alt Image Text](https://github.com/cloud0606/Advanced-Database/blob/master/img/%E6%95%B0%E6%8D%AE%E8%A1%A8%E7%BB%93%E6%9E%842.png)
（同一种颜色表示相同数据）

* ER图
![Alt Image Text](https://github.com/cloud0606/Advanced-Database/blob/master/img/E-R%E5%9B%BE1.png)

## 数据详细说明
* **User Ids** 在 `ratings.csv`和`tags.csv`中是一样的（i.e. 同样的id在两个文件中代表同一个用户）

  
  
* **Movie Ids** 至少拥有一条rating或者一条tag的数据才会被收录到数据集中，movieId在 `ratings.csv`, `tags.csv`, `movies.csv`, and `links.csv` 是一样的。的（i.e. 同样的id在四个文件中代表同一部电影）   

  
* **等级数据文件结构 (ratings.csv)** 所有评级都包含在`ratings.csv`文件中。 标题行后面的此文件的每一行代表一个用户对一部电影的评级，并具有以下格式：  	`userId,movieId,rating,timestamp`
	* 此文件中的行首先由userId排序，然后由movieId排序。
	* rating为5星级，半星增量（0.5星-5.0星）。
	* timestamp表示自1970年1月1日午夜协调世界时（UTC）以来的秒数。

	  
* **标签数据文件结构 (tags.csv)** 所有标签都包含在`tags.csv`文件中。 标题行之后的此文件的每一行代表一个用户应用于一个电影的一个标记，并具有以下格式：
   `userId,movieId,tag,timestamp`
	* 此文件中的行首先由userId排序，然后在同一个用户内由movieId排序。
	* tag是用户生成的有关电影的元数据。 每个标签通常是单个单词或短语。 特定标签的含义，价值和目的由每个用户决定。
	* timestamp表示自1970年1月1日午夜协调世界时（UTC）以来的秒数。


* **电影数据文件结构 (movies.csv)** 电影信息包含在`movies.csv`文件中。 标题行之后的此文件的每一行代表一部电影，并具有以下格式：  
	`movieId,title,genres`
	* 手动输入电影标题或从<https://www.themoviedb.org/>导入电影标题，并在括号中包含发行年份。 这些标题中可能存在错误和不一致。
	* 类型是以管道分隔的列表，可从以下选项中选择：
		* Action
		* Adventure
		* Animation
		* Children's
		* Comedy
		* Crime
		* Documentary
		* Drama
		* Fantasy
		* Film-Noir
		* Horror
		* Musical
		* Mystery
		* Romance
		* Sci-Fi
		* Thriller
		* War
		* Western
		* (no genres listed)
		
		
* **链接数据文件结构 (links.csv)**  可用于链接到其他电影数据源的标识符包含在`links.csv`文件中。 标题行之后的此文件的每一行代表一部电影，并具有以下格式：   
`movieId，imdbId，tmdbId`
	* movieId是<https://movielens.org>使用的电影的标识符。 例如，电影“玩具总动员”的链接为<https://movielens.org/movies/1>。
	* imdbId是<http://www.imdb.com>使用的电影的标识符。 例如，电影“玩具总动员”有链接<http://www.imdb.com/title/tt0114709/>。
	* tmdbId是<https://www.themoviedb.org>使用的电影的标识符。 例如，电影“玩具总动员”的链接为<https://www.themoviedb.org/movie/862>。
	* 使用上面列出的资源受每个提供商的条款约束。
* **标签基因组 (genome-scores.csv 和 genome-tags.csv)**
该数据集包括标签基因组的当前副本。
	* [基因组论文]：http：//files.grouplens.org/papers/tag_genome.pdf
	* 标签基因组是包含电影的标签相关性分数的数据结构。结构是一个密集的矩阵：基因组中的每部电影都有一个基因组*every*标签的值。
	* 正如[本文] [基因组论文]所述，标签基因组编码电影表现出标签所代表的特定属性的强烈程度（大气，发人深省，现实等）。使用机器学习算法对用户贡献的内容（包括标签，评级和文本评论）计算标签基因组。
	* 基因组分为两个文件：
		* 文件`genome-scores.csv`包含以下格式的电影标签相关数据：
		 `movieId,tagId,relevance`
		* 文件`genome-tags.csv`以下列格式提供基因组文件中标签ID的标签描述：
		`tagId,tag`
			* 导出数据集时会生成`tagId`值，因此它们可能因MovieLens数据集的版本而异。

	如果引用标签基因组数据，请包括以下引文：

> Jesse Vig, Shilad Sen, and John Riedl. 2012. The Tag Genome: Encoding Community Knowledge to Support Novel Interaction. ACM Trans. Interact. Intell. Syst. 2, 3: 13:1–13:44. <https://doi.org/10.1145/2362394.2362395>

## 问题

* `tags.csv`和`genome-tags.csv`中的tag存在大小写不一致的情况
