from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage
from botpy.ext.cog_yaml import read
import os

config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))
SPARKAI_APP_ID = config["SPARKAI_APP_ID"]
SPARKAI_API_SECRET = config["SPARKAI_API_SECRET"]
SPARKAI_API_KEY = config["SPARKAI_API_KEY"]
SPARKAI_URL = config["SPARKAI_URL"]
SPARKAI_DOMAIN = config["SPARKAI_DOMAIN"]
PROMPT = config["PROMPT"]

spark = ChatSparkLLM(
    spark_api_url=SPARKAI_URL,
    spark_app_id=SPARKAI_APP_ID,
    spark_api_key=SPARKAI_API_KEY,
    spark_api_secret=SPARKAI_API_SECRET,
    spark_llm_domain=SPARKAI_DOMAIN,
    streaming=False,
)


async def generate_response(content):
    messages = [
        ChatMessage(
            role="system",
            content=PROMPT
        ),
        ChatMessage(
            role="user",
            content=content
        )]
    handler = ChunkPrintHandler()
    response = await spark.agenerate([messages], callbacks=[handler])
    return response.generations[0][0].text
