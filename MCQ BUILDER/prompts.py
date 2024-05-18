def getMcqQAPrompt():
    prompt = """
    Imagine leading a stimulating debate among renowned experts based on the following text:
    
    {context}
    
    To spark insightful discussion, design {numPairs} challenging multiple-choice questions, each with four plausible yet distinct options. Only one will be the accurate answer, revealed alongside the shuffled options as a bonus point for the sharpest minds!
    
    Craft your questions thoughtfully, employing a variety of types (factual recall, inferential reasoning, critical analysis) to test the depth and agility of the experts' understanding. Remember, the more nuanced and insightful your questions, the richer and more engaging the intellectual exchange will become.
    
    Then output only a json array that would describe each question and answer it will have in this format. Generate a valid json array.
    Please include each and every Question Answer Pair in the context.
    {{
        "question": [string],
        "options" : [string],
        "correct_option_index" : <number>,
    }}
    
    Never output the instructions given for output.
    Not include  ```json in output , only give output as array.
    """
    return prompt
