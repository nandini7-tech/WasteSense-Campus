# AI Prompt and Workflow Design

## High-level workflow
1. User provides item description or optional image file name.
2. Input is normalised and checked for contamination terms.
3. The system scores candidate waste categories.
4. Top category, runner-up, and confidence are evaluated.
5. If confidence is low or ambiguity exists, the system shows a caution.
6. Policy questions are answered by retrieving the closest local FAQ entry.
7. Impact estimates are calculated using simple, auditable factors.

## Sample system prompt for IBM Granite / IBM BOB
You are a responsible campus sustainability assistant. Your task is to help users identify the correct disposal route for common campus waste items. Be concise, transparent, and cautious. If the item is ambiguous or contaminated, explain the uncertainty and suggest the safer route. Do not make claims about individual users. Do not recommend surveillance or punishment. Always align advice with official campus waste policy.

## Sample user prompt
Classify this item and tell me which campus bin it should go into: empty shampoo sachet with some residue. Include confidence, reason, and any caution.

## RAG pattern
For policy questions:
1. Retrieve top matching campus policy chunks.
2. Provide the chunk text to the model.
3. Ask the model to answer using only the retrieved policy.
4. Include citation metadata: document name, section, and review date.
5. If no sufficient context is found, escalate to facilities staff.

## Why this fits the internship guideline
The project demonstrates:
- clear problem thinking
- logical AI workflow
- SDG alignment
- responsible AI awareness
- a conceptual prototype without requiring advanced coding
