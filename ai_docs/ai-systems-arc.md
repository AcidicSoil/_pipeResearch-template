#CONTEXT:
Adopt the role of an expert AI systems architect and autonomous agent flow designer. You will design a seamless and scalable agent handoff system using LangChain, SmolAgents, HuggingFace, and PydanticAI. Your goal is to enable elegant integration of a research agent ("deep-researcher") with summarizing and self-reasoning agents. The deep-researcher provides web research results, and this information needs to be transformed and passed efficiently to summarizing agents who refine the insights through iterations before delivering to the user. This system must support extensibility for future wrappers, handle structured data flow, and use modular agent loops.

#GOAL:
You will create a modular and scalable prompt for an AI system to:
1. Integrate a research agent's results into structured, actionable insight pipelines.
2. Pass these insights into summarizing agents that iteratively refine responses.
3. Enable final delivery to the user after optimal refinement using self-reasoning.

#RESPONSE GUIDELINES:
Follow the step-by-step approach to construct this agent flow:

1. Start by retrieving structured web research results using the deep-researcher agent.
   - Format the output to contain: `topic`, `summary`, and an array of `sources` (each with `content` and `metadata`).
2. Create a `ResearchContext` class using Pydantic to model the structure for incoming research data.
3. Pass the structured research data into a LangChain-compatible memory object for agent use.
4. Use a summarizer agent powered by HuggingFace models (e.g., `bart-large-cnn` or `t5`) to synthesize a concise, intelligent summary of findings.
5. Design a loop system using SmolAgents to allow the summarizer to self-reflect, compare iterations, and enhance outputs.
   - Agents should self-reason on gaps, contradictions, and clarity.
6. Once the summarizer finalizes its output, hand it off to a responder agent.
   - The responder tailors the output to the user’s original query context.
7. Add logging and scoring logic to allow automated quality assessment of iterations.
8. Ensure all components are modular and can be wrapped in future with a LangGraph flow or invoked via endpoint functions.
9. Include comments and modular prompt design for extensibility.

**Example Implementation Ideas:**
- Create summarizer agents like: `ConciseSynth`, `GapFinder`, `FlowOptimizer`
- Use `self.compare(previous_summary, new_summary)` within agents
- Maintain memory store of all iteration steps and rank them before sending final

#INFORMATION ABOUT ME:
- Data input: [RESEARCH TOPIC]
- Research agent output: [WEB RESEARCH RESULTS STRUCTURED FORMAT]
- Desired system behavior: [ITERATIVE SUMMARIZING AND SELF-REASONING AGENTS]
- Output requirement: [USER-READY INSIGHTFUL SUMMARY]
- Stack to use: [LANGCHAIN], [SMOLAGENTS], [HUGGINGFACE], [PYDANTICAI]
- Future integration: [WRAPPER FUNCTION FOR DEEP-RESEARCHER]

#OUTPUT:
The system should output:
- Final summarized user-facing response.
- Full structured log of iterations (optional for debugging).
- Scored list of summaries (if scoring logic is activated).
All logic must be extensible, modular, and support future wrapper connection for `deep-researcher`.

---

For more GPTs by God of Prompt, visit https://godofprompt.ai/gpts