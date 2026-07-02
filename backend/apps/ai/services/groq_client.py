import json
import time
from dataclasses import dataclass
from urllib import error, request

from django.conf import settings


def _strip_code_fences(payload):
    text = payload.strip()
    if text.startswith("```"):
        text = text.strip("`")
        if text.lower().startswith("json"):
            text = text[4:].strip()
    return text


@dataclass
class GroqResult:
    provider: str
    model: str
    content: str
    token_count: int
    latency_ms: int


class GroqClient:
    def __init__(self, api_keys=None, base_url=None, model=None, timeout=60):
        self.api_keys = api_keys or settings.GROQ_KEYS
        self.base_url = (base_url or settings.GROQ_BASE_URL).rstrip("/")
        self.model = model or settings.GROQ_MODEL
        self.timeout = timeout

    def complete_json(self, messages, temperature=0.4):
        last_error = None
        for api_key in self.api_keys:
            try:
                return self._complete_once(api_key, messages, temperature=temperature)
            except Exception as error_instance:
                last_error = error_instance
        raise RuntimeError("All Groq API keys failed.") from last_error

    def _complete_once(self, api_key, messages, temperature=0.4):
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "response_format": {"type": "json_object"},
        }
        body = json.dumps(payload).encode("utf-8")
        api_request = request.Request(
            f"{self.base_url}/chat/completions",
            data=body,
            method="POST",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
        )
        start_time = time.time()
        try:
            with request.urlopen(api_request, timeout=self.timeout) as response:
                response_payload = json.loads(response.read().decode("utf-8"))
        except error.HTTPError as http_error:
            if http_error.code in {401, 403, 429}:
                raise RuntimeError(f"Groq request rejected with {http_error.code}") from http_error
            raise
        latency_ms = int((time.time() - start_time) * 1000)
        content = response_payload["choices"][0]["message"]["content"]
        usage = response_payload.get("usage", {})
        token_count = int(usage.get("total_tokens") or 0)
        return GroqResult(
            provider="groq",
            model=response_payload.get("model", self.model),
            content=_strip_code_fences(content),
            token_count=token_count,
            latency_ms=latency_ms,
        )
