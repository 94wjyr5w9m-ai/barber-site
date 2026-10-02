# Booked Solid AI: business files

- `crm.csv`: your lead tracker. Open it in Google Sheets (File → Import → Upload).
  Delete the EXAMPLE row once you add real leads.

## Status values (use exactly these)
new → contacted → replied → call booked → proposal sent → closed won / closed lost

## Rules
- Every lead gets a `next_step` and `next_step_date`. No date means the lead gets forgotten.
- Each morning, sort by `next_step_date` and work top to bottom.
- Keep following up until 6–7 touches, or until they say no.
