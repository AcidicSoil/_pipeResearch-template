#!/bin/bash

uvx --from mcpdoc mcpdoc \
    --urls "LangGraph:https://langchain-ai.github.io/langgraph/llms.txt" "Cline:https://docs.cline.bot/llms.txt" "LangChain:https://python.langchain.com/llms.txt" "AugmentCode:https://docs.augmentcode.com/llms.txt" \
    --allowed-domains langchain-ai.github.io docs.cline.bot python.langchain.com docs.augmentcode.com \
    --transport sse \
    --port 8082 \
    --host localhost &

npx @modelcontextprotocol/inspector