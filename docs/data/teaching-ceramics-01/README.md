# 教学模拟陶片属性数据 01

> **教学模拟数据 / SYNTHETIC TEACHING DATA — 非真实考古发掘资料。**

**标识：** teaching-ceramics-01  
**版本：** 0.1（内部教学样例，待编写组核审）  
**关联章节：** 第3章（数据结构和质量），第6章（方法示例），第10章（类型学比较）  
**规模：** 18个虚构陶片记录；8个变量  
**真实程度：** 全部人工设计，用于教学；不对应任何考古遗址、发掘单位、年代、文化或研究发现。

## 使用目的

帮助无编程基础的本科生识别观测单位、变量类型、类别编码和结构性缺失；讨论人工记录、模型输入与考古解释的区别。

## 文件

- [ceramics.csv](ceramics.csv)：标准 UTF-8 CSV 数据表
- [ceramics_excel_utf8bom.csv](ceramics_excel_utf8bom.csv)：面向 Excel 直接打开的 UTF-8 BOM 版本，数据内容相同
- [data_dictionary.csv](data_dictionary.csv)：标准 UTF-8 变量字典
- [data_dictionary_excel_utf8bom.csv](data_dictionary_excel_utf8bom.csv)：Excel 兼容 UTF-8 BOM 变量字典
- [provenance.md](provenance.md)：数据来源、构造方式与适用边界
- [USAGE.md](USAGE.md)：目前的使用许可状态与发布要求

## 关键质量提示

- `rim_diameter_cm` 仅在口沿碎片有数值；非口沿空白是**结构性缺失**，不是直径0。
- `surface_treatment = 未记录` 是记录缺失，不应视为一种真实装饰类型。
- `context_id` 是虚构编码，不是地点坐标，也不能提供地层、年代信息。
- `coarse_inclusion_flag = 0` 不等于证实粗颗粒不存在。
- 不得利用这些模拟数据推断真实生产工艺、文化分期或社会组织。

## 第6章与第10章的扩展资源

- [虚构9条口沿测量](rim_morphometrics_synthetic.csv)与[Excel兼容版本](rim_morphometrics_excel_utf8bom.csv)
- [KMeans／Ward预制结果](prepared_clusters.csv)与[Excel兼容版本](prepared_clusters_excel_utf8bom.csv)
- [变量补充字典](rim_morphometrics_dictionary.csv)、[算法说明与解释边界](methods_typology_note.md)、[选做复现脚本](reproduce_clusters.py)

这些记录仍然是虚构材料；聚类结果虽由实际算法运行取得，却不能代表考古学证据。两章的必做任务不需要学生训练模型。

## 建议的基础任务

1. 数出记录数，区分一行（陶片）与一列（变量）。
2. 识别名义变量、数值变量与二元编码。
3. 比较“零”“空白”“未记录”在本数据中的意义。
4. 讨论为什么按 `context_id` 比较不意味着可以确定实际年代差异。

**教师用说明：** 为第6章与第10章使用同一底层表时，仍应提供不同的预制输出和不同的评价任务；本数据本身没有真实类型标签或机器模型结果。
