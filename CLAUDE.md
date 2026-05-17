# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

A personal study project for LangChain 1.2, with numbered tutorial scripts in Chinese. Uses `uv` for package management and Python >= 3.12.

## Commands

```bash
# Install dependencies (managed by uv)
uv sync

# Run any script directly
uv run python part1_introduction/01_初始化模型.py
```

## Architecture

The scripts under `part1_introduction/` progress through LangChain concepts in order:

1. **01-02**: Model initialization (`init_chat_model`) with DashScope/OpenAI-compatible providers, and basic invocation
2. **03**: Agent creation via `create_agent`, both blocking (`invoke`) and streaming (`stream` with `stream_mode="messages"`)
3. **04-05**: Message types (`HumanMessage`, etc.) and multimodal input
4. **06-07**: Prompt engineering and few-shot prompting
5. **08-09**: Structured output — LangChain's `with_structured_output` and model-native structured output
6. **10-11**: Tool definition (`@tool` decorator, Pydantic `args_schema`, predefined LangChain tools) and binding tools to agents
7. **12-14**: Short-term memory via `AgentState` + `Checkpointer` (in-memory `InMemorySaver`, persistent `SqliteSaver`), and memory management strategies — trimming, deletion, and `SummarizationMiddleware`

**Key patterns across all scripts:**
- API keys and base URLs are loaded from a `.env` file via `python-dotenv`
- Models are initialized with `init_chat_model()` using the OpenAI-compatible provider pattern (primarily against DashScope's `qwen3.5-plus`)
- Some scripts also use `deepseek-v4-flash` via the DeepSeek provider
- The `resource/` directory stores SQLite checkpoint databases (`.db`) used in the persistence demos
- Scripts are self-contained and meant to be run individually — there is no shared library code
