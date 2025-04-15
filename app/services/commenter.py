import re
from app.utils.qroq_api import generate_with_qroq
from app.utils.logger import log_info, log_error

def comment_code_for_readability(code: str) -> dict:
    """
    Adds helpful inline comments to the provided code using AI.

    Parameters:
    - code (str): Raw source code

    Returns:
    - dict: Result containing commented code or error
    """
    try:
        log_info("Generating code comments using Qroq...")

        prompt = f"""
        You are an expert software engineer. Add inline comments to the following code to make it easily understandable by other developers. Use concise and meaningful comments. Do not modify the code, just add comments.

        ```python
        {code}
        ```
        """

        ai_response = generate_with_qroq(prompt)

        # Clean response if wrapped in code block
        commented_code = re.sub(r'```(python)?', '', ai_response).strip("` \n")

        log_info("Successfully generated commented code.")
        return {"success": True, "commented_code": commented_code}

    except Exception as e:
        log_error(f"Commenter Error: {str(e)}")
        return {"success": False, "error": str(e)}
