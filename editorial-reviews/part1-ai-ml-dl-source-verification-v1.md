# 第一编AI／ML／DL基础文献专项核验与四章精修 V1

**范围：** 2026-10-16上传的一组AI、统计学习、概率机器学习与深度学习专著（含中文译本和同书不同语言/格式版本）。**本轮未启动第五章编写，也未运行真实A6 EM。**

## 来源与书目年份核验

上传文件名中的年份不一定等于原书首版或版权页年份。为避免混用，请区分：

| 上传资料 | 本轮核验情况 | 在第1—4章中的职责 |
|---|---|---|
| Russell & Norvig, *Artificial Intelligence: A Modern Approach*, 4th ed.（文件名2022） | 原书英文第四版；中文译本《人工智能：现代方法》第4版于人民邮电出版社2023年首次印行，英文版权©2021 | 第1章AI作为广义领域、agent与任务环境；第2章AI技术史 |
| Russell & Norvig，《人工智能：现代方法》第4版（文件名2025） | 上传PDF版权信息显示中文**2023年1月第1版**；与英文版重复的授权译本 | 中文术语对照，不作为独立于英文原著的技术证据 |
| Goodfellow, Bengio & Courville, *Deep Learning* | 2016年著作，第1章历史与第5章学习基本原理 | 第2章深度学习史、第4章模型泛化 |
| Bishop & Bishop, *Deep Learning: Foundations and Concepts* | Springer 2024，第1章及前言已检查；完整技术推导未逐页复核 | 第1—2章的技术概念基准 |
| Prince, *Understanding Deep Learning*（文件名2024） | PDF首页写明**2024-11-21在线版本**，并说明MIT Press正式版于**2023年12月**发布 | 第4章性能评价与错误来源 |
| 《理解深度学习》（文件名2025） | 清华大学出版社2025年中译版，原著Prince 2023 | Prince术语的中文对照；不是另一部独立原著 |
| Chollet & Watson, *Deep Learning with Python*, 3rd ed.（文件名2025） | Manning版权页为**2026**，第1、5、6章与目录已核 | 第1章学习、预测、泛化；第3—4章后续实验入门 |
| Chollet & Kalinowski, *Deep Learning with R*, 3rd ed. | Manning版权©2026，第2、5章、结构与目录已核 | 第3章中R/Python跨工具学习路线 |
| James, Witten, Hastie, Tibshirani & Taylor, *An Introduction to Statistical Learning with Applications in Python*（文件名2023） | Springer版权©2023；DOI 10.1007/978-3-031-38747-0 | 第1、3、4章方法分类、变量、泛化与验证 |
| James, Witten, Hastie & Tibshirani, *An Introduction to Statistical Learning with Applications in R*（文件名2024） | 上传PDF实际为**2013原版，2017年第8次印刷勘误版**；DOI 10.1007/978-1-4614-7138-7；**不是2024新版** | R语言路径作为参考，不与Python版混为同一出版物 |
| Murphy, *Probabilistic Machine Learning: An Introduction*（文件名2024） | MIT Press原书版权©**2022**，上传PDF为**2024-06-26 online version**；第1章及缺失数据处理、混合模型等目录已核 | 第3章输入/缺失数据；后续模型方法参考 |
| Murphy, *Probabilistic Machine Learning: Advanced Topics*（文件名2024） | MIT Press原书版权©**2023**，上传PDF为**2024-06-26 online version**；第3.11节Missing data、第6.5 EM | 第4章缺失机制与进阶模型依据 |
| Theodoridis, *Machine Learning: From the Classics to Deep Networks, Transformers, and Diffusion Models*, 3rd ed.（文件名2025） | Academic Press版权页为**2026**；第1章与第3章任务、估计和验证目录已核 | 第2章AI技术史；第4章技术风险补充 |
| Zhang, Lipton, Li & Smola, *Dive into Deep Learning*（文件名2024） | 已核上传书名、作者、章节目录和第2.2、3.6、4.6—4.7节定位；**正式引文年份仍需依具体版本书名页或版权页进一步锁定** | 第3章预处理与数据表示、第4章测试集复用和分布变化 |

## 概念统一及与考古学知识链衔接

| 术语 | 统一中文解释及考古学关联 | 入门要求 |
|---|---|---|
| AI／ML／DL | AI范围较广；ML为其中的重要数据学习方法；DL通常用多层神经网络实现学习 | 第1章认识关系；不要求写代码 |
| supervised/unsupervised/generative | 监督任务从目标标签学习；无监督任务寻找未预设目标结构；生成任务产出新内容 | 不把聚类视作已经发现“真实古文化类型” |
| feature/label/ID | 特征是给模型使用的有意义代理表示；标签是针对任务指定的目标；ID为追溯身份字段，不等于测量变量 | 第3章结合虚构陶片数据字典 |
| training/validation/test | 训练用于拟合、验证用于模型选择、留出的测试用于最终评价；重复调参会污染测试的独立性 | 第1章直观理解，第4章结合遗址/器物分组 |
| generalization | 在研究目标中的未见资料上维持适用表现，而非训练集的高分 | 第4章要把证据外推范围写清楚 |
| archaeological bias vs estimator bias | 保存/调查/标注偏差是考古数据形成和选择问题；偏差—方差权衡描述统计学习模型误差 | 不能混为一谈 |
| MCAR/MAR/MNAR | 统计模型关于缺失过程的条件性假设 | 第4章只作区分；没有从空白字段直接判断机制 |
| agent vs agentic AI | Russell/Norvig的agent是组织广义AI的概念；近年来agentic AI系统的工具使用/自治工作流是新近工程实践和研究方向 | 不应说两者历史定义完全相同，也不当成AI=LLM |

## 已写入正文的精修

1. **第1章：** AI广义框架（Russell/Norvig）、典型程序和ML区别（Chollet）、训练/预测/泛化（James及Chollet）——不扩充数学先修要求。
2. **第2章：** 单独说明计算机AI方法历史与考古学技术采用历史不等同；引用Goodfellow/Bishop/Russell，并保留考古专门论文作为实际采用史依据。
3. **第3章：** 针对真实教材中的统计学习术语，区分标识符、出土关联字段、特征和预测目标，以虚构18条陶片记录设计**不改CSV**的先修检查。
4. **第4章：** 澄清考古保存与取样偏差、标签偏差、统计学偏差—方差权衡的不同；借助Prince、Zhang和James进一步说明新遗址/新摄影条件下的验证。

## 仍未解决的问题与学术边界

- **书目审定HOLD：** Zhang版本年和Russell英文第四版具体印次仍需要版本级核验；上传名不能替代版权页。已在正文做版本说明。
- **文献深读HOLD：** 本轮定向核验了版权页、目录和与章节有关的若干部分，不应称作14份大型专著逐页全文审查；如将来写到某模型的具体精度、实验样本或特定算法推导，必须回原书指定页验证。
- **研究实证HOLD：** AI通论书籍用于定义与方法原理，不能作为任何考古遗址具体成果的直接证据；考古实证仍须论文和数据支持。
- **教材先修边界：** 第1—4章不安排梯度下降推导、概率公式推导、训练CNN/Transformer或强制Python/R；这些属于后续方法教学。第3、4章仍使用原18条**虚构**陶片教材CSV。
- **版权边界：** 不在GitHub公开受版权保护的原书PDF、图像、成段翻译和教材配套受限数据，仅分享本项目原创解释、核查信息和引用。

**本轮是可供本地Quarto核验的定向精修，FINAL SCHOLARLY AUDIT = HOLD，真实A6 EM授权 = HOLD。**
