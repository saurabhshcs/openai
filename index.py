import os
import openai
openai.organization = "org-ZvBs9JwSAWZzMcJ0hm2dmkty"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()