# 上交所股票型ETF涨跌停持仓分析

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📌 项目简介

本项目用于统计上交所所有股票型ETF收盘后持有涨停股和跌停股的金额，并进行升降排序分析。

### 功能特点

- ✅ 自动获取当日涨停/跌停股票池
- ✅ 分析86+只上交所股票型ETF持仓
- ✅ 统计涨跌停股持仓数量和金额
- ✅ 按涨停/跌停金额升降排序
- ✅ 输出详细的涨跌停股明细
- ✅ 生成Excel数据报表
- ✅ 生成LaTeX专业分析报告

## 📁 项目结构

```
├── etf_analysis.py          # 主程序：ETF涨跌停持仓分析
├── ETF涨跌停持仓分析报告.tex  # LaTeX报告源文件
├── ETF涨跌停持仓分析报告.pdf  # 生成的PDF报告
├── ETF涨跌停持仓分析_*.xlsx   # 生成的Excel数据
├── requirements.txt          # Python依赖
└── README.md                 # 项目说明
```

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行分析

```bash
python etf_analysis.py
```

### 3. 生成LaTeX报告

```bash
xelatex ETF涨跌停持仓分析报告.tex
xelatex ETF涨跌停持仓分析报告.tex  # 运行两次生成完整目录
```

## 📊 输出示例

### 涨停股持仓排名

| ETF名称 | 代码 | 涨停股数量 | 金额(万元) |
|--------|------|----------|-----------|
| 1000ETF | 512100 | 10 | 3.82 |
| 500ETF | 510500 | 7 | 7.53 |
| 2000ETF | 560010 | 4 | 1.28 |
| 光伏ETF | 515790 | 3 | 4.13 |

### 跌停股持仓排名

| ETF名称 | 代码 | 跌停股数量 | 金额(万元) |
|--------|------|----------|-----------|
| 光伏ETF | 515790 | 7 | 4.93 |
| 500ETF | 510500 | 4 | 7.42 |
| 1000ETF | 512100 | 4 | 2.23 |

## 📈 数据来源

- **涨跌停数据**：东方财富涨停板池/跌停板池
- **ETF持仓数据**：东方财富基金持仓明细
- **数据接口**：[AKShare](https://github.com/akfamily/akshare)

## ⚠️ 风险提示

- 涨停股持仓可能带来流动性风险和溢价风险
- 跌停股持仓可能导致净值下跌和折价风险
- 本项目仅供学习研究，不构成投资建议

## 📋 依赖环境

- Python 3.8+
- akshare
- pandas
- openpyxl
- TeX Live (用于生成PDF报告)

## 📄 License

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request！
