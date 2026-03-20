# 金融分身应用（图片 + 文字 + 实时新闻）

这个原型应用是 `金融分身` 的当前应用载体。它支持你提供图片和文字样本，学习你的分析思维，然后结合最新财经新闻输出“需要关注的方向”。

## 功能

- 学习你的分析风格（风险偏好、行业偏好、关注因子、预警信号）
- 上传图片并提取金融相关信息（需配置 `OPENAI_API_KEY`）
- 抓取实时新闻（Google News RSS）
- 综合输出：
  - 市场主线
  - 重点跟踪清单
  - 风险清单
  - 48小时行动建议

## 运行

```bash
cd 40_projects/finance_analysis_app
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

可选：配置 OpenAI Key（用于图片理解和更高质量分析）

```bash
set OPENAI_API_KEY=你的key
```

启动：

```bash
streamlit run app.py
```

## 数据存储

- 风格画像：`data/style_profile.json`
- 样本记录：`data/cases/*.md`

## 说明

- 未配置 OpenAI Key 时，应用仍可运行，但图片解析不可用，分析降级为规则引擎。
- 路由入口见：`60_finance/finance_routing.md`
