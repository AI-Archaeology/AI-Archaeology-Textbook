# 参考资源栏目：整理与来源核验记录（v1）

- 整理日期：2026-10-16（America/Vancouver）。
- 基线：`main` 的 `1bdf01d5f3a17e7e6fdf454cee6938143c57f411`（PR #41 合并后）。
- 范围：根据作者提供的四份笔记整理网上参考资源；新增导航、资源导读与分类页面。
- 状态：源文件与静态检查已完成，提交为Draft PR；本地Quarto渲染、预览与生成HTML验证仍待作者执行。

## 一、输入材料与整理目标

本次阅读以下四份作者笔记，合并跨文件及文件内的重复条目，保留有用的资源入口，不将笔记中的检索过程、推测或获取承诺直接写入面向学生的页面。

1. `Online Resources for AI an Archaeology.md`
2. `AI_Archaeology_Case_Studies_Open_Data(1).md`
3. `R and Python for Archaeology.md`
4. `Case Studies.md`

这些笔记同时包含教材、草稿、教程、软件文档、论文、数据档案、目录与课程广告，不能全部按“开放教材”或“完整开放数据”描述。资源页面围绕学生的阅读和学习任务组织；本文件保留核验层级、重要改正与暂缓收录的理由。

## 二、网站结构与编辑边界

| 导航位置 | 源文件 | 内容 |
|---|---|---|
| 参考资源导读 | `references.qmd` | 按学习任务选择、学习起点与资源使用说明。复用原占位页，保留其 URL。 |
| 考古学开放阅读 | `reference-resources/archaeology.qmd` | 入门教材、活动材料、专题图书与报告入口。 |
| R、Python与数字方法 | `reference-resources/programming.qmd` | 编程基础、考古专题教程、软件文档与资源目录。 |
| 人工智能与统计学习 | `reference-resources/ai-learning.qmd` | 统计学习、深度学习、数学基础与进阶阅读。 |
| AI考古研究案例 | `reference-resources/ai-cases.qmd` | 研究论文、项目及代码或数据入口；连接已有核心案例页。 |
| 考古数据与比较研究 | `reference-resources/archaeological-data.qmd` | 测年、空间、土地利用、社会比较与古 DNA 资料。 |

`_quarto.yml` 在“配套资源”之后设置独立的“参考资源”分组。既有 `references.qmd` 从原分组移至新分组；新增五个页面，配置中的页面总数由 64 增为 69。资源页及其小节均关闭编号。正文五编、25章的章节顺序与文件不作修改，各章末尾“参考文献”与本栏目各司其职。本次不开发第5章。

本文件位于 `editorial-reviews/`，不加入书籍导航。网站读者看到用途与访问入口；来源核验的过程性说明留在本文件。

## 三、核验层级与描述规则

| 层级 | 本次实际核对的材料 | 可据此表述 | 不能据此承诺 |
|---|---|---|---|
| 资源原站或作者正文 | 作者、出版机构、机构项目页、在线教材目录与介绍、软件文档 | 资源名称、作者、主题、可见内容和原站列出的获取方式。 | 全书所有论点已逐页审读；每项说明均具有统一许可。 |
| 论文原站 | 出版社摘要、正文、数据或代码可用性声明 | 研究对象与方法的大意，文章声明的资料入口和限制；核验以实际可见栏目为限。 | 数据全部开放、所有样本完整、模型结果已复核。 |
| 仓库或数据记录 | 作者或项目的 README、存档元数据、文件清单、数据说明 | 所提供材料的类型、版本说明、明显的缺失或限制。 | 代码已在当前环境运行，数据已完整下载或实验已复现。 |
| 待补充 | 只见检索条目、课程宣传或无法充分确认的链接 | 内部记录为候选，或作为课程信息而非自学教材描述。 | 自动提升为可直接使用的教材、公开数据集或已验证的教学案例。 |

同一资源在一个主要类别完整列出；跨类别需要时使用内部链接。清除追踪参数、笔记中的自动引用标记和未经支持的“最佳”“最新”“完整可复现”等措辞。免费阅读、开放许可、公开代码与公开数据分别描述。“入门”“进阶”为本书的选读建议，不是原作者的课程认证。

## 四、重要改正与原始来源定位

本轮以资源原站、出版社、机构库、作者代码仓库与正式存档为依据。下表列容易影响学生选择或造成学术误解的事项；其余条目的主入口保留在相应资源页。书籍资源主要核对作者介绍、目录与获取方式，不能把这些检查称为全书学术论证的逐页审核。

| 事项 | 原始来源与位置 | 处理 |
|---|---|---|
| Prince的出版年与在线版本 | [作者官网](https://udlbook.github.io/udlbook/)；官方仓库[HeroSection](https://github.com/udlbook/udlbook/blob/main/src/components/HeroSection/index.jsx)及[Chap08目录](https://github.com/udlbook/udlbook/tree/main/Notebooks/Chap08)。 | 正式著录2023；当前PDF按钮的2025更新日期不替代出版年。核到第8章四个Notebook的目录，未执行；页面只给集中入口。 |
| 免费HTML与PDF有别 | [Goodfellow等官网FAQ](https://www.deeplearningbook.org/)；[McKinney开放版说明](https://wesmckinney.com/book/)。 | 前者官网明确不提供PDF；后者HTML免费、PDF/EPUB购买。删除原笔记可能造成的统一免费电子书印象。 |
| R4DS版次与主题 | [第2版作者页及目录](https://r4ds.hadley.nz/)。 | 介绍导入、整理、变换、可视化与沟通，不沿用旧版笼统的建模覆盖说明。 |
| 草稿与定稿 | [SACC出版页](https://sacc.americananthro.org/publication/open-source-textbook/)；[Marwick书稿一](https://benmarwick.github.io/How-To-Do-Archaeological-Science-Using-R/)、[书稿二](https://benmarwick.github.io/aswr/)；[法文考古R书](https://r-archeo.huma-num.fr/)；[黄湘云书稿](https://xiangyunhuang.github.io/data-analysis-in-action/)。 | Traces在线正文与草稿PDF分别表述。其余书稿保留未完成或开发中状态，不把计划出版年、网页页脚或少量占位章节当成定稿。 |
| ODATE及材料许可 | [主书](https://o-date.github.io/draft/book/)首页、侧栏与页脚；[笔记本目录](https://o-date.github.io/support/notebooks-toc/)。 | 主书与空间Notebook合并为一条。原站CC BY与CC BY-NC-SA说明不一致，只承诺免费阅读与代码入口；不保证Binder运行或全部材料统一授权。 |
| 书名、机构及作者顺序 | [UTA练习册记录](https://mavmatrix.uta.edu/oer_mavsopenpress/29/)Recommended Citation；[UCLA教程页](https://dal.ucla.edu/blog/2024/11/22/r-for-archaeologists/)；[网络科学在线配套](https://book.archnetworks.net/)标题页。 | 练习册按机构推荐引用列Lemke、Ramos、Troutman；UCLA为Digital Archaeology Lab；在线配套作者顺序Peeples–Brughmans，与纸本顺序区别。 |
| Nikita教材与练习数据 | [图书存档](https://zenodo.org/records/6990414)及[数据记录](https://zenodo.org/records/3837331)，元数据与文件清单。 | 两个记录分别对应免费PDF与R练习数据，著录2020。记录上传时间和图书出版时间不混用。 |
| 免费配套材料与付费正文 | [Carlson出版社页](https://www.cambridge.org/core/books/quantitative-methods-in-archaeology-using-r/DEAE593FA2418EA3B8ECD538C34ED2D5)；[archdata](https://CRAN.R-project.org/package=archdata)；[网络科学在线配套](https://book.archnetworks.net/)。 | Carlson正文需购买或机构访问，archdata免费；网络科学配套免费不等于Cambridge纸本全文免费。 |
| 软件与AI模型的区别 | [PyLithics文档](https://alan-turing-institute.github.io/Palaeoanalytics/)，方法介绍。 | 官方明确不使用训练过的机器学习模型；归入轮廓与几何测量工具，不作为深度学习案例。 |
| 非官方目录与目录范围 | [ctv-archaeology README](https://github.com/benmarwick/ctv-archaeology)；[Big Book of R介绍](https://www.bigbookofr.com/)。 | 前者称社区维护目录；后者明确含免费与付费条目，不沿用“官方CRAN Task View”或“全部免费”的概括。 |
| 课程公告与实际存档 | [DAACS录像存档](https://www.daacs.org/research/playlists/doa-archives/doa-fall-2021/)；[SMADA](https://smada.joeroe.io/)；[比萨2025官方取消页](https://old.unipi.it/index.php/summerschool/item/29259-neural-networks-archaeologists-python-cancelled)。 | 前两项有可定位的教学内容，以存档课程收录；比萨2025课标为CANCELLED，不能推荐为已举办课程。其他只有公告的项目见下表。 |
| 正式卷期年与在线年 | [GeoPACHA原论文](https://doi.org/10.15184/aqy.2023.175)Information；[rcarbon方法论文](https://doi.org/10.1017/RDC.2020.95)Information；[Aeneas原论文](https://www.nature.com/articles/s41586-025-09292-5)出版记录。 | GeoPACHA采用2024卷期年，rcarbon采用2021卷期年；Aeneas为Nature645:141–147（2025），不照抄官方仓库旧BibTeX的643卷。本次资源页不改动既有案例著录。 |
| 新近研究不能沿用旧笔记“未确认” | [Tamir](https://doi.org/10.15184/aqy.2026.10360)、[北圣胡安](https://doi.org/10.1017/aaq.2026.10223)、[Bozburun](https://doi.org/10.1017/aap.2025.10142)、[亚马孙西南部](https://doi.org/10.1038/s41586-026-10835-7)，出版社出版信息。 | 均已核实2026发表；采用简短研究用途及实际材料入口，不复制发现数量、准确率或区域外推数值。 |
| 图像、训练资产与输入矩阵 | [GeoPACHA仓库README](https://github.com/geopacha/Antiquity_2023/tree/main/Eyes%20of%20The%20Machine)Processed；[Cholistan代码](https://github.com/horengo/Orengo_et_al_2020_PNAS)训练资产路径；[Tamir目录](https://zenodo.org/records/17988975)Files。 | GeoPACHA不随仓库分发原始影像；Cholistan有Earth Engine资产路径但权限未确认；Tamir存档是考古目录PDF，不等于完整模型输入表。 |
| 模型运行条件 | [Davis等原文](https://d-davis.github.io/publications/Davis_etal_2021_JAS.pdf)，原文第10–11页Data availability；[Nielsen代码README](https://github.com/mnielsen/neural-networks-and-deep-learning)。 | Davis原模型包需ArcGIS Pro许可；Nielsen代码使用Python2.6/2.7。均不承诺当前环境直接运行。 |
| 遗址与遥感资料访问限制 | [纳斯卡原文](https://pmc.ncbi.nlm.nih.gov/articles/PMC11459208/)Data Availability；[北圣胡安原文](https://doi.org/10.1017/aaq.2026.10223)原文第10–11页Data Availability；[Bozburun](https://doi.org/10.1017/aap.2025.10142)Data Availability；[亚马孙西南部](https://www.nature.com/articles/s41586-026-10835-7)Code availability。 | 按各自声明区分公开代码、非限制资料和申请材料。亚马孙西南部原文明确原始LiDAR数据限制访问，已从早期“未确认”记录更新。 |
| p3k14c公开与限制版本 | [数据论文](https://www.nature.com/articles/s41597-022-01118-7)，Data Records、Usage notes及坐标模糊化说明。 | 公开版本中部分坐标已模糊化；Raw、Scrubbed、Graveyard等含敏感地点版本限制访问，不将限制版本全部称为“原始版本”。 |
| 存档内容与研究数值 | [Peripato存档](https://zenodo.org/records/10214943)Description/Files；[Evershed配套README](https://github.com/AdrianTimpson/2020-03-03523A)Archaeological milk residue data/R code。 | 前者提供分析数据、R代码和预测栅格，不等于全套原始LiDAR；后者考古残留资料为汇总表，代码标in progress，不承诺完整逐件实验数据与全套已完成代码。 |
| 更正与资料来源 | [Bevan更正](https://doi.org/10.1073/pnas.1804206115)；[Kohler更正](https://doi.org/10.1038/nature25992)；[Zahid更正](https://pmc.ncbi.nlm.nih.gov/articles/PMC4983861/)。 | 三项均附更正入口。Bevan更正补列资料来源致谢，没有把它描述为人口估计或模型结果的更正。 |
| 撤稿及相关重分析 | [Whitehouse撤稿说明](https://www.nature.com/articles/s41586-021-03656-3)；[相关重分析仓库](https://github.com/babeheim/moralizing-gods-reanalysis)。 | 两项保留内部处置记录，本轮不扩成方法争议专题，也不将已撤稿论文作为支持性证据或普通推荐案例。 |

## 五、候选去重与处置映射

表中的“纳入”是资源导读的收录决定，不表示代码已经运行或研究结果得到本项目复现。各页面只保留短说明与一手入口。本轮没有增加笔记之外的新书籍家族；同一书的已核实语言版本、同一研究的更正和实际存档可以作为同一资源的补充入口。

### 5.1 AI、数学与通用编程资源

两轮重复清单合并为19个资源家族；Murphy两卷与ISL两种语言版本分别说明，因此页面条目数与家族数不同。未命名的“其他讲义”“互动资料”不构造新条目。

| 笔记中的独特候选 | 重复情况与合并方式 | 去向 | 处置 |
|---|---|---|---|
| Understanding Deep Learning | Online Resources笔记前后重复；只留一个家族 | `ai-learning.qmd` | 纳入核心入口，复用官网与Chap08 |
| Dive into Deep Learning | 前后重复，英文与中文属于同一资源家族 | `ai-learning.qmd` | 纳入；中英文入口并列 |
| An Introduction to Statistical Learning | 在“其他免费选项”中出现；补足其两个官方语言版本 | `ai-learning.qmd` | 纳入统计学习入门分组，不重复建第二套书目 |
| Neural Networks and Deep Learning | 两次作为其他选项出现 | `ai-learning.qmd` | 概念辅助保留；原代码环境已明确，当前网页直连可用性核验受限 |
| Probabilistic Machine Learning系列 | 前后重复；Introduction与Advanced Topics各是独立著作 | `ai-learning.qmd` | 两卷分别列，统一作者与2022／2023著录年 |
| Deep Learning（Goodfellow等） | 前后重复 | `ai-learning.qmd` | 进阶保留；删除任何免费PDF暗示 |
| Mathematics for Machine Learning | 前后重复 | `ai-learning.qmd` | 数学补充保留 |
| Machine Learning Systems | 前后重复；现官网两卷合为一个入口 | `ai-learning.qmd` | 系统工程专题保留，不写“最佳／持续更新到2026” |
| Foundations of Machine Learning | 前后重复 | `ai-learning.qmd` | 理论专题保留，明确第2版 |
| Reinforcement Learning: An Introduction | 前后重复 | `ai-learning.qmd` | 专题保留作者入口；**暂缓将具体PDF链路标为已验证可下载** |
| R for Data Science | Online Resources前后重复，并与R and Python笔记第4节重复 | `programming.qmd` | 合并为一条第2版资源 |
| Automate the Boring Stuff with Python | Online Resources前后重复 | `programming.qmd` | 合并，采用已确认的第3版；去掉“约2025” |
| Think Python | Online Resources前后“其他选项”重复 | `programming.qmd` | 纳入第3版官方在线书 |
| Advanced R | Online Resources前后重复 | `programming.qmd` | 合并为第2版，放进阶 |
| Python for Data Analysis | R and Python笔记第4节 | `programming.qmd` | 纳入；HTML与付费电子书区分 |
| Introduction to Cultural Analytics & Python | R and Python笔记第4节 | `programming.qmd` | 纳入通用人文计算 |
| Geocomputation with R | R and Python笔记第4节 | `programming.qmd` | 纳入R空间分析 |
| Geocomputation with Python | R and Python笔记第4节 | `programming.qmd` | 纳入Python空间分析 |
| Big Book of R | R and Python笔记末尾目录条目 | `programming.qmd` | 放检索目录；删除“目录全部免费”暗示 |

### 5.2 考古阅读、专题编程与课程

来源：O指第一份网上资源笔记的考古部分，R指R/Python笔记，P指第二份开放案例笔记的Part II。通用英文书及D2L的重复项已经并入5.1，不再次列出。Traces至SFU进入`archaeology.qmd`；具体编程教材、草稿、工具与目录进入`programming.qmd`。下表的暂缓项目不出现在学生页面。

| 独特候选 | 来源 | 处置 | 理由与必要修正 |
|---|---|---|---|
| Traces | O 多处 | 纳入；各镜像合并 | 改用 Whatcom 实际教材入口；SACC 明确在线版可读、PDF 为草稿。删“最新/最全面/2026 定稿”判断。 |
| Digging into Archaeology | O | 纳入 | 作者为 Amanda **Wolcott** Paskey 与 AnnMarie Beasley Cisneros，按原出版 PDF 与正式书页核名。 |
| Introduction to Archaeology: A Workbook | O | 纳入 | 机构库推荐引用列 Lemke、Ramos、Troutman 三人；明确为课堂练习册，非完整通论。 |
| Key Concepts in Public Archaeology | O | 纳入 | Gabriel Moshenska 为编者，2017，UCL Press；有原出版社和机构库免费全文。 |
| 宋殷讲座纪要 | P | 纳入中文延伸 | 只介绍纪要内容与性质，不把它当作编程课或独立考古发现证据。 |
| Archaeopress Open Access | O 多处 | 合并目录 | 原出版社可定位；本轮页面直接打开间有 503，但官方检索记录明确免费 PDF 集合。 |
| Access Archaeology | O 多处 | 合并但保留授权差异 | 免费个人使用 PDF 与完整开放改编许可不同，不能一概而论。 |
| Wessex Archaeology Open Library | O 多处 | 纳入 | 实际目录及使用条款可读；删会变动的书/报告数量。 |
| LibreTexts Archaeology bookshelf | O 多处 | 纳入目录 | 目录与已列具体教材分别提供检索和阅读入口，不重复增加同名书目；各书格式与许可不同。 |
| OAPEN | O 多处 | 纳入目录 | 库首页本轮超时；官方研究者页面确认无须注册免费阅读下载，属于机构说明核验。 |
| Open Book Publishers | O | 纳入目录 | 提供直接 Archaeology and Religion 分类；不把出版社当作一本教材。 |
| SFU Archaeology Press | O | 纳入目录 | 已核目录和单书 PDF 入口；不把数字化上线年当成原出版年。 |
| Antiquity 免费文章/Project Gallery | O | 暂缓泛目录推荐 | 笔记只有笼统期刊描述，没有唯一文章；实际研究案例由另一页按具体文章处理，不能泛称全刊免费。 |
| ODATE 主书 | R/O/P 多处 | 只在数字方法页纳入 | 直接书入口 + Notebook 目录；不复制到考古阅读页；不保证 Binder 成功执行。 |
| ODATE Spatial Archaeology notebooks | R | 合并到ODATE笔记本入口 | 官方目录明确归 Rachel Opitz，含 Linlithgow、Canmore、Gabii 和遥感练习；不另立与 ODATE 重复的主条目。 |
| Electric Archaeology 2018 notebook 博客 | R | 作为ODATE背景证据 | 属同一笔记本集合的介绍，实际学习入口改为项目 Notebook 目录。 |
| Data Analysis and Visualization in R for Archaeologists | R 多处 | 纳入 | 官方课程明确无编程先修要求，有具体教学数据；名称标明 Carpentries Incubator。 |
| SMADA | R | 纳入 | 2023 存档，但实际教程仍可访问，区别于只有报名通知的课程。 |
| UCLA R for Archaeologists / Bit by Bit | R/P | 合并纳入 | 更正机构名 Digital Archaeology Lab；只核到官方描述与 Box 下载链接，未读取整个下载包。 |
| DAACS Open Academy 2021 | P | 纳入 | 与其他旧课程不同，有实际课程录像与代码存档；以“2021 存档课程”表述。 |
| Nikita Introduction to Statistics Using R | R/P | 纳入 | 作者、书名、2020、ISBN 与官方记录相符；图书及数据分属两个 Zenodo 记录，均可获取，版本号不必在导读中写死。 |
| Lingxiao HE《R数据分析入门》 | P | 纳入中文通用入门 | 实际 HTML 可读；未把它说成考古专用书。 |
| Online Companion to Network Science in Archaeology | R 多处 | 纳入 | 在线配套作者顺序 Peeples–Brughmans；纸本相反。配套免费≠Cambridge 全书免费；CC BY-NC-ND。 |
| Programming Historian 总目录 | R/P | 合并到两篇具体教程 | 保留可直接学习的两篇，不再重复立泛目录主条目；不沿用旧总篇数/语言数。 |
| Calibrating Radiocarbon Dates with R | R | 纳入 | Frerebeau、Lebrun；使用 rcarbon，英语译文 2025，原法文 2021；导读不需要重复版本年份。 |
| Open Context API Cookbook | R | 纳入 | 原平台说明与代码均可定位；介绍 API 和数据整理，不复用它替代具体数据集的权利说明。 |
| Open Context Jupyter notebooks | R | 与API Cookbook合并 | 官方 Cookbook 直接链接到 release 分支中的代码与动物考古测量 Notebook。 |
| Exploring and Analyzing Network Data with Python | R | 纳入 | Ladd、Otis、Warren、Weingart；历史人文数据，不称考古案例。 |
| rcarbon | R/P 多处 | 纳入 | 软件与文档；测年数列的统计概括不直接等于人口史。 |
| Inference from Large Sets of Radiocarbon Dates: Software and Methods | R | 延伸阅读 | Crema、Bevan；正式卷期为 **Radiocarbon 63(1), 2021:23–39**，online first 2020；DOI 10.1017/RDC.2020.95；开放 HTML/PDF。 |
| IOSACal | R | 纳入 | 主文档已迁往 c14.iosa.it；是 Python 校正软件，不是完整考古学 Python 教材。 |
| tesselle | R | 纳入 | 软件包家族；不可描述为一本完整教材。 |
| PyLithics | R | 纳入数字工具 | 官方明确不使用训练过的机器学习模型，不移入“AI研究案例”。 |
| roadDB | R | 纳入 | 有实际作者教程；输出的记录层级与数据库版本须分清；不把查询结果当作独立验证结论。 |
| Carlson Quantitative Methods in Archaeology Using R | R/P 多处 | 纳入参考书并标访问限制 | 2017；正文需要购买/机构访问；删陈旧价格。 |
| archdata | R 多处 | 合并配套数据 | CRAN 明确含 Carlson 书全部数据；工具和数据免费不代表书本文字免费。 |
| How To Do Archaeological Science Using R | R/P 多处 | 纳入补充草稿 | 2017 论坛编辑文集早期草稿；未确认计划中的 Springer 版，不推断已出版。 |
| Archaeological Science with R | R 多处 | 纳入补充草稿 | 初期数据工作流程有内容；后三个主题章仍占位，不沿用“全面覆盖序列、年代与空间”的说明。 |
| R pour l’archéologue | R 多处 | 纳入法文补充书稿 | 已实际读取首页、目录与前言，超出原笔记仅书目核验；可确认三作者与写作中状态。 |
| 黄湘云《R语言数据分析实战》 | P | 纳入中文补充书稿 | 原作者 GitHub Pages 可读；仍标 early development，不能把预计 2026 当作已完成出版。 |
| Digging with Python | R | 纳入专题演示 | 真实作者 Juan Palomeque-Gonzalez；脚本为演示/概念验证，不称全套入门教材或已复现方法。 |
| open-archaeo | R/P 多处 | 合并为一个目录 | 保留实际主题分类，删 548/45/12 等旧计数和“最佳”比较。 |
| ctv-archaeology | R 多处 | 纳入 | 作者明确不是官方 CRAN Task View；修正笔记前段错误。 |
| Matthew Peeples Data and Software | R | 纳入 | 官方作者页提供可检索的脚本与配套材料，最新地址为 /data-and-software/。 |
| ASU Research Tools for Computational Archaeology | R | 作为第二入口合并 | 实际项目说明列年代、空间、分类和组成分析；与作者目录目标相近，可减少一条长列表。 |
| R. Kyle Bocinsky r_tutorials | R | 暂缓主推荐；保留备查 | [仓库](https://github.com/bocinsky/r_tutorials)与[原始 README](https://raw.githubusercontent.com/bocinsky/r_tutorials/master/README.md)确可定位；本轮只读到两行总说明，未核各教程内容/环境，不称失效或不存在。 |
| Simple R, Barbican Research Associates | R | 暂缓 | http://www.barbicanra.co.uk/simple-r.html 在本轮无法读取，HTTPS 请求也失败；未获得足够官方内容确定可用版本，不等于资源不存在。 |
| Network Archaeology Tutorial for Python, Andrew Cabaniss | R | 暂缓主推荐 | [作者仓库](https://github.com/acabaniss/net-arch-tutorial)可读，作者明确 unfinished，使用较旧 Canopy 设置；已有可读 PH 网络课，暂不增加第二个未完成入门教程。 |
| 泛指 SAA Open Science workshops / Ben Marwick 材料 | R | 暂缓笼统条目 | 无具体标题、日期与唯一入口；已收可核的 Marwick 书稿，不能据泛称构造另一套课程。 |
| 泛指其他 R/Python GIS 工具 | R | 不立独立条目 | 无明确候选；已由 geocomputation 书与具体工具文档承担所需导读。 |
| York Data Science for Archaeology ARC00123M | P | 暂缓 | 官方 2026–27 模块目录可定位，但属于硕士课程说明，未取得开放完整教学材料；不把现行课程说成已消失。 |
| Pisa Neural Networks for Archaeologists, with Python（2025） | R/P | 暂缓且纠错 | 官方页明确 **CANCELLED**，不能写成“2025 已举办”；2026 AI for Archaeologists with Python 后续课程仍是公告，不以此推断材料开放。 |
| ICArEHB Machine Learning in Archaeology（2024） | R/P | 暂缓 | 官方课程页面和日期可核，但未找到本轮可核的完整开放教材/练习入口；不继续追查旧招生页。 |
| 北大考古统计与制图暑期课堂（2023/2024/2025） | P | 暂缓课程公告 | 招生通知本身可读，未获得实际开放课件/练习；不可将通知阅读书目反写成课程已公开全部教材。 |
| 北大定量考古学（陈建立）手册摘录 | P | 暂缓 | 原笔记无明确年代或稳定教材入口；未核当前完整开放课程，不推断不存在。 |
| 未指定 CSDN“深度学习在考古学中的应用”博客 | P | 暂缓 | 没有唯一作者/标题/URL，未核实际考古材料与代码，不能提升为教学或案例证据。 |
| Practical Statistics for Data Scientists（北大通知中阅读项） | P | 只保留在通知背景，不另纳入 | 此处是课程参考书提及，尚未核到免费官方全文，不因出现在通知而增加未经核验的开放资源条目。 |

### 5.3 考古案例与数据研究

M1指`AI_Archaeology_Case_Studies_Open_Data(1).md` Part I，M2指`Case Studies.md`。32个独特候选中，30项作为案例、方法综述或数据研究入口收录／合并，撤稿及相关重分析两项暂留本记录。A1–A6沿用原有核心案例编号；C与D为本表的整理编号。

| ID | 独特候选 | 笔记位置／重复来源 | 处置 | 本轮核验依据和边界 |
|---|---|---|---|---|
| C01 | Carter 2021 木炭窑址 | M1 A1；M2 核心6及后段重复 | 合并现有 A1 | 原研究出版社页、作者代码及 JOAD 数据论文 §3 Repository location、License；数据论文逐项列训练影像、XML、模型、结果及许可。Zenodo 三个单独页面本轮抓取失败，不宣称逐包验证。 |
| C02 | Ithaca 2022 | M1 A2；M2 核心1、后段重复、铭文数据段 | 合并现有 A2 | 官方 ithaca README 中 Data generation、License 指向 I.PHI；模型／代码与原始 PHI 语料来源分开。 |
| C03 | Aeneas 2025 | M1 A3；M2 核心2、“未核验线索”、铭文数据段 | 合并现有 A3 | Nature 原页确认 2025、645:141–147；官方 README 公开 led.json/iphi.json 入口、来源及许可。README 自带旧 BibTeX 卷号643与出版社不同，书目以出版社645为准。 |
| C04 | Tusayan White Ware 2021 | M1 A4；M2 核心5及后段“未确认数据” | 合并现有 A4 | Zenodo 元数据与文件列表明确完整影像集、Notebook、补充包，总855.7MB；本轮没有从渲染记录确认具体再利用许可证，不替其声明任意再分发。 |
| C05 | Evron Quarry 2022 | M1 A5；M2 核心3 | 合并现有 A5 | 原论文记录/PMC，作者仓库目录确认 DL_code、FTIR_spectra.zip、Raman spectra Evron lithics、data_set_processed.zip；仓库没有根 README，不是整个仓库404。未解压检查。 |
| C06 | Ivory clustering 2014 | M1 A6；M2 核心4 | 合并现有 A6 | ANEIC 作者项目原页和 core README；概率聚类（最大似然／最大后验）、特征表CC BY-SA3.0、代码MIT。照片不能视为同一开放数据许可。 |
| C07 | Davis 2021 贝壳环 | M1 A7；M2 §2及后段重复 | 纳入案例页 | 作者公开原文PDF，第10页 Data availability 及第11页续行：训练数据与模型存入 ScholarSphere，VOC/Mask-RCNN格式，模型.dlpk需ArcGIS Pro。存档 DOI 本轮未能抓取，不宣称文件已成功下载。 |
| C08 | Orengo 2020 Cholistan | M1 B1；M2 §3及后段重复 | 纳入案例页 | 作者仓库 Last version.js 代码：smileRandomForest；行205–219导入 users/hao23/cholistan/sites_it3、other_it3。只证实作者资产路径，不能据此断言私有或全部公开。 |
| C09 | GeoPACHA Eyes of machine | M1 B2；M2 §3 | 纳入案例页；统一2024 | 出版社确认 Antiquity98(397):245–259、DOI10.15184/aqy.2023.175；作者 README 的 Processed 节明确影像太大未随仓库分发，但提供训练/验证标注和模型。2023是线上年，2024为卷期年。 |
| C10 | Tamir 2026 | M1 B3；M2 §3 | 纳入案例页 | 出版社方法节列RF/SVM/XGBoost、LOOCV、80/20及IArch；Supplement给OSM；引用的Zenodo17988975实际为92.6MB考古目录PDF（元数据发布日期2025-12-19），不等于数值训练矩阵。|
| C11 | Sakai 2024 Nazca | M1 C；M2 §4及后段重复 | 纳入案例页，明示限制 | 原文 Data Availability Statement：非限制资料在文内；训练地画的精确地点无公共数据库发布许可；正当用户需向秘鲁文化部申请，新资料还需作者及相关机构许可。 |
| C12 | Field/Dean 2026 NSJ | M1 C；M2 §4 | 纳入案例页，明示限制 | 出版社PDF第10–11页 Data Availability Statement：代码公开，DEM来自National Map；训练及输出地点不公开，model output可申请。没有将其描述为全开放包。 |
| C13 | Eberl 2023 microdebitage | M1 D；M2 后段候选 | 纳入案例页 | 出版社原页确认AAP11(2):152–163、DOI10.1017/aap.2022.35；Data Availability明确github；两张补充表；已核对作者仓库README（早期计划内容不能当最终研究样本数量）。 |
| C14 | Buławka 2024 qanats | M1 D；M2 后段候选 | 纳入案例页，仅承诺论文 | 作者机构GIAP原页确认JAS171:106053、DOI10.1016/j.jas.2024.106053和YOLOv9、开放论文；作者机构PDF被抓取工具阻断，未证实训练数据或权重下载。 |
| C15 | Bickler 2021 | M1 D；M2 未核验线索段 | 作为方法综述链接合并 | 出版社明确Digital Review，AAP9(2):186–191、DOI10.1017/aap.2021.6；全文可读取。不作原始研究数据案例。 |
| C16 | Peker 2026 Bozburun | M1 D；M2 未核验线索段 | 纳入案例页，明示限制 | 出版社原页确认2026发表、AAP14(2):198–217、DOI10.1017/aap.2025.10142；Data Availability：代码Zenodo16905405，RGB/DEM需土耳其测绘机构研究授权，权重需申请。Open Materials徽章不能转写Open Data。 |
| D01 | Bevan 2017 | M2 大数据§1及优先表 | 纳入数据页 | UCL原仓储元数据，公开2MB研究数据ZIP及DOI10.14324/000.ds.10025178；2018年更正（10.1073/pnas.1804206115）补列资料来源致谢，已附入口；未验证完整存档运行。 |
| D02 | ArchaeoGLOBE 2019 | M2 大数据§2及末尾重复 | 纳入数据页 | 作者研究仓库README确认发表存档CNCANQ、工作数据与R代码，数据CC0、文本图CCBY4；Dataverse当前抓取受阻。README另有旧compendium引用6ZXAGT，优先采用明确标注发表结果的CNCANQ。 |
| D03 | Peripato 2023 | M2 大数据§3及末尾重复 | 纳入数据页 | Zenodo7750985重定向至10214943 v2，元数据明确分析数据库、R代码、线性/log10预测TIFF；方法为bayesPO的fit_bayesPO非齐次泊松点过程。不是两套独立数据；不能称全部LiDAR开放，也不必裁定所有统计模型是否属于广义ML。 |
| D04 | Margaryan 2020 | M2 大数据§4 | 纳入数据页进阶区 | Nature原页的数据声明（检索索引）：序列数据ENA PRJEB37976；机构原文也列同一编号。未检查各run/完整序列文件。 |
| D05 | Lazaridis 2022 | M2 大数据§5 | 纳入数据页进阶区 | 作者Harvard公开原文/PMC Data and materials：Dataverse3AR0CD为genotype，ENAPRJEB54831为aligned-read BAM；不混称同类原始数据。 |
| D06 | Narasimhan 2019 | M2 大数据§6 | 纳入数据页进阶区 | 原文PMC Data and materials：新序列ENA PRJEB32466、混合时间软件Zenodo3263997。未下载序列。 |
| D07 | Evershed 2022 | M2 大数据§8 | 纳入数据页 | 作者README：sherd residues为313行8列汇总，而非逐件完整实验测值；R code标作In progress。原文数据声明指向UK Biobank，不能称现代受试者资料免费任意下载。 |
| D08 | Turchin 2018／Seshat | M2 大数据§8及末尾重复 | 合并成一个项目条目 | 原论文入口；Seshat官网Data页明确论文对应replication spreadsheets、Polaris-2026快照、Equinox旧快照和API。最新快照不等于2018研究数据；未逐项核对2018原版文件。 |
| D09 | Allentoft 2024 Denmark | M2 Additional Nature | 纳入数据页进阶区 | Nature Methods/Data availability明确PRJEB64656、UCPH DOI及Zenodo8196989；Supplementary Data1/2含样本与同位素资料。该文2024已确认，DOI的2023不作出版年。 |
| D10 | Pärssinen 2026 | M2 Additional Nature及末尾重复 | 纳入数据页，合并冲突叙述 | Nature657:420–425，2026-07-29在线；Data availability称相关primary data在正文/补充材料、测年校准在SupplementaryTable1a,b。主编排复核另读Code availability，明确原始LiDAR数据限制访问；删去笔记内相互矛盾的面积／飞行长度及外推数量。 |
| D11 | Schmid/Schiffels 2023 | M2 Additional PNAS | 纳入数据页进阶区 | 作者mobest.analysis.2022 README：发表版本OSF6UWM5，GitHub开发版本会变，主数据依赖AADR v50、未复制入仓库；部分步骤需要HPC环境。提供方法文档更适合导航。 |
| D12 | Kohler 2017 | M2 末尾Publication confirmed | 纳入数据页 | Nature原页明确SupplementaryTable2为研究数据XLS，并链接2018corrigendum10.1038/nature25992；可解除“完全找不到数据”旧结论。房屋面积是财富代理而非直接财富观测。 |
| D13 | Zahid/Robinson/Kelly 2016 | M2 末尾Publication confirmed | 纳入数据页论文阅读条目 | 原论文记录确认PNAS113:931–935及DOI；PMC另有2016更正。原论文PMC本轮抓取遇验证码，独立数据仓储未确认。绝不贴“数据已开放”标签。 |
| D14 | Whitehouse 2019 | M2 末尾Retracted | 暂缓公开资源条目，内部保留 | Nature官方Retraction Note DOI10.1038/s41586-021-03656-3和PubMed34234342确认撤稿；不作支持性证据。 |
| D15 | Beheim相关重分析 | M2 Whitehouse条目内附带独特候选 | 与D14合并为内部方法争议记录 | 作者babeheim/moralizing-gods-reanalysis README说明派生自Whitehouse2019代码、扩展步骤与CCBY-NC-SA4.0；研究确有重分析资源，但本轮不扩成独立争议专题，亦不把其仓库当成原研究已被挽救。 |
| D16 | Bird2022 p3k14c | M2 末尾Gaps附带数据库 | 纳入数据页 | Scientific Data9:27 Data Records与Usage notes：公开处理数据、R与Python；Raw/Scrubbed/Graveyard三集敏感地点受限，北美部分位置模糊化。旧“旗舰期刊之外”的筛选理由不适用于新资源导航目标。 |

## 六、技术验证与后续流程

首轮参考资源提交`fffa29b8`已完成以下源文件静态检查；组织迁移后的链接修订见第八节：

| 检查项 | 结果 |
|---|---|
| 改动范围 | 8个源文件：修改导航及原导读页，新增5个分类页和本报告；无`chapters/`或`docs/`改动。 |
| 导航结构 | “参考资源”紧接“配套资源”；原64个页面的相对顺序保留，新增5个页面，共69个唯一配置路径。 |
| 章节边界 | 原五编、25章路径与顺序保留，第1–4章的章节结构未改；未开发第5章。 |
| 资源页格式 | 六个资源页面均设置`number-sections: false`及单一不编号主标题；分类页表格列数一致，导读表为两列。 |
| 内部链接 | 25个内部链接的目标均在基线树或新增文件中存在。 |
| 外部入口清单 | 六页共151次外链引用、150个唯一URL；ISL两种语言版共用同一官方首页，属于有意共享入口。该统计不表示所有二级下载均已测试。 |
| 文本检查 | 无行尾空白、冲突标记、追踪参数或笔记自动引用残留；读者页无核验过程标题。 |
| 编辑报告 | 本文件未加入书籍导航；资源正文和内部处置记录分别保存。 |
| 待完成 | 本地Quarto渲染、页面预览、生成`docs/`提交，以及其后的远端HTML验证。 |

页面内容另经来源核验人员复核，收紧草稿状态、数据版本与模型许可表述；没有将静态检查写成渲染或实验复现成功。

作者在该分支本地执行`quarto render`与`quarto preview`，查看新栏目及各页，再提交`docs/`。配置预计渲染69个页面。由于整个网站共用侧栏，导航变化会影响既有页面的生成HTML；应在检查差异后提交整个本次生成的`docs/`，不沿用上一轮仅提交两章HTML与搜索索引的范围。

生成文件推送后，核对远端HTML中的栏目位置、六个资源页、内部链接、搜索索引与章节编号，再决定是否合并。当前保留Draft状态，不执行合并。PR #37和PR #39已再次确认仍为打开的Draft，不在本次改动范围内。

## 七、本次验证的实际限制

- 主要资源的作者／机构／出版社页面及仓库说明已按上述范围核对；未逐章审读所有书、未验证所有二级下载、未遍历大型数据包，也未执行课程或研究代码。
- Sutton与Barto作者页、Nielsen在线书本次直连抓取受限；相关介绍依据官方搜索索引及作者仓库。保留官方入口，未将具体PDF下载链路标为已测试。
- UCLA教程下载包已核到机构说明与Box入口，未成功读取包内所有文件；资源页明确以机构下载页介绍为依据。
- Archaeopress部分页面、OAPEN库主页等出现抓取限制，已用相应机构官方介绍或官方检索记录确认资源性质；不将单次抓取失败写成网站失效。
- SFU仅抽查了目录与单书PDF入口；Pressbooks练习册直接访问受限，免费版本依据UTA机构库记录。各集合的每本书仍须按自身版本与许可使用。
- 原作者代码的存在与数据记录的公开不构成当前环境可复现的证明。本轮不改变现有核心案例的复现状态、审核状态或使用条件。


## 八、组织仓库迁移与链接修订（2026-10-16）

作者将仓库转移至GitHub组织AI-Archaeology，后续开发使用以下地址：

- 仓库：https://github.com/AI-Archaeology/AI-Archaeology-Textbook
- 网站：https://ai-archaeology.github.io/AI-Archaeology-Textbook/
- 本PR：https://github.com/AI-Archaeology/AI-Archaeology-Textbook/pull/42

转移后核对：`main`仍为`1bdf01d5f3a17e7e6fdf454cee6938143c57f411`；PR #42仍为打开的Draft，转移前的资源提交`fffa29b8ec6c2704b43ec5ce7cd3b6fc5a9c0903`完整保留。新网站的`index.html`与`references.html`均返回HTTP 200，实际内容与当前`main`的对应`docs/`文件Git blob一致。新资源栏目尚未合并发布。

### 当前链接审计

按资源提交的完整树清单检查83个源文件，范围为所有QMD及非`docs/`、非`editorial-reviews/`的Markdown/YAML文件。三个根文件包含当前仓库旧地址；其余80个文件逐一读取并核对Git blob SHA后，用`rg -n -i`检索旧仓库地址和旧Pages地址，额外命中为零。GitHub代码搜索在刚迁移后返回零条，未以该搜索结果代替实际文件检查。

| 文件 | 本次修订 |
|---|---|
| `_quarto.yml` | `book.repo-url`改为组织仓库地址，供重新渲染时生成正确的仓库与编辑入口。 |
| `index.qmd` | “开放与反馈”中的GitHub与Issues链接改用组织地址。 |
| `README.md` | 更新推送目标，补上组织仓库和新网站链接。 |
| 本报告 | 记录迁移、线上检查、源文件审计及本地同步要求。 |

本次链接修订涉及上表4个文件，计入现有PR #42后累计改动10个文件。参考资源分类、章节正文与原有审核记录均未因迁移重写。YAML与首轮提交比较，仅新增仓库地址这一处配置变化，全书配置页面总数仍为69，其中“参考资源”栏目为6页。

### 本地同步与生成文件

补丁已在首轮资源提交对应文件的副本上通过`git apply --check`，应用后逐文件内容与准备稿一致。这一检查不替代本地Quarto渲染和页面预览。

本地现有项目使用`git remote set-url origin https://github.com/AI-Archaeology/AI-Archaeology-Textbook.git`更新远端地址，然后获取并快进拉取原资源分支，再完整渲染、预览和提交`docs/`。源文件中的地址修订须经本地渲染和生成文件提交后才能反映到线上。

GitHub官方[仓库转移说明](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository)区分仓库重定向与Pages站点：旧仓库位置的Git操作及仓库链接会重定向，关联的Pages网址不自动获得这种重定向。后续教材与教学通知使用上列新网站地址。本PR继续保持Draft，等待本地生成文件及远端HTML验证。

补丁准备阶段的写入记录：通过当前GitHub连接创建组织仓库的Git tree时，GitHub返回`403: Resource not accessible by integration`。源文件修改与本地检查已完成，但该次写入未成功，当时远端PR仍停留在`fffa29b8`。

### 组织安装确认与续作

作者随后在AI-Archaeology组织安装了由OpenAI开发的ChatGPT Codex Connector，并选择仅授权AI-Archaeology-Textbook。2026-10-16续作时，通过当前连接读取组织安装记录与该安装的仓库清单，确认安装ID为`172224741`，授权方式为`selected`，清单中仅包含`AI-Archaeology/AI-Archaeology-Textbook`，与作者提供的配置截图一致。

本次链接修订继续提交到既有分支`feature/reference-resources-guide-v1`，提交前已核对PR #42仍为打开的Draft、头提交仍为`fffa29b8ec6c2704b43ec5ce7cd3b6fc5a9c0903`，并核对补丁基准文件与该提交一致。组织安装确认与实际提交成功分别记录；写入、提交及远端文件复核结果见PR #42的提交历史和说明。本轮不代替作者的本地完整渲染、预览以及随后生成HTML的远端验证。

## 九、本地渲染与远端生成网页验收（2026-10-16）

本节更新第六、八节记录的待办状态。此前的阶段记录保留供追溯；本次验收固定对应作者提交的生成版本 [`ffc24df977ccc04e584f94be3c1edf52db83b877`](https://github.com/AI-Archaeology/AI-Archaeology-Textbook/commit/ffc24df977ccc04e584f94be3c1edf52db83b877)，其唯一父提交为 `01c483b6c2ab667b17994817694f5948e408b3a0`。

### 作者本地记录

作者提供的终端记录 `Pasted text(20261016-222704).txt` 确认：

- 已将远端地址改为组织仓库，并在 `feature/reference-resources-guide-v1` 上拉取到 `01c483b6`。
- 完整运行 `quarto render`，69/69页完成，输出 `docs/index.html`。
- 运行 `quarto preview`，访问首页及六个参考资源页面，随后正常停止预览。
- 暂存后对非HTML文件执行通常的 `git diff --cached --check`；对 `docs/**/*.html` 仅在单次命令中使用 `core.whitespace=-blank-at-eol`，允许Quarto侧栏生成的行尾空格。两项检查均完成，未修改仓库或全局Git配置。
- 提交并推送 `ffc24df9`；终端末尾显示分支与远端一致、工作区干净。

预览日志能证明六页实际被访问，不能单独证明所有外链逐一点击或浏览器布局逐项验收。助手本轮以对应远端静态HTML、源码及索引为技术验收依据，没有将终端访问记录写成助手亲自进行的视觉检查。

### 改动范围与生成结果

| 检查项 | 实际结果 |
|---|---|
| 作者生成提交 | 仅修改70个 `docs/` 文件：64个既有HTML、5个新增分类HTML、1个搜索索引；无章节源码或工作流变动。 |
| 全书页面 | 配置与生成HTML均为69个唯一页面；导航保留五编25章及原有页面顺序。 |
| 全站资源导航 | 逐页检查69个HTML：“参考资源”紧接“配套资源”，六个入口名称、顺序和解析后的相对路径一致。 |
| 组织地址 | 69个HTML中的编辑与问题反馈入口均指向AI-Archaeology组织；未检出原教材仓库或原Pages网址。 |
| 既有正文 | 除有意更新的首页与资源导读外，62个既有页面的 `main` 正文经DOM序列化比较，与基线 `1bdf01d5` 一致，其中包含全部25个章节页面。 |
| 资源正文 | 六页共375个标题、段落及表格单元经文本正规化后，与QMD内容及顺序对应；151次外部链接引用完整保留。 |
| 标题与内部链接 | 六页各有一个不编号主标题；37次正文站内链接或页内锚点引用通过目标检查，资源页面使用的静态文件目标存在。 |
| Prince资源 | 官方教学网站与第8章Notebooks两个指定入口在源码和生成HTML中一致。 |
| 搜索索引 | `docs/search.json` 可解析，共410条记录、69个页面目标；六个资源页对应28条记录，目标与片段锚点有效，无重复objectID。 |
| 编辑边界 | 六页正文及搜索索引未混入本报告、候选处置矩阵或本次编辑专用标题。 |
| 章节保持 | 25个章节源文件的Git blob与基线完全相同；第1–4章主要节数仍为7、8、9、8，且各有一个末尾“参考文献”。 |
| GitHub状态 | 验收时PR #42无合并冲突；该生成提交没有check runs、commit statuses或Actions运行记录，不能称“CI已通过”。PR #37、#39仍为打开的Draft。 |

为防止本地读取或文本落盘改变待验收内容，本轮将69个生成HTML、索引、相关源码和基线HTML共170份文件的实际字节与Git树blob SHA逐一核对，全部一致。

### 既有章稿范围与后续状态

第5–25章源文件仍为既有占位或草稿状态，未设置本项目规范要求的末尾“参考文献”节；这些内容与 `main@1bdf01d5` 完全相同。本次未改动这些章稿，也不将25章路径完整或渲染成功表述为25章正文和参考文献均已完成。后续正式开发相应章节时应按章末规范统一处理，当前继续遵守不开始第5章的要求。

本次资源导航和生成网页验收通过。内部报告的这次追加不改变任何QMD、配置或 `docs/`，无需因报告记录再次渲染。随后按已约定流程解除PR #42的Draft状态，并在确认分支头提交未变后合并；实际合并SHA及GitHub Pages发布结果以PR和部署记录为准。

本轮未重新运行各资源的Notebook、课程或研究代码，未重复下载大型数据包，也未再次逐个检测所有外部网站。此前第七节所列来源访问与复现限制继续有效。
