# SmartVoyage
智能旅行项目
# SmartVoyage: 基于 A2A 协议的多智能体旅行助手

## 📖 项目简介
SmartVoyage 是一个基于 Agent-to-Agent (A2A) 协议构建的多智能体（Multi-Agent）旅行助手系统。项目旨在解决复杂出行场景下，单一智能体工具调用混乱、上下文丢失的问题。

系统采用 **“意图路由 - 工具查询 - 结果总结”** 的三段式架构，主 Agent 作为协调者（Router），能够将用户的复合请求拆解并路由至独立的子 Agent（如天气查询 Agent、票务查询 Agent、票务预定 Agent），最终汇总结果并生成自然语言回复。

> **声明**：本项目为个人复现/架构验证项目，数据来源于模拟 API，旨在验证 A2A 协议在多智能体协同中的工程落地。

## 🏗️ 系统架构
```text
用户输入 (自然语言)
   ↓
[ Router Agent (主控) ] 
   ├── 1. 意图识别 (支持多意图拆解与 Query 改写)
   ├── 2. 状态判断 (Out-of-scope 拦截 / 缺失信息追问)
   ↓ (A2A 协议分发)
   ├── [WeatherQueryAssistant] (端口 5005) - 对接气象 API
   ├── [TicketQueryAssistant] (端口 5006) - 对接票务查询 API
   └── [TicketOrderAssistant] (端口 5007) - 对接订票 API
   ↓ (结果回传)
[ Router Agent (主控) ]
   ├── 3. 结果格式化 (将原始数据二次总结)
   └── 4. 组合输出返回给用户
