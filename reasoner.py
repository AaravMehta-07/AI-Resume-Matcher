from ctransformers import AutoModelForCausalLM

MODEL_PATH = "C:/Aarav/Code/AI Resume Matcher/models/mistral-7b-instruct-v0.1.Q5_K_M.gguf"

# ✅ Load the model
llm = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    model_type="mistral",
    max_new_tokens=512,
    temperature=0.7,
    context_length=2048
)

# Helper function to trim input text to avoid token overflow
def truncate_text(text, max_tokens):
    return text[:max_tokens * 4]  # ~4 chars/token

def generate_reasoning(job_text, resume_text):
    job_text = truncate_text(job_text, max_tokens=900)
    resume_text = truncate_text(resume_text, max_tokens=900)

    prompt = f"""
You are a professional AI hiring assistant.

Given the job description and candidate resume below, do the following:
1. Estimate a **match percentage** from 0% to 100%.
2. Explain **why the candidate is a good or bad fit** for the role.
3. Highlight which **skills and experiences match** the job.
4. Mention **missing qualifications or red flags**, if any.
5. Summarize strengths and concerns.

Only include what is relevant to the job. Be honest, accurate, and detailed.

JOB DESCRIPTION:
\"\"\"
{job_text}
\"\"\"

RESUME:
\"\"\"
{resume_text}
\"\"\"

Now write your evaluation clearly:
"""

    return llm(prompt)
