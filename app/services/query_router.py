def get_search_config(question: str):

    question = question.lower()

    summary_keywords = [
        "summary",
        "summarize",
        "overview",
        "main topics",
        "entire document",
        "whole document",
        "explain everything",
        "all chapters",
        "all topics"
    ]

    comparison_keywords = [
        "compare",
        "difference",
        "vs",
        "versus"
    ]

    # Summary Questions
    if any(keyword in question for keyword in summary_keywords):

        return {
            "k": 20,
            "fetch_k": 30,
            "lambda_mult": 0.7
        }

    # Comparison Questions
    elif any(keyword in question for keyword in comparison_keywords):

        return {
            "k": 8,
            "fetch_k": 15,
            "lambda_mult": 0.6
        }

    # Default Questions
    return {
        "k": 3,
        "fetch_k": 10,
        "lambda_mult": 0.5
    }