import openai
import os
from dotenv import load_dotenv
from typing import List, Any, Optional, TypedDict

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


def remove_python_markdown_formatting(text: str) -> str:
    """Remove the python Markdown formatting from the given text."""
    if text.startswith("```python") and text.endswith("```"):
        return text[len("```python"): -len("```")]
    return text


class Message(TypedDict):
    """A dictionary representing an OpenAI Message object.

    Attributes:
        role (str): The role of the message sender, either "system", "user", or "assistant".
        content (str): The content of the message.
    """

    role: str
    content: str


def call_ai_function(function: str, args: List[Any], description: str) -> str:
    """Call an AI function using the OpenAI API.

    Args:
        function (str): The function to call.
        args (List[Any]): The arguments to pass to the function.
        description (str): The description of the function.

    Returns:
        str: The response from the function.
    """

    # For each arg, if any are None, convert to "None":
    args = [f"{arg}" if arg is not None else "None" for arg in args]
    # parse args to comma separated string
    args: str = ", ".join(args)
    messages: List[Message] = [
        {
            "role": "system",
            "content": f"You are now the following python function: ```# {description}"
            f"\n{function}```\n\nOnly respond with your `return` value as plain text."
                       f" Any changes to a file must ensure they will pass the most rigorous code reviews.",
        },
        {"role": "user", "content": args},
    ]

    return call_openai(messages=messages, temperature=0)


def call_openai(messages: List[Message], temperature: float = 0.0, max_tokens:  Optional[int] = None) -> str:
    """Call the OpenAI API with the provided messages and parameters.

    Args:
        messages (List[Message]): A list of Message objects to send to the API.
        temperature (float, optional): The sampling temperature to use. Defaults to 0.0.
        max_tokens (Optional[int], optional): The maximum number of tokens to generate. Defaults to None.

    Returns:
        str: The response from the API.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    text = response.choices[0].message.content.strip()
    return remove_python_markdown_formatting(text)
