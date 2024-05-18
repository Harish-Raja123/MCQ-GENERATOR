from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
import json
import string
from prompts import *

def util(context, numPairs, inputPrompt, model):
    try:
        stuff_chain = load_qa_chain(model, chain_type="stuff", prompt=inputPrompt)
        stuff_answer = stuff_chain(
            {"input_documents": context, "numPairs": numPairs}, return_only_outputs=True
        )
        output_text = stuff_answer['output_text']
        output_json = json.loads(output_text)
        return output_json
    except Exception as e:
        print(f"Error: {e}")
        return None

def getMcqQAPairs(context, numPairs, model):
    try:
        prompt_template = getMcqQAPrompt()
        prompt = PromptTemplate(
            template=prompt_template, input_variables=["context", "numPairs"]
        )
        return util(context, numPairs, prompt, model)
    except Exception as e:
        print(f"Error: {e}")
        return None