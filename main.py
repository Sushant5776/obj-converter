from fastapi import FastAPI
from utils.logger import get_logger
from fastapi.staticfiles import StaticFiles
from models.home_response import HomeResponse
from models.description_response import DescriptionResponse
from models.description_request import DescriptionRequest
from models.ai_model_input import AIModelInput
from utils.methods import generate_id
from ai.google_flan_t5 import generate_ai_description

app = FastAPI()
logger = get_logger(name="API Logger")


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_model=HomeResponse)
async def home():
    logger.info(msg="Requested Home Page")
    return HomeResponse(message="Hello World!")


@app.post(
    "/create",
    response_model=DescriptionResponse,
    description="Send your product malformed details to this endpoint and received the formatted output.",
)
async def description(product: DescriptionRequest):
    product_dict = product.model_dump()
    ai_input = AIModelInput(**product_dict)

    prompt = f"{ai_input.model_dump_json()} using this information from json data write the product description in 3 to 5 lines of plain text paragraph."

    description_res = generate_ai_description(prompt)

    id = generate_id()
    product_dict["id"] = id

    name = product_dict.pop("name", None)

    if name:
        product_dict["title"] = name

    if "images" in product_dict and type(product_dict["images"]) is list:
        product_dict["imageUrl"] = product_dict["images"][0]

    if "description" in product_dict and type(product_dict["description"]) is list:
        product_dict["description"] = description_res

    return DescriptionResponse(**product_dict)
