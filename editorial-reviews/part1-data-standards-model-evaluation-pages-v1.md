# 第一编第3—4章：资料规范与模型评价原页核验 V1

**核验日期：** 2026-10-17（UTC）。

**基线：** `AI-Archaeology/AI-Archaeology-Textbook`，PR #45 合并后的 `main 8e17c1d3b88d1c3e6b3c8ed939ae9317305863fe`。

**本轮状态：** FAIR、CIDOC CRM和James等的指定原文与页图核验完成；Comer仍为公开全文转录及书目/摘要核实。用户已完成本地Quarto渲染及两章预览访问，远端HTML与搜索索引验收通过；PR #46本轮合并条件已满足，见第7节。

## 1. 范围与接续关系

本轮只处理第3章3.8节现有的本体、CIDOC CRM和FAIR两段说明，以及第4章4.4节“资料偏差与模型泛化”的一个段落。同步[第一编论断矩阵](part1-claim-original-page-interpretation-matrix-v1.md)。不增加教材小节、公式、操作流程或练习。

GitHub预检确认：PR #37、#39均已合并，不再按历史Draft状态处理；PR #45已完成本地渲染和远端发布核验后合并。预检时唯一未关闭的PR为无关Draft #12，本轮不改动。此前17份附件的筛选与第2章采用结果见[新增文献初评](part1-new-literature-assessment-v1.md)，本轮没有重新宣称已读完这些原著。

核验所读的James原书第5章是第4章既有模型评价论点的参考来源，不是开展本教材第5章写作。

## 2. 采用版本与读取等级

| 来源 | 版本和正式入口 | 本轮实际读取范围 |
|---|---|---|
| Wilkinson等，2016，FAIR原始论文 | *Scientific Data* 3:160018；DOI [10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18)；[出版社PDF](https://www.nature.com/articles/sdata201618.pdf) | 出版社原文及PDF；页图目视第1、4、5、8页。正文所用条款在第4页框2 |
| Bekiari等编，2024，CIDOC CRM | *Definition of the CIDOC Conceptual Reference Model*, Volume A，version 7.1.3，February 2024；[官方版本页](https://cidoc-crm.org/Version/version-7.1.3)、[正式定义PDF](https://cidoc-crm.org/sites/default/files/cidoc_crm_version_7.1.3.pdf) | 封面及第9—11页原文与页图；所用模型目的和录入规则边界在第9—10页 |
| James等，2023，Python版统计学习教材 | *An Introduction to Statistical Learning with Applications in Python*，第1版；Springer，DOI [10.1007/978-3-031-38747-0](https://doi.org/10.1007/978-3-031-38747-0)；[作者官网](https://www.statlearning.com/) | 官方作者版原文及指定页图：16—18、28—34、201—204、206—209、212—215页；另核作者版题名页和出版社公开前置页 |
| Comer等，2023，Fort Irwin研究 | *Journal of Archaeological Science: Reports* 48:103824；DOI [10.1016/j.jasrep.2022.103824](https://doi.org/10.1016/j.jasrep.2022.103824) | 作者关联的公开全文转录复核、机构书目与摘要；未取得原PDF或原页图，维持原有证据等级 |

以上“页图目视”仅指列出的页面，不能写成整部原著均已逐页目视。原文读取、图像检查、资料取得和模型复现分别记录；本轮没有运行Notebook或重做实证研究。

### 2.1 版本细节

**FAIR。** 现有书目作者、年份、篇名、卷与文章号正确，保留原条目。当前出版社PDF共9页，所用页的纸面页码与文件页序一致。首页带补遗标记；已读[2019年出版社补遗](https://www.nature.com/articles/s41597-019-0009-6)，其正文只更新原则维护网页的地址，不列出本轮使用条文的变更。论文年份仍为2016，不能用PDF内部2019文件日期代替。

**CIDOC CRM。** [官方版本目录](https://cidoc-crm.org/versions-of-the-cidoc-crm)将7.1.3标为 `Official (ISO Correspondence)`。本轮明确采用这一版本，不写“最新”，也不把目录中的另一状态标签 `Stable` 代入。正式文件共234页，所核页的印刷页码与文件页序一致。封面写明2024年2月，版权行中的2022不是本版本年份。8位编辑依封面为Chryssoula Bekiari、George Bruseker、Erin Canning、Martin Doerr、Philippe Michon、Christian-Emil Ore、Stephen Stead和Athanasios Velios；新增章末书目与这一责任说明一致。

**James。** 书目为Gareth James、Daniela Witten、Trevor Hastie、Robert Tibshirani、Jonathan Taylor五位作者，2023年Python版；现有章末条目已包含这些信息，无需重复新增。出版社著录为XV、607页，电子书ISBN 978-3-031-38747-0。正文PDF来自作者官网的[下载入口](https://hastie.su.domains/ISLP/ISLP_website.pdf.download.html)，该入口明确转向作者关联的公开Google Drive文件（文件ID：`1ajFkHO6zjrdGNqhqW1jKBZdiNGh_8YQ1`）。题名页标示首次印刷日期为2023年7月5日，PDF内部8月文件日期不是新版声明。

作者PDF含613个文件页面，部分前置页及空白页与出版社版本不同，**不得套用一个固定页码偏移**：

| 原书位置 | 作者PDF页序（从1计） | 使用目的 |
|---|---:|---|
| 印刷第1页 | 12 | 说明全书偏移不固定 |
| 印刷第16—18页 | 26—28 | 误差项前提与不可约误差范围 |
| 印刷第28—31页 | 38—41 | 训练与测试误差；2.2.2节在31页开始 |
| 印刷第32—34页 | 42—44 | 式(2.7)、偏差与方差的定义及说明 |
| 印刷第201—204页 | 209—212 | 评价/选择与验证集法 |
| 印刷第206—208页 | 214—216 | k折交叉验证及其两种用途 |
| 印刷第212—215页 | 220—223 | 5.2节为自助法，校正原矩阵定位 |

另从[出版社公开前置页](https://link.springer.com/content/pdf/bfm:978-3-031-38747-0/1)核对题名与版权信息；该独立PDF的文件第3—4页没有显示纸面页码，不把其文件页序当作正文印刷页码。[作者官方勘误](https://www.statlearning.com/errata-python-edition)列出的212、214页软件名与图表/符号问题不改变本轮所用的偏差—方差解释及交叉验证定位。

## 3. 论断—原页—限制—考古应用

| 教材论断或内部核验项 | 原页或条款 | 原文支持与限制 | 本轮处理 |
|---|---|---|---|
| FAIR“可获取”可以有访问条件，“可重用”须说明许可 | Wilkinson等，第4页框2，A1.2、R1.1；同页正文 | 认证、授权和许可均有明确依据。A1.1的开放性说的是通信协议；A2区分数据与元数据可得性。第5页说明FAIR是指导原则，非其自身即为实现规范 | 第3章补入精确页码，采用“身份认证和访问授权”“使用许可”；“永久标识”改为“持久标识” |
| 文化遗产本体帮助整合不同来源资料 | CIDOC CRM 7.1.3，第9—10页Introduction / Objectives | 正式概念及关系支持交换、整合；模型不包办实际数据录入规则。没有核验任何具体数据库对全部类和属性的符合性 | 第3章加入版本链接、页码及正式书目，保留普通语言关系示例 |
| 模型偏差与方差有特定统计含义 | James，第32—34页；式(2.7)在第32页 | 在回归的期望平方误差讨论中，区分偏差平方、估计的方差与误差项方差；不同训练数据集导致同一输入处的拟合预测变化。不是对全部考古不确定性的统一分解 | 第4章补足“方差”的直观含义，保留“可能”等条件性措辞 |
| 训练成绩不能保证未参与训练资料的表现 | James，第28—31页，2.2.1节 | 区分训练和未见资料的预测误差；第31页说明不能仅凭训练/测试误差有差距就认定过拟合 | 第4章收紧引文至第28—31页；Goodfellow的原有节号引用保留，未借此提升其证据等级 |
| 公式前提与考古样本独立性须分开 | James，第16页及第17—18页 | 原书明确误差项与输入独立、均值为零；不可约误差相对于给定输入而言。这不等于田野观察单位独立，也不能把所有保存/记录问题归为不可约误差 | 只在内部记录前提及应用边界，正文保持定性 |
| 交叉验证的评价与选择用途 | James，5.1.1节第202—204页；5.1.3节第206—208页 | 随机分组过程在第206页；第208页区分估计独立数据上的误差与选择误差曲线的最小位置。所核页段未提供一般性的训练/目标同分布保证或空间分组验证方案 | 关闭所核页段的“仅有目录”状态；不向正文增加操作课程 |
| 原矩阵中的5.2节定位 | James，第212—215页 | 5.2节是bootstrap，用于重抽样估计不确定性，不是另一交叉验证小节 | 在矩阵中将交叉验证定位收紧至5.1的实际所用段落 |

FAIR段的遗址位置、图像授权、社区权益，以及本体段的器物、发掘、测量和照片关系，是教材的考古应用示例，不是来源逐字给出的实例或正式属性映射。条件访问不自动赋予共享权，FAIR与CIDOC也不证明材料完整或历史解释正确。

第4章对保存/取样偏差和模型偏差的区分，是以考古资料形成过程与统计定义相互对照的教材解释。James的通用统计说明不能单独证明某种考古随机划分有效，更不能证明跨遗址推广能力。“所核段落未明确给出某条件”只限定本轮读取范围，不代表整部书从未讨论该问题。

## 4. Comer的有限检索结果

现有段落和书目维持。再次读取[作者关联的公开全文转录](https://www.academia.edu/97590860/Sampling_methods_for_archaeological_predictive_modeling_Spatial_autocorrelation_and_model_performance)及[悉尼大学发表记录](https://profiles.sydney.edu.au/ioana.dumitru/publications)，其内容仍与教材第4.7节所引原论文§3印刷第5页、§5印刷第7—8页的论断和转录页码标记吻合：

- 逐次留出遗址或非遗址区域后，仍对所抽取像元评分。
- 随机像元评价分数较高，作者从空间自相关解释差异，并说明两种方案均未使用真正独立的数据。
- 像元分类成绩不能直接等同于新地区完整遗址的发现能力；这一教材限定保留。

[Elsevier开放稿入口](https://www.sciencedirect.com/science/article/am/pii/S2352409X22004874)已定位，但未成功读取；正常公开访问返回403或“Site Unavailable”HTML，未得到PDF。作者页面下载链接同样未取得可读PDF。[JHU作者发表列表](https://www.cis.jhu.edu/~parky/CEP-Publications/journal.html)中的文章号103814与机构记录及DOI不符，不据其替换已核定的103824。

**仍未完成：** 原PDF页面与Figure 5的目视核验；受限原始考古数据的复现。错误响应文件的哈希不属于原论文哈希，不能作为PDF取得证据。未继续扩大检索或改写现有段落。

## 5. 内部来源指纹

以下是实际取得的PDF指纹，便于后续确认同一文件；PDF、页图和长篇文本抽取不进入公共教材仓库。

| 内部阅读文件 | 字节数 / 文件页数 | SHA-256 |
|---|---|---|
| FAIR出版社PDF | 254899 / 9 | `cdddd9f4808f7e3e1f013139c3915ef4d7cdccb008fa947ef5f72b4c7b6ffde7` |
| CIDOC CRM 7.1.3正式PDF | 4596749 / 234 | `412af0e764209389b42735fb50088f3ce670943ef3e7d0214ed197f775bb5553` |
| James作者官网PDF | 20053984 / 613 | `278d3bdd49a8a480c2ff8e03245822caad8a3a48e81afd6d039c52c8fc13ad60` |
| James出版社前置页PDF | 1556669 / 14 | `b56ce37e1e30ef0b2bb91e3670e718df07beb6827c1a4220b3bcc57a31fbbba9` |

Comer本轮没有取得原PDF，不填原PDF哈希或页数。

## 6. 修订与验收

本轮涉及4个源文件：

- `chapters/chapter-03.qmd`：两段说明及一条CIDOC参考文献。
- `chapters/chapter-04.qmd`：一个既有模型评价段落。
- `editorial-reviews/part1-claim-original-page-interpretation-matrix-v1.md`：同步来源等级、页码和接续状态。
- `editorial-reviews/part1-data-standards-model-evaluation-pages-v1.md`：本报告。

**独立内容复核：** 第3章两段及8位编辑书目通过来源对照；第4章“同一输入、不同训练数据集”的解释及两组页码通过原页对照。保留全部可见标题和既有锚点。没有扩写交叉验证教程，也没有将来源核验进度放入教材正文。

**源文件结构检查：通过。** 与基线比较后，第1—4章的全部标题行一致（分别18、20、18、18行），主节数保持7/8/9/8。每章只有一个末尾“参考文献”，条目无重复；第3章仅新增CIDOC条目，其余既有条目保留。具体数量如下：

| 章 | 编号主节数 | 末尾参考文献条目数 |
|---|---:|---:|
| 第1章 | 7 | 10 |
| 第2章 | 8 | 23 |
| 第3章 | 9 | 12 |
| 第4章 | 8 | 13 |

第1—2章内容与基线blob一致；第3—4章所有可见标题、显式锚点与代码围栏数量保持不变。四个源文件通过空白检查，第1—4章通过Pandoc Markdown解析；这不是Quarto渲染结果。矩阵含18条具体核验记录。

**本地与远端验收：通过。** 用户已运行全站 `quarto render`、`quarto preview` 并推送生成提交 `87491502`。远端两章HTML、目录、参考文献与三条更新的搜索记录已和源稿核对，详见第7节。该验收依据用户终端日志与远端文件检查，不表述为独立重现用户macOS上的视觉版面。

本轮关闭的是上述指定引用的来源定位问题。矩阵中其他研究的原页图像、补充材料、历史档案及数据复现限制继续保留；全书学术终审、教学试用和A6实证复现状态均未因本轮自动改变。

## 7. PR #46本地渲染与远端生成文件验收

**追加日期：** 2026-10-17（UTC；用户当地为2026-10-16晚，America/Vancouver）。

- **源文提交：** [`9706267ae7d0ad702a55851e5c6ee978fa05ad63`](https://github.com/AI-Archaeology/AI-Archaeology-Textbook/commit/9706267ae7d0ad702a55851e5c6ee978fa05ad63)。
- **用户生成提交：** [`87491502c12ee1bb3b33895a394c8baa6beb9162`](https://github.com/AI-Archaeology/AI-Archaeology-Textbook/commit/87491502c12ee1bb3b33895a394c8baa6beb9162)，直接父提交为上述源文提交。
- **PR：** [#46](https://github.com/AI-Archaeology/AI-Archaeology-Textbook/pull/46)，基线仍为 `8e17c1d3`。

### 7.1 用户本地记录

用户提供的日志显示69个Quarto页面全部完成渲染，输出为 `docs/index.html`。预览服务在 `http://localhost:5567/` 启动，并记录了第3、4章的访问。预览退出后，`git diff --check` 无输出；只有两章HTML和 `docs/search.json` 变化，共7行增加、6行删除。提交推送成功，最终工作区干净、分支与远端同步。

上述本地执行情况来自用户日志。本轮远端验收没有另行运行用户的本地Quarto或声称目视检查全部69页。

### 7.2 远端内容与结构

| 检查对象 | 验收结果 |
|---|---|
| 生成提交范围 | 仅 `docs/chapters/chapter-03.html`、`docs/chapters/chapter-04.html`、`docs/search.json`，与用户日志一致 |
| 已审源文件 | 两章QMD、矩阵及本报告在生成提交中均与 `9706267a` 的内容和blob哈希相同 |
| 第3章正文与书目 | 两段更新正文及Bekiari新增条目与源稿相符；正式版本与PDF链接对应；一个末尾参考文献，12条无重复 |
| 第4章正文与书目 | 方差说明及第32—34、28—31页引文与源稿相符；参考文献13条，与基线一致 |
| 标题、目录与锚点 | 两章各18个正文标题，编号主节为9和8；标题、目录目标和HTML ID均与基线一致，无重复ID，目录片段目标可解析 |
| 搜索索引 | 仍为410条；仅第3.8节、第3章参考文献、第4.4节的3条 `text` 字段变化，其余407条完全一致；标题、链接、节名等元数据未变 |
| 搜索与页面一致性 | 3条更新搜索文本与对应HTML节内容逐项吻合 |
| 内部记录隔离 | 本轮报告、矩阵及来源指纹未进入两章页面或新增搜索内容；既有其他案例库记录未改变 |
| 独立复核 | 另行核对Git父子关系、生成差异、源码文本、完整HTML结构及搜索索引；未发现需修改的问题 |

远端 `87491502` 的PR check-runs数量为0，commit status也没有状态条目；不据此写“CI通过”。本轮技术验收依据既定的用户本地Quarto流程、远端生成文件对照及独立复核。

### 7.3 已验收生成文件指纹

| 文件 | Git blob SHA-1 | SHA-256 |
|---|---|---|
| `docs/chapters/chapter-03.html` | `d3ac01a508cdad7fbada1cfe996503da2f6d421c` | `a4165ca9c889e02d4ec21116cf439754a1b5678559aecef04678eed0d507454e` |
| `docs/chapters/chapter-04.html` | `3aaf880ea7247da588e0c82bec33e4dec591be44` | `81532ad11841648cde1052020b716222dbdc91cca7cfe44d56d50868f638b30e` |
| `docs/search.json` | `81e2a1b8a6fb6ed1b73707a21bdcaa9e760e5a41` | `bb77c1ef213a1e7350deb81764c3218d30eecb89956726c1adbec001902f355f` |

**验收结论：通过。** 本次收尾仅更新本报告和内部矩阵，已验收的QMD、HTML和搜索文件保持上述版本。PR #46可按既定流程合并；合并后的Pages发布由工作流状态与公开站点另行核对，不把合并前验收等同于已发布。
