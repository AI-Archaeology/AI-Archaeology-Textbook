# 古文字、计算考古、智能体式AI与主动推理资源核验记录 v1

核验日期：2026-10-17（UTC）。本文件是内部编辑记录，不属于教材正文。

## 1. 本轮范围与编辑决定

- 仓库：AI-Archaeology/AI-Archaeology-Textbook。
- 基线：main提交 `decee3e674831ab78a582821f88a62bb9ab6b2ac`，树 `96168ae0891ef593da5082cb45ed26269d830d7d`。已按不可变提交读取文件并核对Git对象哈希。
- PR47已经合并计算考古与网络科学内容。第1、2章的相关段落，以及[R、Python与数字方法](../reference-resources/programming.qmd)中的Brughmans与Peeples配套资源，作为本轮现有内容使用。
- 首批处理31个PDF／EPUB文件，对应27种文献；其中4种与前轮已核版本相同。另有更新计算考古笔记、古文字在线资源笔记、终端日志各1份。去重与文件指纹见附录。随后追加的Agentic AI笔记、PR48终端日志及预览截图另见第9节，不计入首批31件。
- 初稿新增论证集中于古文字研究的任务区分和资料表示；计算考古及主动推理采用少量分层阅读入口。根据用户随后反馈，在第1.2节补充智能体式AI，并统一使用“主动推理”译名。没有把所有上传文献都加入学生参考文献。

| 文件 | 本轮修改 | 教学目的 |
|---|---|---|
| chapters/chapter-01.qmd | 在原第1.3节下增加“古文字与铭文的识别、复原与解释”；在第1.2节下增加“智能体式AI的工作过程”，均为不编号小标题；相对main增加四条章末文献；更新资料说明 | 区分字形分类、复原与考释，说明工具规划与反馈调整，连接已有Ithaca和Aeneas案例 |
| chapters/chapter-03.qmd | 在资料关联的讨论中增加OBIMD短例；增加一条章末文献 | 说明拓片、摹本、释文与标注状态如何关联，以及整理判断为何应保留 |
| reference-resources/ai-cases.qmd | 增加“古文字与铭文”、三类资料入口和“智能体辅助的铭文研究”两项资源 | 从原始资料查询进入论文和数据，区分数据库、模型训练材料与工作流展示 |
| reference-resources/programming.qmd | 原表增加Argote等的R应用教材和Romanowska等的主体模拟教材 | 提供两条具体计算考古练习路线，保留已有网络科学内容 |
| reference-resources/ai-learning.qmd | 增加三项主动推理阅读、ReAct和Huyen两项智能体式AI阅读；统一术语并简述其与ABM的区别 | 阅读任务组织方式、理论框架及各自的评价问题 |
| 本文件 | 记录版本、原页、实际阅读等级、取舍与未决问题 | 使核验和编辑理由可追溯 |

本轮不修改第2、4章或第5—25章，不增加页面、导航或主节，不提交用户上传的书籍、论文全文、图版、数据集及文本提取件。生成HTML仍由用户本地Quarto流程完成。

## 2. 核验等级与页码规则

| 记录用语 | 本轮含义 |
|---|---|
| 原文核验 | 已读取明确列出的原文页或小节；关键采用页另经页面图目视确认。不能据此声称整本专著、全部公式及所引案例都已精读 |
| 原文选读 | 获取全文后选读指定部分；全文提取只是定位工具，不等于逐页审读 |
| 官方书目／摘要／配套说明 | 出版机构、作者机构或官方项目记录确认相应字段；不能代替完整方法和结果 |
| 复用前轮核验 | 本轮核对文件指纹相同，沿用已有报告的明确阅读范围 |
| 待核线索 | 笔记、搜索条目或二手引用尚未完成原始来源追溯，不作为确定论据 |

印刷页与PDF物理页分开记录；PDF序号从1起算。重排PDF和EPUB没有可确认的纸书页码时，使用章节、段落或EPUB内部文件定位。正式期刊版本、作者稿、预印本及数据库版本分别记录。未运行本轮任何论文模型、R示例或NetLogo模型，也未对数学证明作完整重建。

## 3. 本轮采用的主张—原始来源—位置—限制矩阵

下表S1—S8的完整书目列于第4节。

| 落位及主张 | 原始来源与明确位置 | 核验及限制 | 考古学解释／教学处理 |
|---|---|---|---|
| 第1章：图像转写、缺文复原、年代或来源推测、释读是不同任务 | S1，印刷706—707页；PDF4—5页，图2及其前后任务说明 | 原文分类与关键页面已核；这是综述的任务分类，不是同一个模型完成全部任务的实验 | 分类结果对应任务及其标签，不能自动变为文字意义或历史结论 |
| 资源页：以既有学术断代训练模型可能造成循环性 | S1，印刷714页；PDF12页，Chronological Attribution末段 | 原文具体讨论年代标签来自积累的学术认识；不扩大为该页已经论证所有训练标签的问题 | 预测既有断代与取得独立年代证据应分开；正文说明限定于断代 |
| 第1章：人工收集、分类和标注后进行古文字图像识别；形近、少样本与标签分歧影响成绩 | S2，印刷165—170页；PDF2—7页，图3及错例分析 | 已核原文；模型学习已有字形类别。未确认冻结数据版本、器物隔离和完整划分细节 | 分类表现不能作为未释甲骨字破解率；不采用论文中的百分比作概括 |
| 第1章：相似字形可供考释比较 | S2，印刷171—173页；PDF8—10页 | 原文讨论整体字形特征、偏旁关系及候选推荐；并未确认全部候选的音义 | 引文落在“提供比较线索”之后。后续结合原图、语句与相关材料论证，是教材的方法要求 |
| 第3章：关联拓片、重绘并对齐的摹本、释文和字形位置 | S3，印刷3—4、7—8页；图6、表2在第7页；PDF页同印刷页 | 已核正式数据论文。摹本经重绘；编号有片号、记录号和字类标识等用途，不一概称实物唯一ID | 数据表示包含整理者判断，保留材料来源与对应关系 |
| 第3章：区分缺字位置、残损难辨、分类争议 | S3，第7页表2、第8页Data Records续文 | SeatFont与Mark表达不同情况，现代字映射还具有检索用途 | 不把所有状态压缩成一个“未知”值；映射不等于最终考释 |
| R资源：光谱、化学组成、预处理与聚类练习 | S4，印刷1—4、9—10、33—34、56—57、79—81页；已查部分PDF页＝印刷页＋6 | 原文选读；公开配套包目录已核。黑曜岩含地质参照样本；书内也有假设示例 | 按R与统计基础选择练习；不把聚类或示范数据直接当作考古来源结论 |
| 模拟资源：主体、规则与模拟结果 | S5，官方出版社书目、配套指南及仓库README／章节目录；本次追加核读开放导论6—7页，见第9节 | 首轮核入口，本次增加指定原文页；未逐页读全书或运行模型，主要环境为NetLogo | 作为计算考古模拟教材，不因模型含agent而等同于机器学习或主动推理 |
| 主动推理导语：将观测更新、规划与行动相联系 | S6，第1章印刷9—10页；PDF17—18页 | 原页已核；信息收益和目标结果是作者框架中的规划考虑 | 不由框架定义推断古人必定进行同样计算；考古应用仍须明确变量、假设及材料对应 |
| 主动推理与生成式AI的关系 | S7，印刷97—99、107—108页；PDF1—3、11—12页 | 首页体裁为Opinion；第108页所提特定结合策略在作者写作时尚未系统研究 | 作为作者的研究观点阅读，不转成2026年所有AI的能力判断或方法优劣定论 |
| 自由能框架的理论边界 | S8，第12章印刷256—257页；PDF267—268页 | 原页已核；第257页明确承认近似建模的用途，同时质疑更强的生命／目的解释 | 以对照阅读了解论证范围，不写成所有主动推理算法已被否定 |

## 4. 本轮学生内容采用的完整书目

1. **S1**：Sommerschield, Thea, Yannis Assael, John Pavlopoulos, Vanessa Stefanak, Andrew Senior, Chris Dyer, John Bodel, Jonathan Prag, Ion Androutsopoulos, and Nando de Freitas. 2023. “Machine Learning for Ancient Languages: A Survey.” *Computational Linguistics* 49(3): 703–747. [DOI](https://doi.org/10.1162/coli_a_00481)；[ACL正式记录与PDF](https://aclanthology.org/2023.cl-3.5/)。原文45页，PDF页＋702＝印刷页。
2. **S2**：李春桃、张骞、徐昊、高嘉英. 2023. 《基于人工智能技术的古文字研究》. 《吉林大学社会科学学报》63(2): 164–173, 238–239. [DOI](https://doi.org/10.15939/j.jujsse.2023.02.wx2)。PDF1—10页为正文164—173；PDF11—12页含该文英文摘要238—239，并混有其他论文摘要。书目保留摘要页，正文论证只引用相应正文页；不能写成正文延续到174—175页。
3. **S3**：Li, Bang, Jing Yang, Yujie Liang, Xiaobin Hu, Zengmao Ding, Xu Peng, Shengwei Han, Peichao Qin, Donghao Luo, Taisong Jin, Feng Gao, Yongge Liu, and Rongrong Ji. 2026. “OBIMD: A Multi-modal Dataset for Contextual Interpretation of Oracle Bone Inscriptions.” *Scientific Data* 13: 681. [DOI](https://doi.org/10.1038/s41597-026-06967-0)；[Cambridge机构库记录及全文](https://www.repository.cam.ac.uk/items/a4151126-465e-434c-ac41-dcf789ebeeff)。本轮使用10页正式发表版，非2024预印本。官方记录日期为2026-03-14；所获PDF第9页仍含发表日排版占位，不能据占位自行填日。
4. **S4**：Argote, Denisse L., Pedro A. López-García, Manuel A. Torres-García, and Michael C. Thrun. 2024. *Machine Learning for Archaeological Applications in R*. Elements in Current Archaeological Tools and Techniques. Cambridge University Press. [DOI](https://doi.org/10.1017/9781009506625)；[出版社配套](https://www.cambridge.org/argote_machine-learning)。版权／首次出版2024；Cambridge Core在线日期2024-12-10、纸本发行2025-01-16，分别记录。
5. **S5**：Romanowska, Iza, Colin D. Wren, and Stefani A. Crabtree. 2021. *Agent-Based Modeling for Archaeology: Simulating the Complexity of Societies*. SFI Press. [DOI](https://doi.org/10.37911/9781947864382)；[出版社免费PDF与配套入口](https://www.sfipress.org/books/agent-based-modeling-archaeology)。首轮核官方书目及配套说明；本次追加开放导论6—7页原文核验，不宣称原书全部实验已复核。
6. **S6**：Parr, Thomas, Giovanni Pezzulo, and Karl J. Friston. 2022. *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*. MIT Press. [DOI](https://doi.org/10.7551/mitpress/12441.001.0001)；[出版社](https://mitpress.mit.edu/9780262045353/active-inference/)。初版2022-03-29；网站2025-08-05为另列平装发行日期，不把所读原版年份改成2025。
7. **S7**：Pezzulo, Giovanni, Thomas Parr, Paul Cisek, Andy Clark, and Karl Friston. 2024. “Generating meaning: active inference and the scope and limits of passive AI.” *Trends in Cognitive Sciences* 28(2): 97–112. [DOI](https://doi.org/10.1016/j.tics.2023.10.002)；[作者机构库记录](https://researchers.mq.edu.au/en/publications/generating-meaning-active-inference-and-the-scope-and-limits-of-p/)。刊期2024年2月；原页版权及DOI中的2023不改变按该卷期引用的年份。
8. **S8**：Nave, Kathryn. 2025. *A Drive to Survive: The Free Energy Principle and the Meaning of Life*. MIT Press. [出版社及开放阅读入口](https://mitpress.mit.edu/9780262551328/a-drive-to-survive/)。出版日期2025-02-04；纸本ISBN9780262551328。仅将已核章节用于资源导读，不把整部书的立场当作学界一致意见。

初稿第1章新增S1、S2，第3章新增S3；本次第1章再增S9、S10，完整书目见第9节。S4—S8列在相应参考资源条目，不为无关章节重复添加书目。

## 5. 上传文献的实际阅读与取舍

### 5.1 中文原文：8个文件、7篇文献

| 文献 | 本轮实际阅读及明确定位 | 取舍与仍需解决的问题 |
|---|---|---|
| 李春桃等2023古文字研究（S2） | 正文164—173页及英文摘要238—239；关键原页目视核验 | 采用简短任务例。原文167页80.24%不能解释为未知字破解率；冻结数据版本、器物级隔离、完整划分细则未确认 |
| 郅晓娜、宋镇豪. 2026.《大数据与人工智能在甲骨学研究中的应用与展望》.《中国史研究》(1):5—27,194。未确认DOI | 正文5—27及英文摘要194；26页目视核验 | 作为综述和原始研究定位来源。其平台、缀合、识别、智能体介绍并非同一实验；“破解”及数量必须逐项追原文，未逐项核完。本轮不另添一般性综述段 |
| 万娇、阮丽莎、谭植耀、高大伦、江章华、刘祥宇、周科华、周永明、阮勇斌. 2026.《深度学习应用于陶片分期的可行性分析与实践——基于成都平原宝墩文化的案例》.《文物》(5):55—63。[DOI](https://doi.org/10.13619/j.cnki.cn11-1532/k.2026.05.003) | 印刷55、57—63页；56页关键词定位；60页表格目视核验 | 候选保留。须区分陶片与裁切小图、年代与训练遗址、器物特征与埋藏铁质污染；60页紫竹划分表与“外来”验证叙述关系尚不清楚。陶片分类比例不是人口迁徙直接观测 |
| 张松文、杨林、李辉、高圣章. 2026.《人工智能赋能考古研究综述与展望》.《南京师大学报（自然科学版）》49(4):76—85。[DOI](https://doi.org/10.3969/j.issn.1001-4616.2026.04.007) | 印刷76—77、82—83页；其余页关键词定位 | 综述定位材料。未逐篇追溯全部案例；作者将“AI赋能”用于数据学习的局部定义不替代全教材对AI的界定。本轮避免重复扩写 |
| 桑英、侯光良、石轩、王倩倩、赵健赟、杜雨、何家豪. 2026.《基于深度学习的青海湖流域古城遥感识别》.《地理科学进展》45(9):2040—2056。[DOI](https://doi.org/10.18306/dlkxjz.2026.09.014) | 印刷2040、2042、2049—2053页；2051页表4目视核验。未审计所有性能表 | 候选保留。2042页作者报告空间隔离；2049及2051页新点位未见明确墙体、文化层或遗物，依据形态与区位判断，证据弱于摘要“实地确认”的强概括。不能宣布已获独立地层或年代证明。官网发布日期字段出现2026-12-01，不用于推断本轮之前的首次发表日 |
| 李春桃、戚睿华、杨溪、周日鑫. 2023.《基于深度学习技术的青铜鼎分期断代研究》.《出土文献》(3):16—32,154—155。未确认DOI | 印刷16、18—23、25—26、32页及英文摘要；32页其他文章续文排除 | 候选保留。18—20页3690图片不等于独立器物；未确认同器不同照按ID隔离。严格11期78.83%、粗时代88.79%、允许相邻期95.47%不是同一指标；拟合既有断代标签不是独立绝对年代表 |
| 王庆铸、郎剑锋、方辉. 2026.《人工智能辅助陶片拼对——推进聚落考古研究方法的新尝试》.《中原文物》(4):167—172。未确认DOI | 全文167—172页；171—172页目视核验；两文件逐页文本和栅格内容相同 | 作为初步实践候选。缺候选总数、召回率分母及完整划分，正确拼对组数不能换成准确率；跨层位同器联系还须讨论回填、搬运、残留等形成过程，不能单独证明堆积严格同时 |

中文书目以原始页眉、题名页和摘要页为依据。万娇等另经[文物出版社当期介绍](https://www.wenwu.com/newsinfo/11181980.html)核题名、作者及期号；青铜鼎论文经[清华大学《出土文献》目录](https://www.ctwx.tsinghua.edu.cn/info/1093/3036.htm)复核；桑英等经[期刊官方记录](https://www.progressingeography.com/CN/10.18306/dlkxjz.2026.09.014)复核卷期和页码。检索不到DOI时保持“未确认”，不编造标识符。

### 5.2 计算考古与AI思想史：8种上传文献

| 文献与书目更正 | 实际阅读／复用范围 | 本轮决定 |
|---|---|---|
| Argote等2024（S4） | 题名、版权、目录；印刷1—4、9—10、33—34、56—57、79—81页；版权及9、34页目视核验 | 采用一条R专题资源。示例使用R 3.6.1／64位Windows；未在当前macOS／R复现 |
| Morgan, Colleen. 2022. “Current Digital Archaeology.” *Annual Review of Anthropology* 51:213—231。[DOI](https://doi.org/10.1146/annurev-anthro-041320-114101) | 印刷213—215、222—225页；214、225页目视核验 | 理论综述候选；与PR47数字考古实践及理论边界内容重叠，本轮不再加定义段。其转引案例未全部追原文 |
| Buckner, Cameron J. 2024. *From Deep Learning to Rational Machines: What the History of Philosophy Can Teach Us about the Future of Artificial Intelligence*. Oxford University Press。[DOI](https://doi.org/10.1093/oso/9780197653302.001.0001) | 与前轮同文件；复用69—70、73—74、85—89、92页核验，本轮确认题名、版权、目录 | 保留既有评估；在线2023-12-11与版权2024分字段，不重复添加 |
| Pasquinelli, Matteo. 2023. *The Eye of the Master: A Social History of Artificial Intelligence*. Verso。ISBN9781788730068 | 与前轮同文件；复用导论“The many histories of AI”小节核验。重排PDF不套用纸本页码 | AI社会史论证候选，不为本轮扩写一般AI史，也不充当具体中国考古发现的原始证据 |
| Bratton, Benjamin, Anna Greenspan, Amy Ireland, and Bogna Konior, eds. 2025. *Machine Decision Is Not Final: China and the History and Future of Artificial Intelligence*. Urbanomic。ISBN9781913029999 | 附件题名、版权、目录、Greenspan与Konior导论PDF4—12；题名与版权目视核验。377页重排PDF无纸本页码，不套用出版方408页 | 更正为四位编者文集，非Bratton单著；[出版方记录](https://www.urbanomic.com/book/machine-decision-is-not-final/)确认。导论观点须署其具体作者。保留思想史读物，不作为考古原始证据 |
| Togelius, Julian. **2024**. *Artificial General Intelligence*. MIT Press Essential Knowledge Series。ISBN9780262549349 | 附件版权/CIP与目录；导论印刷1—5页（PDF11—15）；版权页目视核验 | 文件名“2026”错误；[MIT记录](https://mitpress.mit.edu/9780262380140/artificial-general-intelligence/)为2024-09-24。所述“当前AI”属于该版语境，本轮不新增AGI专题 |
| Hinz等2025. “Current Key Intersections between Theoretical and Computational Archaeology.” *Advances in Archaeological Practice* 13(4):528—545。[DOI](https://doi.org/10.1017/aap.2025.10102) | 与PR47原件同指纹；复用535—536、538、542—543等页核验 | 已整合于第1、2章；保留现状，不重复增加 |
| Huggett, Jeremy. 2024. “Changing Theory and Practice? CAA and Archaeology’s Digital Turn.” *Journal of Computer Applications in Archaeology* 7(1):316—331。[DOI](https://doi.org/10.5334/jcaa.144) | 与PR47原件同指纹；复用328—329页等核验 | 已整合，保留现状 |

复用依据：[前轮新文献评估](part1-new-literature-assessment-v1.md)与[计算考古整合核验](part1-computational-archaeology-integration-v1.md)。重复文件不会生成新的学术证据或重复书目。

### 5.3 主动推理：15个文件、12种文献

| 文献及版本 | 实际选读 | 本轮决定与论证限制 |
|---|---|---|
| Parr、Pezzulo、Friston2022（S6） | 版权、目录；印刷3—6、9—11、73、105—107、116—119页；9—10页目视核验 | 采用概念入口。106—107页须指定模型、变量与先验；118—119页允许模型部分使用机器学习，不把两者写成互斥方法 |
| Pezzulo等2024（S7） | 印刷97—100、102—103、106—109页；97、99、107—108页目视核验 | 采用Opinion对照。特定结合路径的未决性限于作者写作时，不冒充持续至今的全面实证结论 |
| Nave2025（S8） | 版权、目录；导论4—10页相关论证；255—258及附录259—260页；256—257、260页目视核验 | 采用理论边界阅读。承认近似模型用途，不将批评误写成所有算法无效 |
| Friston, Karl. 2010. “The free-energy principle: a unified brain theory?” *Nature Reviews Neuroscience* 11:127—138。[DOI](https://doi.org/10.1038/nrn2787) | 印刷127—129页定义、Box1及行动／感知；讨论末段定位。未逐项重核神经科学实验 | 内部保留源头综述，题名问号保留。变分自由能是信息论量，不直接等于机器能耗；没有考古实验 |
| Friston, Karl J., et al. 2024. “Designing ecosystems of intelligence from first principles.” *Collective Intelligence* 3(1):1—19。[DOI](https://doi.org/10.1177/26339137231222481) | 原PDF1—3、13—14页；首页体裁Perspective，摘要称white paper | 研究愿景候选。13页阶段和时间表含暂定、愿景性质，不是已实现通用智能。14页披露VERSES资助，记录背景而不据此否定论证 |
| Namjoshi, Sanjeev V. 2026. *Fundamentals of Active Inference: Principles, Algorithms, and Applications of the Free Energy Principle for Engineers*. MIT Press。ISBN9780262050951 | EPUB题名、版权、目录、Preface、Introduction、Part Two “Active Inference Core”；内部位置见下段 | 工程进阶候选，不增加本科初学负担。不虚构EPUB纸本页码；搜索所得ActiveInferenceInstitute/fundamentals自称Unofficial，不能叫作者官方配套；代码未运行 |
| Friston, Karl, Lancelot Da Costa, Alexander Tschantz, Conor Heins, Christopher L. Buckley, Tim Verbelen, and Thomas Parr. 2026. “Active inference and artificial reasoning.” *Nature Communications* 17:10125。[DOI](https://doi.org/10.1038/s41467-026-77209-5) | 1—3、9、11—12页；1、11页目视核验 | 限定三球任务与规则空间的算法研究；先验可能排除正确规则，假定世界模型已知。不能称通用推理已解决，更不是未知铭文释读证据 |
| Parr, Thomas, Giovanni Pezzulo, and Karl J. Friston. 2026. “The active construction of past episodes.” *Translational Neuroscience* 17(1):20250391。[DOI](https://doi.org/10.1515/tnsci-2025-0391) | 1、8—9、12页 | 情景记忆、重放与临床叙事模拟候选。“past episodes”不是根据考古遗存重建历史；DOI和文章号中的2025不替代2026发表年 |
| Adra, Samer. 2026. “Entrepreneurship as active inference.” *Review of Behavioral Economics*, online first, 1—16。[DOI](https://doi.org/10.1108/RBE-04-2026-0001) | 29页作者稿1、24—25页；出版社正式摘要和书目，未取得正式PDF | Conceptual Paper，非考古实证。作者稿24页不能当作期刊24页；两版逐页对应未解决，本轮不采用 |
| Guénin--Carlut, Avel. 2026. “A Tale of Two Principles—Towards a Relational Perspective on the Free Energy Principle.” *Entropy* 28(10):1103。[DOI](https://doi.org/10.3390/e28101103) | 1—3、22—24页；首页目视核验。原页及卷期为2026-10-10、文章1103 | 理论候选。23页不将论证理解为推翻原形式体系；24页承认没有完整一致的替代数学框架，不写成已解决全部理论困难 |
| Guénin–Carlut, Avel, Jadranka Verdonkschot, Laura Désirée Di Paolo, Felipe Criado-Boado, Luis M. Martínez, and Andy Clark. 2026. *From material to cognitive landscapes*. [HAL预印本hal-05471819v1](https://hal.science/hal-05471819v1)，2026-01-22 | 摘要、§0相关定位、§3.2—3.8、§4.1—4.6；重点PDF18—25；1、19、24—25页目视核验 | 稿内副题为“An invitation to Active Inference in archaeology”。未核得正式期刊版；§4.6是未来景观计算实验建议，不是已完成模拟。§3.4、3.6限制从结构推断古人意义和意图；Constant等陶器注意研究尚未追原文 |
| Possati, Luca M. **2026**. *Design for **Entropy**: Active Inference and Technology*. MIT Press。[DOI](https://doi.org/10.7551/mitpress/16062.001.0001)，ISBN9780262056267 | 版权、目录；导论印刷10—11页（PDF18—19）、陶器注意转引137页（PDF153）；版权及10页目视核验 | 文件名“2025”和“Entrophy”均需更正；[出版社](https://mitpress.mit.edu/9780262056267/design-for-entropy/)为2026-09-01。理论专著，不将二手陶器例当已核原实验。合并章节PDF偏移变化，不设全书统一页码偏移 |

Namjoshi EPUB定位：`text/part0000.html`题名；`text/part0001.html`版权；`text/part0003_split_000.html`目录；`text/part0005.html`前言；`text/part0006_split_000.html`导论；`text/part0015.html`第二部分概述。保留这些定位是为后续逐段核查，不把目录结构当作所有技术内容已读。

Friston等2024完整作者顺序：Karl J. Friston、Maxwell J. D. Ramstead、Alex B. Kiefer、Alexander Tschantz、Christopher L. Buckley、Mahault Albarracin、Riddhi J. Pitliya、Conor Heins、Brennan Klein、Beren Millidge、Dalton A. R. Sakthivadivel、Toby St Clere Smithe、Magnus Koudahl、Safae Essafi Tremblay、Capm Petersen、Kaiser Fung、Jason G. Fox、Steven Swanson、Dan Mapes、Gabriel René。

## 6. 在线资源的分类、访问核验与取舍

访问记录截至2026-10-17；读取项目介绍不等于实际完成每项检索，也不保证所有记录完整、可下载或允许再发布。

| 资源及官方入口 | 本轮直接核验到的内容 | 学生入口与边界 |
|---|---|---|
| [殷契文渊](https://jgw.aynu.edu.cn/) | 平台及说明列甲骨著录、字形、文献等；安阳师范学院与中国社会科学院相关团队 | 采用资料检索入口；不采用“最大／首个”排名，不承诺全部功能无需登录 |
| [小學堂](https://xiaoxue.iis.sinica.edu.tw/)及[范围说明](https://xiaoxue.iis.sinica.edu.tw/About/About) | 官方页面列甲骨、金文、战国文字等数据库与字书、音韵入口 | 采用字形与相关文字学资料；没有把全平台自动标作训练集 |
| [中研院史语所历史文物陈列馆甲骨](https://museum.sinica.edu.tw/collection/32/) | 藏品条目、编号、图像、器物说明入口 | 采用便于初学者认识实物的页面；未逐件核所有释文。[旧拓片库入口](https://rub.ihp.sinica.edu.tw/~oracle/)本轮只读到图像导航，不据此承诺全部旧系统功能 |
| [綴玉聯珠](https://www.fdgwz.org.cn/zhuihelab/home) | 官方介绍和检索说明列缀合、提出者、来源及相关意见 | 采用；一项意见被收录不等于无学术争议，不引用页面不同位置的总量数字 |
| [CDLI](https://cdli.earth/) | 当前官方目录与图像、出版记录入口 | 采用新域名；未逐件复核全部底层记录 |
| [Oracc官方文档](https://oracc.museum.upenn.edu/doc/about/) | 官方索引的介绍、文本版本与子项目文档；直接打开多次返回网关／连接错误 | 仅依据官方可检索说明介绍其用途，未完成在线查询功能测试；不把本次连接失败断定为网站停运 |
| [ClassicMayan](https://classicmayan.org/portal/)及[字形目录](https://classicmayan.org/portal/signcatalog) | 项目门户、文本数据库与词典名称、字形和遗址入口 | 采用比较资料入口；动态查询未完整测试，不保证数据库覆盖范围或完成度 |
| [LiBER](https://liber.cnr.it/) | CNR官方说明：线形文字B转写、照片、校勘、出土地点；分别列图像与文本利用规则 | 采用；不概括为无限制的开放训练数据 |
| [OBIMD代码库](https://github.com/libang1991/OBIMD)与[数据卡](https://huggingface.co/datasets/KLOBIP/OBIMD) | README、字段、数据卡与文件列表；代码和数据的许可表述见第7节 | 采用论文及数据入口；不承诺加载器和模型开箱即用 |
| [Argote出版社配套](https://www.cambridge.org/argote_machine-learning) | 公共HTTP读取为200，资源区有5段录像、彩图PDF和ZIP；ZIP已核11个CSV＋1个XLSX，无独立.R文件 | 写“书中R代码、配套数据／录像／彩图”；不称免费独立R代码库；未完整观看录像或运行书内命令 |
| [ABMA配套指南](https://santafeinstitute.github.io/ABMA/)及[官方代码库](https://github.com/SantaFeInstitute/ABMA) | NetLogo、按章材料与模拟流程说明；出版社免费书籍入口 | 采用模拟教材，未运行或检验全部模型 |

更新计算考古笔记前48行与旧版相同，其后增加软件和代码目录。对笔记中的“well-maintained”“most recommended”“regularly updated”等评价，不因搜索摘要或仓库存在就采纳质量排名。已有open-archaeo与tesselle入口不再重复；[lakillo目录](https://github.com/lakillo/archaeology-machine-learning)和[Zenodo v2.0.0](https://zenodo.org/records/13220872)确有分类表及2024-08-05存档，但本轮未逐项测试其链接或代码。

下列仍为线索：笔记中的“Advances in Digital Archaeology”可疑DOI `10.59641/d4g5a1b2c3`；无完整作者／题名的Electronics 14(22):4507条目；Archaeoscape、ArchaeolDA、MLArchaeologyBasics、ENKI、Open Context实验、AI挑战赛、AmalthAI、PyPottery等代码条目。没有据此引用原始结果或保证复现。

古文字笔记中的埃及文字普通导读、印度河文字社交媒体条目，以及Omniglot、hanziyuan等通识／个人资源，本轮未获得足以支持具体研究结论的原始验证。保留为检索线索；所选比较资料不代表全球文字数据库的完整清单。

## 7. 关键未决项及防止误引的处理

1. **S2数据与评价版本**：165页记录数据持续更新，未能确认167页识别成绩对应的完整冻结版本；训练／测试图像是否按实物和来源充分隔离仍未解决。170页把单个候选输出称作“准确率／相似度”，不能直接当作经校准的真实性概率。本轮只述任务和错误来源。
2. **OBIMD验证单位**：第8页Technical Validation按oracle bone ID作9∶1训练／验证划分。没有独立测试集的同等声明，也未确认全部同物异拓、出版重复或相关碎片跨ID去重。不能据此宣称跨地区泛化。缺字占位框被排除，完整数据中的每种状态并非都参与同一基线任务。
3. **OBIMD指标和许可**：第8页表3中摹本主字mAP@50为0.6700，同页正文为0.6666；本轮不引这组成绩。代码库有MIT代码标签，README将数据写为限学术研究、商业使用需许可；数据卡标CC-BY-4.0。两处数据再利用条件有差异，本轮不自行决定优先顺序，学生页限定提示于转载或再发布前确认材料许可。
4. **OBIMD可运行性**：数据页仍指2024预印本，网页查看器报不支持dataset scripts；文件列表可取得。入口存在不等于已测试load_dataset，正式引文采用2026数据论文。
5. **刊年、载体与页码**：Togelius采用2024；Possati采用2026及Entropy；Bratton记四位编者；Li两篇期刊文献的英文摘要页与正文页分开；Adra作者稿与正式版不能混用页码。S1采用正确ACL条目2023.cl-3.5。
6. **模型与历史解释**：陶片分期、古城遥感、青铜鼎分类和跨层拼对的结果，分别还需要检查地点／年代混杂、独立实地证据、标签来源及堆积形成过程。本轮将这些详细问题留在评估表，不挤入两章的新短例。
7. **主动推理与考古联系**：概念专著、Opinion、Perspective、预印本、限定任务算法及情景记忆模型有不同证据地位。尤其景观预印本§4.6的未来建议和Parr2026的记忆研究，不写成已完成的古代行为或历史重建实验。

## 8. 独立复核与技术验证

两章与古文字资源页已另作逐句原文复核；主动推理三行另作页码与论断范围复核。复核后作了以下收窄：

- 将S1第714页的概括明确限定为既有学术断代，而非所有学术判断产生的训练标签。
- 将S2第171—173页的引文落在论文提供相似字形线索处，后续考古解释要求单独陈述。
- OBIMD资源行改指第7页图6与表2，并把许可提示限定到转载／再发布。
- S7所提结合策略“尚未系统研究”明确限定为作者写作时的评价。
- 第1章资料说明明确陶片活动与陶器相似性网络为教学设定，避免将新加的原始研究介绍也归为虚构例。

初稿源提交`4c26354728fda09eb8e005a9676698b7bd7beca6`的静态检查通过：变更范围为5份QMD和本报告；固定基线文件的Git对象哈希一致；第1—4章的原有H2标题逐一未变，主节数分别为7、8、9、8。四章各有一个终末“参考文献”，当时条目数分别为15、26、13、13，未发现章内重复条目或重复DOI。新增内部链接及显式锚点存在，programming.qmd精确新增两行表格。5份QMD的差异通过git diff --no-index --check，Quarto配置中的既有69个页面路径未变。

用户随后提供了完整本地日志：在该源版本上完成69页`quarto render`，预览访问第1章、第3章、AI考古研究案例、R／Python与数字方法、人工智能与统计学习五页；`git diff --check`无输出。生成文件已通过提交`3808eec465e0f3ee7b1607a62b9fd2a434f74132`推送，日志最后显示分支工作区干净。

本次已读取远端`3808eec4`：其父提交为`4c263547`，只修改上述五页HTML及`docs/search.json`，源文件对象哈希全部未变。逐页提取HTML正文，检查初稿新增标题、文字、引页与资源名，并与各页对应的搜索记录核对；五页均通过，搜索JSON共有412条记录且能正确解析。用户截图显示了旧中文译名，由此引出下节修订；访问日志不被扩大为对每个页面所有排版细节的独立目视验收。

`3808eec4`验证的是初稿。下述术语及Agentic AI修订改变了源文件，须再次由用户本地渲染、预览并提交对应HTML和搜索索引，然后核查远端结果。PR48继续保持Draft。此次源修订不重新写入用户已提交的`docs/`。

## 9. 2026-10-17追加：主动推理译名与智能体式AI

### 9.1 用户反馈、版本与范围

用户明确要求将active inference的中文译名统一为“主动推理”，并补充Agentic AI讨论。按此要求修改学生页面和本报告的中文用语；英文题名及文献实际所指不变，不把一般的“推断”一词一并替换。本次已读取`3808eec4`下全部70份QMD源文件进行术语定位：旧译名只在`reference-resources/ai-learning.qmd`的标题与导语中出现。70份源文件与Quarto配置的69个渲染页面属于不同统计范围。

追加源修订以`3808eec465e0f3ee7b1607a62b9fd2a434f74132`及其树`4ced715384421f2c3438f1cd67dc4dc7309ce28a`为父版本，仅修改第1章、ai-learning、ai-cases与本报告。第3章和programming的初稿已渲染部分保留；第5章不启动。第1.2节加入三个短段，以ReAct说明操作机制，用EpiAgent给出真实铭文图像研究例子，另将术语比较放在资源页。

“智能体式AI（Agentic AI）”是本轮采用的中文表达；“主动推理（active inference）”是用户确定的译名。经典agent概念不限于大语言模型；Agentic AI的用语范围在作者与机构之间存在差异。Anthropic的[官方说明](https://www.anthropic.com/engineering/building-effective-agents)在“What are agents?”及“Combining and customizing these patterns”中把预设workflows与动态agents都纳入广义agentic systems。该文标2024-12-19且现已更新部分工具说明，本轮只用其概念边界作内部核查，不把一家机构的分类当作全领域定义，不引用其工具清单。

### 9.2 追加主张—来源—原页—限制

| 采用位置与主张 | 原始来源及定位 | 核验等级与限制 | 教材处理 |
|---|---|---|---|
| 第1.2节：语言模型规划操作、调用检索、读取返回信息并调整 | S9，ICLR定稿3—4页，§2、§3.1；2页图1 | 原文及1、2、3、4、6页目视核验；原实验的检索对象是百科资料，不是考古记录 | 只引用工作机制；区分计算系统的“观察”与考古实物观察，不把模型生成的步骤说明当作内部过程的完整测量 |
| 第1.2节：多步任务仍会无效检索或重复步骤 | S9，第6页表2及相邻分析 | 原文包含推理错误、重复循环和未获取有效信息的情况 | 不从摘要概括为“消除幻觉”；保存中间结果、检查来源是教材提出的考古研究要求 |
| 第1.2节及资源：语言模型安排铭文图像修复工具 | S10，39307—39308页，§§3.1—3.4、图4；PDF4—5 | 正式原文与页图已核；包括去噪、笔画补全、文字线索校正及结果评价，也允许专家反馈 | 限定为图像复原；模型补出的笔画不能替代原件记录，不称未知字已被释读 |
| 学习资源：环境、工具、规划与失误评价 | S11，作者免费节选“Agent Overview”“Planning overview”“Agent Failure Modes and Evaluation” | 已读相应网页全文段落；仅核原书目录，不宣称核读了整本书的对应纸页 | 使用小节定位，提供免费节选入口，不把网页位置写成纸本页码 |
| 资源：Gemini组织调用Ithaca与Aeneas的输出 | S12，官方工作流介绍及末段；官方Predicting the Past操作说明与脚本目录 | 已核官方网页及可取得脚本；未安装或运行工作流；页面无可确认发表日期 | 作为流程阅读，领域模型的性能仍回原论文；不增加未经独立核验的历史发现 |
| 学习资源：ABM中的主体交互与总体模式 | S5，出版社所链开放导论6—7页；分册PDF6—7 | 本次读导论3—8页，6—7页已目视核验；未运行NetLogo模型 | 区分替研究者组织任务的助手与模拟所研究系统的主体；不是声称两种方法不能组合 |
| 学习资源：主动推理不是Agentic AI的同义词 | S6，9—10页；结合S9、S11的任务组织说明 | S6原页复用前轮已核版本；术语关系为基于这些来源的教学综合 | 规划与工具调用本身不足以证明采用主动推理；没有将EpiAgent、Ithaca或Aeneas归入Friston框架 |

### 9.3 本次实际采用的完整书目及版本

1. **S9**：Yao, Shunyu, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. 2023. “ReAct: Synergizing Reasoning and Acting in Language Models.” *The Eleventh International Conference on Learning Representations* (ICLR 2023). [会议记录](https://openreview.net/forum?id=WE_vluYUL-X)；[作者存档](https://arxiv.org/abs/2210.03629)；[所读v3定稿](https://arxiv.org/pdf/2210.03629v3)。初稿上传2022-10-06，所读v3为2023-03-10，页眉和版本记录确认ICLR定稿，按会议年2023引用。PDF含附录共33页，已用印刷页与物理页一致；没有读完全部附录或重跑实验。
2. **S10**：Zhu, Shipeng, Ang Chen, Na Nie, Pengfei Fang, Min-Ling Zhang, and Hui Xue. 2026. “EpiAgent: An Agent-Centric System for Ancient Inscription Restoration.” *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*: 39304–39313. [CVF正式题录与全文](https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_EpiAgent_An_Agent-Centric_System_for_Ancient_Inscription_Restoration_CVPR_2026_paper.html)；[补充材料](https://openaccess.thecvf.com/content/CVPR2026/supplemental/Zhu_EpiAgent_An_Agent-Centric_CVPR_2026_supplemental.pdf)。正文10页，PDF1对应39304页；本次选读正文1—8页及补充材料A.1—A.6、B.1—B.4相关段落。方法页39307—39308及39311页表5、补充材料PDF1—2页已目视核验。arXiv v2（2026-05-27）仅作版本交叉核查，不用预印本DOI冒充已核会议DOI。
3. **S11**：Huyen, Chip. 2025. *AI Engineering: Building Applications with Foundation Models*. O’Reilly Media. [作者书目](https://huyenchip.com/books/)；[出版社目录](https://www.oreilly.com/library/view/ai-engineering/9781098166298/)；[“Agents”免费节选](https://huyenchip.com/2025/01/07/agents.html)，2025-01-07。资源按作者书目引2025；O’Reilly平台列December 2024，这一显示差异保留，未取得版权页，不猜测两日期的关系。作者公开目录已核Agents从275页起、失误评价从298页起；这些只是目录确认的起始页，具体概念以免费节选的小节定位。
4. **S12**：Sommerschield, Thea, Zoi Tsangalidou, and Yannis Assael. n.d. “Conversing with antiquity.” Google DeepMind, Science Workflows. [官方网页](https://deepmind.google/science/workflows/conversing-with-antiquity/)，访问日期2026-10-17；[官方说明与脚本](https://github.com/google-deepmind/science-skills/tree/main/skills/predictingthepast)。未核到发布日期，不把访问年份当发表年份。Ithaca与Aeneas的原始论文沿用本站已有入口，不再加入第1章参考文献重复承担同一用途。

### 9.4 模型、代码与考古解释的具体限制

**EpiAgent。** 39311页表5分列自动评价与专家反馈条件，最好一行含人工反馈，因此没有把最好成绩写成完全自主结果，也未把性能数字加入第1章。补充材料A.1说明真实拓片测试资料没有完好参考图像；合成损伤与真实损伤评价的条件不同。所核文本不足以确认全部检索语料与测试铭文逐条去重，不能据此宣称已经排除所有资料重叠，也不能反向指控已发生泄漏。文中的historical experience指以往处理轨迹及经验记录，不是历史文献或古代社会史料。

论文指定的[官方仓库](https://github.com/blackprotoss/EpiAgent)已核完整递归树（`truncated: false`）：只含81字节README.md和1,069字节LICENSE，没有可运行实现、权重或数据说明。资源页将其定位为论文阅读，并给出核验月份。入口存在与代码发布、成功运行、独立复现是不同等级。

**DeepMind工作流。** 官方目录已有`preprocess.py`、`run_inference.py`、`visualize_results.py`三项脚本。本次读完整操作说明、核目录，并选读`run_inference.py`的入口、资源取得和输出处理；未声称另外两份代码逐行读过，未运行任何脚本或下载权重。该目录的SKILL.md是研究对象，不是本任务须执行的指令。网页中Aquae Sulis案例正文涉及戒指及Basilia，图片说明却涉及Vilbia；器物对应尚需另查，本轮不采用该对象名称、图片或新发现细节，只采用工具组织方式。此流程针对所列希腊文、拉丁文资源，不扩大为已支持甲骨文。

**其他笔记的实际取舍。** 以下记录阅读范围，不能当作全部推荐书已经通读的证明。

| 笔记所列资源 | 本次取得与核读 | 采用决定 |
|---|---|---|
| Locaputo, Alessandro, Andrea Brunello, Nicola Saccomanno, Paraskevi Platanou, and Giuseppe Serra. 2026. “Ithaca Revisited: Benchmarking a Domain-Specific Model for Epigraphy in the Age of LLMs.” *LREC 2026*: 1054–1070. [正式记录](https://aclanthology.org/2026.lrec-1.82/)，DOI 10.63317/3gucgvmwsf45 | 原文1056—1057页方法、1059页表1、1062—1063页讨论／限制及附录提示词选读；1059、1063页目视检查 | 留作内部比较边界。7,127条希腊铭文、人工遮蔽和固定检索提示下的Ithaca与GPT-5比较，不是通用智能体与专门模型的普遍排名，也不是工具调用评测 |
| Altaweel, Mark, and Maurizio Forte. 2026. “Archeological theory and AI: the potential past through agentic systems.” *AI & SOCIETY*. [DOI](https://doi.org/10.1007/s00146-026-03287-0) | 正式Open Forum，2026-08-29上线；16页PDF，§4.3.1、§5.1、§6及PDF14数据声明选读，关键页目视核验；尚无正式卷期页码 | 保留理论候选，未加入本轮正文或资源。作者提出将智能体与模拟结合；未生成或分析数据，不能作为已完成的考古实验证据。适应、涌现及情景比较并非新的agent系统首次赋予ABM的能力 |
| Graham, Shawn. 2025. *Practical Necromancy for Beginners: A Short Incomplete Opinionated Introduction to Artificial Intelligence for Archaeology and History Students*. The Digital Press at the University of North Dakota. [大学记录](https://commons.und.edu/press-books/34/)，DOI 10.31356/dpb034 | 版权、目录、55及137—139页等选读；有关页图已核，作者仓库9份notebooks的目录和README已读，未运行 | 教学资源备选；不是Agentic AI专著。本轮用Huyen说明智能体概念，用原研究说明机制，避免重复扩展一般AI入门材料 |
| Nigro, Lorenzo. 2026. *Archaeology & Artificial Intelligence*. Quaderni di Vicino Oriente XVIII. [官方系列刊物](https://www.vicino-oriente-journal.it/index.php/quaderni-di-vo/article/view/503)，DOI 10.53131/QVO1127-60372026_1 | 2026年4月版，76页PDF；题名、版权、目录及10、26、47—49页选读；不是自主代理系统实验 | 内部备选，相关方法批判与既有章节重合，本轮不增加条目 |
| “殷契行止” | 研发实验室[2025-10-30官方发布](https://jgwsys.aynu.edu.cn/content2024.jsp?urltype=news.NewsContentUrl&wbnewsid=2570&wbtreeid=1035)及校方发布；活动发生于10月29日。确认团队介绍识别、释义查询、文献溯源、摹本生成等功能 | 发布信息与架构／效果验证分开。本轮不新增条目，不采用“首个”“破解”“普遍优于通用模型”等表述；不把它与已有殷契文渊资料库混为一项，未测试系统 |
| Albada, Michael. 2025. *Building Applications with AI Agents: Designing and Implementing Multiagent Systems*. O’Reilly Media. [出版社目录及预览](https://www.oreilly.com/library/view/building-applications-with/9781098176495/) | 官方题录、目录和第1章开头预览；2025年9月。第9章验证主题仅由目录确认，未读该章原文 | 开发进阶备选。本轮优先Huyen可直接阅读的作者节选，不据目录补造正文页码 |
| Gulli、Lanham、Dibia、Biswas与Talukdar、Ozdemir、Bornet、Iusztin与Labonne等英文推荐书，以及黄佳、凌峰、邢云阳、郭泽德等中文书 | 本次仅见笔记中的书目、书商／读者评价线索，未逐一取得原书或完成版次核对 | 保留待核，不写进参考文献；不采纳价格、评分、“最好”“最完整”等判断 |
| 《智問三代》、Electronics 14(22):4507及Apollo／AlphaOracle等线索 | 尚未取得足以逐条对应笔记论断的完整原始记录或论文核验 | 不据不完整书目补写作者、页码、成果或排名；需要具体教学用途时再追核 |

### 9.5 追加附件与公开原件的追溯

以下三件均为用户此次上传，已直接读取；截图已目视查看。它们与附录的上一批附件分开计数，原始文件没有改名或编辑。

| 文件 | 字节数 | SHA-256 | 用途 |
|---|---:|---|---|
| Agentic AI.md | 11,530 | `659d8fc57d785be9f289d83f3ed0e371c3aac124a5f27dafd6215c2a2d2dead4` | 候选文献与资源线索，不把笔记中的推荐语当作研究结果 |
| Pasted text(20261017-073228).txt | 11,528 | `1a246b064c977d1d9f59d06e7059be91af463a670db0216886415f5ec50ed2d9` | PR48初稿的本地渲染、预览、docs提交及推送记录 |
| image(20261017-073136).png | 363,441 | `00d3bdfb2bb4881ee5dc454cf6efda746977e3bee1872b2173551c9626da5235` | 学习资源页旧译名的预览反馈，不作为论文学术证据 |

本次关键公开原件的SHA-256：ReAct v3为`f285b0971ae4a790e402fb93966bed3adde2cf0a04977d08b2b40d6ab0cace69`；EpiAgent正式PDF为`7ccea234b3e7f42b72c35068e08ccb7a94c04edbadf74110c15abea4da388201`；其补充材料为`c99e9137536bb0895a0a9ce517874a9cd6e7d103a0a69609d1eace61f0402cba`；SFI开放导论为`fc31b50a3b81b07fbfa373ae3397a64f0d2cbfb5712320eb76ef6455b5e9f107`。下载原件只作核验，不提交到教材仓库。

### 9.6 此次源修订的验证与待办

第1章、学习资源页和铭文资源页已分别进行独立概念与原文复核；内部候选取舍及版本状态也经另行复核，未发现必须更正的原文对应问题。追加源修订的静态检查通过：原有第1—4章H2标题逐一未变，主节数仍为7、8、9、8；四章各有一个终末“参考文献”，条目数为17、26、13、13，未发现章内重复条目或重复DOI。第1章只增加S9、S10两条；新增双向内部链接和显式锚点均存在。70份QMD快照叠加本次修改后未检出旧译名，本报告也已统一中文用语；四份变更文件通过空白差异检查。

另行清点25章时发现：基线第5—25章的占位或草稿源文件尚无终末“参考文献”。这些文件本次均未改变，属于后续成稿须落实的既有编排事项。因此，本次“章末书目检查通过”明确只指第1—4章，不宣称全25章已达最终书目规范；也不借此启动第5章或扩展本PR。

本次不手改生成HTML。用户重新渲染后，预期产生第1章、ai-learning、ai-cases三个HTML及`docs/search.json`的变化；既有第3章及programming源文件此次未改。需要再次查看第1.2节新小标题、学习资源页两类术语和链接、铭文资源新增两行及目录显示，提交并推送后核查远端；这些步骤完成之前，不合并PR48。

## 附录：附件溯源

### 1. 本批边界与核验方法

本批指用户要求等候续传、随后表示“上传完毕，可以开始”的这一组附件。以当前 `upload/` 中的完整文件名为基础，结合文件修改时间形成的两组相邻落盘记录及三组研究清单交叉核对。修改时间是当前工作区的文件系统记录，不视为出版时间，也不单凭它决定文献身份。

- 本批PDF/EPUB的记录范围：**2026-10-17 06:51:05.977941—06:52:04.229789 UTC**；另3个笔记/日志也在该窗口内。
- 实际检出 **34个文件：30个PDF、1个EPUB、2个Markdown笔记、1个终端文本日志**。
- 对31个PDF/EPUB重新计算SHA-256，逐一与三个专题工作清单中对应记录比对，**31项全部一致**。
- 计算考古组原清单含12个文件，其中2个PDF及1个Markdown属于前批，本批仅纳入该组的8个PDF和更新笔记。排除旧文件后，三个专题清单完整覆盖本批31个PDF/EPUB，无漏项、无交叉重计。
- 前批05:43 UTC记录的 `Hinz 2025 Current Key Intersections between Theoretical and Computational Archaeology.pdf`、`Huggett 2024 Changing Theory and Practice? CAA and Archaeology’s Digital Turn.pdf`、`Computational Archaeology.md` **不计入本批**。其本批重传副本或更新版本按下表各自记录。
- 本轮另行下载的OBIMD正式论文、Sommerschield综述、Argote配套ZIP等是检索核验材料，**不是用户本批上传附件**，也不纳入31件的统计。

### 2. 核实后的统计

| 类别 | 本批PDF/EPUB文件数 | 不同SHA-256数 | 按作品去重后 |
|---|---:|---:|---:|
| 计算考古及相关英文著作 | 8 | 8 | 8 |
| 中文铭文及考古应用 | 8 | 8 | 7 |
| 主动推理 | 15 | 12 | 12 |
| **合计** | **31** | **28** | **27** |

**去重算式：31个文件 − 3组精确重复各多出的1件 − 王庆铸同文版本多出的1件 = 27种作品。** 三组精确重复都是各2件，不存在三件以上的同SHA组。27种作品中有4种与此前核读版本的SHA-256一致；这属于跨批重传，不能再次从本批31件或27种中扣除。若只计本批相对前轮增加的作品，则为23种，但不代表本轮完整通读了23种。

### 3. 本批31个PDF/EPUB的完整清单

编号按上述落盘记录顺序编排，只用于本附录交叉引用。文件名逐字保留；年份、拼写或作者身份纠正在“对应作品与去重说明”栏说明，不悄悄改写原始文件名。

| 编号 | 附件完整文件名 | 字节数 | SHA-256 | 对应作品与去重说明 |
|---|---|---:|---|---|
| F01 | `Togelius 2026 Artificial General Intelligence.pdf` | 5,842,376 | `1c77a3c45e27925c57c3d237640ed08a80a88052faa99c387d776f7d078b3ff6` | Togelius（2024），*Artificial General Intelligence*。文件名误写2026；所用版为2024。 |
| F02 | `Buckner 2024 From Deep Learning to Rational Machines(1).pdf` | 3,124,949 | `36aa97249f7063a0434417d2a94e1b1b129c5e314b28ca2350c636f5f5e6d69a` | Buckner（2024），*From Deep Learning to Rational Machines: What the History of Philosophy Can Teach Us about the Future of Artificial Intelligence*。前批同一字节版本；见下表P1。 |
| F03 | `Friston 2010 The free-energy principle- a unified brain theory.pdf` | 775,117 | `a53cb2602533986e509434d711b5efe250ec6c01b908105731ab3cc12b8d7be2` | Friston（2010），“The free-energy principle: a unified brain theory?”。本批单件。 |
| F04 | `Friston 2026 Active inference and artificial reasoning.pdf` | 1,692,237 | `467f57c8de72ae8f81c368ad55d8e5bb020af057bafdf595d51dd481bfc008fa` | Friston等（2026），“Active inference and artificial reasoning”。本批单件。 |
| F05 | `Friston 2024 Designing ecosystems of intelligence from first principles.pdf` | 869,319 | `261dfabf8acde092f6a17c74c1fe0a80e509b3770960a92a220095ecaa0c5f9d` | Friston等（2024），“Designing ecosystems of intelligence from first principles”。本批单件。 |
| F06 | `Pezzulo 2024 Generating meaning- active inference and the scope and limits of passive AI.pdf` | 1,734,930 | `2334fef90761c0d83caaeaf118b5e6ea47fa897dbae38c9bfcdd61070b882e6e` | Pezzulo等（2024），“Generating meaning: active inference and the scope and limits of passive AI”。本批单件；卷期年份为2024。 |
| F07 | `Bratton 2025 Machine Decision Is Not Final.pdf` | 5,739,232 | `e96a1397afa782fbf5005f62bdb9bbb17ff0850d125f67c61e95d7dae9a4e198` | Bratton、Greenspan、Ireland、Konior编（2025），*Machine Decision Is Not Final: China and the History and Future of Artificial Intelligence*。合编文集，非Bratton单著。 |
| F08 | `Pasquinelli 2023 The Eye of the Master(1).pdf` | 5,236,420 | `75ca68756447cc6f8fe8c70beebe7d70c1c74b678c221203ab5390bb9a6f6c2b` | Pasquinelli（2023），*The Eye of the Master: A Social History of Artificial Intelligence*。前批同一字节版本；见P2。 |
| F09 | `Adra 2026 Entrepreneurship as active inference.pdf` | 540,608 | `52aea57be61ceb7aca16b96eec9c59e58f8e8b6579dff04d77788c1cb6f1019e` | Adra（2026），“Entrepreneurship as active inference”。29页作者稿；不冒充正式期刊16页PDF。 |
| F10 | `Parr 2026 The active construction of past episodes.pdf` | 2,308,493 | `4efa07fc6194ff32f72ba4a7199cc547f3adda86189f0fbe969600c009d85712` | Parr、Pezzulo、Friston（2026），“The active construction of past episodes”。本批单件。 |
| F11 | `Parr 2022 Active Inference.pdf` | 8,030,106 | `7261ccd3df3601c847fc3f1066423a6b7d2f861a613d91da4e1bae011d6bc539` | Parr、Pezzulo、Friston（2022），*Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*。本批单件。 |
| F12 | `Guenin 2026 A Tale of Two Principles.pdf` | 477,971 | `e62aaa9f825668ef7e34666c1b0d2ec189b76d5e0079239d233805fe66dd8238` | Guénin–Carlut（2026），“A Tale of Two Principles—Towards a Relational Perspective on the Free Energy Principle”。批内精确重复组E1。 |
| F13 | `POSSATI 2025 Design for Entrophy.pdf` | 2,600,509 | `80ed46956607a7ed8c4e8b8dd78428ab52ef6d91bbeb625d0d8ee82264efeebd` | Possati（2026），*Design for Entropy: Active Inference and Technology*。批内精确重复组E2；文件名的2025及Entrophy均有误。 |
| F14 | `Guenin 2026 From material to cognitive landscapes.pdf` | 337,191 | `16ac99939c6414c1db48c3f6034da72a5898cdc822998c0ae87949e993f4cd75` | Guénin–Carlut等（2026），*From material to cognitive landscapes*。批内精确重复组E3；HAL预印本v1，不记作已确认期刊版。 |
| F15 | `Namjoshi 2026 Fundamentals of Active Inference.epub` | 70,651,364 | `fdc2c744b6f8dc19d44d71b124d3f5c24372eea65d634377d272b26e4d9afa0c` | Namjoshi（2026），*Fundamentals of Active Inference: Principles, Algorithms, and Applications of the Free Energy Principle for Engineers*。本批唯一EPUB；不据电子重排位置虚构纸本页码。 |
| F16 | `Nave 2025 A Drive to Survive - The Free Energy Principle and the Meaning of Life.pdf` | 13,518,685 | `fd74fa27ab902d5c324b1def63730da9d96eaf170af34139bd8a9e93a7f7b0d4` | Nave（2025），*A Drive to Survive: The Free Energy Principle and the Meaning of Life*。本批单件。 |
| F17 | `郅晓娜 2026 大数据与人工智能在甲骨学研究中的应用与展望_郅晓娜.pdf` | 256,779 | `166b6ea10d49fc46007a2c724b503c3f2bfc556971f236d010665e979fce5697` | 郅晓娜、宋镇豪（2026），《大数据与人工智能在甲骨学研究中的应用与展望》。本批单件。 |
| F18 | `王庆铸 2026 人工智能辅助陶片拼对.pdf` | 1,975,236 | `f2fffe5d8fa96112bbe8bb66881aa765e27e8e7e411963de149b66162f990219` | 王庆铸、郎剑锋、方辉（2026），《人工智能辅助陶片拼对——推进聚落考古研究方法的新尝试》。与F21属同文版本组T1，字节不同。 |
| F19 | `桑英 2026 基于深度学习的青海湖流域古城遥感识别_桑英.pdf` | 3,109,061 | `59b8aba58a3dd7c553ab3e4cfb8c98d7fa9df71e80ef25151744d911a08a57c0` | 桑英等（2026），《基于深度学习的青海湖流域古城遥感识别》。本批单件。 |
| F20 | `万娇 2026 深度学习应用于陶片分期的可...基于成都平原宝墩文化的案例_万娇.pdf` | 2,900,658 | `64fd999709aceb0109bbfa8758ada9d87c085d3bdab1e9f22160beac2ae1b64d` | 万娇等（2026），《深度学习应用于陶片分期的可行性分析与实践——基于成都平原宝墩文化的案例》。本批单件；文件名中的三个点为原名所含字符。 |
| F21 | `人工智能辅助陶片拼对——推进聚落考古研究方法的新尝试_王庆铸.pdf` | 1,975,236 | `e5763b0f91e7fc39e17f3c7dd83197182b129dd28bacfee143f5310374ef879b` | 王庆铸、郎剑锋、方辉（2026），《人工智能辅助陶片拼对——推进聚落考古研究方法的新尝试》。与F18属同文版本组T1，字节不同。 |
| F22 | `Morgan 2022 Current Digital Archaeology.pdf` | 3,799,504 | `765710a6d93a3a38d526ddfc333aec397862e7da64bb190a17f6fc1d60d8c151` | Morgan（2022），“Current Digital Archaeology”。本批单件。 |
| F23 | `Huggett 2024 Changing Theory and Practice? CAA and Archaeology’s Digital Turn(1).pdf` | 4,127,530 | `d2615bebfecff9db0b4a74854c0dfc4ec7e0ba909218d832b20256a8d8590b77` | Huggett（2024），“Changing Theory and Practice? CAA and Archaeology’s Digital Turn”。前批同一字节版本；见P3。 |
| F24 | `Hinz 2025 Current Key Intersections between Theoretical and Computational Archaeology(1).pdf` | 737,303 | `f5be2fb9a5c64a5d62a15958560072edeca127f61ba01f59cbb5b93c5e088e1f` | Hinz等（2025），“Current Key Intersections between Theoretical and Computational Archaeology”。前批同一字节版本；见P4。 |
| F25 | `张松文 2026 人工智能赋能考古研究综述与展望_张松文.pdf` | 1,422,469 | `4176cea58909e311284b53c053838b499e45a61d866c1e032a46678a127d0d08` | 张松文等（2026），《人工智能赋能考古研究综述与展望》。本批单件。 |
| F26 | `李春桃 2023 基于人工智能技术的古文字研究_李春桃.pdf` | 1,875,593 | `f6096da0625c05c6b860dc1f8bc5f9a1f1e373c52a996ed08ec49d8498db94ef` | 李春桃等（2023），《基于人工智能技术的古文字研究》。本批单件；12页PDF含正文164—173及英文摘要238—239。 |
| F27 | `Argote 2024 Machine Learning for Archaeological Applications in R.pdf` | 5,446,081 | `c5debc4f1e55b0a1f247ca32cd0671eeeabbb83023e14b06468c8afef49e39d7` | Argote等（2024），*Machine Learning for Archaeological Applications in R*。附件所用版权/在线版为2024；2025纸本发行日期另计。 |
| F28 | `Guenin 2026 From material to cognitive landscapes(1).pdf` | 337,191 | `16ac99939c6414c1db48c3f6034da72a5898cdc822998c0ae87949e993f4cd75` | Guénin–Carlut等（2026），*From material to cognitive landscapes*。批内精确重复组E3；HAL预印本v1，不记作已确认期刊版。 |
| F29 | `李春桃 2023 基于深度学习技术的青铜鼎分期断代研究_李春桃.pdf` | 2,960,870 | `c3f2fe3d0516c6d8f8213500b9321c63de334afc2ac7a1e56bdef82d7d5ac6a3` | 李春桃等（2023），《基于深度学习技术的青铜鼎分期断代研究》。本批单件。 |
| F30 | `POSSATI 2025 Design for Entrophy(1).pdf` | 2,600,509 | `80ed46956607a7ed8c4e8b8dd78428ab52ef6d91bbeb625d0d8ee82264efeebd` | Possati（2026），*Design for Entropy: Active Inference and Technology*。批内精确重复组E2；文件名的2025及Entrophy均有误。 |
| F31 | `Guenin 2026 A Tale of Two Principles(1).pdf` | 477,971 | `e62aaa9f825668ef7e34666c1b0d2ec189b76d5e0079239d233805fe66dd8238` | Guénin–Carlut（2026），“A Tale of Two Principles—Towards a Relational Perspective on the Free Energy Principle”。批内精确重复组E1。 |

### 4. 批内重复的逐组依据

| 组别 | 文件编号 | 判定 |
|---|---|---|
| E1 | F12、F31 | Guénin–Carlut“两原则”论文；两件完整字节SHA-256相同。 |
| E2 | F13、F30 | Possati *Design for Entropy*；两件完整字节SHA-256相同。 |
| E3 | F14、F28 | Guénin–Carlut等“物质到认知景观”预印本；两件完整字节SHA-256相同。 |
| T1 | F18、F21 | 王庆铸、郎剑锋、方辉陶片拼对论文；SHA-256不同，6页逐页正文提取相同，6页逐页渲染像素相同。作为同一作品、同一可见正文版本去重，不能称作精确字节副本。 |

王庆铸两件附件均为6页、1,975,236字节。使用PyMuPDF 1.26.6逐页 `get_text()` 比对，六页文本全部相等；再以72 dpi、RGB、不含透明通道逐页渲染，尺寸与完整像素序列在六页均相等。该比较直接在内存完成，未依赖文件名判断。

为便于重复执行核对，将六页提取文本按页序、以单个换页字符（U+000C）连接后按UTF-8计算的SHA-256为 `d0066f4fd29a2a8b414ea0cd60c8a57fce63f03dea75e7ae6c8855c119251176`。这个指纹是同一提取方法产生的文本指纹，不等同于PDF文件指纹。

两件PDF元数据中的创建时间不同（F18为`D:20260922141843-08'00'`，F21为`D:20261017140448-08'00'`）；未逐一解释PDF内部所有二进制差异，因此只声称可见正文与本次提取结果相同，不声称差异仅限元数据。

### 5. 四种此前已核读的同版作品

| 跨批编号 | 本批文件 | 前轮可追溯记录 | 本次确认的范围 |
|---|---|---|---|
| P1 | F02：Buckner（2024） | `editorial-reviews/part1-new-literature-assessment-v1.md` §8，A2；此前附件名为 `Buckner 2024 From Deep Learning to Rational Machines.pdf`。 | 本批重新计算的SHA-256与前轮报告完整指纹一致。前轮已读页范围见该报告§2.3、§5；不据相同指纹声称本轮重新通读。 |
| P2 | F08：Pasquinelli（2023） | 同上报告§8，H2；此前附件名为 `Pasquinelli 2023 The Eye of the Master.pdf`。 | 本批SHA-256与前轮完整指纹一致。此前导论阅读及重排页码限制见该报告§2.4、§5。 |
| P3 | F23：Huggett（2024） | `editorial-reviews/part1-computational-archaeology-integration-v1.md` §2.1、§2.5。 | 本批SHA-256与前轮报告一致；同时重新计算当前upload中05:43 UTC旧件的SHA-256，亦与本批一致。旧件不计入31件。 |
| P4 | F24：Hinz等（2025） | 同上报告§2.2、§2.5。 | 本批SHA-256与前轮报告一致；同时重新计算当前upload中05:43 UTC旧件的SHA-256，亦与本批一致。旧件不计入31件。 |

四项指纹对照依据为本轮固定基线中已有的编辑报告文本，而非只依据附件名中的“(1)”或此前口头说明。Buckner及Pasquinelli旧附件本体不在当前upload清单内，故这两项以此前报告保存的文件指纹进行跨批比对，不宣称重新打开了旧附件。

### 6. 另外3个笔记／日志文件

| 编号 | 完整文件名 | 字节数 | SHA-256 | 角色与边界 |
|---|---|---:|---|---|
| N1 | `Computational Archaeology(1).md` | 19,233 | `f98178cfbffd9a03521b515c475c34ecc668dca7eaeec87235deb244805fe147` | 更新的计算考古资源笔记。19,233字节；前批旧笔记9,100字节且SHA不同，旧件不在本批计数内。作为检索与编排线索，具体书目或方法论断另核原文。 |
| N2 | `Online Resources on Ancient Inscriptions.md` | 12,859 | `8463417be6a62bca8b2aa92b03495fec533320cd14a77cdb434f97419f9467c7` | 古文字与铭文在线资源笔记。用于发现平台、论文和数据入口；所列功能、地址及再利用条件需以官方页面和资料说明核对。 |
| N3 | `Pasted text(20261017-064326).txt` | 11,699 | `84f2987161659a0fa1682e22495ebab289b76c29ddb366ffbf15f6617fbef898` | 用户提供的终端记录，包含PR46同步与PR47渲染、推送、随后同步main的过程；末尾显示PR47合并提交decee3e6。它记录此前本地操作，不是学术文献，也不证明本轮新修改已完成本地渲染。 |

### 7. 核验结果与可复用范围

本次实际文件与分组记录支持“31个PDF/EPUB、27种作品、3组批内精确重复、1组不同字节的同文PDF、4种此前已核读的同版作品”的计数，未发现需要更改的总数。

本附录保留文件身份、去重依据及跨批来源。题名、出版年、体裁与实际阅读范围见本报告第3—7节；不能把本附录的收件登记或SHA一致性升级为通读、算法复现或考古结论成立的证据。

### 8. 本轮另行追溯的公开原件

下列为公开来源核验材料，不计入用户上传件数，也不提交原件或配套数据。

| 材料 | 原始入口／版本 | SHA-256 |
|---|---|---|
| Sommerschield等2023正式PDF | [ACL发表版，45页](https://aclanthology.org/2023.cl-3.5.pdf) | `6846b0b9fedf0768af2137b16683a78ead13c6916912fe2eeaf19f7ccdc5cd85` |
| OBIMD2026正式PDF | [Cambridge机构库发表版，10页](https://www.repository.cam.ac.uk/bitstreams/c3ba77bf-a62d-4b5f-82ef-c793dde17297/download) | `519ff82cfc52912908d06f4cad0234a4b72f285844ff0477cdc80d01441d3048` |
| Argote配套ZIP | [出版社资源区所连文件](https://drupal-s3fs-prod.s3.eu-west-1.amazonaws.com/resources/academic/2417/1325/8605/Supplementary_files.zip)，11个CSV及1个XLSX | `910eb0b52c26d9185f22321f4f28b59097b0e186b4efe4d2b1a4221239e63b63` |
