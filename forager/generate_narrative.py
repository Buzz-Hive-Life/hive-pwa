import os
from retropgf_submitter import draft_narrative
out = os.path.join(os.path.dirname(__file__), 'forager_review', 'retropgf_HiveLifeHaven_application.md')
os.makedirs(os.path.dirname(out), exist_ok=True)
narr = draft_narrative()
with open(out, 'w', encoding='utf-8') as f:
    f.write(narr)
print('wrote', out, len(narr), 'bytes')
