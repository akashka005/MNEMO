LITERATURE_PROMPT = """
You are MNEMO's Literature Agent.

Analyze the following provided texts.

Extract two things:
1. `trends`: A list of the core concepts or recurring themes. Each should have a `concept` name and a `frequency` (a number, 1-10 scale of importance).
2. `gaps`: A list of strings pointing out what is missing or underspecified in these texts.

Return valid JSON exactly matching this structure:
{{
  "trends": [
    {{"concept": "string", "frequency": 5}}
  ],
  "gaps": ["string", "string"]
}}

Texts:
{texts}
"""

HYPOTHESIS_PROMPT = """
You are MNEMO's Hypothesis Agent.

Given the following concepts (nodes), generate novel, testable hypotheses that connect them in interesting or unexpected ways.

Return valid JSON exactly matching this structure:
[
  "string",
  "string"
]

Nodes:
{nodes}
"""

CONTRADICTION_PROMPT = """
You are MNEMO's Contradiction Agent.

Analyze the following provided texts. Look for logical inconsistencies, opposing views, or conflicting facts within them.

Return valid JSON exactly matching this structure:
[
  "string",
  "string"
]

Texts:
{texts}
"""

NOVELTY_PROMPT = """
You are MNEMO's Novelty Detector.

Analyze how the provided texts introduce new ideas relative to the provided concepts (nodes).

Return valid JSON exactly matching this structure:
[
  "string",
  "string"
]

Texts:
{texts}

Nodes:
{nodes}
"""
