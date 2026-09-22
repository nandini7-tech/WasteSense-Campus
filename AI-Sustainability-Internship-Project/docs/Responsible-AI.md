# Responsible AI Considerations

## Fairness
The system does not profile users or make judgements about individuals. Recommendations are based on item description, material keywords, and campus policy entries. Ambiguous items receive a caution rather than a forced classification.

## Transparency
Every output includes:
- suggested category
- recommended bin or route
- confidence level
- matched signals
- caution where contamination or ambiguity is likely

This makes the AI behaviour inspectable and suitable for academic review.

## Ethics
The prototype is intentionally non-punitive. It does not recommend cameras, shaming boards, or individual tracking. The goal is assistance, not enforcement.

## Privacy
The offline demo does not transmit data. In a production setting:
- image uploads should require consent
- logs should be anonymised
- retention should be limited
- sensitive items such as sanitary waste should never be individually tracked

## Limitations
The current model uses simplified rules and local sample data. It should be validated with real campus waste policies, facility staff, and student testing before deployment.
