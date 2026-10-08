# Awesome Agent Safety

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)
[![Links checked](https://github.com/tahmidulferdous/awesome-agent-safety/actions/workflows/links.yml/badge.svg)](https://github.com/tahmidulferdous/awesome-agent-safety/actions/workflows/links.yml)

**Agent-specific safety, curated: threat models, guardrails, MCP/A2A security, evals, incidents, and governance — everything a builder needs to ship agents that don't leak, break, or get hijacked.**

*Last updated: 2026-10-08 — see [CHANGELOG.md](CHANGELOG.md).*

### Why this list

Chat-model safety lists stop at refusal and toxicity. Agents perceive, remember, plan, call tools, spend money, and change state — so their risks live in the loop: persistent memory poisoning, tool hijacking, MCP/A2A protocol abuse, multi-agent collusion, irreversible actions. The neighboring lists each cover a slice (security papers, governance tooling, incident corpora); this is the holistic, agent-only view. Every entry was checked against its source, non-agent foundations are quarantined in the appendix, and the guardrail table below compares the defenses head-to-head instead of just linking them.

Scope: threat models, autonomy risks, prompt injection / jailbreaks (agent-specific), memory / RAG / tool / MCP-A2A security, guardrails & runtime defenses, evals / benchmarks / red-teaming, incidents & failure modes, governance / safety cases / auditing, frameworks with safety hooks. An appendix lists adjacent non-agent foundations.

Neighbors and how this differs:
- [ucsb-mlsec/Awesome-Agent-Security](https://github.com/ucsb-mlsec/Awesome-Agent-Security) — papers/blogs on agent security, explicitly does not separate safety vs security.
- [agentrust-io/awesome-ai-governance](https://github.com/agentrust-io/awesome-ai-governance) — governance/compliance tooling.
- [h5i-dev/awesome-ai-agent-incidents](https://github.com/h5i-dev/awesome-ai-agent-incidents) — incident corpus.
- [AbdelStark/awesome-ai-safety](https://github.com/AbdelStark/awesome-ai-safety) — general AI safety, not agent-specific.
- [natnew/awesome-agentops](https://github.com/natnew/awesome-agentops) — production ops with guardrails section.

This list is holistic and agent-only: every entry must involve tool use, memory, multi-step autonomy, or agent protocols.

## Contents

- [Start Here](#start-here)
- [Threat Models & Taxonomies](#threat-models--taxonomies)
- [Autonomy Risks — Deception, Reward Hacking, CoT Faithfulness](#autonomy-risks--deception-reward-hacking-cot-faithfulness)
- [Prompt Injection & Jailbreaks (Agent-Specific)](#prompt-injection--jailbreaks-agent-specific)
- [Memory, RAG, Tool & MCP/A2A Security](#memory-rag-tool--mcpa2a-security)
- [Guardrails & Runtime Defenses](#guardrails--runtime-defenses)
- [Evals, Benchmarks & Red-Teaming](#evals-benchmarks--red-teaming)
- [Incidents & Failure Modes](#incidents--failure-modes)
- [Governance, Safety Cases & Auditing](#governance-safety-cases--auditing)
- [Frameworks with Safety Hooks](#frameworks-with-safety-hooks)
- [Appendix: Adjacent (Non-Agent) Foundations](#appendix-adjacent-non-agent-foundations)
- [Contributing](#contributing)

## Start Here

- [AI Agents Under Threat: A Survey of Key Security Challenges and Future Pathways](https://arxiv.org/abs/2406.02630) (2024) — Security failure modes across the perception–reasoning–action loop: memory tampering, goal hijacking, tool manipulation.
- [Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions](https://arxiv.org/abs/2503.23278) (2025) — MCP architecture + threat model: tool discovery, authorization, execution.
- [A Survey on Autonomy-Induced Security Risks in Large Model-Based Agents](https://arxiv.org/abs/2506.23844) (2025) — Risks that scale with autonomy: memory poisoning, tool misuse, irreversible chains, reward hacking, deception.
- [Safety at Scale: A Comprehensive Survey of Large Model and Agent Safety](https://arxiv.org/abs/2502.05206) (2025) — Maps threats → defenses → datasets for models and agents.
- [How to evaluate control measures for LLM agents?](https://arxiv.org/abs/2504.05259) (2025) — Control evaluations + safety-case scaling (ACL1–5) for misaligned-agent containment.

## Threat Models & Taxonomies

- [The lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) (Simon Willison, 2025) — Private data + untrusted content + external communication in one agent = exfiltration by design; cut one leg.
- [A Survey on Agentic Security: Applications, Threats and Defenses](https://arxiv.org/abs/2510.06445) (2025) — Holistic taxonomy over ~260 papers with lifecycle + cost trade-offs. List: [kagnlp/Awesome-Agentic-Security](https://github.com/kagnlp/Awesome-Agentic-Security).
- [SoK: The Attack Surface of Agentic AI — Tools and Autonomy](https://arxiv.org/abs/2603.22928) (2026, preprint) — Attack surface across decision loops, tool interfaces, environment feedback.
- [TRiSM for Agentic AI](https://arxiv.org/abs/2506.04133) (2025) — Trust, Risk, Security Management framework for multi-agent deployments.
- [SoK: When Safe Agents Fail Together](https://arxiv.org/abs/2609.00595) (2026, preprint) — Multi-agent systemic failure: 197 works, 6 interfaces, 4 adversary positions, 8 paths; audits 44 benches.

## Autonomy Risks — Deception, Reward Hacking, CoT Faithfulness

- [The Chronos Vulnerability: Temporal Persistence and Memory-Based Deception](https://arxiv.org/abs/2607.19433) (2026, preprint) — MINJA / sleeper-agent / session-smuggling threat model for stateful agents.
- [A Concrete Roadmap towards Safety Cases based on Chain-of-Thought Monitoring](https://arxiv.org/abs/2510.19476) (2025) — Safety cases from automated CoT monitoring.
- [Emergent Strategic Reasoning Risks in AI: A Taxonomy-Driven Evaluation Framework](https://arxiv.org/abs/2604.22119) (2026, preprint) — Evaluation gaming, steganography, deceptive reasoning traces.
- [GDM AI Control Roadmap](https://arxiv.org/abs/2607.13087) (2026, preprint) — D1–D4/R1–R3 detection-response tiers + TRAIT&R threat model for insider-misaligned agents.

## Prompt Injection & Jailbreaks (Agent-Specific)

- [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) (Greshake et al., 2023, AISec '23) — The original indirect-prompt-injection paper: retrieved data as arbitrary code execution. Code: [greshake/llm-security](https://github.com/greshake/llm-security).
- [The Landscape of Prompt Injection Threats in LLM Agents](https://arxiv.org/abs/2602.10453) (2026, preprint) — Taxonomy + mitigations + eval practices for agents.
- [Prompt Injection Attacks on Agentic Coding Assistants](https://arxiv.org/abs/2601.17548) (2026, preprint) — Attack surfaces across skills, tool-calling pipelines, protocol ecosystems.
- [SoK: Rethinking Jailbreaking in the Era of Agentic AI](https://arxiv.org/abs/2609.12413) (2026, preprint) — Jailbreaks with persistent memory, tool execution, multi-agent communication.
- [AgentDojo](https://github.com/ethz-spylab/agentdojo) ([paper](https://arxiv.org/abs/2406.13352)) — Indirect prompt injection in stateful multi-tool tasks (97 tasks / 629 cases).
- [InjecAgent](https://github.com/uiuc-kang-lab/InjecAgent) ([paper](https://arxiv.org/abs/2403.02691)) — Single-turn indirect injection (1,054 cases); fast IPI regression.

## Memory, RAG, Tool & MCP/A2A Security

- [A survey of agent interoperability protocols: MCP, ACP, A2A, ANP](https://arxiv.org/abs/2505.02279) (2025) — Compares trust boundaries + protocol attack surfaces.
- [A2ABreak: Systematic Security Analysis of the A2A Protocol](https://arxiv.org/abs/2609.10871) (2026, preprint) — 37-state FSM audit; 11 spec-compliant vulns (context-ID injection, multi-hop identity loss).
- [The Emerged Security and Privacy of LLM Agent: A Survey with Case Studies](https://arxiv.org/abs/2407.19354) (2024) — Data leakage via tool integration, memory, multi-agent interaction.
- [Trustworthiness in Retrieval-Augmented Generation Systems](https://arxiv.org/abs/2409.10102) (2024) — Retrieval poisoning, hallucination, privacy leakage in RAG.
- [SoK: Privacy Risks and Mitigations in RAG Systems](https://arxiv.org/abs/2601.03979) (2026) — Extraction attacks + mitigations across stores, embeddings, query generation.

## Guardrails & Runtime Defenses

Rule: open-source or source-available with repo; commercial API-only noted as such. Pin versions — several repos are archived or very new.

### Guardrail comparison

| Tool | License | MCP-aware | Status |
| --- | --- | --- | --- |
| LlamaFirewall | MIT (code) | — | Maintained (Meta) |
| PromptGuard 2 | Llama Community (model) | — | Maintained (Meta) |
| CaMeL | Apache-2.0 | — | Research artifact, not maintained |
| NeMo Guardrails | Apache-2.0 | Yes (hooks) | Maintained (NVIDIA) |
| Guardrails AI | Apache-2.0 | — | Maintained |
| Invariant Guardrails | Apache-2.0 | Yes (proxy) | Maintained |
| OWASP Agent Memory Guard | Apache-2.0 | — | Maintained (OWASP) |
| MS Agent Governance Toolkit | MIT | Yes (gateway) | Maintained (Microsoft) |
| AI-Infra-Guard | Apache-2.0 | Yes (scan) | Maintained (Tencent) |
| cc-safety-net | MIT | — (CLI hooks) | Maintained (solo) |
| ToolHive | Apache-2.0 | Yes (gateway) | Maintained (Stacklok) |
| E2B | Apache-2.0 | — (sandbox) | Maintained |
| LLM Guard | MIT | — | Archived 2026-07 — pin version |
| Rebuff | Apache-2.0 | — | Archived 2025-05 — pin version |
| mcp-guardian | MIT | Yes (proxy) | New — evaluate |
| mcp-shield | Apache-2.0 | Yes (proxy) | New — evaluate |
| Cordum | BUSL-1.1 (not OSI open-source) | Yes (gateway) | Maintained (commercial) |

- [LlamaFirewall](https://github.com/meta-llama/PurpleLlama/tree/main/LlamaFirewall) (Meta, MIT code) — Layered agent guardrail: PromptGuard + alignment check + CodeShield + regex for tool flows.
- [PromptGuard 2](https://github.com/meta-llama/PurpleLlama/tree/main/Llama-Prompt-Guard-2) (Meta) — Lightweight classifier for injection/jailbreak on inputs + untrusted tool content.
- [CaMeL: Defeating Prompt Injections by Design](https://arxiv.org/abs/2503.18813) (Google DeepMind, 2025) — Capability-based information-flow control: control/data flows extracted from the trusted query, policies enforced at tool calls; 0 successful attacks across 949 AgentDojo runs with provable guarantees. Code: [google-research/camel-prompt-injection](https://github.com/google-research/camel-prompt-injection) (Apache-2.0, research artifact — not a maintained product).
- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) (NVIDIA, Apache-2.0) — Programmable input/dialog/retrieval/execution/output rails (Colang) with MCP hooks.
- [Guardrails AI](https://github.com/guardrails-ai/guardrails) (Apache-2.0) — Input/output guards + Hub validators for structured-output risk checks.
- [Invariant Guardrails](https://github.com/invariantlabs-ai/invariant) (Apache-2.0) — Rule-based agent-trace guardrails + MCP/LLM proxy with injection detectors.
- [OWASP Agent Memory Guard](https://github.com/OWASP/www-project-agent-memory-guard) (Apache-2.0) — Runtime memory firewall: SHA-256 baselines + injection/secret/PII detectors + quarantine/block (ASI06).
- [Microsoft Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit) (MIT) — Policy engine + zero-trust identity + sandboxing + MCP Security Gateway; covers 10/10 OWASP Agentic risks.
- [Tencent AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) (Apache-2.0) — Full-stack red-team: Agent/MCP/Skill scan + infra CVE scan + jailbreak eval.
- [cc-safety-net](https://github.com/kenryu42/cc-safety-net) (MIT) — Pre-execution hook blocking destructive git/rm + secret access across 14+ coding-agent CLIs.
- [ToolHive](https://github.com/stacklok/toolhive) (Apache-2.0) — Container-isolated MCP platform: registry + gateway with Cedar/OIDC authz, tool filtering, audit/OTel.
- [E2B](https://github.com/e2b-dev/e2b) (Apache-2.0) — Isolated cloud sandboxes for agent-generated code (self-hostable).
- [LLM Guard](https://github.com/protectai/llm-guard) (MIT, archived 2026-07) — Input/output scanners (injection, secrets, URLs, code). Pin version.
- [Rebuff](https://github.com/protectai/rebuff) (Apache-2.0, archived 2025-05) — Self-hardening injection detector (heuristics + LLM + VectorDB + canary tokens). Pin version.
- [mcp-guardian](https://github.com/cyberranger93/mcp-guardian) (MIT, new) — Local MCP firewall/proxy + scanner + audit + redaction + CI action.
- [mcp-shield](https://github.com/thuggeelya/mcp-shield) (Apache-2.0, new) — Bandit-for-MCP scanner (0–100 score) + deny/allow proxy + SARIF.
- [Cordum](https://github.com/cordum-io/cordum) (BUSL-1.1, source-available, NOT OSI open-source) — Control plane: policy kernel + human approvals + MCP gateway + audit.
- Lakera Guard — commercial API only (no OSS guard repo); demo client at [lakeraai/guard-demo-client](https://github.com/lakeraai/guard-demo-client). Listed for completeness; prefer OSS above for self-hosting.

## Evals, Benchmarks & Red-Teaming

- [AgentDoG + ATBench](https://github.com/AI45Lab/AgentDoG) ([paper](https://arxiv.org/abs/2601.18491)) — Trajectory-level tool-misuse / injection with root-cause diagnosis; doubles as online guardrail.
- [AgentHarm](https://huggingface.co/datasets/ai-safety-institute/AgentHarm) ([paper](https://arxiv.org/abs/2410.09024)) — Multi-step tool misuse (110 base / 440 aug, 11 harms) with execution scoring.
- [Agent Security Bench (ASB)](https://github.com/agiresearch/ASB) ([paper](https://arxiv.org/abs/2410.02644)) — Full attack/defense matrix (10 scenarios, 400+ tools, memory-poison + Plan-of-Thought backdoor).
- [Agent-SafetyBench](https://arxiv.org/abs/2412.14470) — Broad interactive safety (349 envs / 2,000 cases, 8 risks / 10 failure modes).
- [R-Judge](https://github.com/Lordog/R-Judge) ([paper](https://arxiv.org/abs/2401.10019)) — Risk-awareness judge over trajectories (569 records, 27 scenarios).
- [MCPSecBench](https://github.com/AIS2Lab/MCPSecBench) ([paper](https://arxiv.org/abs/2508.13220)) — MCP-stack security: 17 attacks across 4 surfaces; defenses <30% effective.
- [A2ASecBench](https://safo-lab.github.io/A2ASecBench/) — Runnable A2A exploits (spoofing, cloaking, flooding, forgery, artifact injection) with utility trade-off.
- [ISC-Bench](https://github.com/wuyoscar/ISC-Bench) ([paper](https://arxiv.org/abs/2603.23509)) — Workflow-induced failure: benign task structure that requires harmful output (53 scenarios).
- [AIRTBench](https://github.com/dreadnode/AIRTBench-Code) ([paper](https://arxiv.org/abs/2506.14682)) — Autonomous red-team capability in 70 black-box CTFs; tracks offensive power.
- [WASP: Benchmarking Web Agent Security Against Prompt Injection](https://github.com/facebookresearch/wasp) ([paper](https://arxiv.org/abs/2504.18575), NeurIPS 2025) — End-to-end web-agent hijacking in a sandboxed VisualWebArena; top models fooled by simple human-written injections.
- [OS-Harm: Benchmarking Safety of Computer Use Agents](https://github.com/tml-epfl/os-harm) ([paper](https://arxiv.org/abs/2506.14866), NeurIPS 2025 Spotlight) — 150 OSWorld tasks across deliberate misuse, prompt injection, model misbehavior; automated judge with high human agreement.
- [BenchJack](https://github.com/benchjack/benchjack) ([paper](https://arxiv.org/abs/2605.12673)) — Audits your agent bench for hackability (8 flaw classes, 219 flaws / 10 benches).

## Incidents & Failure Modes

- [GitHub MCP toxic-agent-flow exfiltration (May 2025)](https://invariantlabs.ai/blog/mcp-github-vulnerability) (Invariant Labs) — Indirect injection via public issue → private-repo leak; canonical MCP permission/sandbox test.
- [Claude Code poisoned-config RCE + token exfiltration (CVE-2025-59536 / CVE-2026-21852)](https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536) (Check Point, 2026) — Hooks / `.mcp.json` / base-URL trust bypass; pattern for agent config review.
- [AI Incident Database](https://incidentdatabase.ai/) — Searchable real-harm cases for regression tests + pre-deploy review.
- [OECD AIM — AI Incidents and Hazards Monitor](https://oecd.ai/en/incidents) — ~18k records + taxonomy for governance reporting.
- [LLM Multi-Agent Systems: Challenges and Open Problems](https://arxiv.org/abs/2402.03578) (2024) — Coordination collapse, toxic debate, compounding hallucination chains.
- [LLM-based Agents Suffer from Hallucinations](https://arxiv.org/abs/2509.18970) (2025) — Agent-specific hallucinations across perception, planning, tool use, memory retrieval.
- [Towards Trustworthy GUI Agents](https://arxiv.org/abs/2503.23434) (2025) — Irreversible digital operations: form submission, permission grants, deletions.

## Governance, Safety Cases & Auditing

- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026) — ASI01–ASI10 (goal hijack, tool misuse, identity abuse, supply chain, RCE, memory poisoning, inter-agent comms, cascading failures, trust exploitation, rogue agents) with mitigations. Pin version — evolves fast.
- [OWASP Agentic Skills Top 10 (AST10 v1.0-2026)](https://owasp.org/www-project-agentic-skills-top-10) — Skill-layer risks: isolation, update drift, cross-platform reuse.
- [NIST AI Risk Management Framework 1.0](https://www.nist.gov/itl/ai-risk-management-framework) — Govern/Map/Measure/Manage across agent lifecycle.
- [NIST AI RMF Generative AI Profile (AI 600-1)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) — GAI risks + actions for hallucination, data, misuse controls.
- [EU AI Act — regulatory framework](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) / [EU AI Act explorer](https://www.euaiact.com/) — High-risk (Ch. III) + GPAI systemic-risk duties (Art. 51/55): conformity, logging, incident reporting.
- [Safety Cases for Frontier AI](https://arxiv.org/abs/2410.21572) (2024) — Structured safety argument + evidence pack template for release decisions.
- [Frontier AI Auditing: Toward Rigorous Third-Party Assessment](https://arxiv.org/abs/2601.11699) (2026, preprint) — AAL-1/AAL-2 audits with deep access to verify safety claims.
- [Open Problems in Technical AI Governance](https://arxiv.org/abs/2407.14981) (2024) — Compute verification, privacy-preserving audits, watermarking, structural controls.

## Frameworks with Safety Hooks

- [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/) — Safety callbacks, evaluation tools, multi-agent session management.
- [Dify](https://github.com/langgenius/dify) — Agentic workflows + RAG with moderation, rate limiting, annotation logging.
- [Composio](https://github.com/ComposioHQ/composio) — OAuth token-based IAM + task/resource scoping for tools.

## Appendix: Adjacent (Non-Agent) Foundations

General LLM/AI resources worth knowing; not agent-specific, so kept out of the sections above.

- [SORRY-Bench](https://github.com/SORRY-Bench/sorry-bench) ([paper](https://arxiv.org/abs/2406.14598)) — Refusal balance across 44–45 topics + 20 linguistic mutations; cheap regression for the underlying model.
- [Aegis2.0](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0) ([paper](https://arxiv.org/abs/2501.09004)) — 12 core + 9 fine-grained hazards, ~34k dialogues for training content-safety guards.
- [The AI Risk Repository](https://arxiv.org/abs/2408.12622) (2024) — 74 frameworks / 1,725 risks; causal + domain taxonomy for audit checklists.
- [A Taxonomy of Systemic Risks from General-Purpose AI](https://arxiv.org/abs/2412.07780) (2024) — 13 systemic-risk categories mapped to EU AI Act systemic-risk duties.
- [SoK: Evaluating Jailbreak Guardrails for LLMs](https://arxiv.org/abs/2506.10597) (2025) — Benchmarks external guardrails under adaptive adversaries (chat-LLM setting, not agentic).
- [What Counts as AI Sycophancy?](https://arxiv.org/abs/2605.21778) (2026, preprint) — Taxonomy of sycophantic behaviors: truth-suppression, flattery.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Rules: agent-relevant only (tool/memory/multi-step/protocol), one line per entry (name — what it does — link), no dead links, no commercial API-only tools except where no OSS exists (label them). Run link check before PR.

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](LICENSE)

Code (workflows) under MIT; curated list under CC0-1.0. See [LICENSE](LICENSE).
