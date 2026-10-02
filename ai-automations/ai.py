"""Shared helper: every automation in this folder talks to Claude through here.

Set your key first:  export ANTHROPIC_API_KEY=sk-ant-...
"""
import anthropic

MODEL = "claude-opus-5-5"

# If Claude's safety filters decline a request, "fallbacks" retries it on
# another model automatically instead of failing.
FALLBACK_BETA = "server-side-fallback-2026-07-01"

client = anthropic.Anthropic()


def ask(prompt: str, system: str = "", effort: str = "low") -> str:
    """Send one message to Claude and get the text reply back."""
    response = client.beta.messages.create(
        model=MODEL,
        max_tokens=16000,
        system=system,
        messages=[{"role": "user", "content": prompt}],
        output_config={"effort": effort},
        betas=[FALLBACK_BETA],
        fallbacks="default",
    )
    if response.stop_reason == "refusal":
        raise RuntimeError("Claude declined this request.")
    return "".join(b.text for b in response.content if b.type == "text").strip()


def ask_structured(prompt: str, schema, system: str = "", effort: str = "low"):
    """Like ask(), but returns a validated Pydantic object instead of free text."""
    response = client.beta.messages.parse(
        model=MODEL,
        max_tokens=16000,
        system=system,
        messages=[{"role": "user", "content": prompt}],
        output_format=schema,
        output_config={"effort": effort},
        betas=[FALLBACK_BETA],
        fallbacks="default",
    )
    if response.stop_reason == "refusal":
        raise RuntimeError("Claude declined this request.")
    return response.parsed_output
