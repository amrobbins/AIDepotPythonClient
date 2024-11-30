from enum import Enum


class Resources(Enum):
    LLM_JOB_RESULTS = 'llm/job_results'
    MISTRAL7B_MESSAGE = 'llm/mistral_7b/message'
    MISTRAL7B_EMBEDDING = 'llm/mistral_7b/embed'
    LLAMA3_1_8B_MESSAGE = 'llm/llam3_1_8b/message'
    LLAMA3_1_8B_EMBEDDING = 'llm/llam3_1_8b/embed'
    # TODO: COMPLETE
