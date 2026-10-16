# 第一编引文一致性与关键论文论断核验 V1

**核验日期：** 2026-10-16。**审查范围：** 已合并PR#35及PR#38中第1—4章引用；只处理能核验的具体错误与重要论断。不同于正文，本文件记录审查阶段、文章出版/卷期差异与待核问题，不加入书籍Quarto目录。

## Ⅰ 已据正式出版入口核实的重点文章

| 文献 | 官方或可核实信息 | 与正文对应的论断 | 本轮结论 |
|---|---|---|---|
| Magnani & Clindaniel, “Artificial Intelligence and the Interpretation of the Past” | Cambridge Core，**2025-12-18在线首发**；*Advances in Archaeological Practice* **2026，14(2):218–233**；DOI 10.1017/aap.2025.10110；论文开放全文包含Methods, Results and Discussion | 比较尼安德特人相关生成文字/图像与JSTOR学术摘要语料；指出不同形式呈现过时知识、刻板形象和文化错置 | **已核实正式卷期、线上发表日期、方法与结论原文**。第1章将行文的作者年统一为**2026（注明2025线上首发）**，避免书目与正文出现2025/2026不一致 |
| Bellat et al., “Machine Learning Applications in Archaeological Practices: A Review” | *Journal of Computer Applications in Archaeology* **2025，8(1):282–321**；DOI 10.5334/jcaa.201。正式作者：**Mathias Bellat, Jordy Didier Orellana Figueroa, Jonathan Scott Reeves, Ruhollah Taghizadeh-Mehrjardi, Claudio Tennie, Thomas Scholten**（共同第一作者见论文） | 文献检索年份为**1997–2022**，纳入**135篇**；遗迹自动探测与器物分类较多，无监督/聚类方法相对不足 | **作者、正式出版与样本口径已核实**。第2章目前明确限定为纳入样本，**没有改成考古学整体统计**；论断保持 |
| Orengo, Berganzo-Besga & Lumbreras, “Theory and practice of artificial intelligence in archaeology” | *Journal of Archaeological Science* **2026，190:106571**；DOI 10.1016/j.jas.2026.106571，开放获取 | 代理指标（proxies）受观察、取样、测量、标注及资料来源塑造；小样本、类别不均衡、空间分散与背景异质性影响训练和外推 | **正式著录、摘要及Highlights已核实**；第1、3、4章将其用于考古AI证据限制，符合作者论证 |
| Nikita & Martinón-Torres, “Next generation archaeological science: From the past to the future” | *Journal of Archaeological Science* **2026，192:106603**；DOI 10.1016/j.jas.2026.106603 | 高引用论文的年代趋势及多种考古科学方法互补；不能直接当成整个领域出版分布 | **正式卷期与Highlights已核实**；详细文章抽样方法仍需比照完整Methods，不提升为全文已核验 |

**入口：** https://doi.org/10.1017/aap.2025.10110；https://doi.org/10.5334/jcaa.201；https://doi.org/10.1016/j.jas.2026.106571；https://doi.org/10.1016/j.jas.2026.106603 。

## Ⅱ 本轮发现并实际纠正的正文—书目不对应问题

| 等级 | 位置 | 核验问题 | 修订 |
|---|---|---|---|
| P1 | 第2章，AI方法发展史段 | 正文写**Bickler（2021）**，但该章末未列出此文 | 已补入Bickler, “Machine Learning Arrives in Archaeology”, *Advances in Archaeological Practice* 9(2):186–191, DOI 10.1017/aap.2021.6 |
| P1 | 第2章，同一段 | 正文写**Orengo等（2026）**，但该章末缺该文 | 已补入Orengo等2026, *JAS* 190:106571, DOI 10.1016/j.jas.2026.106571 |
| P2 | 第1章，尼安德特人生成式AI案例 | 正文写Magnani & Clindaniel **2025（线上）**，书目写**2026卷期**，读者可能误解为两篇文章 | 正文统一为**2026**，括注2025-12-18在线首发；章末书目保留2026卷期及2025 online信息 |
| P2 | 全书各章 | 过去多项书目包含“本轮新增/已核验”制作标签，造成正式教材阅读干扰 | PR#34已统一每章一个“参考文献”；此项本轮保持，不再新增前台审查标题 |

## Ⅲ 中文AI书籍具体对应：避免以二手教材替代实证

| 教材论断 | 中文原书位置 | 支持等级 |
|---|---|---|
| 广义AI不仅包括ML/深度网络，还涉及知识、推理、与环境交互 | 刘伟等《人工智能基础》（2025），第1章§§1.2–1.3，直接可见分期和三学派；《人工智能概论》（王栋/卢湖川主编，2025）第1、2章目录与前言 | **A/B**：直接核对到刘伟等相关正文、王栋等目录/前言 |
| AI技术史有多种叙事；最新历史著作对LLM快速演变的时间界限持谨慎态度 | 尼克《人工智能简史》第3版（2026），第3版前言PDF印刷页6–7：作者明确表述历史截止日期的困难 | **A：直接核对作者前言**；作者个人评判和轶事应另查史料 |
| AI有复杂的模型任务、应用与伦理问题 | 王栋、卢湖川主编（2025）第1–4、6、8章前言与目录 | **B：目录与前言**，不可冒充全部章节具体论证已核验 |
| 模型可靠性与责任不能由某个准确率代表 | 盖瑞·马库斯《驯服AI》（2026中译本）前言与第2章，用户文件可见原文 | **A（作者批判观点）**；**不是考古学实验误差的测量** |

## Ⅳ 未解决的学术关键问题

1. 第2章：对聂跃平/杨林2009、关莹/周振宇2022、刘建国2007/2008等中国方法史，**期刊摘要与书目不等于全文实证**；“第一”“最早”绝不可在缺乏原始研究时提出。
2. 第4章：Murphy 2023 §3.11印刷页141–142已核实MCAR/MAR/MNAR定义；**结构性不适用**仍是分析前的领域语义，不能套入上述机制分类。
3. 第4章：关于空间交叉验证，生态方法文献Roberts/Valavi与考古预测模型原始研究必须分开标记证据性质；分块并非通用必胜策略。
4. 文献全量性：本文件只对四篇优先期刊与少量中文基础书进行正文/著录专项核对，不宣称对第一编40余条章末参考文献完成逐页终审。
5. 教学试评仍未有真实学生数据，不能将教师桌面试做宣称为完整验证。

**最终闸门：** `CLAIM-TO-SOURCE HIGH-PRIORITY: IMPROVED`；`FULL FOUR-CHAPTER REFERENCING: PARTIAL/HOLD`；`FINAL PUBLICATION APPROVAL: HOLD`。正文修订仅限三处有依据的引文完整性/年份纠正。
